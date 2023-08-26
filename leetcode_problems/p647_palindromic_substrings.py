# Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward.
# A substring is a contiguous sequence of characters within the string.
# -----------------
# 1 <= s.length <= 1000
# s consists of lowercase English letters.
from string import ascii_lowercase
from random import choice


def count_substrings(s: str) -> int:
    # working_sol (78.85%, 77.64%) -> (109ms, 16.2mb)  time: O(n * k) | space: O(1)
    count: int = 0
    # Try building Palindrome starting from every symbol possible.
    for x in range(len(s)):
        # Even substring, always includes 1 symbol from start.
        l_index: int = x
        r_index: int = x
        # Expand while we can, and count every correct expansion.
        while l_index >= 0 and r_index < len(s) and s[l_index] == s[r_index]:
            count += 1
            l_index -= 1
            r_index += 1
        # Odd substring, always includes 2 symbols from start.
        l_index = x
        r_index = x + 1
        while l_index >= 0 and r_index < len(s) and s[l_index] == s[r_index]:
            count += 1
            l_index -= 1
            r_index += 1
    return count


# Time complexity: O(n * k) -> for every possible index of input_string, building palindromes ->
# n - len of input_string^^| -> worst case len(1000) and 'aaaaa', so for every index we will use k indexes,
# k - expand limit^^|        we always expand in left and right sides, but they never exceed min(left, right) ->
#                            -> like [10] we will only expand left side from [10] to [0], same for right side indexes,
#                            len == 100, [80] -> we will only expand right side for 20 indexes.
#                            How to calc it correctly? Left side is cur_index + 0, and right side is len(s) - cur_index.
#                            Left -> k = cur_index + 0 | Right -> k = len(s) - cur_index
# Auxiliary space: O(1) -> only 3 constant INTs used, none of them depends on input => O(1).
# -----------------
# Ok. There's a better way to do this, we can just start building from every index.
# And add indexes from left and right sides until they're equal, cuz we need ! contiguous sequence ! only.
# Rebuild.
# Actually it should be the same BigO anyway, like worst case ->
# -> we're having len(1000) and str == 'aaaa', so we still will use all n * n pairs => O(n * n)
# But most cases will break when trying to expand with incorrect symbol.
# Can I change recursion to check it?
# Nah. I need to fully rebuild then. Cuz we're just checking all consecutive subs in it, no matter
#  correct or not. So it's can be rebuilt, but essentially will become this solution just with calling
#  recursion on the WHILE loops. Ok. Good exp anyway.


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
