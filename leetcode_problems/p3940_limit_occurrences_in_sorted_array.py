# You are given a sorted integer array nums and an integer k.
# Return an array such that each distinct element appears at most k times,
#  while preserving the relative order of the elements in nums.
# Note: If a distinct element appears at least k times,
#  then it must appear exactly k times in the resulting array.
# --- --- --- ---
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
# nums is sorted in non-decreasing order.
# 1 <= k <= nums.length


def limit_occurrences(nums: list[int], k: int) -> list[int]:
    # working_solution: (62.88%, 70.82%) -> (1ms, 19.27mb)  Time: O(n) Space: O(n)
    out: list[int] = [nums[0]]
    count: int = 1
    prev: int = nums[0]
    for num in nums[1:]:
        if prev == num:
            count += 1
        else:
            count = 1
        if count <= k:
            out.append(num)
        prev = num
    
    return out


# Time complexity: O(n)
# --- --- --- ---
# Space complexity: O(n)


test: list[int] = [1, 1, 1, 2, 2, 3]
test_k: int = 2
test_out: list[int] = [1, 1, 2, 2, 3]
assert test_out == limit_occurrences(test, test_k)

test = [1, 2, 3]
test_k = 1
test_out = [1, 2, 3]
assert test_out == limit_occurrences(test, test_k)
