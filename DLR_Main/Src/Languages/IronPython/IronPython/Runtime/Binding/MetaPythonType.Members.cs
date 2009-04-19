/* ****************************************************************************
 *
 * Copyright (c) Microsoft Corporation. 
 *
 * This source code is subject to terms and conditions of the Microsoft Public License. A 
 * copy of the license can be found in the License.html file at the root of this distribution. If 
 * you cannot locate the  Microsoft Public License, please send an email to 
 * dlr@microsoft.com. By using this source code in any fashion, you are agreeing to be bound 
 * by the terms of the Microsoft Public License.
 *
 * You must not remove this notice, or any other, from this software.
 *
 *
 * ***************************************************************************/


using System; using Microsoft;
using System.Collections.Generic;
using Microsoft.Scripting;
using Microsoft.Linq.Expressions;
using System.Reflection;
using System.Runtime.CompilerServices;
using Microsoft.Runtime.CompilerServices;

using System.Threading;

using Microsoft.Scripting.Actions;
using Microsoft.Scripting.Runtime;

using IronPython.Runtime.Operations;
using IronPython.Runtime.Types;

using Ast = Microsoft.Linq.Expressions.Expression;
using AstUtils = Microsoft.Scripting.Ast.Utils;

namespace IronPython.Runtime.Binding {

    partial class MetaPythonType : MetaPythonObject, IPythonGetable {

        #region MetaObject Overrides

        public override DynamicMetaObject/*!*/ BindGetMember(GetMemberBinder/*!*/ member) {
            return GetMemberWorker(member, BinderState.GetCodeContext(member));            
        }

        private ValidationInfo GetTypeTest() {
            int version = Value.Version;

            return new ValidationInfo(
                Ast.Call(
                    typeof(PythonOps).GetMethod("CheckSpecificTypeVersion"),
                    AstUtils.Convert(Expression, typeof(PythonType)),
                    AstUtils.Constant(version)
                )
            );
        }

        public override DynamicMetaObject/*!*/ BindSetMember(SetMemberBinder/*!*/ member, DynamicMetaObject/*!*/ value) {
            PerfTrack.NoteEvent(PerfTrack.Categories.Binding, "Type SetMember " + Value.UnderlyingSystemType.FullName);
            PerfTrack.NoteEvent(PerfTrack.Categories.BindingTarget, "Type SetMember");
            BinderState state = BinderState.GetBinderState(member);

            if (Value.IsSystemType) {
                MemberTracker tt = MemberTracker.FromMemberInfo(Value.UnderlyingSystemType);
                MemberGroup mg = state.Binder.GetMember(OldSetMemberAction.Make(state.Binder, member.Name), Value.UnderlyingSystemType, member.Name);

                // filter protected member access against .NET types, these can only be accessed from derived types...
                foreach (MemberTracker mt in mg) {
                    if (IsProtectedSetter(mt)) {
                        return new DynamicMetaObject(
                            BindingHelpers.TypeErrorForProtectedMember(Value.UnderlyingSystemType, member.Name),
                            Restrictions.Merge(value.Restrictions).Merge(BindingRestrictions.GetInstanceRestriction(Expression, Value))
                        );
                    }
                }

                // have the default binder perform it's operation against a TypeTracker and then
                // replace the test w/ our own.
                return new DynamicMetaObject(
                    state.Binder.SetMember(
                        member.Name,
                        new DynamicMetaObject(
                            AstUtils.Constant(tt),
                            BindingRestrictions.Empty,
                            tt
                        ),
                        value,
                        AstUtils.Constant(state.Context)
                    ).Expression,
                    Restrictions.Merge(value.Restrictions).Merge(BindingRestrictions.GetInstanceRestriction(Expression, Value))
                );
            }

            return MakeSetMember(member, value);
        }

