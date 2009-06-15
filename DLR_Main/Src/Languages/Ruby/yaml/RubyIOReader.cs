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
#if CODEPLEX_40
using System.Dynamic.Utils;
#else
using Microsoft.Scripting.Utils;
#endif

namespace IronRuby.StandardLibrary.Yaml {
    internal class RubyIOReader : TextReader {
        private readonly RubyIO _io;

        internal RubyIOReader(RubyIO io) {
            _io = io;
        }

        public override int Peek() {
            return _io.PeekByteNormalizeEoln();
        }
        public override int Read() {
            return _io.ReadByteNormalizeEoln();
        }
    }
}
