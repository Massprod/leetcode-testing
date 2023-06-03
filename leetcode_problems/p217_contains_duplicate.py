# Given an integer array nums, return true if any value appears at least twice in the array,
#   and return false if every element is distinct.
# -----------------------
# 1 <= nums.length <= 10 ** 5  ,  -10 ** 9 <= nums[i] <= 10 ** 9


def contains_duplicate(nums: list[int]) -> bool:
    # working_sol (94.72%, 5.5%) -> (532ms, 34.6mb)  time: O(n) | space: O(n)
    doubles: dict[int] = {}
    for num in nums:
        if num in doubles:
            return True
        doubles[num] = True
    return False


# Time complexity: O(n) -> traversing input_list once => O(n)
# n - len of input_list^^|
# Auxiliary space: O(n) -> in the worst case adding all copies of input_list values into doubles => O(n)
# -----------------------
# Well 2 methods I know to solve this.
#   1) Using dict to store everything we meet and return False after double_cross -> time: O(n) , space: O(n).
#   2) Sorting original list, and just checking every value from left to right, until we hit double or not ->
#      -> time: O((n * (log n) + n) , space: O(1).
# There's no extra objective, so I will stick to 1. Speed > Memory.
# Maybe I could come up with something more, but there are no reasons to.


test1 = [1, 2, 3, 1]
test1_out = True
print(contains_duplicate(test1))
assert test1_out == contains_duplicate(test1)

test2 = [1, 2, 3, 4]
test2_out = False
print(contains_duplicate(test2))
assert test2_out == contains_duplicate(test2)

test3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
test3_out = True
print(contains_duplicate(test3))
assert test3_out == contains_duplicate(test3)
