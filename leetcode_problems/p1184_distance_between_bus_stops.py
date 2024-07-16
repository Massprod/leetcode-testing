# A bus has n stops numbered from 0 to n - 1 that form a circle.
# We know the distance between all pairs of neighboring stops where distance[i]
#  is the distance between the stops number i and (i + 1) % n.
# The bus goes along both directions i.e. clockwise and counterclockwise.
# Return the shortest distance between the given start and destination stops.
# ------------------
# 1 <= n <= 10  ** 4
# distance.length == n
# 0 <= start, destination < n
# 0 <= distance[i] <= 10 ** 4
from random import randint


def distance_between_bus_stops(distance: list[int], start: int, destination: int) -> int:
    # working_sol (57.29%, 65.27%) -> (47ms, 17.49mb)  time: O(n) | space: O(1)
    # TODO: change this cringe_fiesta to the normal solution, when im not that tired.
    # All we care is:
    #  start -> left_path -> target.
    #  start -> right_path -> target.
    if start == destination:
        return 0
    out: int | float = float('inf')
    cur_dist: int = 0
    index: int = start
    if start < destination:
        while True:
            cur_dist += distance[index]
            index += 1
            if index == destination:
                out = min(out, cur_dist)
                cur_dist = 0
            if index >= len(distance):
                index = 0
            if index == start:
                out = min(out, cur_dist)
                break
    else:
        while True:
            cur_dist += distance[index - 1]
            index -= 1
            if index == destination:
                out = min(out, cur_dist)
                cur_dist = 0
            if index < 0:
                index = len(distance) - 1
            if index == start:
                out = min(out, cur_dist)
                break
    return out


# Time complexity: O(n) <- n - length of the input array `distance`.
# W.e the case, we're always traversing full circle => O(n).
# ------------------
# Auxiliary space: O(1).


test: list[int] = [1, 2, 3, 4]
test_start: int = 0
test_dest: int = 1
test_out: int = 1
assert test_out == distance_between_bus_stops(test, test_start, test_dest)

test = [1, 2, 3, 4]
test_start = 0
test_dest = 2
test_out = 3
assert test_out == distance_between_bus_stops(test, test_start, test_dest)

test = [1, 2, 3, 4]
test_start = 0
test_dest = 3
test_out = 4
assert test_out == distance_between_bus_stops(test, test_start, test_dest)

test = [randint(0, 10 ** 4) for _ in range(10 ** 4)]
print(test)
