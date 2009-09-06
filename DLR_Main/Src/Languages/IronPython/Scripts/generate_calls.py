#####################################################################################
#
#  Copyright (c) Microsoft Corporation. All rights reserved.
#
# This source code is subject to terms and conditions of the Microsoft Public License. A 
# copy of the license can be found in the License.html file at the root of this distribution. If 
# you cannot locate the  Microsoft Public License, please send an email to 
# ironpy@microsoft.com. By using this source code in any fashion, you are agreeing to be bound 
# by the terms of the Microsoft Public License.
#
# You must not remove this notice, or any other, from this software.
#
#
#####################################################################################

import sys
from generate import generate

MAX_ARGS = 16

def make_params(nargs, *prefix):
    params = ["object arg%d" % i for i in range(nargs)]
    return ", ".join(list(prefix) + params)

def make_params1(nargs, prefix=("CodeContext context",)):
    params = ["object arg%d" % i for i in range(nargs)]
    return ", ".join(list(prefix) + params)

def make_args(nargs, *prefix):
    params = ["arg%d" % i for i in range(nargs)]
    return ", ".join(list(prefix) + params)

def make_args1(nargs, prefix, start=0):
    args = ["arg%d" % i for i in range(start, nargs)]
    return ", ".join(list(prefix) + args)

def make_calltarget_type_args(nargs):
    return ', '.join(['PythonFunction'] + ['object'] * (nargs + 1))

def gen_args_comma(nparams, comma):
    args = ""
    for i in xrange(nparams):
        args = args + comma + ("object arg%d" % i)
        comma = ", "
    return args

def gen_args(nparams):
    return gen_args_comma(nparams, "")

def gen_args_call(nparams, *prefix):
    args = ""
    comma = ""
    for i in xrange(nparams):
        args = args + comma +("arg%d" % i)
        comma = ", "
    if prefix:
        if args:
            args = prefix[0] + ', ' + args
        else:
            args = prefix[0]
    return args

def gen_args_array(nparams):
    args = gen_args_call(nparams)
    if args: return "{ " + args + " }"
    else: return "{ }"

def gen_callargs(nparams):
    args = ""
    comma = ""
    for i in xrange(nparams):
        args = args + comma + ("callArgs[%d]" % i)
        comma = ","
    return args

def gen_args_paramscall(nparams):
    args = ""
    comma = ""
    for i in xrange(nparams):
        args = args + comma + ("args[%d]" % i)
        comma = ","
    return args

builtin_function_switch_template = """case %(argCount)d:
    if (IsUnbound) {
        return typeof(BuiltinFunctionCaller<%(typeParams)s>);
    }
    return typeof(BuiltinMethodCaller<%(typeParams)s>);"""

def builtin_function_callers_switch(cw):
    for nparams in range(MAX_ARGS-2):        
        cw.write(builtin_function_switch_template % {
                  'argCount' : nparams,
                  'typeParams' : ',' * nparams,
                  'dlgParams' : ',' * (nparams + 3),
                 })

builtin_function_caller_template = """class BuiltinFunctionCaller<TFuncType, %(typeParams)s> where TFuncType : class {
    private readonly OptimizingInfo _info;
    public readonly Func<CallSite, CodeContext, TFuncType, %(typeParams)s, object> MyDelegate;
    private readonly BuiltinFunction _func;
%(typeVars)s

    public BuiltinFunctionCaller(OptimizingInfo info, BuiltinFunction func, %(typeCheckParams)s) {
        _func = func;
        _info = info;
        MyDelegate = new Func<CallSite, CodeContext, TFuncType, %(typeParams)s, object>(Call%(argCount)d);
%(argsAssign)s
    }

    public object Call%(argCount)d(CallSite site, CodeContext context, TFuncType func, %(callParams)s) {
        if (func == _func &&
            !_info.ShouldOptimize && 
%(typeCheck)s
           ) {
            return _info.Caller(new object[] { context, %(callArgs)s }, out _info.ShouldOptimize);
        }

        return ((CallSite<Func<CallSite, CodeContext, TFuncType, %(typeParams)s, object>>)site).Update(site, context, func, %(callArgs)s);
    }
}

class BuiltinMethodCaller<TFuncType, %(typeParams)s> where TFuncType : class {
    private readonly OptimizingInfo _info;
    public readonly Func<CallSite, CodeContext, TFuncType, %(typeParams)s, object> MyDelegate;
    private readonly Type _selfType;
    private readonly BuiltinFunctionData _data;
%(typeVars)s

    public BuiltinMethodCaller(OptimizingInfo info, BuiltinFunction func, Type selfType, %(typeCheckParams)s) {
        _selfType = selfType;
        _data = func._data;
        _info = info;
        MyDelegate = new Func<CallSite, CodeContext, TFuncType, %(typeParams)s, object>(Call%(argCount)d);
%(argsAssign)s
    }

    public object Call%(argCount)d(CallSite site, CodeContext context, TFuncType func, %(callParams)s) {
        BuiltinFunction bf = func as BuiltinFunction;
        if (bf != null && !bf.IsUnbound && bf._data == _data &&
            !_info.ShouldOptimize &&
            (_selfType == null || CompilerHelpers.GetType(bf.__self__) == _selfType) &&
%(typeCheck)s
            ) {
            return _info.Caller(new object[] { context, bf.__self__, %(callArgs)s }, out _info.ShouldOptimize);
        }

        return ((CallSite<Func<CallSite, CodeContext, TFuncType, %(typeParams)s, object>>)site).Update(site, context, func, %(callArgs)s);
    }
}
"""

