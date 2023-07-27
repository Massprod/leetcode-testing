# You have n computers. You are given the integer n and a 0-indexed integer array batteries
#   where the ith battery can run a computer for batteries[i] minutes.
# You are interested in running all n computers simultaneously using the given batteries.
# Initially, you can insert at most one battery into each computer.
# After that and at any integer time moment, you can remove a battery from a computer
#   and insert another battery any number of times.
# The inserted battery can be a totally new battery or a battery from another computer.
# You may assume that the removing and inserting processes take no time.
#
# Note that the batteries cannot be recharged.
#
# Return the maximum number of minutes you can run all the n computers simultaneously.
# ----------------------
# 1 <= n <= batteries.length <= 10 ** 5
# 1 <= batteries[i] <= 10 ** 9
from random import randint


def max_run_time(n: int, batteries: list[int]) -> int:
    # working_sol (46.99%, 77.11%) -> (1871ms, 30.3mb)  time: O((log m) * n) | space: O(1)
    left_l: int = 1
    right_l: int = sum(batteries) // n

    def energy_per_pc(max_per_pc: int) -> int:
        all_energy: int = 0
        for bat in batteries:
            all_energy += min(max_per_pc, bat)
        per_pc: int = all_energy // n
        return per_pc

    while left_l < right_l:
        middle: int = ((left_l + right_l) // 2) + 1
        if energy_per_pc(middle) >= middle:
            left_l = middle
            continue
        right_l = middle - 1

    return left_l


# Time complexity: O((log m) * n) -> standard binary search time for range of m =>  O(log m) ->
# n - len of input_array^^|      -> and for each search attempt we're going to traverse whole input_array, once => O(n)
# m - binary search limit^^|     -> O((log m) * n)
# Auxiliary space: O(1) -> only constants used, and energy_per_pc taking constant and reusing input_array(batteries) ->
#                          -> it's only constant space taken for every operation, no matter the input => O(1).
# ----------------------
# Ok. Same binary search problem as p1870, but now we need to decide on what limit of batteries we can use.
# For n computers we can just take sum(batteries) and divide == max_value for every computer to run.
# So we're getting maximum usage of every battery per pc.
# Like 2pc -> [3, 3, 3] use 3 + 3 and switch between last one once for each to get 4h + 4h and 1h left, cuz
# we can't run part of pcs, always all of them or nothing. That's why we need floor division and there could be needed
# extra check to number of batteries and pc cuz we can't run more pc's than batteries but ->
# -> ! 1 <= n <= batteries.length <= 10 ** 5 ! -> ignoring this.
# Now we need to find maximum value we can use until we still have enough energy to run ALL pc's ->
# -> batteries can be [10, 1, 2, 3, 4, 5] and we're already searching like -> what if we use MIDDLE energy per pc? ->
# -> so we can't use MORE than that, but we can use LESS because otherwise it's simply incorrect value for a cur_bat ->
# -> that's why we need to min(max_per_pc, bat) -> summarizing this gives us ALL_ENERGY we can get from batteries,
# with set limit per pc to MIDDLE -> so if there's energy left, we can try and use higher_limit until we run out
# of energy -> or make right limit lower and search for lower_limit.


test1 = [3, 3, 3]
test1_n = 2
test1_out = 4
assert test1_out == max_run_time(test1_n, test1)

test2 = [1, 1, 1, 1]
test2_n = 2
test2_out = 2
assert test2_out == max_run_time(test2_n, test2)

test: list[int] = []
for _ in range(10 ** 3):
    test.append(randint(1, 10 ** 9))
print(test)
