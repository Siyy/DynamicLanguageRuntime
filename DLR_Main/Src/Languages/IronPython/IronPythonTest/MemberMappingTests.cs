/* ****************************************************************************
 *
 * Copyright (c) Microsoft Corporation. 
 *
 * This source code is subject to terms and conditions of the Microsoft Public License. A 
 * copy of the license can be found in the License.html file at the root of this distribution. If 
 * you cannot locate the  Microsoft Public License, please send an email to 
 * ironpy@microsoft.com. By using this source code in any fashion, you are agreeing to be bound 
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
using System.Collections;
using IronPython.Runtime.Operations;

// Includes tests for mapping from .NET interfaces & known types to various Python protocol methods.

namespace IronPythonTest {
    public class GenericCollection : ICollection<int> {
        private List<int> _data = new List<int>();

        #region ICollection<int> Members

        public void Add(int item) {
            _data.Add(item);
        }

        public void Clear() {
            _data.Clear();
        }

        public bool Contains(int item) {
            return _data.Contains(item);
        }

        public void CopyTo(int[] array, int arrayIndex) {
            _data.CopyTo(array, arrayIndex);
        }

        public int Count {
            get { return _data.Count; }
        }

        public bool IsReadOnly {
            get { return false; }
        }

        public bool Remove(int item) {
            return _data.Remove(item);
        }

        #endregion

        #region IEnumerable<int> Members

        public IEnumerator<int> GetEnumerator() {
            return _data.GetEnumerator();
        }

        #endregion

        #region IEnumerable Members

        System.Collections.IEnumerator System.Collections.IEnumerable.GetEnumerator() {
            return ((IEnumerable)_data).GetEnumerator();
        }

        #endregion
    }

    public class IndexableIteration {
        public int this[int index] {
            get {
                if (index > 0) {
                    throw PythonOps.StopIteration();
                }
                return index;
            }
        }
    }
}
