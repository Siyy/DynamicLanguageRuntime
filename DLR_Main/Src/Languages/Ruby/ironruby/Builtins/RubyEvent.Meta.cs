/* ****************************************************************************
 *
 * Copyright (c) Microsoft Corporation. 
 *
 * This source code is subject to terms and conditions of the Microsoft Public License. A 
 * copy of the license can be found in the License.html file at the root of this distribution. If 
 * you cannot locate the  Microsoft Public License, please send an email to 
 * ironruby@microsoft.com. By using this source code in any fashion, you are agreeing to be bound 
 * by the terms of the Microsoft Public License.
 *
 * You must not remove this notice, or any other, from this software.
 *
 *
 * ***************************************************************************/

#if !CLR2
using System.Linq.Expressions;
#else
using Microsoft.Scripting.Ast;
#endif

using System;
using System.Diagnostics;
using System.Dynamic;
using System.Dynamic.Utils;
using Microsoft.Scripting.Utils;
using Microsoft.Scripting.Runtime;
using IronRuby.Runtime;
using IronRuby.Runtime.Calls;
using AstUtils = Microsoft.Scripting.Ast.Utils;
using IronRuby.Compiler;
using System.Reflection;

namespace IronRuby.Builtins {
    using Ast = Expression;

    public partial class RubyEvent : IRubyDynamicMetaObjectProvider {
        public DynamicMetaObject/*!*/ GetMetaObject(Expression/*!*/ parameter) {
            return new Meta(parameter, BindingRestrictions.Empty, this);
        }

        internal sealed class Meta : RubyMetaObject<RubyEvent> {
            public override RubyContext/*!*/ Context {
                get { return Value.Info.Context; }
            }

            protected override MethodInfo/*!*/ ContextConverter {
                get { return Methods.GetContextFromIRubyObject; }
            }

            public Meta(Expression/*!*/ expression, BindingRestrictions/*!*/ restrictions, RubyEvent/*!*/ value)
                : base(expression, restrictions, value) {
            }

            // TODO: +=/-=
        }
    }
}
