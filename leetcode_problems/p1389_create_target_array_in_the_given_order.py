# Given two arrays of integers nums and index.
# Your task is to create target array under the following rules:
#  - Initially target array is empty.
#  - From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
#  - Repeat the previous step until there are no elements to read in nums and index.
# Return the target array.
# It is guaranteed that the insertion operations will be valid.
# ---------------------
# 1 <= nums.length, index.length <= 100
# nums.length == index.length
# 0 <= nums[i] <= 100
# 0 <= index[i] <= i


def create_target_array(nums: list[int], index: list[int]) -> list[int]:
    # working_sol (52.73%, 21.47%) -> (38ms, 16.53mb)  time: O(n * n) | space: O(n)
    out: list[int] = []
    for _index in range(len(nums)):
        out.insert(index[_index], nums[_index])
    return out


# Time complexity: O(n * n) <- n - length of the input arrays `nums` and `index`.
# In the worst case, we're going to have every index == 0.
# So, every value we place will shift every previous value to +1 index => O(n * n).
# ---------------------
# Auxiliary space: O(n)
# We always insert all values from `nums` into `out` => O(n).


test: list[int] = [0, 1, 2, 3, 4]
test_index: list[int] = [0, 1, 2, 2, 1]
test_out: list[int] = [0, 4, 1, 3, 2]
assert test_out == create_target_array(test, test_index)

test = [1, 2, 3, 4, 0]
test_index = [0, 1, 2, 3, 0]
test_out = [0, 1, 2, 3, 4]
assert test_out == create_target_array(test, test_index)

test = [1]
test_index = [0]
test_out = [1]
assert test_out == create_target_array(test, test_index)
