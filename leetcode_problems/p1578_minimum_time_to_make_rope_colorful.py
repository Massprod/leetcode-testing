# Alice has n balloons arranged on a rope.
# You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.
# Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color,
#  so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful.
# You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds)
#   that Bob needs to remove the ith balloon from the rope.
# Return the minimum time Bob needs to make the rope colorful.
# ------------------
# n == colors.length == neededTime.length
# 1 <= n <= 10 ** 5
# 1 <= neededTime[i] <= 10 ** 4
# colors contains only lowercase English letters.
from random import choice, randint
from string import ascii_lowercase


def min_cost(colors: str, neededTime: list[int]) -> int:
    # working_sol (99.80%, 8.18%) -> (739ms, 28.3mb)  time: O(n) | space: O(1)
    # Greedy logic:
    # We only care about deleting same colors, and only balloons with the lowest cost.
    # So, we can just remember balloon with the highest delete cost and delete everything with lower cost.
    # Balloon with the highest time cost, and current color.
    point_1: int = 0
    # Color for whom we have streak of balloons.
    cur_color: str = ''
    out: int = 0
    for index, color in enumerate(colors):
        # New streak => new color, new highest cost
        if color != cur_color:
            point_1, cur_color = index, color
        # Same color, but lower cost => just delete.
        elif neededTime[index] < neededTime[point_1]:
            out += neededTime[index]
        # Same color, but higher cost => update the highest cost.
        else:
            out += neededTime[point_1]
            point_1 = index
    return out


# Time complexity: O(n) <- n - length of input string `colors` or array `neededTime`, same size.
# Traversing original input string `colors` only once => O(n).
# Auxiliary space: O(1).
# Only 2 extra INTs + 1 STRING but with constant size of 1-symbol, none of them depends on input => O(1).


test: str = "abaac"
test_time: list[int] = [1, 2, 3, 4, 5]
test_out: int = 3
assert test_out == min_cost(test, test_time)

test = "abc"
test_time = [1, 2, 3]
test_out = 0
assert test_out == min_cost(test, test_time)

test = "aabaa"
test_time = [1, 2, 3, 4, 1]
test_out = 2
assert test_out == min_cost(test, test_time)

test = ''.join([choice(ascii_lowercase) for _ in range(10 ** 4)])
test_time = [randint(1, 10 ** 4) for _ in range(10 ** 4)]
print(test)
print('!!!!!!!!!!!-')
print(test_time)
