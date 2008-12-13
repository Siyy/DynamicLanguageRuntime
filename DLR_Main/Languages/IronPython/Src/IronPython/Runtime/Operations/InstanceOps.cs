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
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.Reflection;
using System.Runtime.CompilerServices;
using Microsoft.Runtime.CompilerServices;

using System.Runtime.InteropServices;
using IronPython.Runtime.Types;
using Microsoft.Scripting;
using Microsoft.Scripting.Generation;
using Microsoft.Scripting.Runtime;
using Microsoft.Scripting.Utils;

namespace IronPython.Runtime.Operations {
    /// <summary>
    /// InstanceOps contains methods that get added to CLS types depending on what
    /// methods and constructors they define. These have not been added directly to
    /// PythonType since they need to be added conditionally.
    /// 
    /// Possibilities include:
    /// 
    ///     __new__, one of 3 __new__ sets can be added:
    ///         DefaultNew - This is the __new__ used for a PythonType (list, dict, object, etc...) that
    ///             has only 1 default public constructor that takes no parameters.  These types are 
    ///             mutable types, and __new__ returns a new instance of the type, and __init__ can be used
    ///             to re-initialize the types.  This __new__ allows an unlimited number of arguments to
    ///             be passed if a non-default __init__ is also defined.
    ///
    ///         NonDefaultNew - This is used when a type has more than one constructor, or only has one
    ///             that takes more than zero parameters.  This __new__ does not allow an arbitrary # of
    ///             extra arguments.
    /// 
    ///         DefaultNewCls - This is the default new used for CLS types that have only a single ctor
    ///             w/ an arbitray number of arguments.  This constructor allows setting of properties
    ///             based upon an extra set of kw-args, e.g.: System.Windows.Forms.Button(Text='abc').  It
    ///             is only used on non-Python types.
    /// 
    ///     __init__:
    ///         For types that do not define __init__ we have an __init__ function that takes an
    ///         unlimited number of arguments and does nothing.  All types share the same reference
    ///         to 1 instance of this.
    /// 
    ///     next: Defined when a type is an enumerator to expose the Python iter protocol.
    /// 
    /// 
    ///     repr: Added for types that override ToString
    /// 
    ///     get: added for types that implement IDescriptor
    /// </summary>
    public static class InstanceOps {
        [MultiRuntimeAware]
        private static BuiltinFunction _New;
        internal static readonly BuiltinFunction NewCls = CreateFunction("__new__", "DefaultNew", "DefaultNewClsKW");
        internal static readonly BuiltinFunction OverloadedNew = CreateFunction("__new__", "OverloadedNewBasic", "OverloadedNewKW", "OverloadedNewClsKW");
        internal static readonly BuiltinFunction NonDefaultNewInst = CreateNonDefaultNew();
        [MultiRuntimeAware]
        internal static BuiltinMethodDescriptor _Init;

        internal static BuiltinMethodDescriptor Init {
            get {
                if (_Init == null) {
                    _Init = GetInitMethod();
                }
                return _Init;
            }
        }
        

        internal static BuiltinFunction New {
            get {
                if (_New == null) {
                    _New = (BuiltinFunction)PythonTypeOps.GetSlot(
                        TypeInfo.GetExtensionMemberGroup(typeof(object), typeof(ObjectOps).GetMember("__new__")),
                        "__new__",
                        false // privateBinding
                    );
                }
                return _New;
            }
        }

        internal static BuiltinFunction CreateNonDefaultNew() {
            return CreateFunction("__new__", "NonDefaultNew", "NonDefaultNewKW", "NonDefaultNewKWNoParams");
        }

        public static object DefaultNew(CodeContext context, PythonType type\u00F8, params object[] args\u00F8) {
            if (type\u00F8 == null) throw PythonOps.TypeError("__new__ expected type object, got {0}", PythonOps.Repr(context, DynamicHelpers.GetPythonType(type\u00F8)));

            CheckInitArgs(context, null, args\u00F8, type\u00F8);

            return type\u00F8.CreateInstance(context);
        }

        public static object DefaultNewClsKW(CodeContext context, PythonType type\u00F8, [ParamDictionary] IAttributesCollection kwargs\u00F8, params object[] args\u00F8) {
            object res = DefaultNew(context, type\u00F8, args\u00F8);

