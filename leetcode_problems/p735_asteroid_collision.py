# We are given an array asteroids of integers representing asteroids in a row.
# For each asteroid, the absolute value represents its size,
#   and the sign represents its direction (positive meaning right, negative meaning left).
# Each asteroid moves at the same speed.
# Find out the state of the asteroids after all collisions.
# If two asteroids meet, the smaller one will explode.
# If both are the same size, both will explode.
# Two asteroids moving in the same direction will never meet.
# ----------------
# 2 <= asteroids.length <= 10 ** 4
# -1000 <= asteroids[i] <= 1000
# asteroids[i] != 0
from random import randint


def asteroid_collision(asteroids: list[int]) -> list[int]:
    # working_sol (94.6%, 84.31%) -> (93ms, 17.4mb)  time: O(n) | space: O(n)
    list_stack: list[int] = [asteroids[0]]
    for x in range(1, len(asteroids)):
        # All we care is negative asteroids and only when last asteroid is positive.
        if len(list_stack) > 0 and asteroids[x] < 0 and list_stack[-1] > 0:
            # Saving to skip recalcs.
            value: int = abs(asteroids[x])
            # If negative_asteroid is bigger than positives,
            # it will eliminate them ->
            while len(list_stack) > 0 and value > list_stack[-1] > 0:
                list_stack.pop()
            # -> if it's eliminated everything, just append ->
            if len(list_stack) == 0:
                list_stack.append(asteroids[x])
                continue
            # -> still need to check if there's equal positive,
            # if there's we just removing it and negative is destroyed ->
            if value == list_stack[-1]:
                list_stack.pop()
                continue
            # -> if right is lower than we don't care ->
            if value < list_stack[-1]:
                continue
            # -> if right eliminated every positive,
            # but there's still negative asteroids len(list_stack) > 0.
            list_stack.append(asteroids[x])
        # If it's positive we don't care it can't collide with anything.
        # Cuz everything in a stack is already gone far left, or going right.
        else:
            list_stack.append(asteroids[x])
    return list_stack


# Time complexity: O(n) -> traversing whole input_array, once => O(n) -> but there's WHILE loop inside which
# n - len of input_array^^| in the worst case should be extra O(n), because case like 1,1,1...1,1,1,1,-10 =>
#                           => we're going to add all 1 into an after_collide and when -10 encountered, extra
#                           traversing whole after_collide array with already size of (n - 1) to delete all elements
#                           and add -10 as a new asteroid => O(2n) => O(n).
# Auxiliary space: O(n) -> in the worst case every asteroid is negative or positive, and we're just adding them all =>
#                          => getting actual copy of input_array => O(n). On median is θ(log n).
# ----------------
# Only problem is what we need to consider?
# Every right and left collision or from what point?
# Ok. Made test4 -> we need only check collision with POSITIVE with NEGATIVE which comes after positives.
# Then it's just recreating with replacement of a last element.


test: list[int] = [5, 10, -5]
test_out: list[int] = [5, 10]
assert test_out == asteroid_collision(test)

test = [8, -8]
test_out = []
assert test_out == asteroid_collision(test)

test = [10, 2, -5]
test_out = [10]
assert test_out == asteroid_collision(test)

test = [-10, -2, -5, 5, 10, -5, 10]
test_out = [-10, -2, -5, 5, 10, 10]
assert test_out == asteroid_collision(test)

test = [-2, -2, 1, -1]
test_out = [-2, -2]
assert test_out == asteroid_collision(test)

test = [-2, 2, 1, -2]
test_out = [-2]
assert test_out == asteroid_collision(test)

test = [1, 1, -1, -1]
test_out = []
assert test_out == asteroid_collision(test)

test = [1, -2, -2, -2]
test_out = [-2, -2, -2]
assert test_out == asteroid_collision(test)

test = []
for _ in range(10 ** 2):
    test.append(randint(-1000, 1000))
# print(test)
# print(asteroid_collision(test))
