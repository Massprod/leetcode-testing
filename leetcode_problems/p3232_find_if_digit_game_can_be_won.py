# You are given an array of positive integers nums.
# Alice and Bob are playing a game. In the game,
#  Alice can choose either all single-digit numbers or all double-digit numbers from nums,
#  and the rest of the numbers are given to Bob.
# Alice wins if the sum of her numbers is strictly greater than the sum of Bob's numbers.
# Return true if Alice can win this game, otherwise, return false.
# --------------------------
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 99


def can_alice_win(nums: list[int]) -> bool:
    # working_sol (85.31%, 94.55%) -> (51ms, 16.40mb)  time: O(n) | space: O(1)
    doubles: int = 0
    singles: int = 0
    for num in nums:
        if 10 <= num:
            doubles += num
        else:
            singles += num
    # Bob has only option if both options give us an equal sum.
    return not (doubles == singles)


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing `nums`, once => O(n).
# --------------------------
# Auxiliary space: O(1)
# Only two constant INTs used, none of them depends on input => O(1).


test: list[int] = [1, 2, 3, 4, 10]
test_out: bool = False
assert test_out == can_alice_win(test)

test = [1, 2, 3, 4, 5, 14]
test_out = True
assert test_out == can_alice_win(test)

test = [5, 5, 5, 25]
test_out = True
assert test_out == can_alice_win(test)
