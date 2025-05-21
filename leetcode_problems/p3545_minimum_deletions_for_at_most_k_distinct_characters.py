# You are given a string s consisting of lowercase English letters, and an integer k.
# Your task is to delete some (possibly none) of the characters in the string
#  so that the number of distinct characters in the resulting string is at most k.
# Return the minimum number of deletions required to achieve this.
# -----------------------
# 1 <= s.length <= 16
# 1 <= k <= 16
# s consists only of lowercase English letters.
from collections import Counter

from random import choice

from string import ascii_lowercase

from pyperclip import copy


def min_deletion(s: str, k: int) -> int:
    # working_sol (100.00%, 69.82%) -> (0ms, 17.79mb)  time: O(s * log s) | space: O(s)
    # { char: occurs }
    occurrences: dict[str, int] = Counter(s)
    out: int = 0

    sorted_occurs: list[int] = sorted(
        occurrences.values(), reverse=True
    )
    while len(sorted_occurs) > k:
        out += sorted_occurs[-1]
        sorted_occurs.pop()
    
    return out


# Time complexity: O(s * log s)
# In the worst case, we're going to have all chars in `s` being unique.
# Traversing and sorting all the unique chars of `s`, once => O(s * log s).
# -----------------------
# Auxiliary space: O(s)
# `occurrences` <- allocates space for each unique char from `s`.
# `sorted_occurs` <- allocates space for each unique char from `s`.


test: str = 'abc'
test_k: int = 2
test_out: int = 1
assert test_out == min_deletion(test, test_k)

test = 'aabb'
test_k = 2
test_out = 0
assert test_out == min_deletion(test, test_k)

test = 'yyyzz'
test_k = 1
test_out = 2
assert test_out == min_deletion(test, test_k)

test = ''.join([choice(ascii_lowercase) for _ in range(16)])
copy(test)
