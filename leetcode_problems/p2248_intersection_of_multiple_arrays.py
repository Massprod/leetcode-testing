# Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers,
#  return the list of integers that are present in each array of nums sorted in ascending order.
# ----------------
# 1 <= nums.length <= 1000
# 1 <= sum(nums[i].length) <= 1000
# 1 <= nums[i][j] <= 1000
# All the values of nums[i] are unique.


def intersection(nums: list[list[int]]) -> list[int]:
    # working_sol (99.56%, 58.95%) -> (58ms, 16.8mb)  time: O(n * m + k * log k) | space: O(k)
    # ! distinct positive integers !
    # So we can just take everything that occur,
    #  len(nums) times => on every row.
    counted: dict[int, int] = {}
    # Count occurrences.
    for row in nums:
        for num in row:
            if num not in counted:
                counted[num] = 1
                continue
            counted[num] += 1
    intersect: set[int] = set()
    # Add only correct ones.
    for num in counted:
        if counted[num] == len(nums):
            intersect.add(num)
    # ! return the list of integers, sorted in ascending order !
    return sorted(list(intersect))


# Time complexity: O(n * m + k * log k) -> count and store every row => O(n * m) ->
# n - matrix height^^|          -> traverse all unique values stored => O(k) -> worst case every value from k inters ->
# k - matrix max_row_length^^|  -> remake as list and sort => O(k * log k + k) -> O(n * m + k + k * log k + k) =>
# m - matrix average_row_length^^| => O(n * m + k * log k)
# Auxiliary space: O(k) -> worst case, all row values intersects -> so we're just creating dictionary with all values
#                          from max_row => O(k) -> extra set with same values => O(k) -> O(2k) + list on return O(3k).


test: list[list[int]] = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]
test_out: list[int] = [3, 4]
assert test_out == intersection(test)

test = [[1, 2, 3], [4, 5, 6]]
test_out = []
assert test_out == intersection(test)
