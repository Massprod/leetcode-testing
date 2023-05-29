# There are *n* gas stations along a circular route, where the amount of gas at the *ith* station is *gas[i]*.
# You have a car with an unlimited gas tank, and it costs *cost[i]* of gas to travel from the ith station
# to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
# Given two integer arrays *gas* and *cost*, return the starting gas station's index
# if you can travel around the circuit once in the clockwise direction, otherwise return -1.
# If there exists a solution, it is guaranteed to be unique.
# -----------------------
# n == gas.length == cost.length  ,  1 <= n <= 105  ,  0 <= gas[i], cost[i] <= 104


def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    if sum(gas) < sum(cost):
        return -1
    start: int = 0
    while start != len(gas):
        if gas[start] == 0:
            start += 1
            continue
        if not (gas[start] >= cost[start]):
            start += 1
            continue
        current: int = start + 1
        if current >= len(gas):
            current = current - len(gas)
        tank: int = gas[start] + gas[current] - cost[start]
        while current != start:
            tank -= cost[current]
            if tank < 0:
                break
            current += 1
            if current >= len(gas):
                current = current - len(gas)
            tank += gas[current]
        if current == start:
            return start
        else:
            start += 1
    return -1

# Ok. Still not enough.
# -----------------------
# What to cull? Ok. After I culled 0 gas stations, time limit passed ->
# -> so it's correct we can't move from stations with 0 fuel at least for a cost != 0.
# Bruh. we can just change start to a current after we run out of gas, because we're already passed this path and
# sum of fuel on this whole way is not enough to get to (current + 1) station. Try to cull this.
# -----------------------
# Wow. They actually made this test_cases with 0 costs.
# Hmm, if we summarize costs and gas from stations, like we can't make a full circuit if we don't have
# enough fuel in summ_of_all_stations to do this at least once, w.e position we start doesn't matter.
# -----------------------
# Ok. Failed with time_limit, because didn't consider we can't start from station with 0 fuel.
# But I did check to have more or equal fuel to the cost.
# So if we have 0 fuel on start, and our cost is 0, why we can't move?
# Like we're just starting and moving on the same station, why we're not allowed
# and why cost can be a 0 if we're not allowed to move like this?
# -----------------------
# !
# return the starting gas station's index if you can travel around the circuit once in the clockwise direction. !
# ^^No need to check any betweens or anything just left_to_right checks for index in gas and index + 1 in cost,
#   guess it's medium task only because of overlapping with len(gas) to change index.


test1_gas = [1, 2, 3, 4, 5]
test1_cost = [3, 4, 5, 1, 2]
test1_out = 3
print(can_complete_circuit(test1_gas, test1_cost))

test2_gas = [2, 3, 4]
test2_cost = [3, 4, 3]
test2_out = -1
print(can_complete_circuit(test2_gas, test2_cost))

test3_gas = [6, 5, 4, 3, 2, 0, 8, 9, 10, 5]
test3_cost = [4, 6, 5, 3, 2, 0, 0, 7, 8, 6]
print(can_complete_circuit(test3_gas, test3_cost))