def builtin_function_callers(cw):
    for nparams in range(1, MAX_ARGS-2):       
        assignTemplate = "        _type%d = type%d;"
        typeCheckTemplate = "            (_type%d == null || CompilerHelpers.GetType(arg%d) == _type%d)"
        typeVarTemplate = "    private readonly Type " + ', '.join(('_type%d' % i for i in xrange(nparams))) + ';'
        cw.write(builtin_function_caller_template % {
                  'argCount' : nparams,
                  'ctorArgs' : ',' * nparams,
                  'typeParams' : ', '.join(('T%d' % d for d in xrange(nparams))),
                  'callArgs': ', '.join(('arg%d' % d for d in xrange(nparams))),
                  'callParams': ', '.join(('T%d arg%d' % (d,d) for d in xrange(nparams))),
                  'typeCheckParams': ', '.join(('Type type%d' % (d,) for d in xrange(nparams))),
                  'argsAssign' : '\n'.join((assignTemplate % (d,d) for d in xrange(nparams))),
                  'typeCheck' : ' &&\n'.join((typeCheckTemplate % (d,d,d) for d in xrange(nparams))),
                  'dlgParams' : ',' * (nparams + 3),
                  'typeVars' : typeVarTemplate,
                 })

function_caller_template = """
class FunctionCaller<%(typeParams)s> : FunctionCaller {
    public FunctionCaller(int compat) : base(compat) { }
    
    public object Call%(argCount)d(CallSite site, CodeContext context, object func, %(callParams)s) {
        PythonFunction pyfunc = func as PythonFunction;
        if (pyfunc != null && pyfunc._compat == _compat) {
            return ((Func<%(genFuncArgs)s>)pyfunc.func_code.Target)(pyfunc, %(callArgs)s);
        }

        return ((CallSite<Func<CallSite, CodeContext, object, %(typeParams)s, object>>)site).Update(site, context, func, %(callArgs)s);
    }"""
    
defaults_template = """
    public object Default%(defaultCount)dCall%(argCount)d(CallSite site, CodeContext context, object func, %(callParams)s) {
        PythonFunction pyfunc = func as PythonFunction;
        if (pyfunc != null && pyfunc._compat == _compat) {
            int defaultIndex = pyfunc.Defaults.Length - pyfunc.NormalArgumentCount + %(argCount)d;
            return ((Func<%(genFuncArgs)s>)pyfunc.func_code.Target)(pyfunc, %(callArgs)s, %(defaultArgs)s);
        }

        return ((CallSite<Func<CallSite, CodeContext, object, %(typeParams)s, object>>)site).Update(site, context, func, %(callArgs)s);
    }"""

defaults_template_0 = """
public object Default%(argCount)dCall0(CallSite site, CodeContext context, object func) {
    PythonFunction pyfunc = func as PythonFunction;
    if (pyfunc != null && pyfunc._compat == _compat) {
        int defaultIndex = pyfunc.Defaults.Length - pyfunc.NormalArgumentCount;
        return ((Func<%(genFuncArgs)s>)pyfunc.func_code.Target)(pyfunc, %(defaultArgs)s);
    }

    return ((CallSite<Func<CallSite, CodeContext, object, object>>)site).Update(site, context, func);
}"""