        public override DynamicMetaObject/*!*/ BindDeleteMember(DeleteMemberBinder/*!*/ member) {
            PerfTrack.NoteEvent(PerfTrack.Categories.Binding, "Type DeleteMember " + Value.UnderlyingSystemType.FullName);
            PerfTrack.NoteEvent(PerfTrack.Categories.BindingTarget, "Type DeleteMember");
            if (Value.IsSystemType) {
                BinderState state = BinderState.GetBinderState(member);

                MemberTracker tt = MemberTracker.FromMemberInfo(Value.UnderlyingSystemType);

                // have the default binder perform it's operation against a TypeTracker and then
                // replace the test w/ our own.
                return new DynamicMetaObject(
                    state.Binder.DeleteMember(
                        member.Name,
                        new DynamicMetaObject(
                            AstUtils.Constant(tt),
                            BindingRestrictions.Empty,
                            tt
                        )
                    ).Expression,
                    BindingRestrictions.GetInstanceRestriction(Expression, Value).Merge(Restrictions)
                );
            }

            return MakeDeleteMember(member);
        }

        #endregion

        #region IPythonGetable Members

        public DynamicMetaObject/*!*/ GetMember(PythonGetMemberBinder/*!*/ member, Expression/*!*/ codeContext) {
            return GetMemberWorker(member, codeContext);
        }

        #endregion

        #region Gets

        private DynamicMetaObject/*!*/ GetMemberWorker(DynamicMetaObjectBinder/*!*/ member, Expression codeContext) {
            PerfTrack.NoteEvent(PerfTrack.Categories.Binding, "Type GetMember " + Value.UnderlyingSystemType.FullName);
            PerfTrack.NoteEvent(PerfTrack.Categories.BindingTarget, "Type GetMember");

            return new MetaGetBinderHelper(this, member, codeContext, GetTypeTest(), MakeMetaTypeTest(Restrict(this.GetRuntimeType()).Expression)).MakeTypeGetMember();
        }
        
        private ValidationInfo MakeMetaTypeTest(Expression self) {

            PythonType metaType = DynamicHelpers.GetPythonType(Value);
            if (!metaType.IsSystemType) {
                int version = metaType.Version;

                return new ValidationInfo(
                    Ast.Call(
                        typeof(PythonOps).GetMethod("CheckTypeVersion"),
                        self,
                        AstUtils.Constant(version)
                    )
                );
            }

            return ValidationInfo.Empty;
        }
        
        /// <summary>
        /// Base class for performing member binding.  Derived classes override Add methods
        /// to produce the actual final result based upon what the GetBinderHelper resolves.
        /// </summary>
        /// <typeparam name="TResult"></typeparam>
        public abstract class GetBinderHelper<TResult> {
            private readonly PythonType _value;
            private readonly string _name;
            private readonly CodeContext/*!*/ _context;

            public GetBinderHelper(PythonType value, CodeContext/*!*/ context, string name) {
                _value = value;
                _name = name;
                _context = context;
            }

            #region Abstract members

            protected abstract TResult Finish(bool metaOnly);

            protected abstract void AddError();

            protected abstract void AddMetaGetAttribute(PythonType metaType, PythonTypeSlot pts);

            protected abstract void AddMetaSlotAccess(PythonType pt, PythonTypeSlot pts);

            protected abstract void AddMetaOldClassAccess();

            protected abstract void AddSlotAccess(PythonType pt, PythonTypeSlot pts);

            protected abstract void AddOldClassAccess(PythonType pt);

            #endregion

            #region Common Get Code

