# Given an integer n, return true if it is a power of three.
# Otherwise, return false.
# An integer n is a power of three, if there exists an integer x such that n == 3 ** x.
# -----------------
# -2 ** 31 <= n <= 2 ** 31 - 1


def is_power_of_three(n: int) -> bool:
    # working_sol (98.30%, 52.57%) -> (50ms, 16.63mb)  time: O(log n) | space: O(1)
    if n <= 0:
        return False
    # All prime factors should be 3.
    while n > 1:
        if 0 == n % 3:
            n //= 3
        else:
            break
    return 1 == n


# Time complexity: O(log n).
# Auxiliary space: O(1).
