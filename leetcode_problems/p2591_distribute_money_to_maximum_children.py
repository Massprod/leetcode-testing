# You are given an integer money denoting the amount of money (in dollars)
#  that you have and another integer children denoting the number of children that you must distribute the money to.
# You have to distribute the money according to the following rules:
#  - All money must be distributed.
#  - Everyone must receive at least 1 dollar.
#  - Nobody receives 4 dollars.
# Return the maximum number of children who may receive exactly 8 dollars
#  if you distribute the money according to the aforementioned rules.
# If there is no way to distribute the money, return -1.
# ---------------------------
# 1 <= money <= 200
# 2 <= children <= 30
from random import randint


def dist_money(money: int, children: int) -> int:
    # working_sol (26.01%, 99.76%) -> (47ms, 16.38mb)  time: O(n) | space: O(1)
    if money < children:
        return -1
    out: int = 0
    # Trying to give everybody `8` dollars.
    for childs in range(1, children + 1):
        after_distr: int = money - 8
        childs_left: int = children - childs
        # We can at least give a 1 dollar to each left.
        if after_distr >= childs_left:
            out += 1
            money = after_distr
        else:
            childs_left = children - (childs - 1)  # return child, because we can't give him enough
            # We take from sm1 else, who's got `8`.
            if 1 == childs_left and 4 == money:
                out -= 1
            # We give this child, everything what's left.
            money = 0
            break
    # If we have extra money, after we give everyone `8`'s
    #  we should place extra money on some other child with `8`.
    if money > 0:
        out -= 1
    return out


# Time complexity: O(n) <- n - input value of `children`.
# We're always trying to take `n` children and give them all `8` dollars => O(n).
# ---------------------------
# Auxiliary space: O(1)
# Only 3 constant INT's used, none of them depends on input => O(1).


test: int = 20
test_children: int = 3
test_out: int = 1
assert test_out == dist_money(test, test_children)

test = 16
test_children = 2
test_out = 2
assert test_out == dist_money(test, test_children)

test = randint(1, 200)
test_children = randint(2, 30)
print(test, test_children)
