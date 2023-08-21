# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
#   - Only numbers 1 through 9 are used.
#   - Each number is used at most once.
# Return a list of all possible valid combinations.
# The list must not contain the same combination twice, and the combinations may be returned in any order.
# ---------------------
# 2 <= k <= 9
# 1 <= n <= 60


def combination_sum(k: int, n: int) -> list[list[int]]:
    # working_sol (89.80%, 48.72%) -> (35ms, 16.3mb)  time: O(2 ** k) space: O(k * 2 ** k)
    # Essentially we only need to remove duplicates.
    # For this we can use values: 1 -> 9 or 9 -> 1,
    # For the first_index, and for every other index we need to take either
    # HIGHER if we go from 1 -> 9, or LOWER if 9 -> 1 for every step.
    combinations: list[list[int]] = []

    def combs(cur_sum: int, prev_val: int, path: list[int]) -> None:
        # We only care about combinations with K number indexes|values used.
        if len(path) == k:
            # Maintaining sum, to get correct sequence.
            if cur_sum == n:
                combinations.append(path)
            return
        for x in range(prev_val - 1, 0, -1):
            # And we can't take values higher than we need,
            # cuz it's instantly over limit == False.
            if x <= n:
                combs(cur_sum + x, x, path + [x])

    combs(0, 10, [])
    return combinations


# Time complexity: O(2 ** k) -> recursion tree with 2 options and maximum depths of 'k' when all values unique.
# k - limit of numbers to use^^|
# Auxiliary space: O(k * 2 ** k) -> in the worst case, every call ends in correct path, we're adding (2 ** k) paths
#                                into a combinations, and every path is always size of 'k' => O(k * 2 ** k).
# ---------------------
# So we need to delete duplicates like [4, 2, 1] and [1, 2, 4].
# By standard its like place every possible 1 - 9 on every index, once.
# We don't need duplicates, so we can use values only LOWER or HIGHER later?
# Like start from 1, and use only 2 - 9 for second, and if second == 2, only 3 - 9 for third.
# Or 9 -> 8 -> and only 7 -> 1 for Third.
# Still placing everything on indexes, but without duplicating. Let's try.


test_k: int = 3
test_n: int = 7
test_out: list[list[int]] = [[4, 2, 1]]
assert test_out == combination_sum(test_k, test_n)

test_k = 3
test_n = 9
test_out = [[6, 2, 1], [5, 3, 1], [4, 3, 2]]
assert test_out == combination_sum(test_k, test_n)

test_k = 4
test_n = 1
test_out = []
assert test_out == combination_sum(test_k, test_n)