            public TResult MakeTypeGetMember() {
                PythonTypeSlot pts;
                SymbolId name = SymbolTable.StringToId(_name);
                bool isFinal = false, metaOnly = false;
                CodeContext lookupContext = PythonContext.GetContext(_context).DefaultClsBinderState.Context;

                // first look in the meta-class to see if we have a get/set descriptor
                PythonType metaType = DynamicHelpers.GetPythonType(Value);
                foreach (PythonType pt in metaType.ResolutionOrder) {
                    if (pt.TryLookupSlot(lookupContext, name, out pts) && pts.IsSetDescriptor(lookupContext, metaType)) {
                        AddMetaSlotAccess(metaType, pts);
                        if (pts.GetAlwaysSucceeds) {
                            metaOnly = isFinal = true;
                            break;
                        }
                    }
                }

                if (!isFinal) {
                    // then search the MRO to see if we have the value
                    foreach (PythonType pt in Value.ResolutionOrder) {
                        if (pt.IsOldClass) {
                            // mixed new-style/old-style class, search the one slot in it's MRO for the member
                            AddOldClassAccess(pt);
                        } else if (pt.TryLookupSlot(lookupContext, name, out pts)) {
                            AddSlotAccess(pt, pts);

                            if (pts.GetAlwaysSucceeds && pts.IsAlwaysVisible) {
                                isFinal = true;
                                break;
                            }
                        }
                    }
                }

                if (!isFinal) {
                    // then go back to the meta class to see if we have a normal attribute
                    foreach (PythonType pt in metaType.ResolutionOrder) {
                        if (pt.OldClass != null) {
                            // mixed new-style/old-style class, just call our version of __getattribute__
                            // and let it sort it out at runtime.  
                            AddMetaOldClassAccess();
                            isFinal = true;
                            break;
                        } else if (pt.TryLookupSlot(lookupContext, name, out pts)) {
                            AddMetaSlotAccess(metaType, pts);
                            if (pts.GetAlwaysSucceeds) {
                                isFinal = true;
                                break;
                            }
                        }
                    }
                }

                if (!isFinal) {
                    // the member doesn't exist anywhere in the type hierarchy, see if
                    // we define __getattr__ on our meta type.
                    if (metaType.TryResolveSlot(_context, Symbols.GetBoundAttr, out pts) && 
                        !pts.IsSetDescriptor(lookupContext, metaType)) { // we tried get/set descriptors initially
                        
                        AddMetaGetAttribute(metaType, pts);
                    }
                }

                if (!isFinal) {
                    AddError();
                }

                return Finish(metaOnly);
            }
            
            #endregion

            protected PythonType Value {
                get {
                    return _value;
                }
            }
        }

        /// <summary>
        /// Provides the normal meta binder binding.
        /// </summary>
        class MetaGetBinderHelper : GetBinderHelper<DynamicMetaObject> {
            private readonly DynamicMetaObjectBinder _member;
            private readonly MetaPythonType _type;
            private readonly Expression _codeContext;
            private readonly DynamicMetaObject _restrictedSelf;
            private readonly ConditionalBuilder _cb;
            private readonly SymbolId _symName;
            private readonly BinderState _state;
            private readonly ValidationInfo _valInfo, _metaValInfo;
            private ParameterExpression _tmp;

            public MetaGetBinderHelper(MetaPythonType type, DynamicMetaObjectBinder member, Expression codeContext, ValidationInfo validationInfo, ValidationInfo metaValidation)
                : base(type.Value, BinderState.GetBinderState(member).Context, GetGetMemberName(member)) {
                _member = member;
                _codeContext = codeContext;
                _type = type;
                _cb = new ConditionalBuilder(member);
                _symName = SymbolTable.StringToId(GetGetMemberName(member));
                _restrictedSelf = new DynamicMetaObject(
                    AstUtils.Convert(Expression, Value.GetType()),
                    Restrictions.Merge(BindingRestrictions.GetInstanceRestriction(Expression, Value)),
                    Value
                );
                _state = BinderState.GetBinderState(member);
                _valInfo = validationInfo;
                _metaValInfo = metaValidation;
            }

            protected override void AddOldClassAccess(PythonType pt) {
                EnsureTmp();

                _cb.AddCondition(
                    Ast.Call(
                        typeof(PythonOps).GetMethod("OldClassTryLookupOneSlot"),
                        AstUtils.Constant(pt.OldClass),
                        AstUtils.Constant(_symName),
                        _tmp
                    ),
                    _tmp
                );
            }