            if (kwargs\u00F8.Count > 0) {
                foreach (KeyValuePair<object, object> kvp in (IDictionary<object, object>)kwargs\u00F8) {
                    PythonOps.SetAttr(context,
                        res,
                        SymbolTable.StringToId(kvp.Key.ToString()),
                        kvp.Value);
                }
            }
            return res;
        }

        public static object OverloadedNewBasic(CodeContext context, SiteLocalStorage<CallSite<Func<CallSite, CodeContext, object, object[], object>>> storage, BuiltinFunction overloads\u00F8, PythonType type\u00F8, params object[] args\u00F8) {
            if (type\u00F8 == null) throw PythonOps.TypeError("__new__ expected type object, got {0}", PythonOps.Repr(context, DynamicHelpers.GetPythonType(type\u00F8)));
            if (args\u00F8 == null) args\u00F8 = new object[1];
            return overloads\u00F8.Call(context, storage, null, args\u00F8);
        }

        public static object OverloadedNewKW(CodeContext context, BuiltinFunction overloads\u00F8, PythonType type\u00F8, [ParamDictionary] IAttributesCollection kwargs\u00F8) {
            if (type\u00F8 == null) throw PythonOps.TypeError("__new__ expected type object, got {0}", PythonOps.Repr(context, DynamicHelpers.GetPythonType(type\u00F8)));
            
            return overloads\u00F8.Call(context, null, null, ArrayUtils.EmptyObjects, kwargs\u00F8);
        }

        public static object OverloadedNewClsKW(CodeContext context, BuiltinFunction overloads\u00F8, PythonType type\u00F8, [ParamDictionary] IAttributesCollection kwargs\u00F8, params object[] args\u00F8) {
            if (type\u00F8 == null) throw PythonOps.TypeError("__new__ expected type object, got {0}", PythonOps.Repr(context, DynamicHelpers.GetPythonType(type\u00F8)));
            if (args\u00F8 == null) args\u00F8 = new object[1];

