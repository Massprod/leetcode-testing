# You are given a circular array balance of length n,
#  where balance[i] is the net balance of person i.
# In one move, a person can transfer exactly 1 unit of balance
#  to either their left or right neighbor.
# Return the minimum number of moves required so that every person
#  has a non-negative balance. If it is impossible, return -1.
# Note: You are guaranteed that at most 1 index has a negative balance initially.
# --- --- --- ---
# 1 <= n == balance.length <= 10 ** 5
# -10 ** 9 <= balance[i] <= 10 ** 9
# There is at most one negative value in balance initially.
from random import randint
from pyperclip import copy


def min_moves(balance: list[int]) -> int:
    # working_solution: (79.02%, 98.69%) -> (55ms, 29.38mb)  Time: O(n) Space: O(1)
    change_val: int
    # Desc:
    # Take everything from both sides, until we can.
    # And if we got a positive sum => we can balance it out.
    # ---
    s_sum: int = sum(balance)
    # Can't be balanced.
    if 0 > s_sum:
        return -1
    neg_index: int = 0
    for index in range(len(balance)):
        if 0 > balance[index]:
            neg_index = index
            break
    # Array is circular.
    left_index: int = len(balance) - 1 if 0 > (neg_index - 1)  else neg_index - 1
    right_index: int = 0 if len(balance) <= (neg_index + 1) else neg_index + 1
    cur_step: int = 1
    out: int = 0
    while left_index != right_index and 0 > balance[neg_index]:
        if 0 < balance[left_index]:
            change_val = min(balance[left_index], balance[neg_index] * -1)
            balance[left_index] -= change_val
            balance[neg_index] += change_val
            out += change_val * cur_step
            continue
        if 0 < balance[right_index]:
            change_val = min(balance[right_index], balance[neg_index] * -1)
            balance[right_index] -= change_val
            balance[neg_index] += change_val
            out += change_val * cur_step
            continue
        # If both already exhausted, we move to the next option
        left_index = len(balance) - 1 if 0 > (left_index - 1) else left_index - 1
        right_index = 0 if len(balance) <= (right_index + 1) else right_index + 1
        cur_step += 1
    
    # TODO: we can make loop better, but for now it's ok to extra check.
    # We still have something to delete.
    if left_index == right_index and 0 > balance[neg_index]:
        change_val = min(balance[left_index], balance[neg_index] * -1)
        balance[right_index] -= change_val
        balance[neg_index] += change_val
        out += change_val * cur_step
    # We know that we can balance, but it's better to extra check :)
    return -1 if 0 > balance[neg_index] else out


# Time complexity: O(n)
# n - length of the input array `balance`.
# Always traversing the whole input array `balance`, three times => O(3 * n).
# --- --- --- ---
# Space complexity: O(1)


test: list[int] = [5, 1, -4]
test_out: int = 4
assert test_out == min_moves(test)

test = [1, 2, -5, 2]
test_out = 6
assert test_out == min_moves(test)

test = [-3, 2]
test_out = -1
assert test_out == min_moves(test)

test = [randint(0, 10 ** 9) for _ in range(10 ** 5)]
test[randint(0, len(test) - 1)] *= -1
copy(test)  # type: ignore
