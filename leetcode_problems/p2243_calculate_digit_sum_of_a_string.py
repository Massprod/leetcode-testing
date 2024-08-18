# You are given a string s consisting of digits and an integer k.
# A round can be completed if the length of s is greater than k.
# In one round, do the following:
#  - Divide s into consecutive groups of size k such that the first k characters are in the first group,
#    the next k characters are in the second group, and so on.
#    Note that the size of the last group can be smaller than k.
#  - Replace each group of s with a string representing the sum of all its digits.
#    For example, "346" is replaced with "13" because 3 + 4 + 6 = 13.
#  - Merge consecutive groups together to form a new string.
#    If the length of the string is greater than k, repeat from step 1.
# Return s after all rounds have been completed.
# ----------------------------
# 1 <= s.length <= 100
# 2 <= k <= 100
# s consists of digits only.
from string import digits
from random import choice


def digit_sum(s: str, k: int) -> str:
    # working_sol (69.65%, 92.79%) -> (33ms, 16.37mb)  time: O(s) | space: O(s + k)

    def count_round(round_str: str) -> str:
        new_str: list[str] = []
        for index in range(0, len(round_str), k):
            slice_: str = round_str[index: index + k]
            new_str.append(
                str(sum([int(digit) for digit in slice_]))
            )
        return ''.join(new_str)

    while k < len(s):
        s = count_round(s)
    return s


# Time complexity: O(s)
# In a case like `999999` we're still going to have `999` -> `27` -> `9`.
# So, it's linear, but no idea how we can calc times of `count_round`.
# Guess, at max every 3size pair is going to be used 3 times => O(3 * s).
# ----------------------------
# Auxiliary space: O(s + k)
# `new_str` <- will contain `s * 2/3` chars at max => O(s).
# `slice_` <- is always of the size `k` or lower => O(s + k).


test: str = "11111222223"
test_k: int = 3
test_out: str = "135"
assert test_out == digit_sum(test, test_k)

test = "00000000"
test_k = 3
test_out = "000"
assert test_out == digit_sum(test, test_k)

test = ''.join([choice(digits) for _ in range(100)])
print(test)
