# Hercy wants to save money for his first car.
# He puts money in the Leetcode bank every day.
# He starts by putting in $1 on Monday, the first day.
# Every day from Tuesday to Sunday, he will put in $1 more than the day before.
# On every subsequent Monday, he will put in $1 more than the previous Monday.
# Given n, return the total amount of money he will have in the Leetcode bank
#  at the end of the nth day.
# --------------------
# 1 <= n <= 1000


def total_money(n: int) -> int:
    # working_sol (74.78%, 40.24%) -> (37ms, 16.2mb)  time: O(n) | space: O(1)
    out: int = 0
    week: int = 1
    while n:
        out += week
        n -= 1
        # Either 6 days or w.e days we need == n.
        for day in range(1, min(n, 6) + 1):
            out += week + day
            n -= 1
        week += 1
    return out


# Time complexity: O(n).
# Calc for every number from n -> 0.
# Auxiliary space: O(1).


test: int = 20
test_out: int = 96
assert test_out == total_money(test)

test = 4
test_out = 10
assert test_out == total_money(test)

test = 10
test_out = 37
assert test_out == total_money(test)
