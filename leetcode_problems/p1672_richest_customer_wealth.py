# You are given an m x n integer grid accounts where accounts[i][j]
#  is the amount of money the `i` customer has in the `j` bank.
# Return the wealth that the richest customer has.
# A customer's wealth is the amount of money they have in all their bank accounts.
# The richest customer is the customer that has the maximum wealth.
# -----------------------
# m == accounts.length
# n == accounts[i].length
# 1 <= m, n <= 50
# 1 <= accounts[i][j] <= 100
from random import randint


def maximum_wealth(accounts: list[list[int]]) -> int:
    # working_sol (92.55%, 47.60%) -> (46ms, 16.50mb)  time: O(n * m) | space: O(1)
    # `row` => customer | `col` => bank
    out: int = 0
    for customer in range(len(accounts)):
        wealth: int = 0
        for bank in range(len(accounts[0])):
            wealth += accounts[customer][bank]
        out = max(out, wealth)
    return out


# Time complexity: O(n * m) <- n - height of the input matrix `accounts`, m - length of the input matrix `accounts`.
# Always traversing whole input matrix `accounts`, once => O(n * m).
# -----------------------
# Auxiliary space: O(1).
# Only 2 extra constant INTs used, none of them depends on input => O(1).


test: list[list[int]] = [[1, 2, 3], [3, 2, 1]]
test_out: int = 6
assert test_out == maximum_wealth(test)

test = [[1, 5], [7, 3], [3, 5]]
test_out = 10
assert test_out == maximum_wealth(test)

test = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
test_out = 17
assert test_out == maximum_wealth(test)

test = [[randint(1, 100) for _ in range(50)] for _ in range(50)]
print(test)
