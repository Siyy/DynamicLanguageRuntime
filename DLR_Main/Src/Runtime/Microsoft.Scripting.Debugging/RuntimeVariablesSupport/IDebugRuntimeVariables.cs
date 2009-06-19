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


using System.Runtime.CompilerServices;
#if !CODEPLEX_40
using Microsoft.Runtime.CompilerServices;
#endif


namespace Microsoft.Scripting.Debugging {
    /// <summary>
    /// IDebugRuntimeVariables is used to wrap IRuntimeVariables and add properties for retrieving
    /// FunctionInfo and DebugMarker from debuggable labmdas.
    /// </summary>
    internal interface IDebugRuntimeVariables : IRuntimeVariables {
        FunctionInfo FunctionInfo { get; }
        int DebugMarker { get; }
    }
}
