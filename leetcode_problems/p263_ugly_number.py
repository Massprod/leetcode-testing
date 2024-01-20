# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
# Given an integer n, return true if n is an ugly number.
# ------------------
# -2 ** 31 <= n <= 2 ** 31 - 1


def is_ugly(n: int) -> bool:
    # working_sol (73.20%, 55.20%) -> (36ms, 16.59mb)  time: O(log n) | space: O(1)
    if n < 1:
        return False
    # Essentially we need:
    # 1 = (2 ** 0) * (3 ** 0) * (5 ** 0)
    # So, we just need to take all powers to 0.
    while n > 1:
        # Take everything we can until we get 1.
        if 0 == n % 2:
            n //= 2
        elif 0 == n % 3:
            n //= 3
        elif 0 == n % 5:
            n //= 5
        # If we can't take desired prime factor,
        #  then we have something else used.
        else:
            break
    return n == 1


# Time complexity: O(log n).
# At every step we divide input `n` in some parts, so it should be logarithmic => O(log n).
# ------------------
# Auxiliary space: O(1).


test: int = 6
test_out: bool = True
assert test_out == is_ugly(test)

test = 1
test_out = True
assert test_out == is_ugly(test)

test = 14
test_out = False
assert test_out == is_ugly(test)
