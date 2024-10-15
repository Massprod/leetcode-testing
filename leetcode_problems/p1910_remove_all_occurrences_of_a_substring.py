# Given two strings s and part, perform the following operation on s until all occurrences
#  of the substring part are removed:
#  - Find the leftmost occurrence of the substring part and remove it from s.
# Return s after removing all occurrences of part.
# A substring is a contiguous sequence of characters in a string.
# ------------------
# 1 <= s.length <= 1000
# 1 <= part.length <= 1000
# s and part consists of lowercase English letters.
from random import choice
from string import ascii_lowercase


def remove_occurrences(s: str, part: str) -> str:
    # working_sol (52.09%, 11.76%) -> (39ms, 16.74mb)  time: O(s) | space: O(s)
    def check(arr: list[str], word: str) -> bool:
        for index in range(1, len(word) + 1):
            cor_index: int = index * -1
            if arr[cor_index] != word[cor_index]:
                return False
        return True

    stack: list[str] = []
    for char in s:
        stack.append(char)
        if len(stack) >= len(part):
            if check(stack, part):
                for _ in range(len(part)):
                    stack.pop()
    return ''.join(stack)


# Time complexity: O(s)
# In the worst case every symbol we add will trigger `check` => O(s).
# ------------------
# Auxiliary space: O(s)
# In the worst case not a single `part` is present in `s`.
# `stack` <- allocates space for each char from `s` => O(s).


test: str = "daabcbaabcbc"
test_part: str = "abc"
test_out: str = "dab"
assert test_out == remove_occurrences(test, test_part)

test = "axxxxyyyyb"
test_part = "xy"
test_out = "ab"
assert test_out == remove_occurrences(test, test_part)

test = ''.join([choice(ascii_lowercase) for _ in range(1000)])
print(test)
test_part = ''.join([choice(ascii_lowercase) for _ in range(100)])
print('part', test_part)
