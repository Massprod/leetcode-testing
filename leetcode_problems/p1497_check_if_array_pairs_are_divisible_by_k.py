# Given an array of integers arr of even length n and an integer k.
# We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.
# Return true If you can find a way to do that or false otherwise.
# -------------------------
# arr.length == n
# 1 <= n <= 10 ** 5
# n is even.
# -10 ** 9 <= arr[i] <= 10 ** 9
# 1 <= k <= 10 ** 5
from collections import defaultdict


def can_arrange(arr: list[int], k: int) -> bool:
    # working_sol (24.42%, 27.88%) -> (529ms, 30.52mb)  time: O(n) | space: O(n)
    remainder: int
    # { remainder: occurrences }
    remainders: dict[int, int] = defaultdict(int)
    # First loop: Calculate the remainders of each element in the array when divided by k.
    # Note: We adjust the remainder to always be non-negative.
    for value in arr:
        remainder = (value % k + k) % k
        remainders[remainder] += 1
    # Second loop: We check if each element can be paired properly.
    for value in arr:
        remainder = (value % k + k) % k
        # Special case: If remainder is 0, we can only pair these elements with other elements
        # that also give a remainder of 0. Therefore, there must be an even count of such elements.
        if remainder == 0:
            if remainders[remainder] % 2 != 0:
                return False
        # General case: For every remainder `r`, there must be the same number of elements
        # with remainder `k - r` to form pairs that sum up to a multiple of k.
        # Example: If remainder is 2, we need an equal number of elements with remainder `k - 2`.
        elif remainders[remainder] != remainders[k - remainder]:
            return False
    return True


# Time complexity: O(n) <- n - length of the input array `arr`.
# Always traversing input array `arr`, twice => O(2 * n).
# -------------------------
# Auxiliary space: O(n)
# `remainders` <- allocates space for each unique remainder => O(n).


test: list[int] = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9]
test_k: int = 5
test_out: bool = True
assert test_out == can_arrange(test, test_k)

test = [1, 2, 3, 4, 5, 6]
test_k = 7
test_out = True
assert test_out == can_arrange(test, test_k)

test = [1, 2, 3, 4, 5, 6]
test_k = 10
test_out = False
assert test_out == can_arrange(test, test_k)
