# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
# Given a balanced string s, split it into some number of substrings such that:
#  - Each substring is balanced.
# Return the maximum number of balanced strings you can obtain.
# -----------------------
# 2 <= s.length <= 1000
# s[i] is either 'L' or 'R'.
# s is a balanced string.


def balanced_string_split(s: str) -> int:
    # working_sol (91.43%, 54.62%) -> (28ms, 16.46mb)  time: O(s) | space: O(1)
    out: int = 0
    count: int = 0
    for char in s:
        if 'R' == char:
            count -= 1
        elif 'L' == char:
            count += 1
        if 0 == count:
            out += 1
    return out


# Time complexity: O(s)
# Always traversing every char in `s` to count substrings => O(s).
# -----------------------
# Auxiliary space: O(1)
# Only 2 constant INT's used, none of them depends on input => O(1).


test: str = "RLRRLLRLRL"
test_out: int = 4
assert test_out == balanced_string_split(test)

test = "RLRRRLLRLL"
test_out = 2
assert test_out == balanced_string_split(test)

test = "LLLLRRRR"
test_out = 1
assert test_out == balanced_string_split(test)
