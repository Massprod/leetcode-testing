# You are given 2 integer arrays nums1 and nums2 of lengths n and m respectively.
# You are also given a positive integer k.
# A pair (i, j) is called good if nums1[i] is divisible by nums2[j] * k (0 <= i <= n - 1, 0 <= j <= m - 1).
# Return the total number of good pairs.
# -----------------------
# 1 <= n, m <= 50
# 1 <= nums1[i], nums2[j] <= 50
# 1 <= k <= 50


def number_of_pairs(nums1: list[int], nums2: list[int], k: int) -> int:
    # working_sol (28.66%, 63.23%) -> (57ms, 16.57mb)  time: O(n * m) | space: O(1)
    out: int = 0
    for num1 in nums1:
        for num2 in nums2:
            if 0 == num1 % (num2 * k):
                out += 1
    return out


# Time complexity: O(n * m) <- n - length of the input array `nums1`. m - length of the input array `nums2`.
# Simple brute force with nested loop => O(n * m).
# -----------------------
# Auxiliary space: O(1).


test_1: list[int] = [1, 3, 4]
test_2: list[int] = [1, 3, 4]
test_k: int = 1
test_out: int = 5
assert test_out == number_of_pairs(test_1, test_2, test_k)

test_1 = [1, 2, 4, 12]
test_2 = [2, 4]
test_k = 3
test_out = 2
assert test_out == number_of_pairs(test_1, test_2, test_k)
