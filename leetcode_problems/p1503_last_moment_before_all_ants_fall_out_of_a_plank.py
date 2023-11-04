# We have a wooden plank of the length n units.
# Some ants are walking on the plank, each ant moves with a speed of 1 unit per second.
# Some of the ants move to the left, the other move to the right.
# When two ants moving in two different directions meet at some point,
#  they change their directions and continue moving again.
# Assume changing directions does not take any additional time.
# When an ant reaches one end of the plank at a time t, it falls out of the plank immediately.
# Given an integer n and two integer arrays left and right,
#  the positions of the ants moving to the left and the right,
#  return the moment when the last ant(s) fall out of the plank.
# ----------------------
# 1 <= n <= 10 ** 4
# 0 <= left.length <= n + 1
# 0 <= left[i] <= n
# 0 <= right.length <= n + 1
# 0 <= right[i] <= n
# 1 <= left.length + right.length <= n + 1
# All values of left and right are unique, and each value can appear only in one of the two arrays.


def get_last_moment(n: int, left: list[int], right: list[int]) -> int:
    # working_sol (93.53%, 67.63%) -> (139ms, 17.2mb)  time: O(n) | space: O(1)
    # We don't care about collision.
    # Only thing that matter is what maximum distance some ant can travel.
    if not left:
        return n - min(right)
    elif not right:
        return max(left)
    return max(max(left), n - min(right))


# Time complexity: O(k + m) -> worst case == both arrays present -> traversing both of them to get max(left)
# k - len of input array 'left'^^|  and min(right) => O(k + m).
# m - len of input array 'right'^^|
# Auxiliary space: O(1) -> nothing extra => O(1).
# ----------------------
# Guess we don't care about change of directions, like task with robots before.
# All we care is what maximum distance every ant can travel, and we need maximum distance of them all.
# So it should be like: ! max(max(left), n - min(right)) !
# Because left_direction is always will travel (0 <- left_pos) distance,
#  and right_direction always (n - right) for any ants we're given.


test: int = 4
test_left: list[int] = [4, 3]
test_right: list[int] = [0, 1]
test_out: int = 4
assert test_out == get_last_moment(test, test_left, test_right)

test = 7
test_left = []
test_right = [0, 1, 2, 3, 4, 5, 6, 7]
test_out = 7
assert test_out == get_last_moment(test, test_left, test_right)

test = 7
test_left = [0, 1, 2, 3, 4, 5, 6, 7]
test_right = []
test_out = 7
assert test_out == get_last_moment(test, test_left, test_right)
