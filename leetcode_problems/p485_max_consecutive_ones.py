# Given a binary array nums, return the maximum number of consecutive 1's in the array.
# --------------
# 1 <= nums.length <= 10 ** 5
# nums[i] is either 0 or 1.


def find_max_cons_ones(nums: list[int]) -> int:
    # working_sol (90.49%, 65.23%) -> (292ms, 16.5mb)  time: O(n) | space: O(1)
    max_seq: int = 0
    cur_seq: int = 0
    for x in range(len(nums)):
        # Rest when broken.
        if nums[x] == 0:
            max_seq = max(max_seq, cur_seq)
            cur_seq = 0
            continue
        cur_seq += 1
    # Extra check if never broken.
    return max(max_seq, cur_seq)


# Time complexity: O(n) -> traversing whole input_array, once => O(n).
# n - len of input_array^^|
# Auxiliary space: O(1) -> only 2 extra constant INTs used => O(1).


test: list[int] = [1, 1, 0, 1, 1, 1]
test_out: int = 3
assert test_out == find_max_cons_ones(test)

test = [1, 0, 1, 1, 0, 1]
test_out = 2
assert test_out == find_max_cons_ones(test)
