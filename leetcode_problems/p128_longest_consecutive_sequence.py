# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# !
# You must write an algorithm that runs in O(n) time.!
# -----------------------
# 0 <= nums.length <= 10 ** 5
# -10 ** 9 <= nums[i] <= 10 ** 9


def longest_consecutive(nums: list[int]) -> int:
    # working_sol (55.68%, 12.66%) -> (386ms, 34.3mb)  time: O(n) | space: O(n)
    used_values: dict[int, bool] = {}
    # Store every value.
    for num in nums:
        used_values[num] = False
    max_consecutive: int = 0
    # Try to build from some unused value.
    for value in used_values:
        if not used_values[value]:
            used_values[value] = True
            cur_value: int = value - 1
            cur_consecutive: int = 1
            # Decrease.
            while cur_value in used_values and not used_values[cur_value]:
                used_values[cur_value] = True
                cur_consecutive += 1
                cur_value -= 1
            cur_value = value + 1
            # Increase.
            while cur_value in used_values and not used_values[cur_value]:
                used_values[cur_value] = True
                cur_consecutive += 1
                cur_value += 1
            max_consecutive = max(max_consecutive, cur_consecutive)
    return max_consecutive


# Time complexity: O(n) -> worst case == every value unique -> storing every value into dictionary => O(n) ->
# n - len of input array^^| -> trying to build from anything we can, essentially using every value again => O(2n).
# Auxiliary space: O(n) -> dictionary with all values from input array => O(n).


test: list[int] = [100, 4, 200, 1, 3, 2]
test_out: int = 4
assert test_out == longest_consecutive(test)

test = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
test_out = 9
assert test_out == longest_consecutive(test)
