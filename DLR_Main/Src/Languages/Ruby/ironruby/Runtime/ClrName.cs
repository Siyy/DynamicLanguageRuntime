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

#if CODEPLEX_40
using System;
#else
using System; using Microsoft;
#endif
using System.Collections.Generic;
using System.Text;
using System.Threading;
using Microsoft.Scripting.Utils;
using IronRuby.Builtins;

namespace IronRuby.Runtime {
    /// <summary>
    /// Represents a CLR member name that is subject to name mangling.
    /// </summary>
    public class ClrName : IEquatable<ClrName> {
        private readonly string/*!*/ _actual;
        private string _mangled;

        public string/*!*/ ActualName {
            get { return _actual; }
        }

        public string/*!*/ MangledName {
            get {
                if (_mangled == null) {
                    _mangled = RubyUtils.MangleName(_actual);
                }
                return _mangled;
            }
        }

        public ClrName(string/*!*/ actualName) {
            ContractUtils.RequiresNotNull(actualName, "actualName");
            _actual = actualName;
        }

        public bool Equals(ClrName other) {
            return other != null && _actual == other._actual;
        }

        public override bool Equals(object obj) {
            return Equals(obj as ClrName);
        }

        public override int GetHashCode() {
            return _actual.GetHashCode();
        }
    }
}