def function_callers(cw):
    cw.write('internal const int MaxGeneratedFunctionArgs = %d;' % (MAX_ARGS-2))
    cw.write('')
    for nparams in range(1, MAX_ARGS-2):        
        cw.write(function_caller_template % {
                  'typeParams' : ', '.join(('T%d' % d for d in xrange(nparams))),
                  'callParams': ', '.join(('T%d arg%d' % (d,d) for d in xrange(nparams))),
                  'argCount' : nparams,
                  'callArgs': ', '.join(('arg%d' % d for d in xrange(nparams))),
                  'genFuncArgs' : make_calltarget_type_args(nparams),
                 })                    
                 
        for i in xrange(nparams + 1, MAX_ARGS - 2):
            cw.write(defaults_template % {
                      'typeParams' : ', '.join(('T%d' % d for d in xrange(nparams))),
                      'callParams': ', '.join(('T%d arg%d' % (d,d) for d in xrange(nparams))),
                      'argCount' : nparams,
                      'totalParamCount' : i,
                      'callArgs': ', '.join(('arg%d' % d for d in xrange(nparams))),
                      'defaultCount' : i - nparams,
                      'defaultArgs' : ', '.join(('pyfunc.Defaults[defaultIndex + %d]' % curDefault for curDefault in xrange(i - nparams))),
                      'genFuncArgs' : make_calltarget_type_args(i),
                     })                 
        cw.write('}')

def function_callers_0(cw):
    for i in xrange(1, MAX_ARGS - 2):
        cw.write(defaults_template_0 % {
                  'argCount' : i,
                  'defaultArgs' : ', '.join(('pyfunc.Defaults[defaultIndex + %d]' % curDefault for curDefault in xrange(i))),
                  'genFuncArgs' : make_calltarget_type_args(i),
                 })                 

function_caller_switch_template = """case %(argCount)d:                        
    callerType = typeof(FunctionCaller<%(arity)s>).MakeGenericType(typeParams);
    mi = callerType.GetMethod(baseName + "Call%(argCount)d");
    Debug.Assert(mi != null);
    fc = GetFunctionCaller(callerType, funcCompat);
    funcType = typeof(Func<,,,,%(arity)s>).MakeGenericType(allParams);

    return new Binding.FastBindResult<T>((T)(object)Delegate.CreateDelegate(funcType, fc, mi), true);"""
    

def function_caller_switch(cw):
    for nparams in range(1, MAX_ARGS-2):
        cw.write(function_caller_switch_template % {
                  'arity' : ',' * (nparams - 1),
                  'argCount' : nparams,
                 })   

def gen_lazy_call_targets(cw):
    for nparams in range(MAX_ARGS):
        cw.enter_block("public static object OriginalCallTarget%d(%s)" % (nparams, make_params(nparams, "PythonFunction function")))
        cw.write("function.func_code.LazyCompileFirstTarget(function);")
        cw.write("return ((Func<%s>)function.func_code.Target)(%s);" % (make_calltarget_type_args(nparams), gen_args_call(nparams, 'function')))
        cw.exit_block()
        cw.write('')

def gen_recursion_checks(cw):
    for nparams in range(MAX_ARGS):
        cw.enter_block("internal class PythonFunctionRecursionCheck%d" % (nparams, ))
        cw.write("private readonly Func<%s> _target;" % (make_calltarget_type_args(nparams), ))
        cw.write('')
        cw.enter_block('public PythonFunctionRecursionCheck%d(Func<%s> target)' % (nparams, make_calltarget_type_args(nparams)))
        cw.write('_target = target;')
        cw.exit_block()
        cw.write('')
        
        cw.enter_block('public object CallTarget(%s)' % (make_params(nparams, "PythonFunction/*!*/ function"), ))
        cw.write('PythonOps.FunctionPushFrame((PythonContext)function.Context.LanguageContext);')
        cw.enter_block('try')
        cw.write('return _target(%s);' % (gen_args_call(nparams, 'function'), ))
        cw.finally_block()
        cw.write('PythonOps.FunctionPopFrame();')
        cw.exit_block()        
        cw.exit_block()
        cw.exit_block()
        cw.write('')

