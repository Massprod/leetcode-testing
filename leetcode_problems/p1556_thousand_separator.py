# Given an integer n, add a dot (".")
#  as the thousands separator and return it in string format.
# -----------------
# 0 <= n <= 2 ** 31 - 1
from random import randint


def thousand_separator(n: int) -> str:
    # working_sol (99.37%, 66.95%) -> (21ms, 16.43mb)  time: O(n) | space: O(n)
    if not n:
        return '0'
    out: list[str] = []
    count: int = 0
    while n:
        out.append(str(n % 10))
        n //= 10
        count += 1
        if n and 3 == count:
            out += '.'
            count = 0
    return ''.join(out[::-1])


# Time complexity: O(n) <- n - digits of the input value.
# Always using every digit of the `n` => O(n)
# And all of the `n` digits appended in `out` and reverse later => O(2n).
# -----------------
# Auxiliary space: O(n)
# `out` will hold all the digits of `n` and extra string with the same size used for output => O(2n).


test: int = 987
test_out: str = "987"
assert test_out == thousand_separator(test)

test = 1234
test_out = "1.234"
assert test_out == thousand_separator(test)

test = randint(0, 2 ** 31 - 1)
print(test)
