# Initially, you have a bank account balance of 100 dollars.
# You are given an integer purchaseAmount representing the amount
#  you will spend on a purchase in dollars, in other words, its price.
# When making the purchase, first the purchaseAmount is rounded to the nearest multiple of 10.
# Let us call this value roundedAmount. Then, roundedAmount dollars are removed from your bank account.
# Return an integer denoting your final bank account balance after this purchase.
# Notes:
#  - 0 is considered to be a multiple of 10 in this problem.
#  - When rounding, 5 is rounded upward (5 is rounded to 10, 15 is rounded to 20, 25 to 30, and so on).
# -------------------
# 0 <= purchaseAmount <= 100


def account_balance_after(purchaseAmount: int) -> int:
    # working_sol (92.82%, 66.67%) -> (27ms, 16.44mb)  time: O(1) | space: O(1)
    out: int = 100
    if 0 == purchaseAmount:
        return out
    over: int = purchaseAmount % 10
    if 5 <= over:
        purchaseAmount = (purchaseAmount // 10 + 1) * 10
    else:
        purchaseAmount = purchaseAmount // 10 * 10
    return out - purchaseAmount


# Time complexity: O(1)
# -------------------
# Auxiliary space: O(1)


test: int = 9
test_out: int = 90
assert test_out == account_balance_after(test)

test = 15
test_out = 80
assert test_out == account_balance_after(test)

test = 10
test_out = 90
assert test_out == account_balance_after(test)
