# You are given a binary array nums and an integer k.
# A k-bit flip is choosing a subarray of length k from nums
#  and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.
# Return the minimum number of k-bit flips required so that there is no 0 in the array.
# If it is not possible, return -1.
# A subarray is a contiguous part of an array.
# -------------------------
# 1 <= nums.length <= 10 ** 5
# 1 <= k <= nums.length


def min_k_bit_flips(nums: list[int], k: int) -> int:
    # working_sol (95.07%, 76.06%) -> (773ms, 19.58mb)  time: O(n) | space: O(n)
    # [STATE of some index of nums, after flips]
    flipped: list[bool] = [False] * len(nums)
    # Current № of flips we made in a window of size `k`.
    flips_window: int = 0
    out: int = 0
    for index in range(len(nums)):
        # Index is higher than a previous window => decrease number of flips in this window.
        if index >= k:
            if flipped[index - k]:
                flips_window -= 1
        # If we flip `0,` we will get `1` but everything in the window is flipped as well => `flips_window` + 1.
        # So, even if we had `1` which was altered in the window after the first flip,
        #  we still need to flip it another time to get to `1` again.
        if flips_window % 2 == nums[index]:
            # We have something we need to flip, and we already out of boundaries.
            if index + k > len(nums):
                return -1
            flips_window += 1
            flipped[index] = True
            out += 1
    return out


# Time complexity: O(n) <- n - length of the input array `nums`
# Always traversing `num` once => O(n)
# -------------------------
# Auxiliary space: O(n)
# `flipped` is always of the size `n` => O(n).


test: list[int] = [0, 1, 0]
test_k: int = 1
test_out: int = 2
assert test_out == min_k_bit_flips(test, test_k)

test = [1, 1, 0]
test_k = 2
test_out = -1
assert test_out == min_k_bit_flips(test, test_k)

test = [0, 0, 0, 1, 0, 1, 1, 0]
test_k = 3
test_out = 3
assert test_out == min_k_bit_flips(test, test_k)
