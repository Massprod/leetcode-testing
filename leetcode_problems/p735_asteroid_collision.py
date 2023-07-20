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
    after_collide: list[int] = []
    for asteroid in asteroids:
        add: bool = False
        stop: bool = False
        if len(after_collide) == 0:
            after_collide.append(asteroid)
        elif asteroid > 0:
            after_collide.append(asteroid)
        elif asteroid < 0 and after_collide[-1] < 0:
            after_collide.append(asteroid)
        elif asteroid < 0 and after_collide[-1] > 0:
            while len(after_collide) != 1 and 0 < after_collide[-1] <= abs(asteroid):
                if after_collide[-1] < abs(asteroid):
                    add = True
                if after_collide[-1] == abs(asteroid):
                    after_collide.pop()
                    add = False
                    stop = True
                    break
                after_collide.pop()
            if stop:
                continue
            if after_collide[-1] > abs(asteroid):
                continue
            if len(after_collide) == 1 and 0 < after_collide[-1] < abs(asteroid):
                after_collide.pop()
                after_collide.append(asteroid)
                continue
            if len(after_collide) == 1 and 0 < after_collide[-1] == abs(asteroid):
                after_collide.pop()
                continue
            if add:
                after_collide.append(asteroid)
    return after_collide


# Ok. Failed all commits, because lights went out for 8+ hours and I wanted to maintain daily_streak.
# So just rushed fails to get most tricky tests and build around it.
# ----------------
# Only problem is what we need to consider?
# Every right and left collision or from what point?
# Ok. Made test4 -> we need only check collision with POSITIVE with NEGATIVE which comes after positives.
# Then it's just recreating with replacement of a last element.


test1 = [5, 10, -5]
test1_out = [5, 10]
print(asteroid_collision(test1))

test2 = [8, -8]
test2_out = []
print(asteroid_collision(test2))

test3 = [10, 2, -5]
test3_out = [10]
print(asteroid_collision(test3))

test4 = [-10, -2, -5, 5, 10, -5, 10]
test4_out = [-10, -2, -5, 5, 10, 10]
print(asteroid_collision(test4))

test5 = [-2, -2, 1, -1]
test5_out = [-2, -2]
print(asteroid_collision(test5))

test6 = [-2,2,1,-2]
test6_out = [-2]
print(asteroid_collision(test6))

test7 = [1, 1,-1,-1]
test7_out = [-1]
print(asteroid_collision(test7))

test = []
for _ in range(10 ** 2):
    test.append(randint(-1000, 1000))
print(test)
print(asteroid_collision(test))
