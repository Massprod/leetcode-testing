# You are given a 0-indexed integer array nums and an integer threshold.
# Find the length of the longest subarray of nums starting at index l
#   and ending at index r (0 <= l <= r < nums.length) that satisfies the following conditions:
#   - nums[l] % 2 == 0
#   - For all indices i in the range [l, r - 1], nums[i] % 2 != nums[i + 1] % 2
#   - For all indices i in the range [l, r], nums[i] <= threshold
# Return an integer denoting the length of the longest such subarray.
# Note: A subarray is a contiguous non-empty sequence of elements within an array.
# ---------------
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
# 1 <= threshold <= 100
from random import randint


def longest_alternating_sub(nums: list[int], threshold: int) -> int:
    # working_sol (99.65%, 85.9%) -> (287ms, 16.2mb)  time: O(n) | space: O(1)
    # Unique case, actually can be deleted, working correctly anyway.
    # Just a placeholder when started.
    if len(nums) == 1:
        if nums[0] % 2 == 0 and nums[0] <= threshold:
            return 1
        return 0
    max_sub: int = 0
    # Using window to maintain sub_seq
    left_l: int = 0
    right_l: int = 0
    # We're not shrinking window, but resetting it.
    # Trigger for this, actually need to change it later.
    new_start: bool = True
    for x in range(len(nums)):
        # Second rule, any value should be <= threshold.
        if nums[x] <= threshold:
            # Building rule, we can't start sub_seq if first value of it
            # doesn't satisfy -> nums[x] % == 0 and nums[x] <= threshold.
            if new_start and nums[x] % 2 == 0:
                new_start = False
                # New limits.
                left_l = x
                right_l = x
                # If we found at least 1 correct value, it's sub_seq by itself == 1.
                max_sub = max(max_sub, 1)
                continue
            # Expand window.
            if not new_start:
                # Every value we're trying to add should satisfy First rule
                # nums[i] % 2 != nums[i + 1] % 2, and our right_limit points to a last sub_seq value.
                if nums[right_l] % 2 != nums[x] % 2:
                    right_l += 1
                    # If we break or expand we need to recheck max_sub.
                    # +1 for 0 indexed array.
                    max_sub = max(max_sub, right_l - left_l + 1)
                    continue
                new_start = True
                # If we break or expand we need to recheck max_sub.
                # +1 for 0 indexed array.
                if right_l != left_l:
                    max_sub = max(max_sub, right_l - left_l + 1)
                # Using FOR loop, so either I need to rebuild with other
                # pointers, or I need to reset window after we break instantly, at the same X.
                if new_start and nums[x] % 2 == 0:
                    new_start = False
                    left_l = x
                    right_l = x
        else:
            # We can't use it at all, doesn't satisfy Second rule.
            # And second rule is for every value in sub_seq.
            if right_l != left_l:
                max_sub = max(max_sub, right_l - left_l + 1)
            # And we can't rebuild from it, so we're just skipping
            # and rebuilding somewhere else.
            new_start = True
    return max_sub


# Time complexity: O(n) -> traversing whole input_array, once => O(n) -> we're resetting window on index we break
# n - len of input_array^^| or next correct index, but we're always using any index only once.
# Auxiliary space: O(1) -> only extra constants used, none of them depends on input => O(1).
# ---------------
# Ok. Next time I will use more test_cases, cuz I test like 5 with maximum constraints and they were all correct.
# But there was mistake with not instantly resetting window, and extra +1 for max_sub when we had same limits.
# All this mistakes comes from using FOR loop, because I could just use some pointers to indexes we're checking now.
# And then I would miss the part with resetting it, cuz index wasn't be incremented automatically ->
# -> so for a future, it's better to maintain it more precisely, then just standard loop.
# Cuz I'm reusing new_start and nums[x] % 2 == 0, only because we're insta changing x to x + 1 after we failed, and
# needed a new_start to reset window.
# Well it's 27% success rate problem, so I guess it's correct for me to fail 3/4 :).
# But better to recheck and don't rush solutions, even when max_constraints are correct. But easy task...
# ---------------
# Window problem, I guess. But instead of shrinking window I need to restart it,
# when incorrect value is met.


test1 = [3, 2, 5, 4]
test1_thresh = 5
test1_out = 3
assert test1_out == longest_alternating_sub(test1, test1_thresh)

test2 = [1, 2]
test2_thresh = 2
test2_out = 1
assert test2_out == longest_alternating_sub(test2, test2_thresh)

test3 = [2, 3, 4, 5]
test3_thresh = 4
test3_out = 3
assert test3_out == longest_alternating_sub(test3, test3_thresh)

test4 = [13, 37, 46, 16, 17, 65, 16, 25, 84, 17, 78, 94, 93, 69, 27, 99, 46, 2, 26, 36]
test4_thresh = 74
test4_out = 2
assert test4_out == longest_alternating_sub(test4, test4_thresh)

# test5 -> failed -> Cuz I placed case with len == 1, and forgot to recheck it after.
test5 = [1]
test5_thresh = 1
test5_out = 0
assert test5_out == longest_alternating_sub(test5, test5_thresh)

# test6 -> failed -> Cuz I wasn't resetting counter for correct X.
test6 = [4, 10, 3]
test6_thresh = 10
test6_out = 2
assert test6_out == longest_alternating_sub(test6, test6_thresh)

# test7 -> failed -> Literally No idea, cuz I didn't change anything, and it worked locally, but I guess
#                    missed something when copied. But didn't see what. Recopied all correct...
#                    Ok. I tried to delete part with % 2 check for the new_start -> which can't be correct,
#                    because we get in this start if threshold and passed, but we still need to check % 2 == 0,
#                    and I bragged thinking that if we get here, we passed all checks and deleted it on Leet.
#                    This is why locally it worked correctly, cuz here I didn't delete it.
#                    W.e still failed 3 commits for really no reasons, just needed to extra check.
test7 = [2, 2, 5, 1, 6, 7, 8]
test7_thresh = 17
test7_out = 3
assert test7_out == longest_alternating_sub(test7, test7_thresh)

test: list[int] = []
for _ in range(100):
    test.append(randint(1, 100))
test_thresh: int = randint(1, 100)
print(test)
print(test_thresh)
