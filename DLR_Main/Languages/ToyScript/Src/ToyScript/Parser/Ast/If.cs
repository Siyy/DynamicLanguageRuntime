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
using Microsoft.Scripting.Ast;
using AstUtils = Microsoft.Scripting.Ast.Utils;

namespace ToyScript.Parser.Ast {
    class If : Statement {
        private readonly ToyExpression _test;
        private readonly Statement _then;
        private readonly Statement _else;

        public If(SourceSpan span, ToyExpression test, Statement then, Statement @else)
            : base(span) {
            _test = test;
            _then = then;
            _else = @else;
        }

        protected internal override Expression Generate(ToyGenerator tg) {
            IfStatementBuilder ifb = AstUtils.If(
                tg.AddSpan(
                    new SourceSpan(Span.Start, _test.End),
                    tg.ConvertTo(typeof(bool), _test.Generate(tg))
                ),
                _then.Generate(tg)
            );
                
            if (_else == null){
                return ifb;
            }else{
                return ifb.Else(_else.Generate(tg));
            }
        }
    }
}