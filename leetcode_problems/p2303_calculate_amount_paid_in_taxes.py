# You are given a 0-indexed 2D integer array brackets where brackets[i] = [upperi, percenti]
#  means that the ith tax bracket has an upper bound of upperi and is taxed at a rate of percenti.
# The brackets are sorted by upper bound (i.e. upperi-1 < upperi for 0 < i < brackets.length).
# Tax is calculated as follows:
#  - The first upper0 dollars earned are taxed at a rate of percent0.
#  - The next upper1 - upper0 dollars earned are taxed at a rate of percent1.
#  - The next upper2 - upper1 dollars earned are taxed at a rate of percent2.
#  - And so on.
# You are given an integer income representing the amount of money you earned.
# Return the amount of money that you have to pay in taxes.
# Answers within 10 ** -5 of the actual answer will be accepted.
# --------------------------
# 1 <= brackets.length <= 100
# 1 <= upperi <= 1000
# 0 <= percenti <= 100
# 0 <= income <= 1000
# upperi is sorted in ascending order.
# All the values of upperi are unique.
# The upper bound of the last tax bracket is greater than or equal to income.


def calculate_tax(brackets: list[list[int]], income: int) -> float:
    # working_sol (57.98%, 36.96%) -> (71ms, 16.63mb)  time: O(n) | space: O(1)
    out: float = 0.0
    # `income` <- upper bound we should pay taxes with.
    prev_pay: int = 0
    for tax_money, tax_rate in brackets:
        cur_pay: int = min(tax_money, income)
        out += (cur_pay - prev_pay) * (tax_rate / 100)
        prev_pay = cur_pay
    return out


# Time complexity: O(n) <- n - length of the input array `brackets`.
# Always using every pair from `brackets` => O(n).
# --------------------------
# Auxiliary space: O(1)
# Only 2 constant INTs and FLOAT used, none of them depends on input => O(1).


test: list[list[int]] = [[3, 50], [7, 10], [12, 25]]
test_income: int = 10
test_out: float = 2.65000
assert test_out == calculate_tax(test, test_income)

test = [[1, 0], [4, 25], [5, 50]]
test_income = 2
test_out = 0.25000
assert test_out == calculate_tax(test, test_income)

test = [[2, 50]]
test_income = 0
test_out = 0.00000
assert test_out == calculate_tax(test, test_income)
