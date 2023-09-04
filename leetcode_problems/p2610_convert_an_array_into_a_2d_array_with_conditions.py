# You are given an integer array nums.
# You need to create a 2D array from nums satisfying the following conditions:
#   - The 2D array should contain only the elements of the array nums.
#   - Each row in the 2D array contains distinct integers.
#   - The number of rows in the 2D array should be minimal.
# Return the resulting array. If there are multiple answers, return any of them.
# Note that the 2D array can have a different number of elements on each row.
# ---------------------
# 1 <= nums.length <= 200
# 1 <= nums[i] <= nums.length
from random import randint


def find_matrix(nums: list[int]) -> list[list[int]]:
    # working_sol (99.45%, 55.82%) -> (45ms, 16.3mb)  time: O(n) | space: O(n)
    # ! Each row in the 2D array contains distinct integers !
    # Only thing we actually care.
    # So all we need is count everything and place maximum
    #  distinct INTs on every row.
    distinct: dict[int, int] = {}
    # Maintain maximum repeats, row can be a 1 INT placed.
    max_steps: int = 0
    for num in nums:
        if num in distinct:
            distinct[num] += 1
        else:
            distinct[num] = 1
        max_steps = max(max_steps, distinct[num])
    matrix: list[list[int]] = []
    while max_steps:
        # New row.
        matrix.append([])
        for integer in distinct:
            # With all available INTs.
            if distinct[integer] > 0:
                matrix[-1].append(integer)
                distinct[integer] -= 1
        max_steps -= 1
    return matrix


# Time complexity: O(n) -> traversing whole input array to count everything => O(n) ->
# n - len of input_array^^| -> creating rows with all counted values, essentially same index traverse => O(n).
# Auxiliary space: O(n) -> for every index saving its value into a dictionary => O(n).
# ---------------------
# Seems like we don't care about anything, except distinct integers on each.
# So just count everything and place as max as possible distinct integers on each row.


test: list[int] = [1, 3, 4, 1, 2, 3, 1]
test_out: list[list[int]] = [[1, 3, 4, 2], [1, 3], [1]]
assert test_out == find_matrix(test)

test = [1, 2, 3, 4]
test_out = [[1, 2, 3, 4]]
assert test_out == find_matrix(test)

test = [randint(1, 200) for _ in range(200)]
print(test)
