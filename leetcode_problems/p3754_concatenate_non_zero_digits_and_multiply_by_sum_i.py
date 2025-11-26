# You are given an integer n.
# Form a new integer x by concatenating all the non-zero digits of n
#  in their original order. If there are no non-zero digits, x = 0.
# Let sum be the sum of digits in x.
# Return an integer representing the value of x * sum.
# --- --- --- ---
# 0 <= n <= 10 ** 9


def sum_and_multiply(n: int) -> int:
    # working_solution: (100%, 36.86%) -> (0ms, 17.86mb)  Time: O(n) Space: O(n)
    if 0 == n:
        return 0
    non_zeroes: list[str] = [
        val if val != '0' else '' for val in str(n)
    ]
    non_zeroes_str: str = ''.join(non_zeroes)
    non_zeroes_sum: int = sum([int(val) for val in non_zeroes_str])
    out: int = int(non_zeroes_str) * non_zeroes_sum

    return out


# Time complexity: O(n)
# In the worst case there's no `0` in the `n`.
# Converting `n` to list with strings representings digits => O(n).
# Extra traversing every digit to get the sum => O(2 * n).
# --- --- --- ---
# Space complexity: O(n)
# `non_zeroes` <- allocates space for each digit => O(n).
# `non_zeroes_str` <- allocates space for each digit => O(2 * n).


test: int = 10203004
test_out: int = 12340
assert test_out == sum_and_multiply(test)

test = 1000
test_out = 1
assert test_out == sum_and_multiply(test)
