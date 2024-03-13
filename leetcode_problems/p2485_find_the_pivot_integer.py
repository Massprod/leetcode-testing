# Given a positive integer n, find the pivot integer x such that:
#   - The sum of all elements between 1 and x inclusively equals the sum
#      of all elements between x and n inclusively.
# Return the pivot integer x. If no such integer exists, return -1.
# It is guaranteed that there will be at most one pivot index for the given input.
# -----------------------
# 1 <= n <= 1000


def pivot_integer(n: int) -> int:
    # working_sol (60.68%, 59.17%) -> (46ms, 16.52mb)  time: O(n) | space: O(1)
    suffix: int = sum(range(1, n + 1))
    prefix: int = 1
    val: int = 1
    while suffix > 0:
        if prefix == suffix:
            return val
        suffix -= val
        val += 1
        prefix += val
    return -1
    # # Overcomplicated solution.
    # # Essentially we're just checking equal sums on both sides from some index.
    # # So, we can just take sum(1, n + 1) and start from [0] take from whole sum and increase starting val.
    # prefixes: list[int] = [num for num in range(1, n + 1)]
    # for ind in range(1, len(prefixes)):
    #     prefixes[ind] += prefixes[ind - 1]
    # suffixes: list[int] = [num for num in range(1, n + 1)]
    # for ind in range(len(suffixes) - 2, -1, -1):
    #     suffixes[ind] += suffixes[ind + 1]
    # # Suffix == Prefix == Same sum on both sides.
    # set_prefixes: set[tuple[int, int]] = set(enumerate(prefixes))
    # set_suffixes: set[tuple[int, int]] = set(enumerate(suffixes))
    # for pair in set_prefixes:
    #     if pair in set_suffixes:
    #         # We always have 1 -> n, values but their indexes are lower by 1.
    #         return pair[0] + 1
    # return -1


# Time complexity: O(n)
# Both solutions have Linear complexity, and same approach. Just didn't notice it at first.
# Auxiliary space: O(1) and O(n).


test: int = 8
test_out: int = 6
assert test_out == pivot_integer(test)

test = 1
test_out = 1
assert test_out == pivot_integer(test)

test = 4
test_out = -1
assert test_out == pivot_integer(test)
