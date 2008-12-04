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
using System.Collections.Generic;
using System.Text;
using System.IO;
using Microsoft.Scripting;

namespace IronRuby.Tests {
    public class BinaryContentProvider : StreamContentProvider {
        public byte[] Buffer { get; set; }

        public BinaryContentProvider(byte[]/*!*/ buffer) {
            Buffer = buffer;
        }

        public override Stream/*!*/ GetStream() {
            return new MemoryStream(Buffer);
        }
    }
}
