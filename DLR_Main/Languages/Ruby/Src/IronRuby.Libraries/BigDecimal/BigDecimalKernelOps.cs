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


using System.Runtime.InteropServices;
using IronRuby.Builtins;
using IronRuby.Runtime;
using Microsoft.Scripting.Runtime;

namespace IronRuby.StandardLibrary.BigDecimal {
    [RubyModule(Extends = typeof(Kernel))]
    public static class KernelOps {
        [RubyMethod("BigDecimal", RubyMethodAttributes.PrivateInstance)]
        [RubyMethod("BigDecimal", RubyMethodAttributes.PublicSingleton)]
        public static object CreateBigDecimal(RubyContext/*!*/ context, object/*!*/ self, [DefaultProtocol]MutableString value, [Optional]int n) {
            return BigDecimal.Create(BigDecimalOps.GetConfig(context), value.ConvertToString(), n);
        }
    }

}
