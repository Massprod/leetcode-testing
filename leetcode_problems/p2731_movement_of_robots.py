# Some robots are standing on an infinite number line with their initial coordinates given
#   by a 0-indexed integer array nums and will start moving once given the command to move.
# The robots will move a unit distance each second.
# You are given a string s denoting the direction in which robots will move on command.
# 'L' means the robot will move towards the left side or negative side of the number line,
#   whereas 'R' means the robot will move towards the right side or positive side of the number line.
# If two robots collide, they will start moving in opposite directions.
# Return the sum of distances between all the pairs of robots d seconds after the command.
# Since the sum can be very large, return it modulo 10 ** 9 + 7.
# Note:
#   For two robots at the index i and j, pair (i,j) and pair (j,i) are considered the same pair.
#   When robots collide, they instantly change their directions without wasting any time.
#   Collision happens when two robots share the same place in a moment.
#   For example, if a robot is positioned in 0 going to the right and another is positioned in 2 going to the left,
#     the next second they'll be both in 1, and they will change direction
#     and the next second the first one will be in 0, heading left, and another will be in 2, heading right.
#   For example, if a robot is positioned in 0 going to the right and another is positioned in 1 going to the left,
#     the next second the first one will be in 0, heading left, and another will be in 1, heading right.
# ------------------
# 2 <= nums.length <= 10 ** 5
# -2 * 10 ** 9 <= nums[i] <= 2 * 10 ** 9
# 0 <= d <= 10 ** 9
# nums.length == s.length
# s consists of 'L' and 'R' only
# nums[i] will be unique.
from random import randint, choice


def sum_distance(nums: list[int], s: str, d: int) -> int:
    # working_sol (99.36%, 45.75%) -> (406ms, 29.38mb)  time: O(n) | space: O(1)
    # Used HINTS. Cuz it's a book task unsolvable without knowing basics:
    # ! Observe that if you ignore collisions, the resultant positions
    #   of robots after d seconds would be the same. ! ->
    length: int = len(nums)
    # -> So we can just move all of them in one step.
    for y in range(length):
        if s[y] == 'R':
            nums[y] += 1 * d
            continue
        nums[y] -= 1 * d
    # ! After d seconds, sort the ending positions
    #   and use prefix sum to calculate the distance sum. !
    nums.sort()
    summ: int = 0
    # We need only pairs, and [0] doesn't have robots before it.
    prefix: int = nums[0]
    for x in range(1, length):
        # prefix == summ of every robot before current.
        # x * nums[x] == value needed for all pairs combined.
        # Normally we're using nums[5] - nums[4], nums[5] - nums[3] etc.
        # For every robot before, we're calculating distance between these robots
        # and current nums[5]. But we can use nums[5] * 5, and we're getting full_value
        # and prefix == summ of everything before -> nums[5] * 5 - nums[4] - nums[3] etc.
        # We can use prefix_sum to get nums[4] + nums[3] + nums[2] etc. ->
        # nums[5] * 5 - prefix == correct_summ. ->
        # -> So it's just all pairs calculated at once.
        summ += x * nums[x] - prefix
        # Standard prefix increment.
        prefix += nums[x]
    # ! return it modulo 10 ** 9 + 7 !
    return summ % (10 ** 9 + 7)


# Time complexity: O(n) -> traversing whole input_array once, and move all robots in their end_places => O(n) ->
# n - len of input_array^^| -> calculating summ of a distances with prefix_sum => O(n).
# Auxiliary space: O(1) -> sorting in_place => O(1) -> using only 3 constant INTs => O(1).
# ------------------
# Yep. Tested with max_constraints, and it's totally TLE. No idea how to cull it, taking a HINT:
#  ! Observe that if you ignore collisions, the resultant positions of robots after d seconds would be the same. !
# ^^So we don't need to check and change directions at all. Ok, it's working correctly with basic test_cases.
# But still TLE with max_constraints, another HINT:
#  ! After d seconds, sort the ending positions and use prefix sum to calculate the distance sum. !
# ------------------
# 2 Cycles for every d(second) move every robot, see who is colliding -> change they're move_direction,
# repeat until d != 0. Should be correct.
# This problem is like 30% success rate, so I guess there's some harsh time_limit, and mine solution
# with just cycles is really slow. Summ is like O(n * n) and 2 cycles is O(n * n) each,
# even with memorizing of already checked values it's still slow. What can I cull?


test: list[int] = [-2, 0, 2]
test_s: str = "RLL"
test_d: int = 3
test_out: int = 8
assert test_out == sum_distance(test, test_s, test_d)

test = [1, 0]
test_s = "RL"
test_d = 2
test_out = 5
assert test_out == sum_distance(test, test_s, test_d)

test = [15, 12, -10, 8, -6, -8, -11, -21]
test_s = "RLLRLRLR"
test_d = 4034
test_out = 129321
assert test_out == sum_distance(test, test_s, test_d)

test = [
    881055899, 1859532521, -744446222, 1193598556, 1167110472, 729862034, 1656114337, 801303843, -342499289, 72399034
]
test_s = "RRLLLLRRRR"
test_d = 4034
test_out = 423631013
assert test_out == sum_distance(test, test_s, test_d)

test = []
test_s = ''
choose: list[str] = ['R', 'L']
used: set[int] = set()
for _ in range(10 ** 1):
    value: int = randint(-2 * 10 ** 9, 2 * 10 ** 9)
    while value in used:
        value = randint(-2 * 10 ** 9, 2 * 10 ** 9)
    test.append(value)
    test_s += choice(choose)
test_d = randint(0, 10 ** 9)
# print(test)
# print(test_s)
# print(test_d)
# print(sum_distance(test, test_s, test_d))
