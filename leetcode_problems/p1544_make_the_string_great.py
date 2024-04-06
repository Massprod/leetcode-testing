# Given a string s of lower and upper case English letters.
# A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:
#   - 0 <= i <= s.length - 2
#   - s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
# To make the string good, you can choose two adjacent characters that make the string bad and remove them.
# You can keep doing this until the string becomes good.
# Return the string after making it good.
# The answer is guaranteed to be unique under the given constraints.
# Notice that an empty string is also good.
# -----------------------------
# 1 <= s.length <= 100
# s contains only lower and upper case English letters.
from random import choice
from string import ascii_uppercase, ascii_lowercase


def make_good(s: str) -> str:
    # working_sol (75.56%, 46.83%) -> (35ms, 16.53mb)  time: O(s) | space: O(s)
    stack: list[str] = []
    for char in s:
        if stack and char.lower() == stack[-1].lower():
            if char.isupper() and stack[-1].islower():
                stack.pop()
            elif char.islower() and stack[-1].isupper():
                stack.pop()
            else:
                stack.append(char)
        else:
            stack.append(char)
    return ''.join(stack)


# Time complexity: O(s)
# Single traverse of the whole input string `s` => O(s).
# -----------------------------
# Auxiliary space: O(s)
# Worst case: we can't delete anything == `aaaaaaaaaaaaaaaaaaa`.
# Our stack will be a size of `s` => O(s).


test: str = "leEeetcode"
test_out: str = "leetcode"
assert test_out == make_good(test)

test = "abBAcC"
test_out = ""
assert test_out == make_good(test)

test = "s"
test_out = "s"
assert test_out == make_good(test)

test = ''.join([choice([choice(ascii_uppercase), choice(ascii_lowercase)]) for _ in range(100)])
print(test)
