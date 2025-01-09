# You have n boxes. You are given a binary string boxes of length n,
#  where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.
# In one operation, you can move one ball from a box to an adjacent box.
# Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so,
#  there may be more than one ball in some boxes.
# Return an array answer of size n, where answer[i] is the minimum number of operations
#  needed to move all the balls to the ith box.
# Each answer[i] is calculated considering the initial state of the boxes.
# ------------------------
# n == boxes.length
# 1 <= n <= 2000
# boxes[i] is either '0' or '1'.
import pyperclip
from random import choice


def min_operations(boxes: str) -> list[int]:
    # working_sol (73.15%, 41.05%) -> (9ms, 17.83mb)  time: O(n) | space: O(n)
    out: list[int] = []
    # Every ball we have after the current cell.
    # We will have to make an extra swap to place it in the current cell.
    # So, we need to count how many balls after cell == `suffix_balls`.
    suffix_balls: int = 0
    suffix_actions: int = 0
    # We don't need a `0` index.
    for box in boxes[-1:0:-1]:
        suffix_balls += int(box)
        suffix_actions += suffix_balls
    # Because `0` index only uses suffix
    out.append(suffix_actions)
    # Same for the prefix.
    prefix_balls: int = int(boxes[0])
    prefix_actions: int = prefix_balls
    for box in boxes[1:]:
        cur_balls: int = int(box)
        # Every step we make.
        # We will need 1 less swap for all balls on the right side.
        suffix_actions -= suffix_balls
        # And we need to maintain count of balls on the right side.
        suffix_balls -= cur_balls
        out.append(
            suffix_actions + prefix_actions
        )
        # Every extra ball == new swap for this ball.
        prefix_balls += cur_balls
        prefix_actions += prefix_balls
    
    return out


# Time complexity: O(n) <- n - length of the input string `boxes`.
# Always traversing whole input string, twice => O(2 * n).
# ------------------------
# Auxiliary space: O(n)
# `out` <- allocates space for each index of `boxes` => O(n).


test: str = "110"
test_out: list[int] = [1, 1, 3]
assert test_out == min_operations(test)

test = "001011"
test_out = [11, 8, 5, 4, 3, 4]
assert test_out == min_operations(test)

test = ''.join([choice(['0', '1']) for _ in range(2000)])
pyperclip.copy(test)
