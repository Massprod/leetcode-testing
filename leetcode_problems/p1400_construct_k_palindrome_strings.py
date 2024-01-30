# Given a string s and an integer k, return true
#  if you can use all the characters in s to construct k palindrome strings or false otherwise.
# ---------------------
# 1 <= s.length <= 10 ** 5
# s consists of lowercase English letters.
# 1 <= k <= 10 ** 5
from random import choice
from collections import Counter
from string import ascii_lowercase


def can_construct(s: str, k: int) -> bool:
    # working_sol (92.97%, 55.08%) -> (63ms, 17.42mb)  time: O(s) | space: O(s)
    # If we use every symbol as palindrome, we still won't have enough palindromes.
    if k > len(s):
        return False
    all_syms: dict[str, int] = Counter(s)
    odd: int = 0
    for sym, occurs in all_syms.items():
        if occurs % 2:
            odd += 1
    # We need to use EVERY symbol from `s`.
    # And if we have ODD palindrome we can use it only as WHOLE.
    # So, if there's more than `k` ODD palindromes, some of them won't be used
    #  and symbols in them as well.
    # EVEN palindromes, can be used in w.e options: connected to ODD or used as STANDALONE.
    # And they're always using all symbols.
    if odd > k:
        return False
    return True


# Time complexity: O(s).
# Traversing whole input string `s` once, to get all occurrences => O(s).
# Worst case: all symbols in `s` are unique.
# Extra traversing dict with all symbols `all_syms` and there's (keys == len(s)) => O(s).
# ---------------------
# Auxiliary space: O(s).
# We store every unique symbol from `s`, and in the worst case ALL unique => O(s).


test: str = "annabelle"
test_k: int = 2
test_out: bool = True
assert test_out == can_construct(test, test_k)

test = "leetcode"
test_k = 3
test_out = False
assert test_out == can_construct(test, test_k)

test = "true"
test_k = 4
test_out = True
assert test_out == can_construct(test, test_k)

test = ''.join([choice(ascii_lowercase) for _ in range(10 ** 5)])
print(test)
