# Given an integer array nums, in which exactly two elements appear only once
#  and all the other elements appear exactly twice. Find the two elements that appear only once.
# You can return the answer in any order.
# You must write an algorithm that runs in linear runtime complexity
#  and uses only constant extra space.
# ----------------------------
# 2 <= nums.length <= 3 * 10 ** 4
# -2 ** 31 <= nums[i] <= 2 ** 31 - 1
# Each integer in nums will appear twice, only two integers will appear once.
from random import randint


def single_number(nums: list[int]) -> list[int]:
    # working_sol (86.03%, 99.37%) -> (52ms, 18.18mb)  time: O(n) | space: O(1)
    # num1 ^ num2 ^ num3 ... ^ numN <- always will give us 0 if only duplicates.
    # Cuz, we have 2 unique, they will leave bit's placed.
    # Which is different bits, because they're not annulled by each other.
    all_xor: int = 0
    for num in nums:
        all_xor ^= num
    shift: int = 0
    # Means, we can take any bit that have different placement in both nums.
    while not all_xor & 1:
        all_xor >>= 1
        shift += 1
    rsb: int = 1 << shift
    # And use it to differentiate between 2 groups.
    # One will have a bit placed, and the other doesn't.
    # It can be annulled by other nums or not, but we are 100% sure it's going to be set
    #  in one of our unique values.
    # And it's not going to be placed in another unique value.
    first: int = 0
    second: int = 0
    for num in nums:
        if rsb & num:
            first ^= num
        else:
            second ^= num
    return [first, second]


# Time complexity: O(n) <- n - length of an input array `nums`.
# We're always traversing `nums` once to get all_xor => O(n).
# Extra traverse of the whole `nums` to get XOR of the 2 groups => O(n)
# ----------------------------
# Auxiliary space: O(1).
# Only 4 constant INT's used, none of them depends on input => O(1).


test: list[int] = [1, 2, 1, 3, 2, 5]
test_out: list[int] = [3, 5]
assert test_out == single_number(test)

test = [-1, 0]
test_out = [-1, 0]
assert test_out == single_number(test)

test = [0, 1]
test_out = [1, 0]
assert test_out == single_number(test)

test = []
used: set[int] = set()
all_set: int = 0
for _ in range(10 ** 2):
    chosen: int = randint(-2 ** 31, 2 ** 31 - 1)
    while chosen in used:
        chosen = randint(-2 ** 31, 2 ** 31 - 1)
    test.append(chosen)
    if all_set == 2:
        test.append(chosen)
    else:
        all_set += 1
    used.add(chosen)
print(test)
