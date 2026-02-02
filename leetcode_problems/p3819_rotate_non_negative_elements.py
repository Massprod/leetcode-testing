# You are given an integer array nums and an integer k.
# Rotate only the non-negative elements of the array to the left
#  by k positions, in a cyclic manner.
# All negative elements must stay in their original positions and must not move.
# After rotation, place the non-negative elements back into the array in the new order,
#  filling only the positions that originally contained non-negative values
#  and skipping all negative positions.
# Return the resulting array.
# --- --- --- ---
# 1 <= nums.length <= 10 ** 5
# -10 ** 5 <= nums[i] <= 10 ** 5
# 0 <= k <= 10 ** 5


def rotate_elements(nums: list[int], k: int) -> list[int]:
    # working_solution: (85.15%, 40.86%) -> (131ms, 36.4mb)  Time: O(n) Space: O(n)
    positives: list[int] = [_ for _ in nums if 0 <= _]
    if not positives:
        return nums
    # Remove full cycles.
    shift_index: int = k % len(positives)
    shifted: list[int] = positives[shift_index:] + positives[:shift_index]
    # Replace positives.
    index: int = 0
    for ind, val in enumerate(nums):
        if 0 > val:
            continue
        nums[ind] = shifted[index]
        index += 1
    
    return nums


# Time complexity: O(n) <- n - length of the input array `nums`
# --- --- --- ---
# Space complexity: O(n)


test: list[int] = [1, -2, 3, -4]
test_k: int = 3
test_out: list[int] = [3, -2, 1, -4]
assert test_out == rotate_elements(test, test_k)

test = [-3, -2, 7]
test_k = 1
test_out = [-3, -2, 7]
assert test_out == rotate_elements(test, test_k)

test = [5, 4, -9, 6]
test_k = 2
test_out = [6, 5, -9, 4]
assert test_out == rotate_elements(test, test_k)