def gen_recursion_delegate_switch(cw):
    for nparams in range(MAX_ARGS):
        cw.case_label('case %d:' % nparams)
        cw.write('finalTarget = new Func<%s>(new PythonFunctionRecursionCheck%d((Func<%s>)finalTarget).CallTarget);' % (make_calltarget_type_args(nparams), nparams, make_calltarget_type_args(nparams)))
        cw.write('break;')
        cw.dedent()
    
def get_call_type(postfix):
    if postfix == "": return "CallType.None"
    else: return "CallType.ImplicitInstance"


def make_call_to_target(cw, index, postfix, extraArg):
        cw.enter_block("public override object Call%(postfix)s(%(params)s)", postfix=postfix,
                       params=make_params1(index))
        cw.write("if (target%(index)d != null) return target%(index)d(%(args)s);", index=index,
                 args = make_args1(index, extraArg))
        cw.write("throw BadArgumentError(%(callType)s, %(nargs)d);", callType=get_call_type(postfix), nargs=index)
        cw.exit_block()

def make_call_to_targetX(cw, index, postfix, extraArg):
        cw.enter_block("public override object Call%(postfix)s(%(params)s)", postfix=postfix,
                       params=make_params1(index))
        cw.write("return target%(index)d(%(args)s);", index=index, args = make_args1(index, extraArg))
        cw.exit_block()

def make_error_calls(cw, index):
        cw.enter_block("public override object Call(%(params)s)", params=make_params1(index))
        cw.write("throw BadArgumentError(CallType.None, %(nargs)d);", nargs=index)
        cw.exit_block()

        if index > 0:
            cw.enter_block("public override object CallInstance(%(params)s)", params=make_params1(index))
            cw.write("throw BadArgumentError(CallType.ImplicitInstance, %(nargs)d);", nargs=index)
            cw.exit_block()

def gen_call(nargs, nparams, cw, extra=[]):
    args = extra + ["arg%d" % i for i in range(nargs)]
    cw.enter_block("public override object Call(%s)" % make_params1(nargs))
    
    # first emit error checking...
    ndefaults = nparams-nargs
    if nargs != nparams:    
        cw.write("if (Defaults.Length < %d) throw BadArgumentError(%d);" % (ndefaults,nargs))
    
    # emit the common case of no recursion check
    if (nargs == nparams):
        cw.write("if (!EnforceRecursion) return target(%s);" % ", ".join(args))
    else:        
        dargs = args + ["Defaults[Defaults.Length - %d]" % i for i in range(ndefaults, 0, -1)]
        cw.write("if (!EnforceRecursion) return target(%s);" % ", ".join(dargs))
    
    # emit non-common case of recursion check
    cw.write("PushFrame();")
    cw.enter_block("try")

    # make function body
    if (nargs == nparams):
        cw.write("return target(%s);" % ", ".join(args))
    else:        
        dargs = args + ["Defaults[Defaults.Length - %d]" % i for i in range(ndefaults, 0, -1)]
        cw.write("return target(%s);" % ", ".join(dargs))
    
    cw.finally_block()
    cw.write("PopFrame();")
    cw.exit_block()
        
    cw.exit_block()

def gen_params_callN(cw, any):
    cw.enter_block("public override object Call(CodeContext context, params object[] args)")
    cw.write("if (!IsContextAware) return Call(args);")
    cw.write("")
    cw.enter_block("if (Instance == null)")
    cw.write("object[] newArgs = new object[args.Length + 1];")
    cw.write("newArgs[0] = context;")
    cw.write("Array.Copy(args, 0, newArgs, 1, args.Length);")
    cw.write("return Call(newArgs);")
    cw.else_block()
    
    # need to call w/ Context, Instance, *args
    
    if any:
        cw.enter_block("switch (args.Length)")
        for i in xrange(MAX_ARGS-1):
                if i == 0:
                    cw.write(("case %d: if(target2 != null) return target2(context, Instance); break;") % (i))
                else:
                    cw.write(("case %d: if(target%d != null) return target%d(context, Instance, " + gen_args_paramscall(i) + "); break;") % (i, i+2, i+2))
        cw.exit_block()
        cw.enter_block("if (targetN != null)")
        cw.write("object [] newArgs = new object[args.Length+2];")
        cw.write("newArgs[0] = context;")
        cw.write("newArgs[1] = Instance;")
        cw.write("Array.Copy(args, 0, newArgs, 2, args.Length);")
        cw.write("return targetN(newArgs);")
        cw.exit_block()
        cw.write("throw BadArgumentError(args.Length);")
        cw.exit_block()
    else:
        cw.write("object [] newArgs = new object[args.Length+2];")
        cw.write("newArgs[0] = context;")
        cw.write("newArgs[1] = Instance;")
        cw.write("Array.Copy(args, 0, newArgs, 2, args.Length);")
        cw.write("return target(newArgs);")
        cw.exit_block()
        
    cw.exit_block()
    cw.write("")

