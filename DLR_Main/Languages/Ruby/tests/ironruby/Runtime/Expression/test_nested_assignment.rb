# ****************************************************************************
#
# Copyright (c) Microsoft Corporation. 
#
# This source code is subject to terms and conditions of the Microsoft Public License. A 
# copy of the license can be found in the License.html file at the root of this distribution. If 
# you cannot locate the  Microsoft Public License, please send an email to 
# ironruby@microsoft.com. By using this source code in any fashion, you are agreeing to be bound 
# by the terms of the Microsoft Public License.
#
# You must not remove this notice, or any other, from this software.
#
#
# ****************************************************************************


require '../../util/assert.rb'

# left side of assignment may contain a parenthesized list of terms.
# it extracts the corresponding rvalue, assigning it to the parenthesized terms, before continuing
# with higher-level assignment.

# (a) = 3: syntax error

