# You are given a 0-indexed integer array nums. The array nums is beautiful if:
#   - nums.length is even.
#   - nums[i] != nums[i + 1] for all i % 2 == 0.
# Note that an empty array is considered beautiful.
# You can delete any number of elements from nums.
# When you delete an element, all the elements to the right of the deleted
#  element will be shifted one unit to the left to fill the gap created
#  and all the elements to the left of the deleted element will remain unchanged.
# Return the minimum number of elements to delete from nums to make it beautiful.
# ------------------------
# 1 <= nums.length <= 10 ** 5
# 0 <= nums[i] <= 10 ** 5
from random import randint


def min_deletion(nums: list[int]) -> int:
    # working_sol (72.32%, 93.79%) -> (949ms, 30.59mb)  time: O(n) | space: O(n)
    out: int = 0
    # [All EVEN indexes we checked]
    stack: list[int] = []
    switch: bool = False
    # Every time we delete any element, everything on the right side is switched.
    # Which means every ODD index, becomes EVEN and EVEN => ODD.
    # So, after deletion we need to change our actions towards these Indexes.
    for index, num in enumerate(nums):
        # Even.
        if not index % 2:
            # And we have our Default order => then we don't need to check [index - 1]
            if not switch:
                stack.append(num)
            # Otherwise, it's actually an ODD index, and we need to check our EVEN index inside `stack`.
            # nums[evenIndex] != nums[evenIndex + 1]
            elif stack and stack[-1] == num:
                out += 1
                # And after every deletion, it's changing ORDER of the right side.
                switch = False
        # ODD.
        elif index % 2:
            # And we don't have Default order => actually EVEN index.
            if switch:
                stack.append(num)
            # Otherwise, it's default ODD index, and we need to check our EVEN index with it.
            # nums[evenIndex] != nums[evenIndex + 1]
            elif stack and stack[-1] == num:
                out += 1
                switch = True
    # Because we only care about nums[evenIndex + 1].
    # Best option is to delete, last element. Because it doesn't have +1.
    # And we can find what's left with (len(nums) - out), because `out` == all elements we deleted.
    if (len(nums) - out) % 2:
        out += 1
    return out


# Time complexity: O(n) <- n - length of input array `nums`.
# Worst case we have ODD `len(nums)`, and every element is the same.
# Means we will use every element into stack and delete it from it, so we're using every index TWICE => O(2n).
# ------------------------
# Auxiliary space: O(n).
# `stack` will allocate space for every element from `nums` => O(n).


test: list[int] = [1, 1, 2, 3, 5]
test_out: int = 1
assert test_out == min_deletion(test)

test = [1, 1, 2, 2, 3, 3]
test_out = 2
assert test_out == min_deletion(test)

test = [randint(0, 3) for _ in range(10 ** 5)]
print(test)
