# You are given an integer array nums of length n and an integer k.
# For each index i, define its instability score as
#  max(nums[0..i]) - min(nums[i..n - 1]).
# In other words:
#  - max(nums[0..i]) is the largest value among the elements from index 0 to index i.
#  - min(nums[i..n - 1]) is the smallest value among the elements from index i to index n - 1.
# An index i is called stable if its instability score is less than or equal to k.
# Return the smallest stable index. If no such index exists, return -1.
# --- --- --- ---
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 10 ** 9
# 0 <= k <= 10 ** 9
import heapq


def first_stable_index(nums: list[int], k: int) -> int:
    # working_solution: (100%, 100%) -> (7ms, 19.45mb)  Time: O(n * log n) Space: O(n)
    prev_max: int = -1
    min_heap: list[tuple[int, int]] = [
        (value, index) for index, value in enumerate(nums)
    ]
    heapq.heapify(min_heap)
    for index in range(len(nums)):
        prev_max = max(prev_max, nums[index])
        while min_heap and min_heap[0][1] < index:
            heapq.heappop(min_heap)
        min_val, _ = min_heap[0]
        inst: int = prev_max - min_val
        if inst <= k:
            return index
        
    return -1


# Time complexity: O(n * log n)
# n - length of the input array `nums`
# --- --- --- ---
# Space complexity: O(n)


test: list[int] = [5, 0, 1, 4]
test_k: int = 3
test_out: int = 3
assert test_out == first_stable_index(test, test_k)

test = [3, 2, 1]
test_k = 1
test_out = -1
assert test_out == first_stable_index(test, test_k)

test = [0]
test_k = 0
test_out = 0
assert test_out == first_stable_index(test, test_k)
