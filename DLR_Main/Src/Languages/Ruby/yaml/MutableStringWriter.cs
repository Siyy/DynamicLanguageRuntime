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
using System.IO;
using System.Text;
using IronRuby.Builtins;
using Microsoft.Scripting.Utils;

namespace IronRuby.StandardLibrary.Yaml {

    internal class MutableStringWriter : TextWriter {
        private readonly MutableString _storage;

        public MutableStringWriter(MutableString/*!*/ storage) {
            Assert.NotNull(storage);
            _storage = storage;
        }

        public override Encoding/*!*/ Encoding {
            get { return _storage.Encoding.Encoding; }
        }

        public override void  Write(char value) {
            _storage.Append(value);
        }

        public override void Write(char[]/*!*/ buffer, int index, int count) {
            _storage.Append(buffer, index, count);
        }

        internal MutableString/*!*/ String {
            get { return _storage; }
        }
    }
}