            return overloads\u00F8.Call(context, null, null, args\u00F8, kwargs\u00F8);
        }

        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA1801:ReviewUnusedParameters", MessageId = "self"), System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA1801:ReviewUnusedParameters", MessageId = "context"), System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA1801:ReviewUnusedParameters", MessageId = "args\u00F8")]
        public static void DefaultInit(CodeContext context, object self, params object[] args\u00F8) {
        }

        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA1801:ReviewUnusedParameters", MessageId = "self"), System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA1801:ReviewUnusedParameters", MessageId = "kwargs\u00F8"), System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA1801:ReviewUnusedParameters", MessageId = "context"), System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA1801:ReviewUnusedParameters", MessageId = "args\u00F8")]
        public static void DefaultInitKW(CodeContext context, object self, [ParamDictionary] IAttributesCollection kwargs\u00F8, params object[] args\u00F8) {
        }

        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA1801:ReviewUnusedParameters", MessageId = "context")]
        [StaticExtensionMethod]
        public static object NonDefaultNew(CodeContext context, PythonType type\u00F8, params object[] args\u00F8) {
            if (type\u00F8 == null) throw PythonOps.TypeError("__new__ expected type object, got {0}", PythonOps.Repr(context, DynamicHelpers.GetPythonType(type\u00F8)));
            if (args\u00F8 == null) args\u00F8 = new object[1];
            return type\u00F8.CreateInstance(context, args\u00F8);
        }

        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA1801:ReviewUnusedParameters", MessageId = "context")]
        [StaticExtensionMethod]
        public static object NonDefaultNewKW(CodeContext context, PythonType type\u00F8, [ParamDictionary] IAttributesCollection kwargs\u00F8, params object[] args\u00F8) {
            if (type\u00F8 == null) throw PythonOps.TypeError("__new__ expected type object, got {0}", PythonOps.Repr(context, DynamicHelpers.GetPythonType(type\u00F8)));
            if (args\u00F8 == null) args\u00F8 = new object[1];

            string []names;
            GetKeywordArgs(kwargs\u00F8, args\u00F8, out args\u00F8, out names);
            return type\u00F8.CreateInstance(context, args\u00F8, names);
        }

        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA1801:ReviewUnusedParameters", MessageId = "context")]
        [StaticExtensionMethod]
        public static object NonDefaultNewKWNoParams(CodeContext context, PythonType type\u00F8, [ParamDictionary] IAttributesCollection kwargs\u00F8) {
            if (type\u00F8 == null) throw PythonOps.TypeError("__new__ expected type object, got {0}", PythonOps.Repr(context, DynamicHelpers.GetPythonType(type\u00F8)));

            string[] names;
            object[] args;
            GetKeywordArgs(kwargs\u00F8, ArrayUtils.EmptyObjects, out args, out names);
            return type\u00F8.CreateInstance(context, args, names);
        }

        public static object IterMethod(CodeContext/*!*/ context, object self) {
            return self;
        }

        public static object NextMethod(object self) {
            IEnumerator i = (IEnumerator)self;
            if (i.MoveNext()) return i.Current;
            throw PythonOps.StopIteration();
        }

        public static int LengthMethod(ICollection self) {
            return self.Count;
        }

        public static int GenericLengthMethod<T>(ICollection<T> self) {
            return self.Count;
        }

        public static string SimpleRepr(object self) {
            return String.Format("<{0} object at {1}>",
                PythonTypeOps.GetName(self),
                PythonOps.HexId(self));
        }

        public static string FancyRepr(object self) {
            PythonType pt = (PythonType)DynamicHelpers.GetPythonType(self);
            // we can't call ToString on a UserType because we'll stack overflow, so
            // only do FancyRepr for reflected types.
            if (pt.IsSystemType) {
                string toStr = self.ToString();
                if (toStr == null) toStr = String.Empty;

                // get the type name to display (CLI name or Python name)
                Type type = pt.UnderlyingSystemType;
                string typeName = type.FullName;

                // Get the underlying .ToString() representation.  Truncate multiple
                // lines, and don't display it if it's object's default representation (type name)

                // skip initial empty lines:
                int i = 0;
                while (i < toStr.Length && (toStr[i] == '\r' || toStr[i] == '\n')) i++;

                // read the first non-empty line:
                int j = i;
                while (j < toStr.Length && toStr[j] != '\r' && toStr[j] != '\n') j++;

                // skip following empty lines:
                int k = j;
                while (k < toStr.Length && (toStr[k] == '\r' || toStr[k] == '\n')) k++;

                if (j > i) {
                    string first_non_empty_line = toStr.Substring(i, j - i);
                    bool has_multiple_non_empty_lines = k < toStr.Length;

                    return String.Format("<{0} object at {1} [{2}{3}]>",
                        typeName,
                        PythonOps.HexId(self),
                        first_non_empty_line,
                        has_multiple_non_empty_lines ? "..." : String.Empty);

                } else {
                    return String.Format("<{0} object at {1}>",
                             typeName,
                             PythonOps.HexId(self));
                }
            }
            return SimpleRepr(self);
        }

        public static object ReprHelper(CodeContext context, object self) {
            return ((ICodeFormattable)self).__repr__(context);
        }

        public static string ToStringMethod(object self) {
            string res = self.ToString();
            if (res == null) return String.Empty;
            return res;
        }

        // Value equality helpers:  These are the default implementation for classes that implement
        // IValueEquality.  We promote the ReflectedType to having these helper methods which will
        // automatically test the type and return NotImplemented for mixed comparisons.  For non-mixed
        // comparisons we have a fully optimized version which returns bool.

        public static bool ValueEqualsMethod<T>(T x, [NotNull]T y) 
            where T : IValueEquality {
            return x.ValueEquals(y);
        }

        public static bool ValueNotEqualsMethod<T>(T x, [NotNull]T y)
            where T : IValueEquality {
            return !x.ValueEquals(y);
        }

        [return: MaybeNotImplemented]
        public static object ValueEqualsMethod<T>([NotNull]T x, object y) 
            where T : IValueEquality {
            if (!(y is T)) return NotImplementedType.Value;

            return ScriptingRuntimeHelpers.BooleanToObject(x.ValueEquals(y));
        }

        [return: MaybeNotImplemented]
        public static object ValueNotEqualsMethod<T>([NotNull]T x, object y) 
            where T : IValueEquality {
            if (!(y is T)) return NotImplementedType.Value;

            return ScriptingRuntimeHelpers.BooleanToObject(!x.ValueEquals(y));
        }

        [return: MaybeNotImplemented]
        public static object ValueEqualsMethod<T>(object y, [NotNull]T x)
            where T : IValueEquality {
            if (!(y is T)) return NotImplementedType.Value;

            return ScriptingRuntimeHelpers.BooleanToObject(x.ValueEquals(y));
        }

        [return: MaybeNotImplemented]
        public static object ValueNotEqualsMethod<T>(object y, [NotNull]T x)
            where T : IValueEquality {
            if (!(y is T)) return NotImplementedType.Value;

            return ScriptingRuntimeHelpers.BooleanToObject(x.ValueEquals(y));
        }

        // TODO: Remove me
        public static object ValueHashMethod(object x) {
            return ((IValueEquality)x).GetValueHashCode();
        }

        public static int GetHashCodeMethod(object x) {
            return x.GetHashCode();
        }

        public static bool EqualsMethod(object x, object y) {
            return x.Equals(y);
        }

        public static bool NotEqualsMethod(object x, object y) {
            return !x.Equals(y);
        }

        /// <summary>
        /// Provides the implementation of __enter__ for objects which implement IDisposable.
        /// </summary>
        public static object EnterMethod(IDisposable/*!*/ self) {
            return self;
        }

        /// <summary>
        /// Provides the implementation of __exit__ for objects which implement IDisposable.
        /// </summary>
        public static void ExitMethod(IDisposable/*!*/ self, object exc_type, object exc_value, object exc_back) {
            self.Dispose();
        }

        [PropertyMethod, StaticExtensionMethod]
        public static List/*!*/ Get__all__<T>(CodeContext/*!*/ context) {
            Debug.Assert(typeof(T).IsSealed && typeof(T).IsAbstract, "__all__ should only be produced for static members"); 

            PythonType pt = DynamicHelpers.GetPythonTypeFromType(typeof(T));

            List names = new List();
            foreach (string name in pt.GetMemberNames(context)) {
                object res;
                if (IsStaticTypeMemberInAll(context, pt, SymbolTable.StringToId(name), out res)) {
                    names.AddNoLock(name);
                }
            }

            return names;
        }

        /// <summary>
        /// Determines if a type member can be imported.  This is used to treat static types like modules.
        /// </summary>
        private static bool IsStaticTypeMemberInAll(CodeContext/*!*/ context, PythonType/*!*/ pt, SymbolId name, out object res) {
            PythonTypeSlot pts;
            res = null;
            if (pt.TryResolveSlot(context, name, out pts)) {
                if (name == Symbols.Doc || name == Symbols.Class) {
                    // these exist but we don't want to clobber __doc__ on import * or bring in __class__
                    return false;
                } else if (pts is ReflectedGetterSetter) {
                    // property or indexer, these fetch the value at runtime, the user needs to explicitly
                    // import them using from type import property
                    return false;
                }

                ReflectedField rf = pts as ReflectedField;
                if (rf != null && !rf.info.IsInitOnly && !rf.info.IsLiteral) {
                    // only bring in read-only fields, if the value can change the user needs to explicitly
                    // import by name
                    return false;
                }

                BuiltinMethodDescriptor method = pts as BuiltinMethodDescriptor;
                if (method != null && (!method.DeclaringType.IsSealed || !method.DeclaringType.IsAbstract)) {
                    // inherited object member on a static class (GetHashCode, Equals, etc...)
                    return false;
                }

                BuiltinFunction bf = pts as BuiltinFunction;
                if (bf != null && (!bf.DeclaringType.IsSealed || !bf.DeclaringType.IsAbstract)) {
                    // __new__/ReferenceEquals inherited from object
                    return false;
                }

                if (pts.TryGetValue(context, null, pt, out res)) {
                    return true;
                }
            }

            res = null;
            return false;
        }

        /// <summary>
        /// Implements __contains__ for types implementing IEnumerable of T.
        /// </summary>
        public static bool ContainsGenericMethod<T>(CodeContext/*!*/ context, IEnumerable<T> enumerable, T value) {
            foreach(T item in enumerable) {
                if (PythonOps.EqualRetBool(context, item, value)) {
                    return true;
                }
            }

            return false;
        }

        /// <summary>
        /// Implements __contains__ for types implementing IEnumerable
        /// </summary>
        public static bool ContainsMethod(CodeContext/*!*/ context, IEnumerable enumerable, object value) {
            IEnumerator ie = enumerable.GetEnumerator();
            while (ie.MoveNext()) {
                if (PythonOps.EqualRetBool(context, ie.Current, value)) {
                    return true;
                }
            }

            return false;
        }

        /// <summary>
        /// Implements __contains__ for types implementing IEnumerable of T.
        /// </summary>
        public static bool ContainsGenericMethodIEnumerator<T>(CodeContext/*!*/ context, IEnumerator<T> enumerator, T value) {
            while (enumerator.MoveNext()) {
                if (PythonOps.EqualRetBool(context, enumerator.Current, value)) {
                    return true;
                }
            }

            return false;
        }

        /// <summary>
        /// Implements __contains__ for types implementing IEnumerable
        /// </summary>
        public static bool ContainsMethodIEnumerator(CodeContext/*!*/ context, IEnumerator enumerator, object value) {
            while (enumerator.MoveNext()) {
                if (PythonOps.EqualRetBool(context, enumerator.Current, value)) {
                    return true;
                }
            }

            return false;
        }

        public static object GetMethod(CodeContext context, object self, object instance, [Optional]object typeContext) {
            PythonTypeSlot dts = self as PythonTypeSlot;
            PythonType dt = typeContext as PythonType;

            Debug.Assert(dts != null);

            object res;
            if (dts.TryGetValue(context, instance, dt, out res))
                return res;

            // context is hiding __get__
            throw PythonOps.AttributeErrorForMissingAttribute(dt == null ? "?" : dt.Name, Symbols.GetDescriptor);
        }

