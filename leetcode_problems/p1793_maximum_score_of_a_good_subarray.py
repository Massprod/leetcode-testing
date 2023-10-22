# You are given an array of integers nums (0-indexed) and an integer k.
# The score of a subarray (i, j) is defined as min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1).
# A good subarray is a subarray where i <= k <= j.
# Return the maximum possible score of a good subarray.
# ---------------------
# 1 <= nums.length <= 10 ** 5
# 1 <= nums[i] <= 2 * 10 ** 4
# 0 <= k < nums.length
from random import randint


def maximum_score(nums: list[int], k: int) -> int:
    # working_sol (97.96%, 93.88%) -> (846ms, 26.7mb)  time: O(n) | space: O(1)
    # We need Highest score, so we need to maintain the highest
    #  min_value possible, and expand our window as far as possible.
    left_l: int = k
    right_l: int = k
    # Min of current window(subarray).
    cur_min: int = nums[k]
    # 1 * nums[k] <- case with len == 1.
    highest_score: int = 1 * nums[k]
    # Left|Right step options we can make.
    left_min: int = k
    right_min: int = k
    last_l: bool = False
    last_r: bool = False
    while left_l > 0 or right_l < len(nums) - 1:
        # Expand left and right sides while we can.
        while left_l > 0 and nums[left_l - 1] >= cur_min:
            left_l -= 1
        while right_l < len(nums) - 1 and nums[right_l + 1] >= cur_min:
            right_l += 1
        highest_score = max(highest_score, cur_min * (right_l - left_l + 1))
        # After edge indexes used once, we shouldn't consider them again.
        if not last_l:
            # Reached edge index, and already used it.
            # Because we're checking nums[left_l - 1], we will use it and annul after.
            # ! 1 <= nums[i] <= 2 * 10 ** 4 ! <- everything out of this range works, just a placeholder.
            if left_l == 0:
                last_l = True
                left_min = 0
            else:
                left_min = nums[left_l - 1]
        if not last_r:
            if right_l == len(nums) - 1:
                last_r = True
                right_min = 0
            else:
                right_min = nums[right_l + 1]
        cur_min = max(left_min, right_min)
    return highest_score


# Time complexity: O(n) -> essentially we're using every index of the array only once => O(n).
# n - len of input array 'nums'^^|
# Auxiliary space: O(1) -> only constant variables used, none of them depends on input => O(1).
# ---------------------
# Essentially we need some window with maximum option of (j - i + 1) * min(of this window).
# And we always need to start from k, because we need to include it ! i <= k <= j !.
# How we can maintain the highest option?
# If we're making window longer => higher option, but  only if min value is still the same.
# So, just maintain the lowest value of window and step right or left depending on where we can step.
# And we can make steps only if there's something higher on this step_index.
# If only lower step options => update min and continue. Until there's some indexes to check.
# Should be correct.


test: list[int] = [1, 4, 3, 7, 4, 5]
test_k: int = 3
test_out: int = 15
assert test_out == maximum_score(test, test_k)

test = [5, 5, 4, 5, 4, 1, 1, 1]
test_k = 0
test_out = 20
assert test_out == maximum_score(test, test_k)

test = [randint(1, 2 * 10 ** 4) for _ in range(10 ** 3)]
print(test)
