# You are given a 0-indexed array of strings garbage where garbage[i]
#  represents the assortment of garbage at the ith house.
# garbage[i] consists only of the characters 'M', 'P' and 'G' representing one unit of metal,
#  paper and glass garbage respectively.
# Picking up one unit of any type of garbage takes 1 minute.
# You are also given a 0-indexed integer array travel where travel[i] is the number of minutes
#  needed to go from house i to house i + 1.
# There are three garbage trucks in the city, each responsible for picking up one type of garbage.
# Each garbage truck starts at house 0 and must visit each house in order;
#  however, they do not need to visit every house.
# Only one garbage truck may be used at any given moment.
# While one truck is driving or picking up garbage, the other two trucks cannot do anything.
# Return the minimum number of minutes needed to pick up all the garbage.
# -----------------------
# 2 <= garbage.length <= 10 ** 5
# garbage[i] consists of only the letters 'M', 'P', and 'G'.
# 1 <= garbage[i].length <= 10
# travel.length == garbage.length - 1
# 1 <= travel[i] <= 100
from random import randint, choice


def garbage_collection(garbage: list[str], travel: list[int]) -> int:
    # working_sol (74.87%, 61.98%) -> (861ms, 39.2mb)  time: O(n) | space: O(1)
    # (garbage_type: last_house to visit)
    houses: dict[str, int] = {
        'M': 0,
        'P': 0,
        'G': 0,
    }
    time: int = 0
    for x in range(len(garbage)):
        # ! garbage[i] consists of only the letters 'M', 'P', and 'G' !
        for garbage_type in garbage[x]:
            time += 1
            houses[garbage_type] = x
    for house in houses:
        # travel[h] == (h - 1) -> h, travel cost from (house -> house - 1).
        # '-1' for correct indexing.
        time += sum(travel[:houses[house]])
    return time


# Time complexity: O(n) -> worst case == every truck should visit last house => we will traverse 'garbage' => O(n) ->
# n - len of input array 'garbage'^^| -> extra traverse of the whole 'travel' => O(n + (n - 1)).
# Auxiliary space: O(1) -> dictionary with constant keys, values + one constant INT => O(1).


test_g: list[str] = ["G", "P", "GP", "GG"]
test_t: list[int] = [2, 4, 3]
test_out: int = 21
assert test_out == garbage_collection(test_g, test_t)

test_g = ["MMM", "PGM", "GP"]
test_t = [3, 10]
test_out = 37
assert test_out == garbage_collection(test_g, test_t)

test_g = [choice(['M', 'P', 'G']) for _ in range(10 ** 3)]
test_t = [randint(1, 100) for _ in range((10 ** 3) - 1)]
# print(test_g)
# print('-------!!')
# print(test_t)
