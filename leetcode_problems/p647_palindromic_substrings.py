# Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward.
# A substring is a contiguous sequence of characters within the string.
# -----------------
# 1 <= s.length <= 1000
# s consists of lowercase English letters.
from string import ascii_lowercase
from random import choice


def count_substrings(s: str) -> int:
    # working_sol (5%, 5.54%) -> (1050ms, 181.3mb)  time: O(n * n) | space: O(n * n)
    recur_cache: dict[tuple[int, int]: int] = {}

    def check(l_index: int, r_index: int) -> int:
        # Already incremented
        if (l_index, r_index) in recur_cache:
            return 0
        if l_index == r_index:
            return 0
        count: int = 0
        if s[l_index: r_index + 1] == s[l_index: r_index + 1][::-1]:
            count += 1
        # Taking every string possible from input_string.
        count += check(l_index + 1, r_index)
        count += check(l_index, r_index - 1)
        recur_cache[l_index, r_index] = count
        return count

    return len(s) + check(0, len(s) - 1)


# Time complexity: O(n * n) -> recursion for every pair of indexes, used once => O(n * n).
# n - len of input_array^^|
# Auxiliary space: O(n * n) -> all pairs saved in cache => O(n * n)


test: str = "abc"
test_out: int = 3
assert test_out == count_substrings(test)

test = "aaa"
test_out = 6
assert test_out == count_substrings(test)

test = ''
for _ in range(1000):
    test += choice(ascii_lowercase)
print(test)
