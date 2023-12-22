# Given a string s of zeros and ones, return the maximum score after splitting the string
#  into two non-empty substrings (i.e. left substring and right substring).
# The score after splitting a string is the number of zeros in the left substring
#  plus the number of ones in the right substring.
# ---------------------
# 2 <= s.length <= 500
# The string s consists of characters '0' and '1' only.
from random import choice


def max_score(s: str) -> int:
    # working_sol (98.91%, 5.69%) -> (29ms, 17.24mb)  time: O(n) | space: O(1)
    cur_score: int = s.count('1')
    # '0' not present.
    if cur_score == len(s):
        return len(s) - 1
    # '1' not present.
    if cur_score == 0:
        return len(s) - 1
    # We have maximum score of right side == '1'.
    # If we slice from the right index side:
    #  every '0' => +1 to maximum score of left side
    #  every '1' => -1 to maximum score of right side.
    # Last index doesn't matter, it's either already counted as '1'
    #  or it's '0' and we can't include it.
    out: int = 0
    for x in range(len(s) - 1):
        if s[x] == '0':
            cur_score += 1
        else:
            cur_score -= 1
        out = max(out, cur_score)
    return out


# Time complexity: O(n) <- n - length of input string `s`.
# Single traverse of `s` to count() all '1' => O(n).
# Extra traverse to get maximum score `out` => O(n - 1).
# Auxiliary space: O(1).
# Only 2 extra INTs used, none of them depends on input => O(1).


test: str = "011101"
test_out: int = 5
assert test_out == max_score(test)

test = "00111"
test_out = 5
assert test_out == max_score(test)

test = "1111"
test_out = 3
assert test_out == max_score(test)

test = "11100"
test_out = 2
assert test_out == max_score(test)

test = "111111111111111111111111111111111111111111111111111111111111111110"
test_out = 64
assert test_out == max_score(test)

test = ''.join([choice(['0', '1']) for _ in range(500)])
print(test)
