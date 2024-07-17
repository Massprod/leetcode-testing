# Given a string text, you want to use the characters of text
#  to form as many instances of the word "balloon" as possible.
# You can use each character in text at most once.
# Return the maximum number of instances that can be formed.
# ------------------------
# 1 <= text.length <= 10 ** 4
# text consists of lower case English letters only.
from random import choice
from string import ascii_lowercase
from collections import defaultdict


def max_number_of_balloons(text: str) -> int:
    # working_sol (72.78%, 94.16%) -> (35ms, 16.49mb)  time: O(n) | space: O(n)
    allowed_chars: set[str] = {'b', 'a', 'l', 'o', 'n'}
    # { char: occurs }
    chars_count: dict[str, int] = defaultdict(int)
    for char in text:
        if char in allowed_chars:
            chars_count[char] += 1
    # Not all chars from `balloon` is present.
    if len(chars_count) < 5:
        return 0
    out: int = 10 ** 4
    for char, occur in chars_count.items():
        # We use them in pairs.
        if 'l' == char:
            out = min(out, occur // 2)
        elif 'o' == char:
            out = min(out, occur // 2)
        else:
            out = min(out, occur)
    return out


# Time complexity: O(n) <- n - length of the input string `text`.
# We're always traversing `test` once to count ever chars from `allowed_chars` => O(n).
# In the worst-case `text` is only contains `balons`,
#  and we're going to traverse every key in `chars_count` == `n` => O(2n).
# ------------------------
# Auxiliary space: O(n)
# Same worst-case, we're going to have every unique char from `balons` stored in `chars_count` => O(n).


test: str = "nlaebolko"
test_out: int = 1
assert test_out == max_number_of_balloons(test)

test = "loonbalxballpoon"
test_out = 2
assert test_out == max_number_of_balloons(test)

test = "leetcode"
test_out = 0
assert test_out == max_number_of_balloons(test)

test = ''.join([choice(ascii_lowercase) for _ in range(10 ** 4)])
print(test)
