# There are n 1-indexed robots, each having a position on a line, health, and movement direction.
# You are given 0-indexed integer arrays positions, healths,
#  and a string directions (directions[i] is either 'L' for left or 'R' for right).
# All integers in positions are unique.
# All robots start moving on the line simultaneously at the same speed in their given directions.
# If two robots ever share the same position while moving, they will collide.
# If two robots collide, the robot with lower health is removed from the line,
#  and the health of the other robot decreases by one.
# The surviving robot continues in the same direction it was going.
# If both robots have the same health, they are both removed from the line.
# Your task is to determine the health of the robots that survive the collisions,
#  in the same order that the robots were given, i.e. final heath of robot 1 (if survived),
#  final health of robot 2 (if survived), and so on. If there are no survivors, return an empty array.
# Return an array containing the health of the remaining robots (in the order they were given in the input),
#  after no further collisions can occur.
# Note: The positions may be unsorted.
# ---------------------
# 1 <= positions.length == healths.length == directions.length == n <= 10 ** 5
# 1 <= positions[i], healths[i] <= 10 ** 9
# directions[i] == 'L' or directions[i] == 'R'
# All values in positions are distinct
from random import randint, choice


def survived_robots_healths(positions: list[int], healths: list[int], directions: str) -> list[int]:
    # working_sol (87.41%, 71.85%) -> (1114ms, 41.1mb)  time: O(n * log n) | space: O(n)
    # (position: index) <- index == id of the robot.
    # We're given input of 3 lists with every robot id is equal to list index.
    # Need this for -> ! remaining robots (in the order they were given in the input) !
    ids: dict[int, int] = {}
    for x in range(len(positions)):
        ids[positions[x]] = x
    # All robots have same speed, they will never override someone.
    # Essentially it will be a que of collisions:
    #   r1->r2->r3-> <-r4<-r5<-r6
    # So, only thing we care is R-L collision.
    # Just sort() and check all robots from left -> right.
    positions.sort()
    might_collide: list[int] = []
    # Only option for collision is R -> <- L
    # Store robots with R direction in a stack
    #  to get them in correct order and check for collisions.
    for pos in positions:
        if directions[ids[pos]] == 'L':
            while might_collide and healths[ids[pos]] > 0:  # '> 0' for easier read.
                # R survives.
                if healths[might_collide[-1]] > healths[ids[pos]]:
                    healths[might_collide[-1]] -= 1
                    healths[ids[pos]] = 0
                # L survives.
                elif healths[might_collide[-1]] < healths[ids[pos]]:
                    healths[might_collide.pop()] = 0
                    healths[ids[pos]] -= 1
                # Both gone.
                elif healths[might_collide[-1]] == healths[ids[pos]]:
                    healths[might_collide.pop()] = 0
                    healths[ids[pos]] = 0
        if directions[ids[pos]] == 'R':
            might_collide.append(ids[pos])
    survivors: list[int] = [health for health in healths if health > 0]
    return survivors


# Time complexity: O(n * log n) -> all input_array are equal, we always traverse positions to get indexing => O(n) ->
# n - len of input_arrays^^| -> always sorting positions for easier processing of collision => O(n * log n) ->
#                            -> main traverse of positions again to get collision survivors => O(n) ->
#                            -> last traverse of healths with same size as positions to get survivors => O(n).
# Auxiliary space: O(n) -> dictionary to store robot_ids(original positions indexing) => O(n) ->
#                       -> extra list with robots who goes Right, worst case == everyone goes Right => O(n) ->
#                       -> extra list with survivors, same worst case everyone survives => O(n) => O(3n).
# ---------------------
# First we don't care about speed. Only one robot per position and same speed.
# Cuz all robots having same speed, so they will never overrun someone, and only thing we should consider is collision.
# Collision between any robots will be possible only, and only when 1 robot going Right and other going Left.
# Only problem is to find them fast. If we take any robot, and it goes Left then we need all robots on the left side.
# And only one which goes Right, extra we need to sort them to get the closest robot, which will collide first.
# Essentially we're just taking Any robot who goes Right and check him with every other robot on his right_side,
#  who goes Left. So we can just sort them by position in ascending order. Then we can just go from left -> right,
#  and check robots one by one. Find counterpart for one who goes Right, and ignore Left_travelers when there's no
#  Right on left side.
# Stack? Maintain stack with Right_travelers, should be correct.
# All correct, but ! the health of the remaining robots (in the order they were given in the input) !.
# So we need to maintain robots order for correct healths.
# See 2 ways:
#   1) enumerate() or list with all indexes sorted by positions.
#   2) dictionary with (position: index)
# Can we annul? Yep, test_case#2 we delete robots when their health == 0, not just leaving them with 0.
# Sort as before, and traverse position use stored indexes to get robot healths and direction.
# Let's try. Working correctly.


test_pos: list[int] = [5, 4, 3, 2, 1]
test_healths: list[int] = [2, 17, 9, 15, 10]
test_directs: str = "RRRRR"
test_out: list[int] = [2, 17, 9, 15, 10]
assert test_out == survived_robots_healths(test_pos, test_healths, test_directs)

test_pos = [3, 5, 2, 6]
test_healths = [10, 10, 15, 12]
test_directs = "RLRL"
test_out = [14]
assert test_out == survived_robots_healths(test_pos, test_healths, test_directs)

test_pos = [1, 2, 5, 6]
test_healths = [10, 10, 11, 11]
test_directs = "RLRL"
test_out = []
assert test_out == survived_robots_healths(test_pos, test_healths, test_directs)

test_pos = [randint(1, 10 ** 9) for _ in range(10 ** 3)]
test_healths = [randint(1, 10 ** 9) for _ in range(10 ** 3)]
test_directs = ''.join([choice(['L', 'R']) for _ in range(10 ** 3)])
print(test_pos)
print('!-------BREAK')
print(test_healths)
print(test_directs)
