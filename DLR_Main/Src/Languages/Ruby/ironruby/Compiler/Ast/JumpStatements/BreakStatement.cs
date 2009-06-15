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


using Microsoft.Scripting;
#if CODEPLEX_40
using MSA = System.Linq.Expressions;
#else
using MSA = Microsoft.Linq.Expressions;
#endif
using AstUtils = Microsoft.Scripting.Ast.Utils;

namespace IronRuby.Compiler.Ast {
#if CODEPLEX_40
    using Ast = System.Linq.Expressions.Expression;
#else
    using Ast = Microsoft.Linq.Expressions.Expression;
#endif

    public partial class BreakStatement : JumpStatement {
        public BreakStatement(Arguments arguments, SourceSpan location)
            : base(arguments, location) {
        }

        // see Ruby Language.doc/Runtime/Control Flow Implementation/Break
        internal override MSA.Expression/*!*/ Transform(AstGenerator/*!*/ gen) {

            MSA.Expression transformedReturnValue = TransformReturnValue(gen);

            // eval:
            if (gen.CompilerOptions.IsEval) {
                return Methods.EvalBreak.OpCall(gen.CurrentScopeVariable, AstFactory.Box(transformedReturnValue));
            }

            // loop:
            if (gen.CurrentLoop != null) {
                return Ast.Block(
                    Ast.Assign(
                        gen.CurrentLoop.ResultVariable,
                        Ast.Convert(transformedReturnValue, gen.CurrentLoop.ResultVariable.Type)
                    ),
                    Ast.Break(gen.CurrentLoop.BreakLabel),
                    AstUtils.Empty()
                );
            }

            // block:
            if (gen.CurrentBlock != null) {
                return gen.Return(Methods.BlockBreak.OpCall(gen.CurrentBlock.BfcVariable, AstFactory.Box(transformedReturnValue)));
            }

            // primary frame:
            return Methods.MethodBreak.OpCall(AstFactory.Box(transformedReturnValue));
        }
    }
}
