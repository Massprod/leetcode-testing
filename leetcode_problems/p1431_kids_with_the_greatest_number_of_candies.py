# There are n kids with candies. You are given an integer array candies,
#   where each candies[i] represents the number of candies the ith kid has,
#   and an integer extraCandies, denoting the number of extra candies that you have.
# Return a boolean array result of length n, where result[i] is true if,
#   after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids,
#   or false otherwise.
# Note that multiple kids can have the greatest number of candies.
# --------------------
# n == candies.length
# 2 <= n <= 100
# 1 <= candies[i] <= 100
# 1 <= extraCandies <= 50


def kids_candies(candies: list[int | bool], extraCandies: int) -> list[bool]:
    # working_sol (83.25%, 93.98%) -> (44ms, 16.2mb)  time: O(n) | space: O(1)
    max_val: int = 0
    # Find max and give every kid extras.
    for x in range(len(candies)):
        max_val = max(max_val, candies[x])
        candies[x] = candies[x] + extraCandies
    # Kids with >= maximum == True.
    for y in range(len(candies)):
        if candies[y] >= max_val:
            candies[y] = True
            continue
        candies[y] = False
    return candies


# Time complexity: O(n) -> double traverse of original input_array => O(2n).
# n - len of input_array^^|
# Auxiliary space: O(1) -> using original input to store results and only 1 extra constant INT => O(1).
# --------------------
# Get max, check every kid + extra being >= max. But I want to do this without getting max() first.
# W.e anyway there's 2 traverses, cuz we need to know maximum until we can decide True|False.


test: list[int] = [2, 3, 5, 1, 3]
test_extra: int = 3
test_out: list[bool] = [True, True, True, False, True]
assert test_out == kids_candies(test, test_extra)

test = [4, 2, 1, 1, 2]
test_extra = 1
test_out = [True, False, False, False, False]
assert test_out == kids_candies(test, test_extra)