            private void EnsureTmp() {
                if (_tmp == null) {
                    _tmp = Ast.Variable(typeof(object), "tmp");
                    _cb.AddVariable(_tmp);
                }
            }

            protected override void AddSlotAccess(PythonType pt, PythonTypeSlot pts) {
                pts.MakeGetExpression(
                        _state.Binder,
                        _codeContext,
                        null,
                        AstUtils.Convert(AstUtils.WeakConstant(Value), typeof(PythonType)),
                        _cb
                    );

                if (!pts.IsAlwaysVisible) {
                    _cb.AddCondition(Ast.Call(typeof(PythonOps).GetMethod("IsClsVisible"), _codeContext));
                }
            }

            protected override void AddMetaOldClassAccess() {
                // mixed new-style/old-style class, just call our version of __getattribute__
                // and let it sort it out at runtime.  
                _cb.FinishCondition(
                    Ast.Call(
                        AstUtils.Convert(
                            Expression,
                            typeof(PythonType)
                        ),
                        typeof(PythonType).GetMethod("__getattribute__"),
                        _codeContext,
                        AstUtils.Constant(GetGetMemberName(_member))
                    )
                );
            }

            protected override void AddError() {
                // TODO: We should preserve restrictions from the error
                _cb.FinishCondition(GetFallbackError(_member).Expression);
            }

            protected override void AddMetaGetAttribute(PythonType metaType, PythonTypeSlot pts) {
                EnsureTmp();

                _cb.AddCondition(
                    Ast.Call(
                        typeof(PythonOps).GetMethod("SlotTryGetBoundValue"),
                        _codeContext,
                        AstUtils.Constant(pts, typeof(PythonTypeSlot)),
                        Expression,
                        AstUtils.Constant(metaType),
                        _tmp
                    ),
                    Ast.Dynamic(
                            _state.InvokeOne,
                            typeof(object),
                            _codeContext,
                            _tmp,
                            AstUtils.Constant(GetGetMemberName(_member))
                    )
                );
            }

            protected override void AddMetaSlotAccess(PythonType metaType, PythonTypeSlot pts) {
                ParameterExpression tmp = Ast.Variable(typeof(object), "slotRes");
                pts.MakeGetExpression(_state.Binder,
                    _codeContext,
                    Expression,
                    AstUtils.Constant(metaType),
                    _cb
                );

                if (!pts.IsAlwaysVisible) {
                    _cb.AddCondition(Ast.Call(typeof(PythonOps).GetMethod("IsClsVisible"), _codeContext));
                }
            }

           
            protected override DynamicMetaObject/*!*/ Finish(bool metaOnly) {
                DynamicMetaObject res = _cb.GetMetaObject(_restrictedSelf);

                if (metaOnly) {
                    res = BindingHelpers.AddDynamicTestAndDefer(
                        _member,
                        res,
                        new DynamicMetaObject[] { _type },
                        _metaValInfo
                    );
                } else if (!Value.IsSystemType) {
                    res =  BindingHelpers.AddDynamicTestAndDefer(
                        _member,
                        res,
                        new DynamicMetaObject[] { _type },
                        _valInfo
                    );
                }

                return res;
            }

            private DynamicMetaObject/*!*/ GetFallbackError(DynamicMetaObjectBinder/*!*/ member) {
                if (member is PythonGetMemberBinder) {
                    // accessing from Python, produce our error
                    PythonGetMemberBinder pb = member as PythonGetMemberBinder;
                    if (pb.IsNoThrow) {
                        return new DynamicMetaObject(
                            Expression.Constant(OperationFailed.Value),
                            BindingRestrictions.GetInstanceRestriction(Expression, Value).Merge(Restrictions)
                        );
                    } else {
                        return new DynamicMetaObject(
                            Ast.Throw(
                                Ast.Call(
                                    typeof(PythonOps).GetMethod(
                                        "AttributeErrorForMissingAttribute",
                                        new Type[] { typeof(string), typeof(SymbolId) }
                                    ),
                                    AstUtils.Constant(DynamicHelpers.GetPythonType(Value).Name),
                                    AstUtils.Constant(SymbolTable.StringToId(pb.Name))
                                ),
                                typeof(object)
                            ),
                            BindingRestrictions.GetInstanceRestriction(Expression, Value).Merge(Restrictions)
                        );
                    }
                }

                // let the calling language bind the .NET members
                return ((GetMemberBinder)member).FallbackGetMember(_type);
            }

