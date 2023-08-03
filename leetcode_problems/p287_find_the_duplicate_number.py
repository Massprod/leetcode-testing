# Given an array of integers nums containing n + 1 integers where
#   each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.
# -------------------------
# 1 <= n <= 10 ** 5
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer which appears two or more times.
# Follow up:
#   How can we prove that at least one duplicate number must exist in nums?
#   Can you solve the problem in linear runtime complexity?


def find_duplicate(nums: list[int]) -> int:
    # working_sol (96.90%, 67.56%) -> (524ms, 31mb)  time: O(n) | space: O(1)
    # Standard Floyd cycle detection.
    slow: int = nums[0]
    fast: int = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow


# Time complexity: O(n) -> standard Floyd cycle by the book => O(n).
# Auxiliary space: O(1) -> only 2 extra INTs used, doesn't depend on input => O(1).
# -------------------------
# How can we prove that at least one duplicate number must exist in nums?
# -> We're given [1, n] range of integers inside the array, but length of the array is (n + 1) ->
# -> so there's always at least 1 out of bound value, and it's 100% duplicate cuz all always inside this range.
# Can you solve the problem in linear runtime complexity?
# -> Tried to solve this without Floyd, and constant space, but it's only working for 1 duplicate.
# With Floyd, it's always linear time_complexity. Guess I need to remember that Floyd can be used anywhere,
# if we need a cycle search. Duplicates -> Array/Linked_lists/w.e -> Cycle ->
# -> Because duplicates will always point the same spot. No matter what structure we use.
# -------------------------
# Wow. Didn't even think about using Floyd here, but it's actually can be used anywhere.
# Cuz we can use values as index_markers, cuz array is range 1 -> n + 1,  so it's always pointing to some value
# inside the array, and we're capable of finding the loop then it's duplicate.
# -------------------------
# Ok. Mistake, I was thinking that we're always given range but no.
# We always have digits from 1 -> n, but they can all be duplicates or just 3, 4, 5.
# So I need to consider minimum value as well.
# Ok. It's working solution for only 1 duplicate if there's more, I can't see how I can do this with,
# sum_range approach. Rebuild.
# -------------------------
# Same as p 268, but now we need duplicates.
# Only difference is that I will just get negative number, which is duplicate.


test: list[int] = [1, 3, 4, 2, 2]
test_out: int = 2
assert test_out == find_duplicate(test)

test = [3, 1, 3, 4, 2]
test_out = 3
assert test_out == find_duplicate(test)

test = [2, 2, 2, 2, 2]
test_out = 2
assert test_out == find_duplicate(test)

test = [2, 5, 9, 6, 9, 3, 8, 9, 7, 1]
test_out = 9
assert test_out == find_duplicate(test)
