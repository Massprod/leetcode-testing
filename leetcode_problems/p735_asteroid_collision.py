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
    # working_sol (46.84%, 84.31%) -> (114ms, 17.4mb)  time: O(n) | space: O(n)
    after_collide: list[int] = []
    for asteroid in asteroids:
        add: bool = False
        stop: bool = False
        # base case
        if len(after_collide) == 0:
            after_collide.append(asteroid)
        # positive always goes in
        elif asteroid > 0:
            after_collide.append(asteroid)
        # negative and everything before is correct negatives
        elif asteroid < 0 and after_collide[-1] < 0:
            after_collide.append(asteroid)
        # negative, but last added positive
        elif asteroid < 0 and after_collide[-1] > 0:
            # if positive is lower -> delete and add
            # if positive is equal -> delete and don't add
            while len(after_collide) != 1 and 0 < after_collide[-1] <= abs(asteroid):
                # case with positive being lower
                if after_collide[-1] < abs(asteroid):
                    add = True
                # case with positive being equal ->
                # -> break and don't add negative, cuz they destroyed themselves
                if after_collide[-1] == abs(asteroid):
                    after_collide.pop()
                    add = False
                    stop = True
                    break
                # pop() until higher, equal or negative is met
                after_collide.pop()
            # change_it!, placeholder to make this in 20m for streak.
            if stop:
                continue
            # if last element is positive and higher, doing nothing
            if after_collide[-1] > abs(asteroid):
                continue
            # if last element is positive and lower, replace
            if len(after_collide) == 1 and 0 < after_collide[-1] < abs(asteroid):
                after_collide.pop()
                after_collide.append(asteroid)
                continue
            # if last element is positive and equal, delete don't add
            if len(after_collide) == 1 and 0 < after_collide[-1] == abs(asteroid):
                after_collide.pop()
                continue
            # if every positive element was deleted, and last positive deleted was LOWER
            if add:
                after_collide.append(asteroid)
    return after_collide


# Time complexity: O(n) -> traversing whole input_array, once => O(n) -> but there's WHILE loop inside which
# n - len of input_array^^| in the worst case can be extra O(n), because case like 1,1,1...1,1,1,1,-10 =>
#                           => we're going to add all 1 into an after_collide and when -10 encountered, extra
#                           traversing whole after_collide array with already size of (n - 1) to delete all elements
#                           and add -10 as a new asteroid => O(n) -> O(n) + O(n) => O(n).
# Auxiliary space: O(n) -> in the worst case every asteroid is negative or positive, and we're just adding them all =>
#                          => getting actual copy of input_array => O(n). On median is θ(log n).
# ----------------
# Ok. Failed all commits, because lights went out for 8+ hours and I wanted to maintain daily_streak.
# So I just rushed fails to get most tricky tests and build around it.
# Well, at least made it in 20m. Rebuild sometimes later.
# ----------------
# Only problem is what we need to consider?
# Every right and left collision or from what point?
# Ok. Made test4 -> we need only check collision with POSITIVE with NEGATIVE which comes after positives.
# Then it's just recreating with replacement of a last element.


test1 = [5, 10, -5]
test1_out = [5, 10]
print(asteroid_collision(test1))
assert test1_out == asteroid_collision(test1)

test2 = [8, -8]
test2_out = []
print(asteroid_collision(test2))
assert test2_out == asteroid_collision(test2)

test3 = [10, 2, -5]
test3_out = [10]
print(asteroid_collision(test3))
assert test3_out == asteroid_collision(test3)

test4 = [-10, -2, -5, 5, 10, -5, 10]
test4_out = [-10, -2, -5, 5, 10, 10]
print(asteroid_collision(test4))
assert test4_out == asteroid_collision(test4)

test5 = [-2, -2, 1, -1]
test5_out = [-2, -2]
print(asteroid_collision(test5))
assert test5_out == asteroid_collision(test5)

test6 = [-2, 2, 1, -2]
test6_out = [-2]
print(asteroid_collision(test6))
assert test6_out == asteroid_collision(test6)

test7 = [1, 1, -1, -1]
test7_out = []
print(asteroid_collision(test7))
assert test7_out == asteroid_collision(test7)

# test = []
# for _ in range(10 ** 2):
#     test.append(randint(-1000, 1000))
# print(test)
# print(asteroid_collision(test))
