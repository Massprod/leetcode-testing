# Given an binary array nums and an integer k,
#  return true if all 1's are at least k places away from each other, otherwise return false.
# --------------------
# 1 <= nums.length <= 10 ** 5
# 0 <= k <= nums.length
# nums[i] is 0 or 1


def k_length_apart(nums: list[int], k: int) -> bool:
    # working_sol (94.19%, 72.29%) -> (407ms, 19.28mb)  time: O(n) | space: O(1)
    cur_dist: int = 0
    try:
        first_one: int = nums.index(1) + 1
    except ValueError:
        return True
    for index in range(first_one, len(nums)):
        if nums[index]:
            if cur_dist < k:
                return False
            cur_dist = 0
            continue
        cur_dist += 1
    return True


# Time complexity: O(n) <- n - length of the input array `nums`
# Always traversing whole input array `nums`, once => O(n).
# --------------------
# Auxiliary space: O(1).
# Only one constant INT used => O(1).


test: list[int] = [1, 0, 0, 0, 1, 0, 0, 1]
test_k: int = 2
test_out: bool = True
assert test_out == k_length_apart(test, test_k)

test = [1, 0, 0, 1, 0, 1]
test_k = 2
test_out = False
assert test_out == k_length_apart(test, test_k)
