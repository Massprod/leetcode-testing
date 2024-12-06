# You are given an integer array banned and two integers n and maxSum.
# You are choosing some number of integers following the below rules:
#  - The chosen integers have to be in the range [1, n].
#  - Each integer can be chosen at most once.
#  - The chosen integers should not be in the array banned.
#  - The sum of the chosen integers should not exceed maxSum.
# Return the maximum number of integers you can choose following the mentioned rules.
# --------------------------
# 1 <= banned.length <= 10 ** 4
# 1 <= banned[i], n <= 10 ** 4
# 1 <= maxSum <= 10 ** 9


def max_count(banned: list[int], n: int, maxSum: int) -> int:
    # working_sol: (81.14%, 9.90%) -> (41ms, 18.99mb)  time: O(m + n) | space: O(m)
    not_usable: set[int] = set(banned)
    out: int = 0
    run_sum: int = 0
    for val in range(1, n + 1):
        if val in not_usable:
            continue
        run_sum += val
        if run_sum > maxSum:
            break
        out += 1
    return out


# Time complexity: O(m + n) <- m - length of the input array `banned`.
# Always converting `banned` into a `set` => O(m).
# In the worst case every value in `range(1, n + 1)` can be used => O(m + n).
# --------------------------
# Auxiliary space: O(m).
# `not_usable` <- allocates space for each value from `banned` => O(m).


test_banned: list[int] = [1, 6, 5]
test_n: int = 5
test_max_sum: int = 6
test_out: int = 2
assert test_out == max_count(test_banned, test_n, test_max_sum)

test_banned = [1, 2, 3, 4, 5, 6, 7]
test_n = 8
test_max_sum = 1
test_out = 0
assert test_out == max_count(test_banned, test_n, test_max_sum)

test_banned = [11]
test_n = 7
test_max_sum = 50
test_out = 7
assert test_out == max_count(test_banned, test_n, test_max_sum)
