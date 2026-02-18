# You are given an integer array nums of length n.
# An element at index i is called dominant if:
#  nums[i] > average(nums[i + 1], nums[i + 2], ..., nums[n - 1])
# Your task is to count the number of indices i that are dominant.
# The average of a set of numbers is the value obtained by adding all
#  the numbers together and dividing the sum by the total number of numbers.
# Note: The rightmost element of any array is not dominant.
# --- --- --- ---
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100​​​​​​​


def dominant_indices(nums: list[int]) -> int:
    # working_solution: (100%, 66.42%) -> (0ms, 19.38mb)  Time: O(n) Space: O(1)
    out: int = 0
    cur_avg_len: int = len(nums)
    cur_avg_sum: int = sum(nums)
    cur_avg: float = cur_avg_sum / cur_avg_len
    for index in range(len(nums)- 1):
        cur_val: int = nums[index]
        cur_avg_sum -= cur_val
        cur_avg_len -= 1
        cur_avg = cur_avg_sum / cur_avg_len
        if cur_val > cur_avg:
            out += 1
    
    return out


# Time complexity: O(n)
# n - length of the input array `nums`
# --- --- --- ---
# Space complexity: O(1)


test: list[int] = [5, 4, 3]
test_out: int = 2
assert test_out == dominant_indices(test)

test = [4, 1, 2]
test_out = 1
assert test_out == dominant_indices(test)
