# You are given a 0-indexed integer array nums whose length is a power of 2.
# Apply the following algorithm on nums:
#  1. Let n be the length of nums. If n == 1, end the process.
#     Otherwise, create a new 0-indexed integer array newNums of length n / 2.
#  2. For every even index i where 0 <= i < n / 2,
#     assign the value of newNums[i] as min(nums[2 * i], nums[2 * i + 1]).
#  3. For every odd index i where 0 <= i < n / 2,
#     assign the value of newNums[i] as max(nums[2 * i], nums[2 * i + 1]).
#  4. Replace the array nums with newNums.
#  5. Repeat the entire process starting from step 1.
# Return the last number that remains in nums after applying the algorithm.
# -----------------------
# 1 <= nums.length <= 1024
# 1 <= nums[i] <= 10 ** 9
# nums.length is a power of 2.


def min_max_game(nums: list[int]) -> int:
    # working_sol (75.11%, 57.58%) -> (51ms, 16.76mb)  time: O(n * log n) | space: O(n)
    def cycle(array: list[int]) -> list[int]:
        if 1 == len(array):
            return array
        new_array: list[int] = []
        for index in range(len(array) // 2):
            if index % 2:
                new_array.append(
                    max(array[2 * index], array[2 * index + 1])
                )
            else:
                new_array.append(
                    min(array[2 * index], array[2 * index + 1])
                )
        return new_array

    while 1 != len(nums):
        nums = cycle(nums)
    return nums[0]


# Time complexity: O(n * log n) <- n - length of the input array `nums`.
# Always traversing `nums` in full, then slicing it in half and traversing again
#  similar to merge sort => O(n * log n).
# -----------------------
# Auxiliary space: O(n)
# First cycle will return as an array of size `n // 2` => O(n // 2).
# Other cycle will return smaller arrays, so it's max size we use.


test: list[int] = [1, 3, 5, 2, 4, 8, 2, 2]
test_out: int = 1
assert test_out == min_max_game(test)

test = [3]
test_out = 3
assert test_out == min_max_game(test)
