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

#if CODEPLEX_40
using System;
#else
using System; using Microsoft;
#endif
using System.Collections;
using System.Collections.Generic;

namespace Microsoft.Scripting.Debugging {
#if CODEPLEX_40
    using Ast = System.Linq.Expressions.Expression;
#else
    using Ast = Microsoft.Linq.Expressions.Expression;
#endif

    internal static class InvokeTargets {
        internal static Type GetGeneratorFactoryTarget(Type[] parameterTypes) {
            Type[] typeArgs = new Type[parameterTypes.Length + 2];
            typeArgs[0] = typeof(DebugFrame);
            parameterTypes.CopyTo(typeArgs, 1);
            typeArgs[parameterTypes.Length + 1] = typeof(IEnumerator);

            if (typeArgs.Length <= 16) {
                return Ast.GetFuncType(typeArgs);
            } else {
                return DelegateHelpers.MakeNewCustomDelegateType(typeArgs);
            }
        }
    }
}