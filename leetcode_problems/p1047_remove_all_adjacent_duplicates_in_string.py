# You are given a string s consisting of lowercase English letters.
# A duplicate removal consists of choosing two adjacent and equal letters and removing them.
# We repeatedly make duplicate removals on s until we no longer can.
# Return the final string after all such duplicate removals have been made.
# It can be proven that the answer is unique.
# -------------------------
# 1 <= s.length <= 10 ** 5
# s consists of lowercase English letters.
from random import choice
from string import ascii_lowercase


def remove_duplicates(s: str) -> str:
    # working_sol (85.65%, 72.72%) -> (53ms, 17.34mb)  time: O(s) | space: O(s)
    stack: list[str] = []
    for char in s:
        if stack and char == stack[-1]:
            while stack and char == stack[-1]:
                stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)


# Time complexity: O(s).
# In the worst case, everything will be added and deleted from `stack`, every char used twice => O(2s).
# -------------------------
# Auxiliary space: O(s)
# `stack` will allocate space for every char in `s` => O(s).


test: str = "abbaca"
test_out: str = "ca"
assert test_out == remove_duplicates(test)

test = "azxxzy"
test_out = "ay"
assert test_out == remove_duplicates(test)

test = ''.join([choice(ascii_lowercase) for _ in range(10 ** 5)])
print(test)
