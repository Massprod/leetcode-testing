# You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B',
#  representing the color of the ith block.
# The characters 'W' and 'B' denote the colors white and black, respectively.
# You are also given an integer k, which is the desired number of consecutive black blocks.
# In one operation, you can recolor a white block such that it becomes a black block.
# Return the minimum number of operations needed such that there is at least one
#   occurrence of k consecutive black blocks.
# --------------------------
# n == blocks.length
# 1 <= n <= 100
# blocks[i] is either 'W' or 'B'.
# 1 <= k <= n
from random import choice

from pyperclip import copy


def minimum_recolors(blocks: str, k: int) -> int:   
    # working_sol (100.00%, 62.29%) -> (0ms, 17.76mb)  time: O(n) | space: O(1)
    w_sign: str = 'W'
    w_count: int = 0
    b_count: int = 0
    
    def count_sign(sign: str, add: bool = True) -> None:
        nonlocal w_count, b_count, w_sign
        if w_sign == sign:
            w_count += 1 if add else -1
        else:
            b_count += 1 if add else -1
    
    left_l: int = 0
    right_l: int = k
    for index in range(right_l):
        count_sign(blocks[index])
    # We can have more `black` then we get negative.
    # Or we're going to have amount we need to color, positive.
    out: int = max(0, k - b_count)
    while right_l < len(blocks):
        count_sign(blocks[left_l], False)
        left_l += 1
        count_sign(blocks[right_l])
        right_l += 1
        out = min(out, max(0, k - b_count))

    return out


# Time complexity: O(n) <- n - length of the input string `blocks`
# Always traversing whole input string `blocks`, once => O(n).
# --------------------------
# Auxiliary space: O(1)
# Only 6 constant INTs are used => O(1).


test: str = 'WBBWWBBWBW'
test_k: int = 7
test_out: int = 3
assert test_out == minimum_recolors(test, test_k)

test = 'WBWBBBW'
test_k = 2
test_out = 0
assert test_out == minimum_recolors(test, test_k)

test = ''.join([choice(['W', 'B']) for _ in range(100)])
copy(test)