CODE = """
public static object Call(%(params)s) {
    FastCallable fc = func as FastCallable;
    if (fc != null) return fc.Call(%(args)s);

    return PythonCalls.Call(func, %(argsArray)s);
}"""

def gen_python_switch(cw):
    for nparams in range(MAX_ARGS):
        genArgs = make_calltarget_type_args(nparams)
        cw.write("""case %d: 
    originalTarget = (Func<%s>)OriginalCallTarget%d;
    return typeof(Func<%s>);""" % (nparams, genArgs, nparams, genArgs))

fast_type_call_template = """
class FastBindingBuilder<%(typeParams)s> : FastBindingBuilderBase {
    public FastBindingBuilder(CodeContext context, PythonType type, PythonInvokeBinder binder, Type siteType, Type[] genTypeArgs) :
        base(context, type, binder, siteType, genTypeArgs) {
    }

    protected override Delegate GetNewSiteDelegate(PythonInvokeBinder binder, object func) {
        return new Func<%(newInitDlgParams)s>(new NewSite<%(typeParams)s>(binder, func).Call);
    }

    protected override Delegate MakeDelegate(int version, Delegate newDlg, LateBoundInitBinder initBinder) {
        return new Func<%(funcParams)s>(
            new FastTypeSite<%(typeParams)s>(
                version, 
                (Func<%(newInitDlgParams)s>)newDlg,
                initBinder
            ).CallTarget
        );
    }
}

class FastTypeSite<%(typeParams)s> {
    private readonly int _version;
    private readonly Func<%(newInitDlgParams)s> _new;
    private readonly CallSite<Func<%(nestedSlowSiteParams)s>> _initSite;

    public FastTypeSite(int version, Func<%(newInitDlgParams)s> @new, LateBoundInitBinder initBinder) {
        _version = version;
        _new = @new;
        _initSite = CallSite<Func<%(nestedSlowSiteParams)s>>.Create(initBinder);
    }

    public object CallTarget(CallSite site, CodeContext context, object type, %(callTargetArgs)s) {
        PythonType pt = type as PythonType;
        if (pt != null && pt.Version == _version) {
            object res = _new(context, type, %(callTargetPassedArgs)s);
            _initSite.Target(_initSite, context, res, %(callTargetPassedArgs)s);

            return res;
        }

        return ((CallSite<Func<%(funcParams)s>>)site).Update(site, context, type, %(callTargetPassedArgs)s);
    }
}

class NewSite<%(typeParams)s> {
    private readonly CallSite<Func<%(nestedSiteParams)s>> _site;
    private readonly object _target;

    public NewSite(PythonInvokeBinder binder, object target) {
        _site = CallSite<Func<%(nestedSiteParams)s>>.Create(binder);
        _target = target;
    }

    public object Call(CodeContext context, object typeOrInstance, %(callTargetArgs)s) {
        return _site.Target(_site, context, _target, typeOrInstance, %(callTargetPassedArgs)s);
    }
}
"""
def gen_fast_type_callers(cw):
    for nparams in range(1, 6):       
        funcParams = 'CallSite, CodeContext, object, ' + ', '.join(('T%d' % d for d in xrange(nparams))) + ', object'
        newInitDlgParams = 'CodeContext, object, ' + ', '.join(('T%d' % d for d in xrange(nparams))) + ', object'
        callTargetArgs = ', '.join(('T%d arg%d' % (d, d) for d in xrange(nparams)))
        callTargetPassedArgs = ', '.join(('arg%d' % (d, ) for d in xrange(nparams)))
        nestedSiteParams = 'CallSite, CodeContext, object, object, ' + ', '.join(('T%d' % d for d in xrange(nparams))) + ', object'
        nestedSlowSiteParams = 'CallSite, CodeContext, object, ' + ', '.join(('T%d' % d for d in xrange(nparams))) + ', object'
        cw.write(fast_type_call_template % {
                  'typeParams' : ', '.join(('T%d' % d for d in xrange(nparams))),
                  'funcParams' : funcParams,
                  'newInitDlgParams' : newInitDlgParams,
                  'callTargetArgs' : callTargetArgs,
                  'callTargetPassedArgs': callTargetPassedArgs,
                  'nestedSiteParams' : nestedSiteParams,
                  'nestedSlowSiteParams' : nestedSlowSiteParams,
                 })
                 
