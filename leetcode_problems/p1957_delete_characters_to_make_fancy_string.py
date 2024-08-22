# A fancy string is a string where no three consecutive characters are equal.
# Given a string s, delete the minimum possible number of characters from s to make it fancy.
# Return the final string after the deletion.
# It can be shown that the answer will always be unique.
# -------------------------
# 1 <= s.length <= 10 ** 5
# s consists only of lowercase English letters.


def make_fancy_string(s: str) -> str:
    # working_sol (82.04%, 92.65%) -> (306ms, 18.28mb)  time: O(s) | space: O(s)
    out: list[str] = []
    stack: list[str] = []
    for char in s:
        if stack and stack[-1] == char:
            if len(stack) < 2:
                stack.append(char)
            continue
        out += stack
        stack = [char]
    out += stack
    return ''.join(out)


# Time complexity: O(s)
# Always traversing whole input string `s`, once => O(s).
# Stack is never exceeding size of `2`, so we can say its constant to append it.
# -------------------------
# Auxiliary space: O(s)
# In the worst case, there's only correct sequences.
# `out` <- will allocate space for each char in `s` => O(s).


test: str = "leeetcode"
test_out: str = "leetcode"
assert test_out == make_fancy_string(test)

test = "aaabaaaa"
test_out = "aabaa"
assert test_out == make_fancy_string(test)

test = "aab"
test_out = "aab"
assert test_out == make_fancy_string(test)
