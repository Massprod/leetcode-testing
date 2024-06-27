# Given a string s and an integer k, reverse the first k characters
#  for every 2k characters counting from the start of the string.
# If there are fewer than k characters left, reverse all of them.
# If there are less than 2k but greater than or equal to k characters,
#  then reverse the first k characters and leave the other as original.
# ---------------------------
# 1 <= s.length <= 10 ** 4
# s consists of only lowercase English letters.
# 1 <= k <= 10 ** 4
from random import choice
from string import ascii_lowercase


def reverse_str(s: str, k: int) -> str:
    # working_sol (88.04%, 96.69%) -> (31ms, 16.58mb)  time: O(s) | space: O(s)
    out: str = ''
    for start in range(0, len(s), 2 * k):
        leave: str = s[start + k: start + 2 * k]
        reverse: str = s[start:start + k][::-1]
        out += reverse + leave
    return out


# Time complexity: O(s)
# Even with a step `2 * k` we're still traversing whole input string `s` and using every index in slicing => O(n).
# ---------------------------
# Auxiliary space: O(s)
# Essentially we're always creating a copy of the original `s` but with different ordering => O(s)


test: str = "abcdefg"
test_k: int = 2
test_out: str = "bacdfeg"
reverse_str(test, test_k)
assert test_out == reverse_str(test, test_k)

test = "abcd"
test_k = 2
test_out = "bacd"
assert test_out == reverse_str(test, test_k)

test = "a"
test_k = 1
test_out = "a"
assert test_out == reverse_str(test, test_k)

test = ''.join([choice(ascii_lowercase) for _ in range(10 ** 4)])
print(test)
