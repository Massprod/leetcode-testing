# Given a positive integer num, split it into two
#  non-negative integers num1 and num2 such that:
# - The concatenation of num1 and num2 is a permutation of num.
#   - In other words, the sum of the number of occurrences of each digit in
#     num1 and num2 is equal to the number of occurrences of that digit in num.
#   - num1 and num2 can contain leading zeros.
# Return the minimum possible sum of num1 and num2.
# Notes:
# - It is guaranteed that num does not contain any leading zeros.
# - The order of occurrence of the digits in num1 and num2
#   may differ from the order of occurrence of num.
# ------------------------
# 10 <= num <= 10 ** 9


def split_num(num: int) -> int:
    # working_sol (100.0%, 58.32%) -> (0ms, 17.75mb)  time: O(n * log n) | space: O(n)
    # Best approach is to add minimum values in the alternating order.
    vals: list[str] = sorted(str(num), key=lambda x: int(x))
    out: list[list[str]] = [[], []]
    for index, val in enumerate(vals):
        out[index % 2].append(val)

    return int(''.join(out[0])) + int(''.join(out[1]))


# Time complexity: O(n * log n) <- n - digits in the input value `num`.
# Always converting `num` to string and sorting all the digits => O(n * log n).
# Extra traversing all digits of the `num` => O(n * log n + n).
# ------------------------
# Auxiliary space: O(n)
# `vals` <- allocates space for each digits from `num` => O(n).


test: int = 4325
test_out: int = 59
assert test_out == split_num(test)

test = 687
test_out = 75
assert test_out == split_num(test)
