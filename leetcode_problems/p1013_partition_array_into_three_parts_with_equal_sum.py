# Given an array of integers arr, return true if we can partition the array
#  into three non-empty parts with equal sums.
# Formally, we can partition the array if we can find indexes i + 1 < j
#  with (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... +
#  arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])
# --------------------
# 3 <= arr.length <= 5 * 10 ** 4
# -10 ** 4 <= arr[i] <= 10 ** 4


def can_three_parts(arr: list[int]) -> bool:
    # working_sol (96.72%, 35.46%) -> (223ms, 23.40mb)  time: O(n) | space: O(1)
    # Can we split in 3?
    cor_part: float = sum(arr) / 3
    if not cor_part.is_integer():
        return False
    # If we can, then we can try to build these parts.
    cor_partition: int = int(cor_part)
    cur_partition: int = 0
    partitions: int = 0
    for val in arr:
        cur_partition += val
        if cur_partition == cor_partition:
            cur_partition = 0
            partitions += 1
            # In cases like [0, 0, 0, 0] or [-5, 5, -5, 5] etc.
            # We're going to have more than 3 partitions,
            #  but these extra parts can be used as 1.
            # So, we can just reshuffle them and still have 3 parts.
            if 3 <= partitions:
                return True
    return 3 <= partitions


# Time complexity: O(n) <- n - length of the input array `arr`.
# Always traversing `arr` to get `cor_part` => O(n).
# Extra traversing every value in `arr` to get # of correct parts => O(2 * n).
# --------------------
# Auxiliary space: O(1)
# Only 3 constant INT's and 1 FLOAT used, none of them depends on input => O(1).


test: list[int] = [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]
test_out: bool = True
assert test_out == can_three_parts(test)

test = [0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]
test_out = False
assert test_out == can_three_parts(test)

test = [3, 3, 6, 5, -2, 2, 5, 1, -9, 4]
test_out = True
assert test_out == can_three_parts(test)

test = [0, 0, 0, 0, 0, 0]
test_out = True
assert test_out == can_three_parts(test)
