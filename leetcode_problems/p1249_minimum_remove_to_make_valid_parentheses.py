# Given a string s of '(' , ')' and lowercase English characters.
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions )
#  so that the resulting parentheses string is valid and return any valid string.
# Formally, a parentheses string is valid if and only if:
#  - It is the empty string, contains only lowercase characters, or
#  - It can be written as AB (A concatenated with B), where A and B are valid strings, or
#  - It can be written as (A), where A is a valid string.
# --------------------------
# 1 <= s.length <= 10 ** 5
# s[i] is either'(' , ')', or lowercase English letter.
from random import choice
from collections import deque
from string import ascii_lowercase


def min_remove(s: str) -> str:
    # working_sol (22.10%, 95.54%) -> (99ms, 17.90mb)  time: O(s) | space: O(s)
    stack: deque[str] = deque([])
    open_br: str = '('
    close_br: str = ')'
    out: str = ''
    _open: int = 0
    _close: int = 0
    for char in s:
        # More|Equal close brackets => we need to close every opener.
        # Or there's no openers, so we need to use every char and ignore close bracket.
        if _close >= _open or (open_br == char and not _open and _close):
            open_limit = close_limit = min(_open, _close)
            while stack:
                if open_br == stack[0]:
                    if open_limit:
                        out += stack.popleft()
                        open_limit -= 1
                    else:
                        stack.popleft()
                elif close_br == stack[0]:
                    if close_limit:
                        out += stack.popleft()
                        close_limit -= 1
                    else:
                        stack.popleft()
                elif open_br != stack[0] and close_br != stack[0]:
                    out += stack.popleft()
            _open = 0
            _close = 0
        if open_br == char:
            _open += 1
        elif close_br == char:
            _close += 1
        stack.append(char)
    # If there's no trigger at the end, we still need to add all the symbols.
    open_limit = close_limit = min(_open, _close)
    while stack:
        if open_br == stack[0]:
            if open_limit:
                out += stack.popleft()
                open_limit -= 1
            else:
                stack.popleft()
        elif close_br == stack[0]:
            if close_limit:
                out += stack.popleft()
                close_limit -= 1
            else:
                stack.popleft()
        elif open_br != stack[0] and close_br != stack[0]:
            out += stack.popleft()
    return out


# Time complexity: O(s)
# In any case we will use every index twice, add to stack and pop from it => O(2s).
# --------------------------
# Auxiliary space: O(s)
# Worst case, there's no brackets, so we will just add every symbol into `stack` => O(s)


test: str = "lee(t(c)o)de)"
test_out: str = "lee(t(c)o)de"
assert test_out == min_remove(test)

test = "a)b(c)d"
test_out = "ab(c)d"
assert test_out == min_remove(test)

test = "))(("
test_out = ""
assert test_out == min_remove(test)

test = ")bafxznws)ojlmi)shbbjnan(nc)(ajlhmtmxdehqquyaes(zrsijfutwgqj)vvjrmht(qlj(sm(vfxvayebzhpponobudynmotf"
test_out = "bafxznwsojlmishbbjnan(nc)(ajlhmtmxdehqquyaeszrsijfutwgqj)vvjrmhtqljsmvfxvayebzhpponobudynmotf"
assert test_out == min_remove(test)

test_symbs: list[str] = ['(', ')'] + list(ascii_lowercase)
test = ''.join([choice(test_symbs) for _ in range(10 ** 5)])
print(test)
