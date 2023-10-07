# You are given three integers n, m and k.
# You should build the array arr which has the following properties:
#   - arr has exactly n integers.
#   - 1 <= arr[i] <= m where (0 <= i < n).
#   - After applying the mentioned algorithm to arr, the value search_cost is equal to k.
# Return the number of ways to build the array arr under the mentioned conditions.
# As the answer may grow large, the answer must be computed modulo 10 ** 9 + 7.
# ----------------------
# 1 <= n <= 50
# 1 <= m <= 100
# 0 <= k <= n


def num_of_arrays(n: int, m: int, k: int) -> int:
    # working_sol (28.32%, 5.31%) -> (1345ms, 43.7mb)  time: O(n * m ** 2 * k) | space: O(n * m * k)
    # We can't place enough to make search_cost == k.
    if m < k:
        return 0
    recur_cache: dict[tuple[int, int, int], int] = {}

    def check(index: int, maximum: int, to_use: int) -> int:
        """
        :param index: current index of the array.
        :param maximum: current maximum in the array.
        :param to_use: breakpoints we can use, when: maximum < array[index]
        :return:
        """
        if (index, maximum, to_use) in recur_cache:
            return recur_cache[index, maximum, to_use]
        # ! array has exactly 'n' integers !
        if index == n:
            # ! the value search_cost is equal to 'k' !
            if not to_use:
                return 1
            return 0
        # Don't choose new maximum.
        count: int = maximum * check(index + 1, maximum, to_use)
        # Choose new maximum.
        # We can use => ! 1 <= arr[i] <= m !.
        for new_maximum in range(maximum + 1, m + 1):
            count += check(index + 1, new_maximum, to_use - 1)
        recur_cache[index, maximum, to_use] = count
        return count

    return check(0, 0, k) % (10 ** 9 + 7)


# Time complexity: O(n * m ** 2 * k) -> always finding (n * m * k) states and for worst calls loop for 'm' values.
# n - input value 'n'^^|
# m - input value 'm'^^|
# k - input value 'k'^^|
# Auxiliary space: O(n * m * k) -> caching all (n * m * k) possible states => O(n * m * k).


test_n: int = 2
test_m: int = 3
test_k: int = 1
test_out: int = 6
assert test_out == num_of_arrays(test_n, test_m, test_k)

test_n = 5
test_m = 2
test_k = 3
test_out = 0
assert test_out == num_of_arrays(test_n, test_m, test_k)

test_n = 9
test_m = 1
test_k = 1
test_out = 1
assert test_out == num_of_arrays(test_n, test_m, test_k)

test_n = 50
test_m = 100
test_k = 50
test_out = 538992043
assert test_out == num_of_arrays(test_n, test_m, test_k)
