# Given a string s of zeros and ones, return the maximum score after splitting the string
#  into two non-empty substrings (i.e. left substring and right substring).
# The score after splitting a string is the number of zeros in the left substring
#  plus the number of ones in the right substring.
# ---------------------
# 2 <= s.length <= 500
# The string s consists of characters '0' and '1' only.
from random import choice


def max_score(s: str) -> int:
    # working_sol (86.87%, 5.69%) -> (36ms, 17.20mb)  time: O(n) | space: O(n)
    # [left side score of '0', for every index]
    prefixes: list[int] = [0]
    prefix: int = 0
    # Calc prefix for last index, to check if there's '0' present in case like '1110'.
    for x in range(1, len(s) + 1):
        prefix = prefix + (1 if s[x - 1] == '0' else 0)
        prefixes.append(prefix)
    suffix: int = 0
    # There's no '0' present, but we still need to slice in 2 substrings => -1 element.
    if not prefixes[-1]:
        return len(s) - 1
    out: int = prefixes[-2] + int(s[-1])  # last index only have prefix and itself as score, if we slice on left.
    # Calc suffix for 0 index, to check if there's '1' present in case like '01111'.
    for x in range(len(s) - 2, -2, -1):
        suffix = suffix + (1 if s[x + 1] == '1' else 0)
        if x > 0:
            # Every index except 0, can be sliced on both sides, so we can include it as +1 in score.
            out = max(out, prefixes[x] + suffix + 1)
        elif x == 0:
            # 0 index can't be sliced on left side and only counted in score if it's '0'.
            out = max(out, suffix + (1 if s[x] == '0' else 0))
    # There's no '1' present.
    if not suffix:
        return len(s) - 1
    return out


# Time complexity: O(n) <- n - length of input string `s`.
# Single traverse of every index of `s` to get all prefixes => O(n).
# Extra traverse to calculate maximum score => O(n).
# Auxiliary space: O(n).
# Extra array `prefixes` with size of (n + 1), because we calculate prefix for the last index.
# Which we don't need, but it's shorter than extra check of [-1] being '1' or '0', same for suffix.
# And 3 extra constant INTs, none of them depends on input => O(1).


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
