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
using System; using Microsoft;


using Microsoft.Linq.Expressions;
using Microsoft.Scripting;
using Microsoft.Scripting.Utils;
using IronRuby.Runtime.Calls;
using IronRuby.Runtime;
using IronRuby.Compiler.Generation;
using System.Diagnostics;

namespace IronRuby.Builtins {
    public partial class Proc {
        public sealed partial class Subclass : Proc, IRubyObject {
            // called by Proc#new rule when creating a Ruby subclass of Proc:
            public Subclass(RubyClass/*!*/ rubyClass, Proc/*!*/ proc) 
                : base(proc) {
                Assert.NotNull(rubyClass);
                Debug.Assert(!rubyClass.IsSingletonClass);
                ImmediateClass = rubyClass;
            }

            public override Proc/*!*/ Copy() {
                return new Subclass(ImmediateClass.NominalClass, this);
            }
        }
    }
}
