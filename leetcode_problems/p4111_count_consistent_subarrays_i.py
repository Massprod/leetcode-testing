# You are given an integer array nums.
# A subarray is called consistent if the bitwise AND
#  of all its elements is equal to the minimum value of the subarray.
# Return the number of consistent subarrays in nums.
# --- --- --- ---
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100


def count_consistent(nums: list[int]) -> int:
    # working_solution: (100%, 100%) -> (49ms, 19.18mb)  Time: O(n) Space: O(1)
    out: int = 0
    for index in range(len(nums)):
        start: int = nums[index]
        min_val: int = nums[index]
        for new_index in range(index, len(nums)):
            start &= nums[new_index]
            min_val = min(nums[new_index], min_val)
            if min_val == start:
                out += 1

    return out


# Time complexity: O(n ** 2)
# n - length of the input array `nums`
# --- --- --- ---
# Space complexity: O(1)


test: list[int] = [5, 3, 1, 2]
test_out: int = 6
assert test_out == count_consistent(test)

test = [1, 1, 1]
test_out = 6
assert test_out == count_consistent(test)

test = [0]
test_out = 1
assert test_out == count_consistent(test)
