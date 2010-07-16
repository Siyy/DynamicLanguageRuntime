/* ****************************************************************************
 *
 * Copyright (c) Microsoft Corporation. 
 *
 * This source code is subject to terms and conditions of the Apache License, Version 2.0. A 
 * copy of the license can be found in the License.html file at the root of this distribution. If 
 * you cannot locate the  Apache License, Version 2.0, please send an email to 
 * dlr@microsoft.com. By using this source code in any fashion, you are agreeing to be bound 
 * by the terms of the Apache License, Version 2.0.
 *
 * You must not remove this notice, or any other, from this software.
 *
 *
 * ***************************************************************************/

namespace IronPython.Compiler {
    public partial class Tokenizer {

        Token NextOperator(int ch) {
            switch (ch) {
                #region Generated Tokenize Ops

                // *** BEGIN GENERATED CODE ***
                // generated by function: tokenize_generator from: generate_ops.py

                case '+':
                    if (NextChar('=')) {
                        return Tokens.AddEqualToken;
                    }
                    return Tokens.AddToken;
                case '-':
                    if (NextChar('=')) {
                        return Tokens.SubtractEqualToken;
                    }
                    return Tokens.SubtractToken;
                case '*':
                    if (NextChar('=')) {
                        return Tokens.MultiplyEqualToken;
                    }
                    if (NextChar('*')) {
                        if (NextChar('=')) {
                            return Tokens.PowerEqualToken;
                        }
                        return Tokens.PowerToken;
                    }
                    return Tokens.MultiplyToken;
                case '/':
                    if (NextChar('=')) {
                        return Tokens.DivideEqualToken;
                    }
                    if (NextChar('/')) {
                        if (NextChar('=')) {
                            return Tokens.FloorDivideEqualToken;
                        }
                        return Tokens.FloorDivideToken;
                    }
                    return Tokens.DivideToken;
                case '%':
                    if (NextChar('=')) {
                        return Tokens.ModEqualToken;
                    }
                    return Tokens.ModToken;
                case '<':
                    if (NextChar('>')) {
                        return Tokens.LessThanGreaterThanToken;
                    }
                    if (NextChar('=')) {
                        return Tokens.LessThanOrEqualToken;
                    }
                    if (NextChar('<')) {
                        if (NextChar('=')) {
                            return Tokens.LeftShiftEqualToken;
                        }
                        return Tokens.LeftShiftToken;
                    }
                    return Tokens.LessThanToken;
                case '>':
                    if (NextChar('>')) {
                        if (NextChar('=')) {
                            return Tokens.RightShiftEqualToken;
                        }
                        return Tokens.RightShiftToken;
                    }
                    if (NextChar('=')) {
                        return Tokens.GreaterThanOrEqualToken;
                    }
                    return Tokens.GreaterThanToken;
                case '&':
                    if (NextChar('=')) {
                        return Tokens.BitwiseAndEqualToken;
                    }
                    return Tokens.BitwiseAndToken;
                case '|':
                    if (NextChar('=')) {
                        return Tokens.BitwiseOrEqualToken;
                    }
                    return Tokens.BitwiseOrToken;
                case '^':
                    if (NextChar('=')) {
                        return Tokens.ExclusiveOrEqualToken;
                    }
                    return Tokens.ExclusiveOrToken;
                case '=':
                    if (NextChar('=')) {
                        return Tokens.EqualsToken;
                    }
                    return Tokens.AssignToken;
                case '!':
                    if (NextChar('=')) {
                        return Tokens.NotEqualsToken;
                    }
                    return BadChar(ch);
                case '(':
                    _state.ParenLevel++;
                    return Tokens.LeftParenthesisToken;
                case ')':
                    _state.ParenLevel--;
                    return Tokens.RightParenthesisToken;
                case '[':
                    _state.BracketLevel++;
                    return Tokens.LeftBracketToken;
                case ']':
                    _state.BracketLevel--;
                    return Tokens.RightBracketToken;
                case '{':
                    _state.BraceLevel++;
                    return Tokens.LeftBraceToken;
                case '}':
                    _state.BraceLevel--;
                    return Tokens.RightBraceToken;
                case ',':
                    return Tokens.CommaToken;
                case ':':
                    return Tokens.ColonToken;
                case '`':
                    return Tokens.BackQuoteToken;
                case ';':
                    return Tokens.SemicolonToken;
                case '~':
                    return Tokens.TwiddleToken;
                case '@':
                    return Tokens.AtToken;

                // *** END GENERATED CODE ***

                #endregion
            }

            return null;
        }
    }
}
