# Given a string s, find the length of the longest substring without repeating characters
# --------------------
# 0 <= s.length <= 5 * 10 ** 4
# s consists of English letters, digits, symbols and spaces.
from random import choice
from string import ascii_letters, digits


def longest_sub(s: str) -> int:
    # working_sol (95.89%, 94.41%) -> (48ms, 16.3mb)  time: O(n) | space: O(n)
    used: set[str] = set()
    # Standard sliding window.
    start: int = 0
    longest: int = 0
    cur_sub: int = 0
    for x in range(len(s)):
        # Expand.
        if s[x] not in used:
            used.add(s[x])
            cur_sub += 1
        # Shrink.
        else:
            longest = max(longest, cur_sub)
            # Delete everything until duplicate.
            while s[start] != s[x]:
                used.remove(s[start])
                start += 1
                cur_sub -= 1
            # Duplicate is still in cur_sub, but sub starts after it.
            start += 1
    # Extra check for last index.
    longest = max(longest, cur_sub)
    return longest


# Time complexity: O(n) -> traverse of whole input string => O(n) -> standard sliding window, so in worst case
# n - len of input string^^| we will use every index twice to add and delete it from window => O(2n).
# Auxiliary space: O(n) -> no duplicates, every symbol of input string will be stored in set(used) => O(n).


test: str = "abcabcbb"
test_out: int = 3
assert test_out == longest_sub(test)

test = "bbbbb"
test_out = 1
assert test_out == longest_sub(test)

test = "pwwkew"
test_out = 3
assert test_out == longest_sub(test)

test = ' '
test_out = 1
assert test_out == longest_sub(test)

test = ''
for _ in range(10 ** 4):
    test += choice([choice(ascii_letters), choice(digits)])
print(test)
