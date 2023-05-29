# There are *n* gas stations along a circular route, where the amount of gas at the *ith* station is *gas[i]*.
# You have a car with an unlimited gas tank, and it costs *cost[i]* of gas to travel from the ith station
# to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
# Given two integer arrays *gas* and *cost*, return the starting gas station's index
# if you can travel around the circuit once in the clockwise direction, otherwise return -1.
# If there exists a solution, it is guaranteed to be unique.
# -----------------------
# n == gas.length == cost.length  ,  1 <= n <= 105  ,  0 <= gas[i], cost[i] <= 104


def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    # working_sol (9.46%, 17.88%) -> (1175ms, 22.3mb)  time: O(n) | space: O(1)
    if sum(gas) < sum(cost):
        return -1
    start: int = 0
    tank: int = 0
    for station in range(len(gas)):
        tank += gas[station] - cost[station]
        if tank < 0:
            start = station + 1
            tank = 0
    if start == len(gas):
        start = start - len(gas)
        return start
    return start


# Time complexity: O(n) -> traversing once whole input_lists to calculate sums => O(n) + O(n) => O(2n) ->
# n - len of input_list^^  -> and traversing indexes of both input_lists once to calc tank => O(n) -> O(3n)
#                          -> for a correct input_lists it's always linear O(n).
# Space complexity: O(1) -> only 2 extra constants used (2 INTs: start, tank) ->
#                          -> for a correct input_lists it's always constant O(1).
# -----------------------
# Failed a lot of commits, but actually made working solution on 1 try.
# Just as always no indication about time they want, better to always try to cull everything from the start.
# But how can I start culling parts of the solution if I don't even know if it's working?
# Either make own tests, or just fail like this...
# -----------------------
# OK. At least this time_limits passed.
# Ok. Forgot to update tank, we're starting new start at (break + 1) station
# -----------------------
# Ok. Totally can't break time_limit just by changing it. What else can we do with path?
# Summarize all path and break on negative gas, by assuming that we have sum(gas) > sum(cost) ->
# -> and assume that somewhere on the way we will just get this gas? ->
# -> like if we don't have a fuel to get from 0 1, but we have correct equals on gas + cost,
#    means there's some gas on the way we can take and still make full circle. How to do this?
# Instead of *current* which I wanted to start from (start + 1 station), start from 0gas - 0cost?
# Either full_circle or nothing, instantly checked by sum(gas) < sum(cost) ->
# -> so yeah, either station cycle will give us enough fuel to make circle ->
# -> or it's going to be gathered somewhere later but 100% enough after check -> no reasons to check both ways.
# -----------------------
# Hmm. If we need to have fuel at least equal to a cost.
# Can we just summarize everything until we hit rock_bottom with empty tank?
# That's already done and if we're not checking from a start to a full circle, how can we get info about other half?
# Like summ of first_half is equal to first_half_costs, but what about other half?
# Ok we can cull other half, because we're already checked that it can be done by sum(gas) < sum(cost)
# Not enough.
# -----------------------
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
assert test1_out == can_complete_circuit(test1_gas, test1_cost)

test2_gas = [2, 3, 4]
test2_cost = [3, 4, 3]
test2_out = -1
print(can_complete_circuit(test2_gas, test2_cost))
assert test2_out == can_complete_circuit(test2_gas, test2_cost)

test3_gas = [6, 5, 4, 3, 2, 0, 8, 9, 10, 5]
test3_cost = [4, 6, 5, 3, 2, 0, 0, 7, 8, 6]
test3_out = 0
print(can_complete_circuit(test3_gas, test3_cost))
assert test3_out == can_complete_circuit(test3_gas, test3_cost)
