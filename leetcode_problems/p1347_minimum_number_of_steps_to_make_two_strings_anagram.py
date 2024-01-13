# You are given two strings of the same length s and t.
# In one step you can choose any character of t and replace it with another character.
# Return the minimum number of steps to make t an anagram of s.
# An Anagram of a string is a string that contains the same characters
#  with a different (or the same) ordering.
# -------------------
# 1 <= s.length <= 5 * 10 ** 4
# s.length == t.length
# s and t consist of lowercase English letters only.
from random import choice
from collections import Counter
from string import ascii_lowercase


def min_steps(s: str, t: str) -> int:
    # working_sol (32.02%, 21.41%) -> (207ms, 17.90mb)  time: O(n) | space: O(n).
    # {symbol: occurs}
    all_chars: dict[str, int] = Counter(s)
    # ! s.length == t.length ! <- we can always make Anagram.
    for char in t:
        # We can cover `char` without change -> no switch.
        if char in all_chars and all_chars[char]:
            all_chars[char] -= 1
    # We need to cover what's left -> 1 switch(step) for 1 char(symbol).
    return sum(all_chars.values())


# Time complexity: O(n) <- n - length of input string `s` or `t`, both equal sized.
# Single traverse of `s` to get all symbol occurrences => O(n).
# Single traverse of `t` to take out all symbols we can cover => O(n).
# Worst case: every symbol is unique.
# Extra traverse of all unique symbols to get sum() of values => O(n).
# -------------------
# Auxiliary space: O(n).
# Same worst case, every symbol will be stored as key, value pair => O(n).
# -------------------
# Can be done faster with 2 Counter()'s, it's less readable and I don't like.
# But x2 faster, because we're not doing double IF check on every symbol.


test: str = 'bab'
test_t: str = 'aba'
test_out: int = 1
assert test_out == min_steps(test, test_t)

test = "leetcode"
test_t = "practice"
test_out = 5
assert test_out == min_steps(test, test_t)

test = "anagram"
test_t = "mangaar"
test_out = 0
assert test_out == min_steps(test, test_t)

test = ''.join([choice(ascii_lowercase) for _ in range(5 * 10 ** 4)])
test_t = ''.join([choice(ascii_lowercase) for _ in range(5 * 10 ** 4)])
print(f'{test}\n\n{test_t}')
