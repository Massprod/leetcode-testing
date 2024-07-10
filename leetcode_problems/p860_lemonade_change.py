# At a lemonade stand, each lemonade costs $5.
# Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills).
# Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.
# You must provide the correct change to each customer
#  so that the net transaction is that the customer pays $5.
# Note that you do not have any change in hand at first.
# Given an integer array bills where bills[i] is the bill the ith customer pays,
#  return true if you can provide every customer with the correct change, or false otherwise.
# --------------------------
# 1 <= bills.length <= 10 ** 5
# bills[i] is either 5, 10, or 20.
from random import choice


def lemonade_change(bills: list[int]) -> bool:
    # working_sol (93.12%, 40.63%) -> (603ms, 21.15mb)  time: O(n) | space: O(1)
    change: dict[int, int] = {
        5: 0,
        10: 0,
        20: 0,
    }
    for bill in bills:
        change[bill] += 1
        to_give: int = bill - 5
        # The Best distribution method is to give the highest bill we have.
        # Because, we can use lower bills to build the higher one, and can't do this in reverse :)
        while change[20] and to_give >= 20:
            to_give -= 20
            change[20] -= 1
        while change[10] and to_give >= 10:
            to_give -= 10
            change[10] -= 1
        while change[5] and to_give >= 5:
            to_give -= 5
            change[5] -= 1
        if 0 != to_give:
            return False
    return True


# Time complexity: O(n) <- n - length of the input array `bills`.
# We're always traversing whole input array `bills` and depleting every value in it if we can,
#  the maximum value is 20, so we can treat as a constant => O(n).
# --------------------------
# Auxiliary space: O(1)
# `change` is always of the same size (3) => O(1).


test: list[int] = [5, 5, 5, 10, 20]
test_out: bool = True
assert test_out == lemonade_change(test)

test = [5, 5, 10, 10, 20]
test_out = False
assert test_out == lemonade_change(test)

test = [5 for _ in range(100)] + [choice([5, 10, 20]) for _ in range(10 ** 3)]
print(test)
