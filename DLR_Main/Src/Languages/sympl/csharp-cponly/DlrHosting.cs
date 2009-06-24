using System;
using System.Collections.Generic;
//using System.Linq;
using System.Text;
using Microsoft.Scripting.Runtime;

#if USE35
// Needed for type language implementers need to support DLR Hosting, such as
// ScriptCode.
using Microsoft.Scripting;
// Needed for IDynamicMetaObjectProvider and friends.
using Microsoft.Scripting;
using Microsoft.Linq.Expressions;
using Microsoft;
#else
using System.Linq.Expressions;
using System.Dynamic;
using System.Linq;
#endif

using Microsoft.Scripting.Utils;

using Path = System.IO.Path;


namespace SymplSample.Hosting {

    // The Sympl LanguageContext is the representation of the language and the
    // workhorse at the language implementation level for supporting the DLR
    // Hosting APIs.  It has many members on it, but we only have to override
    // a couple to get basic DLR hosting support enabled.
    //
    // One extra override we provide is GetService<T> so that we can return the
    // original Sympl hosting object we build before supporting DLR hosting.
    // program.cs uses this to create symbols in it's little REPL.
    //
    // Other things a LanguageContext might do are provide an implementation for
    // ObjectOperations, offer other services (exception formatting, colorization,
    // tokenization, etc), provide ExecuteProgram semantics, and so on.
    //
    public sealed class SymplLangContext : LanguageContext {
        private readonly Sympl _sympl;

        public SymplLangContext(ScriptDomainManager manager,
                                IDictionary<string, object> options)
            : base(manager) {
            // TODO: parse options
            // TODO: register event  manager.AssemblyLoaded
            _sympl = new Sympl(manager.GetLoadedAssemblyList(), manager.Globals);
        }

        // This is all that's needed to run code on behalf of language-independent
        // DLR hosting.  Sympl defines its own subtype of ScriptCode.
        //
        protected override ScriptCode CompileSourceCode(
                SourceUnit sourceUnit, CompilerOptions options, ErrorSink errorSink) {
            using (var reader = sourceUnit.GetReader()) {
                try {
                    switch (sourceUnit.Kind) {
                        case SourceCodeKind.SingleStatement:
                        case SourceCodeKind.Expression:
                        case SourceCodeKind.AutoDetect:
                        case SourceCodeKind.InteractiveCode:
                            return new SymplScriptCode(
                                _sympl, _sympl.ParseExprToLambda(reader),
                                sourceUnit);
                        case SourceCodeKind.Statements:
                        case SourceCodeKind.File:
                            return new SymplScriptCode(
                                _sympl,
                                _sympl.ParseFileToLambda(sourceUnit.Path, reader),
                                sourceUnit);
                        default:
                            throw Assert.Unreachable;
                    }
                }
                catch (Exception e) {
                    // Real language implementation would have a specific type
                    // of exception.  Also, they would pass errorSink down into
                    // the parser and add messages while doing tighter error
                    // recovery and continuing to parse.
                    errorSink.Add(sourceUnit, e.Message, SourceSpan.None, 0,
                                  Severity.FatalError);
                    return null;
                }
            }
        }

        // We expose the original Sympl hosting object for creating Symbols or
        // other pre-existing uses of it (see Main in program.cs).
        //
        public override TService GetService<TService>(params object[] args) {
            if (typeof(TService) == typeof(Sympl)) {
                return (TService)(object)_sympl;
            }
            return base.GetService<TService>(args);
        }

    } //SymplLangContext

    
    
    // This class represents Sympl compiled code for the language implementation
    // support the DLR Hosting APIs require.  The DLR Hosting APIs call on
    // this class to run code in a new ScriptScope (represented as Scope at the
    // language implementation level or a provided ScriptScope.
    //
    public sealed class SymplScriptCode : ScriptCode {
        private readonly Expression<Func<Sympl,
                                         IDynamicMetaObjectProvider, object>>
                         _lambda;
        private readonly Sympl _sympl;
        private Func<Sympl, IDynamicMetaObjectProvider, object> _compiledLambda;

        public SymplScriptCode(
             Sympl sympl, 
             Expression<Func<Sympl, IDynamicMetaObjectProvider, object>> lambda,
             SourceUnit sourceUnit)
             : base(sourceUnit) {
            _lambda = lambda;
            _sympl = sympl;
        }

        public override object Run() {
            return Run(new Scope());
        }

        public override object Run(Scope scope) {
            if (_compiledLambda == null) {
                _compiledLambda = _lambda.Compile();
            }
            var module = new SymplModuleDlrScope(scope);
            if (this.SourceUnit.Kind == SourceCodeKind.File) {
                // Simple way to convey script rundir for RuntimeHelpers.SymplImport
                // to load .sympl files relative to the current script file.
                DynamicObjectHelpers.SetMember(module, "__file__",
                                               Path.GetFullPath(this.SourceUnit.Path));
            }
            return _compiledLambda(_sympl, module);
        }
    }



    // This class represents Sympl modules or globals scopes.  We derive from
    // DynamicObject for an easy IDynamicMetaObjectProvider implementation, and
    // just hold onto the DLR internal scope object.  Languages typically have
    // their own scope so that 1) it can flow around an a dynamic object and 2)
    // to dope in any language-specific behaviors, such as case-INsensitivity.
    //
    public sealed class SymplModuleDlrScope : DynamicObject {
        private readonly Scope _scope;

        public SymplModuleDlrScope(Scope scope) {
            _scope = scope;
        }

        public override bool TryGetMember(GetMemberBinder binder, out object result) {
            return _scope.TryGetName(SymbolTable.StringToCaseInsensitiveId(binder.Name),
                                     out result);
        }

        public override bool TrySetMember(SetMemberBinder binder, object value) {
            _scope.SetName(SymbolTable.StringToId(binder.Name), value);
            return true;
        }
    }


} // SymplSample.Hosting namespace
