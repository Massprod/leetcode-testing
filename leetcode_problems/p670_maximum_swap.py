# You are given an integer num.
# You can swap two digits at most once to get the maximum valued number.
# Return the maximum valued number you can get.
# ------------------------
# 0 <= num <= 10 ** 8
from random import randint


def maximum_swap(num: int) -> int:
    # working_sol (84.92%, 97.49%) -> (30ms, 16.39mb)  time: O(n) | space: O(n)
    # [ str(digit) ]
    str_num: list[str] = list(str(num))
    num_length: int = len(str_num)
    # [ indexes of maximum value on the right side of this index ]
    max_suffix: list[int] = [index for index in range(num_length - 1)] + [num_length - 1]
    for index in range(num_length - 2, -1, -1):
        if str_num[index] <= str_num[max_suffix[index + 1]]:
            max_suffix[index] = max_suffix[index + 1]
        else:
            max_suffix[index] = index
    for index in range(num_length - 1):
        if str_num[index] < str_num[max_suffix[index]]:
            str_num[index], str_num[max_suffix[index]] = str_num[max_suffix[index]], str_num[index]
            return int(''.join(str_num))
    return num


# Time complexity: O(n) <- n - number of digits in `num`.
# Always traversing every digit of `num`, twice => O(n).
# ------------------------
# Auxiliary space: O(n)
# `str_num` <- allocates space for each digit from `num` => O(n).
# `max_suffix` <- allocates space for each digit from `num` as well => O(2 * n).


test: int = 2736
test_out: int = 7236
assert test_out == maximum_swap(test)

test = 9973
test_out = 9973
assert test_out == maximum_swap(test)

test = randint(0, 10 ** 8)
print(test)
