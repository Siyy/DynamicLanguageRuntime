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


using Microsoft.Linq.Expressions;
using Microsoft.Scripting;

namespace ToyScript.Parser.Ast {

    class Member : ToyExpression {
        private readonly ToyExpression _target;
        private readonly string _member;

        public Member(SourceSpan span, ToyExpression target, string member)
            : base(span) {
            _target = target;
            _member = member;
        }

        protected internal override Expression Generate(ToyGenerator tg) {
            return tg.GetMember(_member, _target.Generate(tg));
        }
    }
}