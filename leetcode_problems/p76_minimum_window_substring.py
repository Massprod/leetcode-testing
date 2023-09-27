# Given two strings s and t of lengths m and n respectively, return the minimum window substring
#   of s such that every character in t (including duplicates) is included in the window.
#   If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.
# --------------------------
# m == s.length
# n == t.length
# 1 <= m, n <= 10 ** 5
# s and t consist of uppercase and lowercase English letters.
# --------------------------
# Follow up: Could you find an algorithm that runs in O(m + n) time?
from collections import Counter
from random import choice, randint
from string import ascii_letters


def min_window(s: str, t: str) -> str:
    # working_sol (56.36%, 98.46%) -> (120ms, 17mb)  time: O(n + m) | space: O(m)
    # All we need to maintain from 't'.
    all_symbols: dict[str, int] = Counter(t)
    # Standard sliding window.
    left_l: int = 0
    right_l: int = 0
    # # of correct symbols used.
    count: int = 0
    min_sub: list[int] = [0, 0]
    max_dif: int = len(s) + 1
    new: bool = True
    while right_l != len(s):
        # Add everything we can, no matter duplicates.
        if s[right_l] in all_symbols:
            # But, only count symbols which still not satisfied.
            if all_symbols[s[right_l]] > 0:
                count += 1
            # Count exceeding symbols,
            #  then we could delete them on left side.
            all_symbols[s[right_l]] -= 1
            right_l += 1
            if count == len(t):
                # Try to delete everything we can on left side.
                # (exceeding symbols or symbols we don't need)
                while s[left_l] not in all_symbols or all_symbols[s[left_l]] < 0:
                    if s[left_l] in all_symbols:
                        all_symbols[s[left_l]] += 1
                    left_l += 1
                    new = True
                # To cull extra calcs, better to ignore not changed substrings.
                # Because count will stay the same after it's reached len(t).
                if new:
                    new = False
                    # A little bit faster than creating slice and checking its length.
                    # less diff == less distance == shorter substring.
                    cur_dif: int = right_l - left_l
                    # Can't be lower.
                    if cur_dif == len(t):
                        return s[left_l: right_l]
                    elif max_dif > cur_dif:
                        max_dif = cur_dif
                        min_sub[0], min_sub[1] = left_l, right_l
        else:
            right_l += 1
    return s[min_sub[0]: min_sub[1]]


# Time complexity: O(n + m) -> traverse of all indexes of 't' to count occurrences => O(m) ->
# n - len of input string 's'^^| -> sliding window with using every index once if we don't shrink it ->
# m - len of input string 't'^^| -> and in the worst case we will use every index twice => O(2n + m).
# Auxiliary space: O(m) -> dictionary with all unique symbols of input string: 't' => O(m).
# --------------------------
# Ok. Changed to 52%+, 126ms. Possible to make it faster, but it's more than enough for now.
# At least x2 of pre-revisit version.


test: str = "ADOBECODEBANC"
test_t: str = "ABC"
test_out: str = "BANC"
assert test_out == min_window(test, test_t)

test = 'ADOBECODEBANC'
test_t = "AABC"
test_out = "ADOBECODEBA"
assert test_out == min_window(test, test_t)

test = "a"
test_t = "a"
test_out = "a"
assert test_out == min_window(test, test_t)

test = "a"
test_t = "aa"
test_out = ""
assert test_out == min_window(test, test_t)

test = "A"
test_t = "a"
test_out = ""
assert test_out == min_window(test, test_t)

test = "acbbaca"
test_t = "aba"
test_out = "baca"
assert test_out == min_window(test, test_t)

test = ''
for _ in range(10 ** 4):
    test += choice(ascii_letters)
test_t = test[randint(0, len(test) // 2): randint((len(test) // 2) + 1, len(test) - 1)]
# print(test)
# print('-----------------')
# print(test_t)