            private Expression/*!*/ Expression {
                get {
                    return _type.Expression;
                }
            }

            private BindingRestrictions Restrictions {
                get {
                    return _type.Restrictions;
                }
            }


        }

        /// <summary>
        /// Provides delegate based fast binding.
        /// </summary>
        internal class FastGetBinderHelper : GetBinderHelper<TypeGetBase> {
            private readonly PythonGetMemberBinder _binder;
            private readonly int _version;
            private readonly int _metaVersion;
            private bool _canOptimize;
            private List<FastGetDelegate> _gets=  new List<FastGetDelegate>();

            public FastGetBinderHelper(PythonType type, CodeContext context, PythonGetMemberBinder binder)
                : base(type, context, binder.Name) {
                // capture these before we start producing the result
                _version = type.Version;
                _metaVersion = DynamicHelpers.GetPythonType(type).Version;
                _binder = binder;
            }
            
            public Func<CallSite, object, CodeContext, object> GetBinding() {
                Dictionary<string, TypeGetBase> cachedGets = GetCachedGets();

                TypeGetBase dlg;
                lock (cachedGets) {                    
                    if (!cachedGets.TryGetValue(_binder.Name, out dlg) || !dlg.IsValid(Value)) {
                        var binding = MakeTypeGetMember();
                        if (binding != null) {
                            dlg = cachedGets[_binder.Name] = binding;
                        }
                    }
                }

                if (dlg != null && dlg.ShouldUseNonOptimizedSite) {                    
                    return dlg._func;
                }
                return null;
            }

            private Dictionary<string, TypeGetBase> GetCachedGets() {
                if (_binder.IsNoThrow) {
                    Dictionary<string, TypeGetBase> cachedGets = Value._cachedTypeTryGets;
                    if (cachedGets == null) {
                        Interlocked.CompareExchange(
                            ref Value._cachedTypeTryGets,
                            new Dictionary<string, TypeGetBase>(),
                            null);

                        cachedGets = Value._cachedTypeTryGets;
                    }
                    return cachedGets;
                } else {
                    Dictionary<string, TypeGetBase> cachedGets = Value._cachedTypeGets;
                    if (cachedGets == null) {
                        Interlocked.CompareExchange(
                            ref Value._cachedTypeGets,
                            new Dictionary<string, TypeGetBase>(),
                            null);

                        cachedGets = Value._cachedTypeGets;
                    }
                    return cachedGets;
                }
            }

            protected override void AddOldClassAccess(PythonType pt) {
                _gets.Add(new OldClassDelegate(pt, SymbolTable.StringToId(_binder.Name)).Target);
            }

            class OldClassDelegate {
                private readonly WeakReference _type;
                private readonly SymbolId _name;

                public OldClassDelegate(PythonType oldClass, SymbolId name) {
                    _type = oldClass.GetSharedWeakReference();
                    _name = name;
                }

                public bool Target(CodeContext context, object self, out object result) {
                    return PythonOps.OldClassTryLookupOneSlot(((PythonType)_type.Target).OldClass, _name, out result);
                }
            }

            protected override void AddSlotAccess(PythonType pt, PythonTypeSlot pts) {
                if (pts.CanOptimizeGets) {
                    _canOptimize = true;
                }

                if (pts.IsAlwaysVisible) {
                    _gets.Add(new SlotAccessDelegate(pts, Value).Target);
                } else {
                    _gets.Add(new SlotAccessDelegate(pts, Value).TargetCheckCls);
                }
            }

            class SlotAccessDelegate {
                private readonly PythonTypeSlot _slot;
                private readonly PythonType _owner;
                private readonly WeakReference _weakOwner;
                private readonly WeakReference _weakSlot;
                