def gen_fast_type_caller_switch(cw):
    for nparams in range(1, 6):
        cw.write('case %d: baseType = typeof(FastBindingBuilder<%s>); break;' % (nparams, (',' * (nparams - 1))))

fast_init_template = """
class FastInitSite<%(typeParams)s> {
    private readonly int _version;
    private readonly PythonFunction _slot;
    private readonly CallSite<Func<CallSite, CodeContext, PythonFunction, object, %(typeParams)s, object>> _initSite;

    public FastInitSite(int version, PythonInvokeBinder binder, PythonFunction target) {
        _version = version;
        _slot = target;
        _initSite = CallSite<Func<CallSite, CodeContext, PythonFunction, object,  %(typeParams)s, object>>.Create(binder);
    }

    public object CallTarget(CallSite site, CodeContext context, object inst, %(callParams)s) {
        IPythonObject pyObj = inst as IPythonObject;
        if (pyObj != null && pyObj.PythonType.Version == _version) {
            _initSite.Target(_initSite, context, _slot, inst, %(callArgs)s);
            return inst;
        }

        return ((CallSite<Func<CallSite, CodeContext, object,  %(typeParams)s, object>>)site).Update(site, context, inst, %(callArgs)s);
    }

    public object EmptyCallTarget(CallSite site, CodeContext context, object inst, %(callParams)s) {
        IPythonObject pyObj = inst as IPythonObject;
        if ((pyObj != null && pyObj.PythonType.Version == _version) || DynamicHelpers.GetPythonType(inst).Version == _version) {
            return inst;
        }

        return ((CallSite<Func<CallSite, CodeContext, object,  %(typeParams)s, object>>)site).Update(site, context, inst, %(callArgs)s);
    }
}
"""

MAX_FAST_INIT_ARGS = 6
def gen_fast_init_callers(cw):
    for nparams in range(1, MAX_FAST_INIT_ARGS):       
        callParams = ', '.join(('T%d arg%d' % (d, d) for d in xrange(nparams)))
        callArgs = ', '.join(('arg%d' % (d, ) for d in xrange(nparams)))
        cw.write(fast_init_template % {
                  'typeParams' : ', '.join(('T%d' % d for d in xrange(nparams))),
                  'callParams' : callParams,
                  'callArgs': callArgs,
                 })

def gen_fast_init_switch(cw):
    for nparams in range(1, MAX_FAST_INIT_ARGS):
        cw.write("case %d: initSiteType = typeof(FastInitSite<%s>); break;" % (nparams, ',' * (nparams-1), ))

def gen_fast_init_max_args(cw):
    cw.write("public const int MaxFastLateBoundInitArgs = %d;" % MAX_FAST_INIT_ARGS)

def main(): 
    return generate(
        ("Python Fast Init Max Args", gen_fast_init_max_args),
        ("Python Fast Init Switch", gen_fast_init_switch),
        ("Python Fast Init Callers", gen_fast_init_callers),
        ("Python Fast Type Caller Switch", gen_fast_type_caller_switch),
        ("Python Fast Type Callers", gen_fast_type_callers),
        ("Python Recursion Enforcement", gen_recursion_checks),
        ("Python Recursion Delegate Switch", gen_recursion_delegate_switch),
        ("Python Lazy Call Targets", gen_lazy_call_targets),
        ("Python Builtin Function Optimizable Callers", builtin_function_callers),
        ("Python Builtin Function Optimizable Switch", builtin_function_callers_switch),
        ("Python Zero Arg Function Callers", function_callers_0),
        ("Python Function Callers", function_callers),
        ("Python Function Caller Switch", function_caller_switch),
        ("Python Call Target Switch", gen_python_switch),
    )

if __name__ == "__main__":
    main()
