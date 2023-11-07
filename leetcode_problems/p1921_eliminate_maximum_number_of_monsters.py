# You are playing a video game where you are defending your city from a group of n monsters.
# You are given a 0-indexed integer array dist of size n, where dist[i]
#  is the initial distance in kilometers of the ith monster from the city.
# The monsters walk toward the city at a constant speed.
# The speed of each monster is given to you in an integer array speed of size n,
#  where speed[i] is the speed of the ith monster in kilometers per minute.
# You have a weapon that, once fully charged, can eliminate a single monster.
# However, the weapon takes one minute to charge. The weapon is fully charged at the very start.
# You lose when any monster reaches your city.
# If a monster reaches the city at the exact moment the weapon is fully charged, it counts as a loss,
#  and the game ends before you can use your weapon.
# Return the maximum number of monsters that you can eliminate before you lose,
#  or n if you can eliminate all the monsters before they reach the city.
# ----------------------------
# n == dist.length == speed.length
# 1 <= n <= 10 ** 5
# 1 <= dist[i], speed[i] <= 10 ** 5
from random import randint
from math import ceil


def eliminate_max(dist: list[int], speed: list[int]) -> int:
    # working_sol (68.73%, 99.48%) -> (694ms, 30.5mb)  time: O(n * log n) | space: O(n)
    if len(dist) == 1:
        return 1
    # Essentially all we care is when more than 1 monster arrive at the same time.
    # Or within interval of 1 minute, because:
    # ! If a monster reaches the city at the exact moment the weapon is fully charged, it counts as a loss !
    arrival: list[int] = []
    for x in range(len(dist)):
        arrival.append(ceil(dist[x] / speed[x]))
    arrival.sort()
    # ! 1 <= dist[i], speed[i] <= 10 ** 5 ! <- we can always kill first.
    # And after killing we're always at 1 minute mark.
    arrival[0] = 1
    eliminations: int = 1
    # Time we have before next monster arrives.
    time_before: int = 0
    for x in range(1, len(arrival)):
        time_before += arrival[x] - arrival[x - 1]
        # We need at least 1 minute, rule above.
        if not time_before:
            break
        # We can shoot and need 1 minute to reload.
        time_before -= 1
        eliminations += 1
    return eliminations


# Time complexity: O(n * log n) -> calc arrival times for every monster => O(n) ->
# n - len of input arrays 'dist'|'speed'^^| -> sorting them in ascending order => O(n * log n) ->
#                                           -> worst case == we can kill all -> extra traverse of 'n' elements to get
#                                           all monsters we can kill => O(n).
# Auxiliary space: O(n) -> creating list 'arrival' with all arrival times with size equal to inputs => O(n).


test_dist: list[int] = [1, 3, 4]
test_speed: list[int] = [1, 1, 1]
test_out: int = 3
assert test_out == eliminate_max(test_dist, test_speed)

test_dist = [1, 1, 2, 3]
test_speed = [1, 1, 1, 1]
test_out = 1
assert test_out == eliminate_max(test_dist, test_speed)

test_dist = [3, 2, 4]
test_speed = [5, 3, 2]
test_out = 1
assert test_out == eliminate_max(test_dist, test_speed)

test_dist = [1, 3, 3, 3]
test_speed = [5, 1, 1, 1]
test_out = 3
assert test_out == eliminate_max(test_dist, test_speed)

test_dist = [4, 2, 3]
test_speed = [2, 1, 1]
test_out = 3
assert test_out == eliminate_max(test_dist, test_speed)

test_dist = [3, 5, 7, 4, 5]
test_speed = [2, 3, 6, 3, 2]
test_out = 2
assert test_out == eliminate_max(test_dist, test_speed)

test_dist = [randint(1, 10 ** 5) for _ in range(10 ** 3)]
test_speed = [randint(1, 10 ** 5) for _ in range(10 ** 3)]
print(test_dist)
print('==================!')
print(test_speed)
