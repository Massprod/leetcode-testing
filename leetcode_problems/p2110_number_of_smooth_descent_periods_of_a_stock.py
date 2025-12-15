# You are given an integer array prices representing the daily price history of a stock,
#  where prices[i] is the stock price on the ith day.
# A smooth descent period of a stock consists of one or more contiguous days
#  such that the price on each day is lower than the price on the preceding day
#  by exactly 1. The first day of the period is exempted from this rule.
# Return the number of smooth descent periods.
# --- --- --- ---
# 1 <= prices.length <= 10 ** 5
# 1 <= prices[i] <= 10 ** 5


def get_descent_periods(prices: list[int]) -> int:
    # working_solution: (72.76%, 90.30%) -> (55ms, 29.63mb)  Time: O(n) Space: O(1)
    out: int = 1
    streak: int = 1
    for index in range(1, len(prices)):
        if prices[index] == prices[index - 1] -1:
            streak += 1
        else:
            streak = 1
        out += streak

    return out


# Time complexity: O(n)
# n - length of the input array `prices`
# Always traversing the whole input array `prices`, once => O(n).
# --- --- --- ---
# Space complexity: O(1)


test: list[int] = [3, 2, 1, 4]
test_out: int = 7
assert test_out == get_descent_periods(test)

test = [8, 6, 7, 7]
test_out = 4
assert test_out == get_descent_periods(test)

test = [1]
test_out = 1
assert test_out == get_descent_periods(test)
