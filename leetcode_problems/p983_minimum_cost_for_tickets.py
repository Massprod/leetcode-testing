# You have planned some train traveling one year in advance.
# The days of the year in which you will travel are given as an integer array days.
# Each day is an integer from 1 to 365.
# Train tickets are sold in three different ways:
#  - a 1-day pass is sold for costs[0] dollars,
#  - a 7-day pass is sold for costs[1] dollars, and
#  - a 30-day pass is sold for costs[2] dollars.
# The passes allow that many days of consecutive travel.
#  - For example, if we get a 7-day pass on day 2,
#    then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
# Return the minimum number of dollars you need to travel every day
#  in the given list of days.
# ----------------------------
# 1 <= days.length <= 365
# 1 <= days[i] <= 365
# days is in strictly increasing order.
# costs.length == 3
# 1 <= costs[i] <= 1000


def min_cost_tickets(days: list[int], costs: list[int]) -> int:
    # working_sol (80.42%, 6.91%) -> (3ms, 18.42mb)  time: O(n) | space: O(n)
    # { day: min_cost }
    cache: dict[int, int] = {}
    needs_travel: set[int] = set(days)

    def dp(cur_day: int) -> int:
        nonlocal costs
        # Already finished travel.
        if cur_day > days[-1]:
            return 0
        # We don't need a pass, because we're not traveling on this day.
        if cur_day not in needs_travel:
            return dp(cur_day + 1)
        # Already visited.
        if cur_day in cache:
            return cache[cur_day]
        
        one_day_pass: int = costs[0] + dp(cur_day + 1)
        seven_days_pass: int = costs[1] + dp(cur_day + 7)
        thirty_days_pass: int = costs[2] + dp(cur_day + 30)
        # We need minimum cost.
        cache[cur_day] = min(
            one_day_pass,
            seven_days_pass,
            thirty_days_pass
        )
        return cache[cur_day]
    
    return dp(days[0])


# Time complexity: O(n) <- n - length of the input array `days`.
# `needs_travel` <- traversing `days` to get all days on which we need to travel.
# We're always calculating states of all the starting days from `days` => O(n).
# ----------------------------
# Auxiliary space: O(n)
# `cache` <- allocates space for all calculated states => O(n).
# `needs_travel` <- allocates space for each day from `days` => O(2 * n).
# Recursion stack is at man == `n`, if we have 0 -> `n` travel needed => O(3 * n).


test: list[int] = [1, 4, 6, 7, 8, 20]
test_costs: list[int] = [2, 7, 15]
test_out: int = 11
assert test_out == min_cost_tickets(test, test_costs)

test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31]
test_costs = [2, 7, 15]
test_out = 17
assert test_out == min_cost_tickets(test, test_costs)