#if !SILVERLIGHT
        /// <summary>
        /// Implements __reduce_ex__ for .NET types which are serializable.  This uses the .NET
        /// serializer to get a string of raw data which can be serialized.
        /// </summary>
        public static PythonTuple SerializeReduce(CodeContext/*!*/ context, object/*!*/ self, int protocol) {
            PythonTuple data = ClrModule.Serialize(self);

            object deserializeNew;
            bool res = PythonContext.GetContext(context).ClrModule.TryGetName(
                SymbolTable.StringToId("Deserialize"),
                out deserializeNew
            );
            Debug.Assert(res);

            return PythonTuple.MakeTuple(
                deserializeNew,                 // function to call, clr.DeserializeNew 
                data,                           // data to pass to it - our type & the raw data from the .NET serializer
                null                            // state, unused
            );
        }
#endif

        public static string Format(IFormattable formattable, string format) {
            return formattable.ToString(format, null);
        }

        internal static void CheckInitArgs(CodeContext context, IAttributesCollection dict, object[] args, PythonType pt) {
            PythonTypeSlot dts;
            object initObj;
            if (((args != null && args.Length > 0) || (dict != null && dict.Count > 0)) &&
                (pt.TryResolveSlot(context, Symbols.Init, out dts)) && dts.TryGetValue(context, null, pt, out initObj) &&
                initObj == Init) {

                throw PythonOps.TypeError("default __new__ does not take parameters");
            }
        }

        private static BuiltinMethodDescriptor GetInitMethod() {
            PythonTypeSlot pts;
            TypeCache.Object.TryResolveSlot(DefaultContext.Default, Symbols.Init, out pts);

            Debug.Assert(pts != null);
            return (BuiltinMethodDescriptor)pts;
        }

        private static BuiltinFunction CreateFunction(string name, params string[] methodNames) {
            MethodBase[] methods = new MethodBase[methodNames.Length];
            for (int i = 0; i < methods.Length; i++) {
                methods[i] = typeof(InstanceOps).GetMethod(methodNames[i]);
            }
            return BuiltinFunction.MakeMethod(name, methods, typeof(object), FunctionType.Function | FunctionType.AlwaysVisible);
        }

        private static void GetKeywordArgs(IAttributesCollection dict, object[] args, out object[] finalArgs, out string[] names) {
            finalArgs = new object[args.Length + dict.Count];
            Array.Copy(args, finalArgs, args.Length);
            names = new string[dict.Count];
            int i = 0;
            foreach (KeyValuePair<object, object> kvp in (IDictionary<object, object>)dict) {
                names[i] = (string)kvp.Key;
                finalArgs[i + args.Length] = kvp.Value;
                i++;
            }
        }
    }
}