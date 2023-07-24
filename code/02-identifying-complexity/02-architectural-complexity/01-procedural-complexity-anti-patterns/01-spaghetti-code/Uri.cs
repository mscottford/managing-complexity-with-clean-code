// The `RecreateParts` method below was copied from the .NET `runtime` project,
// specifically the `src/libraries/System.Private.Uri/src/System/Uri.cs` file.
// It was retrieved from
// https://github.com/dotnet/runtime/blob/78b45adbf20ab365f86d3b81c067d90719eaa7d0/src/libraries/System.Private.Uri/src/System/Uri.cs#L2752-L2987
// on July 23, 2023.
//
// The code's license is at the bottom of this file.

private ReadOnlySpan<char> RecreateParts(scoped ref ValueStringBuilder dest, string str, UriComponents parts, ushort nonCanonical, UriFormat formatAs)
{
    //Scheme and slashes
    if ((parts & UriComponents.Scheme) != 0)
    {
        dest.Append(_syntax.SchemeName);
        if (parts != UriComponents.Scheme)
        {
            dest.Append(':');
            if (InFact(Flags.AuthorityFound))
            {
                dest.Append('/');
                dest.Append('/');
            }
        }
    }

    //UserInfo
    if ((parts & UriComponents.UserInfo) != 0 && InFact(Flags.HasUserInfo))
    {
        ReadOnlySpan<char> slice = str.AsSpan(_info.Offset.User, _info.Offset.Host - _info.Offset.User);

        if ((nonCanonical & (ushort)UriComponents.UserInfo) != 0)
        {
            switch (formatAs)
            {
                case UriFormat.UriEscaped:
                    if (NotAny(Flags.UserEscaped))
                    {
                        UriHelper.EscapeString(slice, ref dest, checkExistingEscaped: true, UriHelper.UnreservedReservedExceptQuestionMarkHash);
                    }
                    else
                    {
                        // We would ideally throw here if InFact(Flags.E_UserNotCanonical) but currently just accept user input known as invalid
                        dest.Append(slice);
                    }
                    break;

                case UriFormat.SafeUnescaped:
                    UriHelper.UnescapeString(slice[..^1],
                        ref dest, '@', '/', '\\',
                        InFact(Flags.UserEscaped) ? UnescapeMode.Unescape : UnescapeMode.EscapeUnescape,
                        _syntax, isQuery: false);
                    dest.Append('@');
                    break;

                case UriFormat.Unescaped:
                    UriHelper.UnescapeString(slice,
                        ref dest, c_DummyChar, c_DummyChar, c_DummyChar,
                        UnescapeMode.Unescape | UnescapeMode.UnescapeAll,
                        _syntax, isQuery: false);
                    break;

                default: //V1ToStringUnescape
                    dest.Append(slice);
                    break;
            }
        }
        else
        {
            dest.Append(slice);
        }

        if (parts == UriComponents.UserInfo)
        {
            //strip '@' delimiter
            dest.Length--;
        }
    }

    // Host
    if ((parts & UriComponents.Host) != 0)
    {
        string host = _info.Host!;

        if (host.Length != 0)
        {
            UnescapeMode mode;
            if (formatAs != UriFormat.UriEscaped && HostType == Flags.BasicHostType
                && (nonCanonical & (ushort)UriComponents.Host) != 0)
            {
                // only Basic host could be in the escaped form
                mode = formatAs == UriFormat.Unescaped
                    ? (UnescapeMode.Unescape | UnescapeMode.UnescapeAll) :
                        (InFact(Flags.UserEscaped) ? UnescapeMode.Unescape : UnescapeMode.EscapeUnescape);
            }
            else
            {
                mode = UnescapeMode.CopyOnly;
            }

            var hostBuilder = new ValueStringBuilder(stackalloc char[StackallocThreshold]);

            // NormalizedHost
            if ((parts & UriComponents.NormalizedHost) != 0)
            {
                host = UriHelper.StripBidiControlCharacters(host, host);

                // Upconvert any punycode to unicode, xn--pck -> ?
                if (!DomainNameHelper.TryGetUnicodeEquivalent(host, ref hostBuilder))
                {
                    hostBuilder.Length = 0;
                }
            }

            UriHelper.UnescapeString(hostBuilder.Length == 0 ? host : hostBuilder.AsSpan(),
                ref dest, '/', '?', '#',
                mode,
                _syntax, isQuery: false);

            hostBuilder.Dispose();

            // A fix up only for SerializationInfo and IpV6 host with a scopeID
            if ((parts & UriComponents.SerializationInfoString) != 0 && HostType == Flags.IPv6HostType && _info.ScopeId != null)
            {
                dest.Length--;
                dest.Append(_info.ScopeId);
                dest.Append(']');
            }
        }
    }

    //Port (always wants a ':' delimiter if got to this method)
    if ((parts & UriComponents.Port) != 0 &&
        (InFact(Flags.NotDefaultPort) || ((parts & UriComponents.StrongPort) != 0 && _syntax.DefaultPort != UriParser.NoDefaultPort)))
    {
        dest.Append(':');

        const int MaxUshortLength = 5;
        bool success = _info.Offset.PortValue.TryFormat(dest.AppendSpan(MaxUshortLength), out int charsWritten);
        Debug.Assert(success);
        dest.Length -= MaxUshortLength - charsWritten;
    }

    //Path
    if ((parts & UriComponents.Path) != 0)
    {
        GetCanonicalPath(ref dest, formatAs);

        // (possibly strip the leading '/' delimiter)
        if (parts == UriComponents.Path)
        {
            int offset;
            if (InFact(Flags.AuthorityFound) && dest.Length != 0 && dest[0] == '/')
            {
                offset = 1;
            }
            else
            {
                offset = 0;
            }

            return dest.AsSpan(offset);
        }
    }

    //Query (possibly strip the '?' delimiter)
    if ((parts & UriComponents.Query) != 0 && _info.Offset.Query < _info.Offset.Fragment)
    {
        int offset = (_info.Offset.Query + 1);
        if (parts != UriComponents.Query)
            dest.Append('?');

        UnescapeMode mode = UnescapeMode.CopyOnly;

        if ((nonCanonical & (ushort)UriComponents.Query) != 0)
        {
            if (formatAs == UriFormat.UriEscaped)
            {
                if (NotAny(Flags.UserEscaped))
                {
                    UriHelper.EscapeString(
                        str.AsSpan(offset, _info.Offset.Fragment - offset),
                        ref dest, checkExistingEscaped: true, UriHelper.UnreservedReservedExceptHash);

                    goto AfterQuery;
                }
            }
            else
            {
                mode = formatAs switch
                {
                    V1ToStringUnescape => (InFact(Flags.UserEscaped) ? UnescapeMode.Unescape : UnescapeMode.EscapeUnescape) | UnescapeMode.V1ToStringFlag,
                    UriFormat.Unescaped => UnescapeMode.Unescape | UnescapeMode.UnescapeAll,
                    _ => InFact(Flags.UserEscaped) ? UnescapeMode.Unescape : UnescapeMode.EscapeUnescape
                };
            }
        }

        UriHelper.UnescapeString(str, offset, _info.Offset.Fragment,
            ref dest, '#', c_DummyChar, c_DummyChar,
            mode, _syntax, isQuery: true);
    }
AfterQuery:

    //Fragment (possibly strip the '#' delimiter)
    if ((parts & UriComponents.Fragment) != 0 && _info.Offset.Fragment < _info.Offset.End)
    {
        int offset = _info.Offset.Fragment + 1;
        if (parts != UriComponents.Fragment)
            dest.Append('#');

        UnescapeMode mode = UnescapeMode.CopyOnly;

        if ((nonCanonical & (ushort)UriComponents.Fragment) != 0)
        {
            if (formatAs == UriFormat.UriEscaped)
            {
                if (NotAny(Flags.UserEscaped))
                {
                    UriHelper.EscapeString(
                        str.AsSpan(offset, _info.Offset.End - offset),
                        ref dest, checkExistingEscaped: true, UriHelper.UnreservedReserved);

                    goto AfterFragment;
                }
            }
            else
            {
                mode = formatAs switch
                {
                    V1ToStringUnescape => (InFact(Flags.UserEscaped) ? UnescapeMode.Unescape : UnescapeMode.EscapeUnescape) | UnescapeMode.V1ToStringFlag,
                    UriFormat.Unescaped => UnescapeMode.Unescape | UnescapeMode.UnescapeAll,
                    _ => InFact(Flags.UserEscaped) ? UnescapeMode.Unescape : UnescapeMode.EscapeUnescape
                };
            }
        }

        UriHelper.UnescapeString(str, offset, _info.Offset.End,
            ref dest, '#', c_DummyChar, c_DummyChar,
            mode, _syntax, isQuery: false);
    }

AfterFragment:
    return dest.AsSpan();
}

// The license text below was copied from https://github.com/dotnet/runtime/blob/78b45adbf20ab365f86d3b81c067d90719eaa7d0/LICENSE.TXT

// The MIT License (MIT)
//
// Copyright(c).NET Foundation and Contributors
//
// All rights reserved.
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.