                public SlotAccessDelegate(PythonTypeSlot slot, PythonType owner) {
                    if (owner.IsSystemType) {
                        _owner = owner;
                        _slot = slot;
                    } else {
                        _weakOwner = owner.GetSharedWeakReference();
                        _weakSlot = new WeakReference(slot);
                    }
                }

                public bool TargetCheckCls(CodeContext context, object self, out object result) {
                    if (PythonOps.IsClsVisible(context)) {
                        return Slot.TryGetValue(context, null, Type, out result);
                    }

                    result = null;
                    return false;
                }
                
                public bool Target(CodeContext context, object self, out object result) {
                    return Slot.TryGetValue(context, null, Type, out result);
                }

                public bool MetaTargetCheckCls(CodeContext context, object self, out object result) {
                    if (PythonOps.IsClsVisible(context)) {
                        return Slot.TryGetValue(context, self, Type, out result);
                    }

                    result = null;
                    return false;
                }

                public bool MetaTarget(CodeContext context, object self, out object result) {
                    return Slot.TryGetValue(context, self, Type, out result);
                }

                private PythonType Type {
                    get {
                        return _owner ?? (PythonType)_weakOwner.Target;
                    }
                }

                private PythonTypeSlot Slot {
                    get {
                        return _slot ?? (PythonTypeSlot)_weakSlot.Target;
                    }
                }
            }

            protected override void AddMetaOldClassAccess() {
                // mixed new-style/old-style class, just call our version of __getattribute__
                // and let it sort it out at runtime.  
                _gets.Add(new MetaOldClassDelegate(_binder.Name).Target);
            }

            class MetaOldClassDelegate {
                private readonly string _name;
                public MetaOldClassDelegate(string name) {
                    _name = name;
                }

                public bool Target(CodeContext context, object self, out object result) {
                    result = ((PythonType)self).__getattribute__(context, _name);
                    return true;
                }
            }

            protected override void AddError() {
                if (_binder.IsNoThrow) {
                    _gets.Add(new ErrorBinder(_binder.Name).TargetNoThrow);
                } else {
                    _gets.Add(new ErrorBinder(_binder.Name).Target);
                }
            }

            protected override void AddMetaGetAttribute(PythonType metaType, PythonTypeSlot pts) {
                _gets.Add(new MetaGetAttributeDelegate(pts, metaType, _binder.Name).Target);
            }

            class MetaGetAttributeDelegate {
                private readonly string _name;
                private readonly PythonType _metaType;
                private readonly WeakReference _weakMetaType;
                private readonly PythonTypeSlot _slot;
                private readonly WeakReference _weakSlot;

                public MetaGetAttributeDelegate(PythonTypeSlot slot, PythonType metaType, string name) {
                    _name = name;

                    if (metaType.IsSystemType) {
                        _metaType = metaType;
                        _slot = slot;
                    } else {
                        _weakMetaType = metaType.GetSharedWeakReference();
                        _weakSlot = new WeakReference(slot);
                    }
                }

                public bool Target(CodeContext context, object self, out object result) {
                    object value;

                    if (Slot.TryGetValue(context, self, MetaType, out value)) {
                        result = PythonOps.CallWithContext(context, value, _name);
                        return true;
                    }

                    result = null;
                    return false;
                }

                private PythonType MetaType {
                    get {
                        return _metaType ?? (PythonType)_weakMetaType.Target;
                    }
                }

                private PythonTypeSlot Slot {
                    get {
                        return _slot ?? (PythonTypeSlot)_weakSlot.Target;
                    }
                }
            }

            protected override void AddMetaSlotAccess(PythonType metaType, PythonTypeSlot pts) {
                if (pts.CanOptimizeGets) {
                    _canOptimize = true;
                }

                if (pts.IsAlwaysVisible) {
                    _gets.Add(new SlotAccessDelegate(pts, metaType).MetaTarget);
                } else {
                    _gets.Add(new SlotAccessDelegate(pts, metaType).MetaTargetCheckCls);
                }
            }


