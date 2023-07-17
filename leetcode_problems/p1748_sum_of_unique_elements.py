# You are given an integer array nums.
# The unique elements of an array are the elements that appear exactly once in the array.
# Return the sum of all the unique elements of nums.
# ----------------
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
from random import randint


def sum_of_unique(nums: list[int]) -> int:
    # working_sol (98.37%, 94.63%) -> (37ms, 16.14mb)  time: O(n) | space: O(n)
    uniques: dict[int, int] = {}
    # all positive constraints, can be 0
    summ: int = 0
    for num in nums:
        # first_encounter
        if num not in uniques:
            uniques[num] = 1
            summ += num
            continue
        # second_encounter
        if uniques[num] == 1:
            summ -= num
            uniques[num] += 1
    return summ


# Time complexity: O(n) -> traversing whole input_array, once => O(n).
# n - len of input_array^^|
# Auxiliary space: O(n) -> in the worst case every value is unique and will be stored in dictionary => O(n).
# ----------------
# Actually can be done with 1 walk. Just delete anything that we meet again, and increment by 1.
# Cuz only values we didn't encounter more than 1 is matter.


test1 = [1, 2, 3, 2]
test1_out = 4
assert test1_out == sum_of_unique(test1)

test2 = [1, 1, 1, 1, 1]
test2_out = 0
assert test2_out == sum_of_unique(test2)

test3 = [1, 2, 3, 4, 5]
test3_out = 15
assert test3_out == sum_of_unique(test3)

test: list[int] = []
for _ in range(100):
    test.append(randint(1, 100))
print(test)
print(sum_of_unique(test))
