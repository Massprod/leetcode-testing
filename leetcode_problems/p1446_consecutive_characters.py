# The power of the string is the maximum length
#  of a non-empty substring that contains only one unique character.
# Given a string s, return the power of s.
# ------------------
# 1 <= s.length <= 500
# s consists of only lowercase English letters.


def max_power(s: str) -> int:
    # working_sol (61.30%, 63.68%) -> (42ms, 16.49mb)  time: O(s) | space: O(1)
    out: int = 1
    cur_power: int = 1
    for index in range(1, len(s)):
        if s[index - 1] == s[index]:
            cur_power += 1
        else:
            out = max(out, cur_power)
            cur_power = 1
    out = max(out, cur_power)
    return out


# Time complexity: O(s)
# Always traversing whole `s`, once => O(s).
# ------------------
# Auxiliary space: O(1)
# Only 2 constant INTs used, none of them depends on input => O(1).


test: str = "leetcode"
test_out: int = 2
assert test_out == max_power(test)

test = "abbcccddddeeeeedcba"
test_out = 5
assert test_out == max_power(test)
