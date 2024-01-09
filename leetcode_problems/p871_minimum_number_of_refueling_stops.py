# A car travels from a starting position to a destination which is
#  target miles east of the starting position.
# There are gas stations along the way.
# The gas stations are represented as an array stations where stations[i] = [positioni, fueli]
#  indicates that the ith gas station is positioni miles east of the starting position
#  and has fueli liters of gas.
# The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it.
# It uses one liter of gas per one mile that it drives.
# When the car reaches a gas station, it may stop and refuel,
#  transferring all the gas from the station into the car.
# Return the minimum number of refueling stops the car must make in order to reach its destination.
# If it cannot reach the destination, return -1.
# Note that if the car reaches a gas station with 0 fuel left,
#  the car can still refuel there.
# If the car reaches the destination with 0 fuel left, it is still considered to have arrived.
# ----------------------------
# 1 <= target, startFuel <= 10 ** 9
# 0 <= stations.length <= 500
# 1 <= positioni < positioni+1 < target
# 1 <= fueli < 10 ** 9
import heapq
from random import randint


def min_refuel_stops(target: int, startFuel: int, stations: list[list[int]]) -> int:
    # working_sol (97.46%, 20.76%) -> (100ms, 17.64mb)  time: O(n * log n) | space: O(n)
    if startFuel >= target:
        return 0
    # For the last station == target, we only care about being capable to reach it.
    # So, we need to add it as `station` and w.e fuel.
    stations.append([target, 0])
    visited_stations: list[int] = []
    heapq.heapify(visited_stations)
    out: int = 0
    # Try to visit every station with `startFuel` we currently have.
    for station, (distance, fuel) in enumerate(stations):
        # Fuel we will have after reaching `station`.
        cur_fuel: int = startFuel - distance
        # If we can't reach it with our current level of `startFuel`,
        #  we need to stop and fill at some station.
        # We need minimum, so we can choose `best` option from all previously visited.
        # Filling at these stations until we have enough fuel to reach current `station`.
        while cur_fuel < 0 and visited_stations:
            best: int = heapq.heappop(visited_stations) * -1
            cur_fuel += best
            out += 1
            startFuel += best
        # If we're not capable of filling enough from previous stations, then it's unreachable.
        if cur_fuel < 0:
            return -1
        # Add every station we can visit(reach) with our current fuel `startFuel`,
        #  into a maxHeap to choose best option after.
        heapq.heappush(visited_stations, fuel * -1)
    return out


# Time complexity: O(n * log n) <- n - length of input array `stations`.
# We traverse whole input array `stations` and for each index push current station fuel into a heap.
# Every heappop(), heappush() == (log k) <- k current # of heap elements.
# In the worst case, we will have `n` elements in heap `visited_station` and will try to get enough fuel to
#  reach `target` => O(n * log n).
# ----------------------------
# Auxiliary space: O(n).
# Worst case: we can reach every station except `target`.
# So, every station will be added into a heap `visited_stations` except `target`.
# But target, is extra station we add to check after we visited all others, so it's not in `station` by default => O(n).


test: int = 1
test_fuel: int = 1
test_stations: list[list[int]] = []
test_out: int = 0
assert test_out == min_refuel_stops(test, test_fuel, test_stations)

test = 100
test_fuel = 1
test_stations = [[10, 100]]
test_out = -1
assert test_out == min_refuel_stops(test, test_fuel, test_stations)

test = 100
test_fuel = 10
test_stations = [[10, 60], [20, 30], [30, 30], [60, 40]]
test_out = 2
assert test_out == min_refuel_stops(test, test_fuel, test_stations)

test = 100
test_fuel = 50
test_stations = [[50, 50]]
test_out = 1
assert test_out == min_refuel_stops(test, test_fuel, test_stations)

test = 100
test_fuel = 25
test_stations = [[25, 25], [50, 25], [75, 25]]
test_out = 3
assert test_out == min_refuel_stops(test, test_fuel, test_stations)

test = randint(100, 10 ** 9)
test_fuel = randint(100, 10 ** 9)
test_stations = sorted([[randint(1, test) for _ in range(2)] for _ in range(500)], key=lambda x: x[0])
print(
    f'{test}\n\n'
    f'{test_fuel}\n\n'
    f'{test_stations}'
)
