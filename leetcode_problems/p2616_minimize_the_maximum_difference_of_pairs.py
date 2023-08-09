# You are given a 0-indexed integer array nums and an integer p.
# Find p pairs of indices of nums such that the maximum difference amongst all the pairs is minimized.
# Also, ensure no index appears more than once amongst the p pairs.
# Note that for a pair of elements at the index i and j,
#   the difference of this pair is |nums[i] - nums[j]|, where |x| represents the absolute value of x.
# Return the minimum maximum difference amongst all p pairs. We define the maximum of an empty set to be zero.
# --------------------
# 1 <= nums.length <= 10 ** 5
# 0 <= nums[i] <= 10 ** 9
# 0 <= p <= (nums.length) / 2
from random import randint


def minimize_max(nums: list[int], p: int) -> int:
    # working_sol (92.26%, 78.6%) -> (921ms, 30.9mb)  time: O(n * log m) | space: O(1)
    # We need difference of value_pairs.
    # So we're not obligated to save index_placement.
    # It's faster and easier to check value_pairs after sorting in asc.
    nums.sort()
    # Minimum diff by description.
    left_l: int = 0
    # Maximum diff we can get after sorting, ascending order.
    right_l: int = nums[-1] - nums[0]

    def check_pairs(diff: int) -> int:
        # Greedy count.
        pair_count: int = 0
        index: int = 1
        # Count every correct value_pair.
        while index < len(nums):
            # If pair_diff is lower|equal than we need, then
            # we can make diff value even lower and recheck ->
            # -> so it's correct pair to count.
            if nums[index] - nums[index - 1] <= diff:
                pair_count += 1
                # We can't reuse indexes, skipping pair.
                index += 2
                continue
            # Diff of pair is higher, ignore.
            # Because we need to make diff higher first.
            index += 1
        return pair_count

    # Standard BS method.
    while left_l < right_l:
        middle: int = (left_l + right_l) // 2
        # There's more|equal pairs with current diff.
        # So we can try to make it lower and recheck.
        if check_pairs(middle) >= p:
            right_l = middle
            continue
        # Otherwise, higher.
        left_l = middle + 1
    return left_l


# Time complexity: O(n * log m) -> standard binary_search with traversing of whole input_array for every option.
# m -> inclusive range of value options == 0 -> max_diff(nums[-1] - nums[0]) <- after sorting^^|
# n -> input array^^|
# Auxiliary space: O(1) -> sort() in_place, and using 5 constant INTs => O(1).
# --------------------
# Again BS, cuz we need to find some limit with condition.
# Sort to get max_diff, and we could actually check indexes for pairs, without reusing.
# Only question is -> how we change value, like if we get p == correct_pairs, stop?
# No we can try to make it lower and lower. Ok. Then it's always shift to left side -> lowest.


test: list[int] = [10, 1, 2, 7, 1, 3]
test_p: int = 2
test_out: int = 1
assert test_out == minimize_max(test, test_p)

test = [4, 2, 1, 2]
test_p = 1
test_out = 0
assert test_out == minimize_max(test, test_p)

test = []
for _ in range(10 ** 4):
    test.append(randint(0, 10 ** 9))
test_p = randint(0, len(test) // 2)
print(test)
print(test_p)
