# Given an integer array nums and an integer k, return the maximum sum of a non-empty subsequence
#   of that array such that for every two consecutive integers in the subsequence,
#   nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.
# A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array,
#   leaving the remaining elements in their original order.
# ------------------
# 1 <= k <= nums.length <= 10 ** 5
# -10 ** 4 <= nums[i] <= 10 ** 4
from collections import deque
from random import randint


def constrained_subset_sum(nums: list[int], k: int) -> int:
    # working_sol (85.64%, 55.80%) -> (1378ms, 30.1mb)  time: O(n) | space: O(n)
    length: int = len(nums)
    # Unique case with 1 value, there's only 1 subseq.
    if length == 1:
        return nums[0]
    # p239 -> sliding_window for reference.
    # Same approach, storing every correct index,
    # and delete everything lower or incorrect.
    que: deque = deque()
    # Either skip 0 index, here or in loop.
    # Cuz we can't take nums[que[0]] when que is empty.
    que.append(0)
    for x in range(1, length):
        # We allowed to use indexes in x - k -> x, inclusive.
        # Delete every incorrect index for every new added.
        while len(que) != 0 and x - k > que[0]:
            que.popleft()
        # nums[x] -> always incremented by maximum_prefix_sum.
        # We need subsequence with maximum_sum, so if at any moment
        # our maximum_prefix_sum goes negative, we can't use it.
        # Because it's only going to make sub_sum lower, and we don't need it.
        # Means we're starting a new subsequence from this index.
        nums[x] = nums[x] + max(0, nums[que[0]])
        # We only need maximum_prefix_sum within correct indexes.
        # Any index with less value should be deleted.
        # nums[x] -> after incrementing by maximum_prefix_sum, becomes
        # maximum_prefix_sum itself.
        while len(que) != 0 and nums[que[-1]] <= nums[x]:
            que.pop()
        # Adding correct index into the que.
        que.append(x)
    # Should be possible to maintain max_value at all times,
    # but it's still going to check every nums[x] for max_value = max(nums[x], max_value)
    # Even more indexes will be checked. Better to just extra traverse to get max_value.
    return max(nums)


# Time complexity: O(n) -> every index will be used once, visited in loop and added into a que() ->
# n - len of input_array^^| -> guess the worst case is like k == 1, then we're going to delete every index from que()
#                           n - times, for every new index, so it's O(2n) => O(n).
# Auxiliary space: O(n) -> if every index can be used, like k == len(input) -> so every index can be used, and
#                          all of them are descending, we're never going to have nums[que[-1]] <= nums[x],
#                          ending us with -> len(que) == len(input) => O(n).
# ------------------
# HINT -> ! dp[i] = nums[i] + max(0, dp[i-k], dp[i-k+1], ..., dp[i-1]) !
# But we can store it in nums itself, and ! dp[i-k], dp[i-k+1], ..., dp[i-1]  ! <- prefix_sum.
# Only difference is that we're not summarizing everything, but choosing max_value.
# Because we don't need negative values at all, they will be annulled for == 0.
# HINT -> ! Use a heap with the sliding window technique to optimize the dp. !
# So it's the same as p239, with storing all correct indexes for a window and leaving only maximum_value.


test: list[int] = [10, 2, -10, 5, 20]
test_k: int = 2
test_out: int = 37
assert test_out == constrained_subset_sum(test, test_k)

test = [-1, -2, -3]
test_k = 1
test_out = -1
assert test_out == constrained_subset_sum(test, test_k)

test = [10, -2, -10, -5, 20]
test_k = 2
test_out = 23
assert test_out == constrained_subset_sum(test, test_k)

test = []
for _ in range(10 ** 5):
    test.append(randint(-10 ** 4, 10 ** 4))
test_k = randint(1, len(test))
# print(test)
# print(test_k)
