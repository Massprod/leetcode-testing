# You are given two positive integers low and high.
# An integer x consisting of 2 * n digits is symmetric if the sum of the first n digits
#  of x is equal to the sum of the last n digits of x.
# Numbers with an odd number of digits are never symmetric.
# Return the number of symmetric integers in the range [low, high].
# ---------------------------
# 1 <= low <= high <= 10 ** 4


def count_symmetric_integers(low: int, high: int) -> int:
    # working_sol (90.48%, 62.21%) -> (437ms, 16.53mb)  time: O(high - low) | space: O(high)
    # Probably there's some math, but it beats 90%, so w.e
    out: int = 0

    def get_digits(integer: int) -> list[int]:
        out_: list[int] = []
        while integer:
            out_.append(integer % 10)
            integer //= 10
        return out_

    for value in range(low, high + 1):
        value_digits: list[int] = get_digits(value)
        if len(value_digits) % 2:
            continue

        middle: int = len(value_digits) // 2
        if sum(value_digits[:middle]) == sum(value_digits[middle:]):
            out += 1
    return out


# Time complexity: O(high - low)
# Always using every value in range (high - low) inclusive => O(high - low).
# ---------------------------
# Auxiliary space: O(high)
# W.e the case, the most digits are going to be in the highest value.
# And we store them in `out`, extra making 2 slices of it => O(high).


test_low: int = 1
test_high: int = 100
test_out: int = 9
assert test_out == count_symmetric_integers(test_low, test_high)

test_low = 1200
test_high = 1230
test_out = 4
assert test_out == count_symmetric_integers(test_low, test_high)