            protected override TypeGetBase/*!*/ Finish(bool metaOnly) {
                if (metaOnly) {
                    if (DynamicHelpers.GetPythonType(Value).IsSystemType) {
                        return new SystemTypeGet(_binder, _gets.ToArray(), Value, metaOnly, _canOptimize);
                    } else {
                        return new TypeGet(_binder, _gets.ToArray(), metaOnly ? _metaVersion : _version, metaOnly, _canOptimize);
                    }
                } else {
                    if (Value.IsSystemType) {
                        return new SystemTypeGet(_binder, _gets.ToArray(), Value, metaOnly, _canOptimize);
                    }
                    return new TypeGet(_binder, _gets.ToArray(), metaOnly ? _metaVersion : _version, metaOnly, _canOptimize);
                }
            }

            class ErrorBinder {
                private readonly string _name;

                public ErrorBinder(string name) {
                    _name = name;
                }

                public bool TargetNoThrow(CodeContext context, object self, out object result) {
                    result = OperationFailed.Value;
                    return true;
                }

                public bool Target(CodeContext context, object self, out object result) {
                    throw PythonOps.AttributeErrorForMissingAttribute(
                        DynamicHelpers.GetPythonType(self).Name,
                        SymbolTable.StringToId(_name));
                }
            }
        }
        
        #endregion

        #region Sets

        private DynamicMetaObject/*!*/ MakeSetMember(SetMemberBinder/*!*/ member, DynamicMetaObject/*!*/ value) {
            DynamicMetaObject self = Restrict(typeof(PythonType));

            return BindingHelpers.AddDynamicTestAndDefer(
                member,
                new DynamicMetaObject(
                    Ast.Call(
                        typeof(PythonOps).GetMethod("PythonTypeSetCustomMember"),
                        AstUtils.Constant(BinderState.GetBinderState(member).Context),
                        self.Expression,
                        AstUtils.Constant(SymbolTable.StringToId(member.Name)),
                        AstUtils.Convert(
                            value.Expression,
                            typeof(object)
                        )
                    ),
                    self.Restrictions.Merge(value.Restrictions)
                ),
                new DynamicMetaObject[] { this, value },
                TestUserType()
            );
        }

        private bool IsProtectedSetter(MemberTracker mt) {
            PropertyTracker pt = mt as PropertyTracker;
            if (pt != null) {
                MethodInfo mi = pt.GetSetMethod(true);
                if (mi != null && (mi.IsFamily || mi.IsFamilyOrAssembly)) {
                    return true;
                }
            }

            FieldTracker ft = mt as FieldTracker;
            if (ft != null) {
                return ft.Field.IsFamily || ft.Field.IsFamilyOrAssembly;
            }

            return false;
        }

        #endregion

        #region Deletes

        private DynamicMetaObject/*!*/ MakeDeleteMember(DeleteMemberBinder/*!*/ member) {
            DynamicMetaObject self = Restrict(typeof(PythonType));
            return BindingHelpers.AddDynamicTestAndDefer(
                member,
                new DynamicMetaObject(
                    Ast.Call(
                        typeof(PythonOps).GetMethod("PythonTypeDeleteCustomMember"),
                        AstUtils.Constant(BinderState.GetBinderState(member).Context),
                        self.Expression,
                        AstUtils.Constant(SymbolTable.StringToId(member.Name))
                    ),
                    self.Restrictions
                ),
                new DynamicMetaObject[] { this },
                TestUserType()
            );
        }

        #endregion

        #region Helpers

        private ValidationInfo/*!*/ TestUserType() {
            return new ValidationInfo(
                Ast.Not(
                    Ast.Call(
                        typeof(PythonOps).GetMethod("IsPythonType"),
                        AstUtils.Convert(
                            Expression,
                            typeof(PythonType)
                        )
                    )
                )
            );
        }

        #endregion
    }
}