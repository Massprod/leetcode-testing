# You are given a 0-indexed 1-dimensional (1D) integer array original,
#  and two integers, m and n.
# You are tasked with creating a 2-dimensional (2D) array with  m rows and n columns
#  using all the elements from original.
# The elements from indices 0 to n - 1 (inclusive) of original should form the first row of the constructed 2D array,
#  the elements from indices n to 2 * n - 1 (inclusive)
#  should form the second row of the constructed 2D array, and so on.
# Return an m x n 2D array constructed according to the above procedure,
#  or an empty 2D array if it is impossible.
# ---------------------------
# 1 <= original.length <= 5 * 10 ** 4
# 1 <= original[i] <= 10 ** 5
# 1 <= m, n <= 4 * 10 ** 4


def construct_2d_array(original: list[int], m: int, n: int) -> list[list[int]]:
    # working_sol (86.09%, 82.00%) -> (664ms, 23.76mb)  time: O(k) | space: O(k)
    out: list[list[int]] = []
    if m * n != len(original):
        return out
    left: int = 0
    right: int = n
    for row in range(m):
        out.append(
            original[left: right]
        )
        left += n
        right += n
    return out


# Time complexity: O(k) <- k - length of the input array `original`.
# Always using every index of the `original`, once => O(k).
# `k` == `m * n` <- if we can build.
# ---------------------------
# Auxiliary space: O(k)
# `out` <- allocates space for each value from `original`.


test: list[int] = [1, 2, 3, 4]
test_m: int = 2
test_n: int = 2
test_out: list[list[int]] = [[1, 2], [3, 4]]
assert test_out == construct_2d_array(test, test_m, test_n)

test = [1, 2, 3]
test_m = 1
test_n = 3
test_out = [[1, 2, 3]]
assert test_out == construct_2d_array(test, test_m, test_n)

test = [1, 2]
test_m = 1
test_n = 1
test_out = []
assert test_out == construct_2d_array(test, test_m, test_n)
