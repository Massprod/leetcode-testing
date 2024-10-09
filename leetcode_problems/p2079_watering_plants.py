# You want to water n plants in your garden with a watering can. The plants are arranged in a row
#   and are labeled from 0 to n - 1 from left to right where the ith plant is located at x = i.
# There is a river at x = -1 that you can refill your watering can at.
# Each plant needs a specific amount of water.
# You will water the plants in the following way:
#  - Water the plants in order from left to right.
#  - After watering the current plant, if you do not have enough water to completely water the next plant,
#    return to the river to fully refill the watering can.
#  - You cannot refill the watering can early.
# You are initially at the river (i.e., x = -1).
# It takes one step to move one unit on the x-axis.
# Given a 0-indexed integer array plants of n integers,
#  where plants[i] is the amount of water the ith plant needs,
#  and an integer capacity representing the watering can capacity,
#  return the number of steps needed to water all the plants.
# ----------------------------
# n == plants.length
# 1 <= n <= 1000
# 1 <= plants[i] <= 10 ** 6
# max(plants[i]) <= capacity <= 10 ** 9
from random import randint
from collections import deque


def watering_plants(plants: list[int], capacity: int) -> int:
    # working_sol (24.83%, 67.08%) -> (53ms, 16.63mb)  time: O(n) | space: O(n)
    out: int = 0
    distance: int = 0
    que: deque[int] = deque(plants)
    while que:
        water = capacity
        out += distance
        while que and water >= que[0]:
            distance += 1
            water -= que.popleft()
        out += distance
    return out

# Time complexity: O(n) <- n - length of the input array `plants`.
# Converting `plants` to deque => O(n).
# Extra using every value from this deque => O(n + n).
# ----------------------------
# Auxiliary space: O(n)
# `que` <- allocates space for each value from `plants` => O(n).


test: list[int] = [2, 2, 3, 3]
test_capacity: int = 5
test_out: int = 14
assert test_out == watering_plants(test, test_capacity)

test = [1, 1, 1, 4, 2, 3]
test_capacity = 4
test_out = 30
assert test_out == watering_plants(test, test_capacity)

test = [7, 7, 7, 7, 7, 7, 7]
test_capacity = 8
test_out = 49
assert test_out == watering_plants(test, test_capacity)

test = [randint(1, 10 ** 6) for _ in range(1000)]
print(test)
