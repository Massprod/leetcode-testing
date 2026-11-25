# You are given an integer array nums.
# An element in nums is called dominant if it is greater than or equal
#  to the average of its immediate neighbors.
# The immediate neighbors of nums[i] are nums[i - 1] and nums[i + 1],
#  when those indices exist.
# A single element with no neighbors is considered dominant.
# Return the number of dominant elements in nums.
# --- --- --- ---
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100


def count_dominant_elements(nums: list[int]) -> int:
    # working_solution: (23.76%, 99.36%) -> (6ms, 18.86mb)  Time: O(n) Space: O(1)
    out: int = 0
    for index in range(len(nums)):
        left_neighbour: int = 0
        right_neighbour: int = 0
        if 0 <= index - 1:
            left_neighbour = nums[index - 1]
        if len(nums) > index + 1:
            right_neighbour = nums[index + 1]
        current: int = nums[index]
        values: int = 2 if left_neighbour and right_neighbour else 1
        average: int = (left_neighbour + right_neighbour) / values
        out += 1 if current >= average else 0
    
    return out


# Time complexity: O(n)
# n - length of the input array `nums`
# --- --- --- ---
# Space complexity: O(1)


test: list[int] = [1, 10, 2]
test_out: int = 1
assert test_out == count_dominant_elements(test)

test = [6, 4, 2]
test_out = 2
assert test_out == count_dominant_elements(test)

test = [7]
test_out = 1
assert test_out == count_dominant_elements(test)
