# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# 1 <= n <= 45

def climb_stairs(n: int) -> int:
    # working_sol (11.67%, 27.84%) -> (48ms, 16.2mb)  time: O(n) | space: O(n)
    stairs: list[int] = [1]
    ways: int = 0
    for x in range(1, n + 1):
        double_jump: int = x - 2 - 1
        single_jump: int = x - 1
        if double_jump >= 0:
            ways -= stairs[double_jump]
        ways += stairs[single_jump]
        stairs.append(ways)
    return stairs[-1]

# Time complexity: O(n) -> one for_loop for values from 1 to n + 1 => O(n) ->
#                          -> appending ways to stairs => O(1) -> worst_case O(n)
# Space complexity: O(n) -> constants and creating one list - stairs, with size of n => O(n)

# Flow:
#   Starting with stairs[1] -> there's only one possible way to reach FIRST_STAIR ->
#   -> for every stair number from 1 to n + 1 (to include last_index=n) counting number of possible ways to reach it ->
#   -> if we can make double_jump than it's always going to be more than 0 and value of double_jump
#      is number of stair we can jump from, and it's index of a stair in STAIRS ->
#   -> giving us a value of number of possible ways to reach this stair, which we can add to sum_of_all == ways ->
#   -> same with single jump -> repeating it until we reach n_stair => stairs[-1] == all_ways
#
# ---------------------------
# First solution, is working with recursion but O(2 ** n) is not enough.
# Second solution -> semi_googled, we're counting all possible ways in one loop, similar to matrix_ways before.
# ---------------------------
# From right_to_left, left_to_right leaving us with O(2 ** n) recursion, and both hits time_limit.


test1 = 2
test1_out = 2
print(climb_stairs(test1))
assert test1_out == climb_stairs(test1)

test2 = 3
test2_out = 3
print(climb_stairs(test2))
assert test2_out == climb_stairs(test2)


test3 = 10
test3_out = 89
print(climb_stairs(test3))
assert test3_out == climb_stairs(test3)

# test4 - failed -> time_limit, I did most simple wait and didn't think about task a lot, cuz it's easy.
#                   It's working, but too slow.
test4 = 38
test4_out = 63245986
print(climb_stairs(test4))
assert test4_out == climb_stairs(test4)

test5 = 5
test5_out = 8
print(climb_stairs(test5))
assert test5_out == climb_stairs(test5)
