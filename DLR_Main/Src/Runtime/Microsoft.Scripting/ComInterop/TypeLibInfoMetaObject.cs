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


#if !SILVERLIGHT

using System.Collections.Generic;
#if CODEPLEX_40
using System.Dynamic;
using System.Linq.Expressions;
#else
using Microsoft.Scripting;
using Microsoft.Linq.Expressions;
#endif
using Microsoft.Scripting.Utils;
using AstUtils = Microsoft.Scripting.Ast.Utils;

namespace Microsoft.Scripting.ComInterop {

    internal sealed class TypeLibInfoMetaObject : DynamicMetaObject {
        private readonly ComTypeLibInfo _info;

        internal TypeLibInfoMetaObject(Expression expression, ComTypeLibInfo info)
            : base(expression, BindingRestrictions.Empty, info) {
            _info = info;
        }

        public override DynamicMetaObject BindGetMember(GetMemberBinder binder) {
            ContractUtils.RequiresNotNull(binder, "binder");
            string name = binder.Name;

            if (name == _info.Name) {
                name = "TypeLibDesc";
            } else if (name != "Guid" &&
                name != "Name" &&
                name != "VersionMajor" &&
                name != "VersionMinor") {

                return binder.FallbackGetMember(this);
            }

            return new DynamicMetaObject(
                Expression.Convert(
                    Expression.Property(
                        AstUtils.Convert(Expression, typeof(ComTypeLibInfo)),
                        typeof(ComTypeLibInfo).GetProperty(name)
                    ),
                    typeof(object)
                ),
                ComTypeLibInfoRestrictions(this)
            );
        }

        public override IEnumerable<string> GetDynamicMemberNames() {
            return _info.GetMemberNames();
        }

        private BindingRestrictions ComTypeLibInfoRestrictions(params DynamicMetaObject[] args) {
            return BindingRestrictions.Combine(args).Merge(BindingRestrictions.GetTypeRestriction(Expression, typeof(ComTypeLibInfo)));
        }
    }
}

#endif
