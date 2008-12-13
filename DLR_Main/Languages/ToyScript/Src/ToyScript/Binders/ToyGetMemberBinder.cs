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

namespace ToyScript.Binders {
    internal class ToyGetMemberBinder : GetMemberBinder {
        internal ToyGetMemberBinder(string name)
            : base(name, false) {
        }

        public override object CacheIdentity {
            get { return this; }
        }

        public override int GetHashCode() {
            return 197 ^ base.GetHashCode();
        }

        public override bool Equals(object obj) {
            return base.Equals(obj as ToyGetMemberBinder);
        }

        public override DynamicMetaObject FallbackGetMember(DynamicMetaObject self, DynamicMetaObject onBindingError) {
            if (self.HasValue) {
                return ClsBinder.BindObjectGetMember(this, self);
            } else {
                return ClsBinder.BindTypeGetMember(this, self);
            }
        }
    }
}
