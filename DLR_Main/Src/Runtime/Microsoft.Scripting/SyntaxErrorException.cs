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
using System.Runtime.Serialization;
#if CODEPLEX_40
using System.Dynamic;
#else
using Microsoft.Scripting;
#endif
using System.Security.Permissions;
using Microsoft.Scripting.Utils;

namespace Microsoft.Scripting {

    [Serializable]
    public class SyntaxErrorException : Exception {
        private SourceSpan _span;

        private string _sourceCode;
        private string _sourceLine;
        private string _sourcePath;

        private Severity _severity;
        private int _errorCode;

        public SyntaxErrorException() : base() { }

        public SyntaxErrorException(string message) : base(message) { }

        public SyntaxErrorException(string message, Exception innerException)
            : base(message, innerException) {
        }

        public SyntaxErrorException(string message, SourceUnit sourceUnit, SourceSpan span, int errorCode, Severity severity)
            : base(message) {
            ContractUtils.RequiresNotNull(message, "message");

            _span = span;
            _severity = severity;
            _errorCode = errorCode;
            if (sourceUnit != null) {
                _sourcePath = sourceUnit.Path;
                try {
                    _sourceCode = sourceUnit.GetCode();
                    _sourceLine = sourceUnit.GetCodeLine(Line);
                } catch (System.IO.IOException) {
                    // could not get source code.
                }
            }
        }

        public SyntaxErrorException(string message, string path, string code, string line, SourceSpan span, int errorCode, Severity severity)
            : base(message) {
            ContractUtils.RequiresNotNull(message, "message");

            _span = span;
            _severity = severity;
            _errorCode = errorCode;

            _sourcePath = path;
            _sourceCode = code;
            _sourceLine = line;
        }

#if !SILVERLIGHT
        protected SyntaxErrorException(SerializationInfo info, StreamingContext context)
            : base(info, context) {

            _span = (SourceSpan)info.GetValue("Span", typeof(SourceSpan));
            _sourceCode = info.GetString("SourceCode");
            _sourcePath = info.GetString("SourcePath");
            _severity = (Severity)info.GetValue("Severity", typeof(Severity));
            _errorCode = info.GetInt32("ErrorCode");
        }

        [SecurityPermission(SecurityAction.LinkDemand, Flags = SecurityPermissionFlag.SerializationFormatter)]
        public override void GetObjectData(SerializationInfo info, StreamingContext context) {
            ContractUtils.RequiresNotNull(info, "info");

            base.GetObjectData(info, context);
            info.AddValue("Span", _span);
            info.AddValue("SourceCode", _sourceCode);
            info.AddValue("SourcePath", _sourcePath);
            info.AddValue("Severity", _severity);
            info.AddValue("ErrorCode", _errorCode);
        }
#endif

        /// <summary>
        /// Unmapped span.
        /// </summary>
        public SourceSpan RawSpan {
            get { return _span; }
        }

        public string SourceCode {
            get { return _sourceCode; }
        }

        public string SourcePath {
            get { return _sourcePath; }
        }

        public Severity Severity {
            get { return _severity; }
        }

        public int Line {
            get { return _span.Start.Line; }
        }

        public int Column {
            get { return _span.Start.Column; }
        }

        public int ErrorCode {
            get { return _errorCode; }
        }

        // TODO: fix
        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Design", "CA1024:UsePropertiesWhereAppropriate")]
        public string GetSymbolDocumentName() {
            return _sourcePath;
        }

        // TODO: fix
        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Design", "CA1024:UsePropertiesWhereAppropriate")]
        public string GetCodeLine() {
            return _sourceLine;
        }
    }
}
