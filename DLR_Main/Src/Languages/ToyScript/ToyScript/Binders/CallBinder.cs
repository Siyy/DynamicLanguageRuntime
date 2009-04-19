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
using Microsoft.Scripting;
using Microsoft.Linq.Expressions;

namespace ToyScript.Binders {
    sealed class CallBinder : InvokeBinder {
        public CallBinder() 
            :base(new CallInfo(0)){
        }

        public override int GetHashCode() {
            return 197 ^ base.GetHashCode();
        }

        public override bool Equals(object obj) {
            CallBinder cb = obj as CallBinder;
            return cb != null && base.Equals(obj);
        }

        public override DynamicMetaObject FallbackInvoke(DynamicMetaObject target, DynamicMetaObject[] args, DynamicMetaObject onBindingError) {
            throw new NotImplementedException();
        }
    }
}