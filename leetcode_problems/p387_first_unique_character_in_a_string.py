# Given a string s, find the first non-repeating character in it and return its index.
# If it does not exist, return -1.
# -------------------
# 1 <= s.length <= 10 ** 5
# s consists of only lowercase English letters.
from random import choice
from string import ascii_lowercase


def first_uniq_char(s: str) -> int:
    # working_sol (27.40%, 82.5%) -> (156ms, 16.5mb)  time: O(n) | space: O(n)
    # symbol: (index, occurrences)
    all_symbs: dict[str, tuple[int, int]] = {}
    for x in range(len(s)):
        if s[x] not in all_symbs:
            all_symbs[s[x]] = (x, 1)
            continue
        all_symbs[s[x]] = (all_symbs[s[x]][0], all_symbs[s[x]][1] + 1)
    min_index: int = len(s)
    for index, occurs in all_symbs.values():
        if occurs == 1:
            min_index = min(min_index, index)
    if min_index == len(s):
        return -1
    return min_index


# Time complexity: O(n) -> traversing whole input_string to get symbols and occurrences => O(n) ->
# n - len of input_string^^| -> traversing again to find min_index => O(n). <- worst case with all symbols unique.
# Auxiliary space: O(n) -> saving all symbols, with worst case == all symbols unique, all will be saved => O(n).


test: str = "leetcode"
test_out: int = 0
assert test_out == first_uniq_char(test)

test = "loveleetcode"
test_out = 2
assert test_out == first_uniq_char(test)

test = "aabb"
test_out = -1
assert test_out == first_uniq_char(test)

test = ''
for _ in range(10 ** 3):
    test += choice(ascii_lowercase)
print(test)
