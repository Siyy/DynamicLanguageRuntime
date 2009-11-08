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

#if !CLR2
using MSAst = System.Linq.Expressions;
#else
using MSAst = Microsoft.Scripting.Ast;
#endif

using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.CompilerServices;

using Microsoft.Scripting;
using Microsoft.Scripting.Utils;

using AstUtils = Microsoft.Scripting.Ast.Utils;

namespace IronPython.Compiler.Ast {
    using Ast = MSAst.Expression;
    
    public sealed class SuiteStatement : Statement {
        private readonly Statement[] _statements;

        public SuiteStatement(Statement[] statements) {
            Assert.NotNull(statements);
            _statements = statements;
        }

        public IList<Statement> Statements {
            get { return _statements; }
        } 

        public override MSAst.Expression Reduce() {
            if (_statements.Length == 0) {
                return AstUtils.Empty();
            }

            ReadOnlyCollectionBuilder<MSAst.Expression> statements = new ReadOnlyCollectionBuilder<MSAst.Expression>();

            int curStart = -1;
            foreach (var statement in _statements) {
                // CPython debugging treats multiple statements on the same line as a single step, we
                // match that behavior here.
                if (statement.Start.Line == curStart) {
                    statements.Add(new DebugInfoRemovalExpression(statement, curStart));
                } else {
                    if (statement.CanThrow && statement.Start.IsValid) {
                        statements.Add(UpdateLineNumber(statement.Start.Line));
                    }

                    statements.Add(statement);
                }
                curStart = statement.Start.Line;
            }
            
            return Ast.Block(statements.ToReadOnlyCollection());
        }

        internal class DebugInfoRemovalExpression : MSAst.Expression {
            private MSAst.Expression _inner;
            private int _start;

            public DebugInfoRemovalExpression(MSAst.Expression expression, int line) {
                _inner = expression;
                _start = line;
            }

            public override MSAst.Expression Reduce() {
                return RemoveDebugInfo(_start, _inner.Reduce());
            }

            public override MSAst.ExpressionType NodeType {
                get {
                    return MSAst.ExpressionType.Extension;
                }
            }

            public override System.Type Type {
                get {
                    return _inner.Type;
                }
            }

            public override bool CanReduce {
                get {
                    return true;
                }
            }
        }

        public override void Walk(PythonWalker walker) {
            if (walker.Walk(this)) {
                if (_statements != null) {
                    foreach (Statement s in _statements) {
                        s.Walk(walker);
                    }
                }
            }
            walker.PostWalk(this);
        }

        public override string Documentation {
            get {                
                if (_statements.Length > 0) {
                    return _statements[0].Documentation;
                }
                return null;
            }
        }

        internal override bool CanThrow {
            get {
                foreach (Statement stmt in _statements) {
                    if (stmt.CanThrow) {
                        return true;
                    }
                }
                return false;
            }
        }
    }
}
