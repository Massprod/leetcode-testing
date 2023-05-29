# There are n gas stations along a circular route, where the amount of gas at the ith station is *gas[i]*.
#  You have a car with an unlimited gas tank, and it costs *cost[i]* of gas to travel from the ith station
# to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
#  Given two integer arrays gas and cost, return the starting gas station's index
# if you can travel around the circuit once in the clockwise direction, otherwise return -1.
#  If there exists a solution, it is guaranteed to be unique.
# -----------------------
# n == gas.length == cost.length  ,  1 <= n <= 105  ,  0 <= gas[i], cost[i] <= 104


def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    pass


test1_gas = [1, 2, 3, 4, 5]
test1_cost = [3, 4, 5, 1, 2]
test1_out = 3

test2_gas = [2, 3, 4]
test2_cost = [3, 4, 3]
test2_out = -1
