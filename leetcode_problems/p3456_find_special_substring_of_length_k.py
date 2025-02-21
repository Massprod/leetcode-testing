# You are given a string s and an integer k.
# Determine if there exists a substring
#  of length exactly k in s that satisfies the following conditions:
#  1. The substring consists of only one distinct character (e.g., "aaa" or "bbb").
#  2. If there is a character immediately before the substring,
#     it must be different from the character in the substring.
#  3. If there is a character immediately after the substring,
#     it must also be different from the character in the substring.
# Return true if such a substring exists.
# Otherwise, return false.
# ------------------------
# 1 <= k <= s.length <= 100
# s consists of lowercase English letters only.
from random import choice

from string import ascii_lowercase

from pyperclip import copy


def has_special_substring(s: str, k: int) -> bool:
    # working_sol (100.00%, 64.98%) -> (0ms, 17.76mb)  time: O(s) | space: O(s)
    stack: list[str] = []
    left_l: int = 0
    right_l: int = 0
            
    while right_l < len(s):
        if stack and s[right_l] == stack[-1]:
            stack.append(s[right_l])
        else:
            stack = [s[right_l]]
            left_l = right_l
        if k == len(stack):
            left_shift: int = left_l - 1
            right_shift: int = right_l + 1
            left_cor: bool = False
            right_cor: bool = False
            # Either exist and different.
            # Or it shouldn't exist at all.
            if ((0 <= left_shift < len(s)
                and s[left_shift] != stack[-1])
                or not 0 <= left_shift < len(s)):
                left_cor = True
            # Same logic.
            if ((0 <= right_shift < len(s)
                and s[right_shift] != stack[-1])
                or not 0 <= right_shift < len(s)):
                right_cor = True
            if left_cor and right_cor:    
                return True
        right_l += 1
    
    return False
        

# Time complexity: O(s)
# In the worst case we're going to have `k` == 1.
# And all chars of `s` is going to be equal.
# We will use every index, twice: add to stack, pop from stack => O(s).
# ------------------------
# Auxiliary space: O(s)
# In the worst case whole input string `s` is going to be a subarray we need.
# `stack` <- allocates space for each char from `s` => O(s).


test: str = "aaabaaa"
test_k: int = 3
test_out: bool = True
assert test_out == has_special_substring(test, test_k)

test = "abc"
test_k = 2
test_out = False
assert test_out == has_special_substring(test, test_k)

test = 'h'
test_k = 1
test_out = True
assert test_out == has_special_substring(test, test_k)

test = 'dii'
test_k = 1
test_out = True
assert test_out == has_special_substring(test, test_k)

test = ''.join([choice(ascii_lowercase) for _ in range(100)])
copy(test)
