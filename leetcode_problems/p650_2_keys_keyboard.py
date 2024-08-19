# There is only one character 'A' on the screen of a notepad.
# You can perform one of two operations on this notepad for each step:
#  - Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
#  - Paste: You can paste the characters which are copied last time.
# Given an integer n, return the minimum number of operations to get the character 'A'
#  exactly n times on the screen.
# ---------------------------
# 1 <= n <= 1000
from functools import cache


def min_steps(n: int) -> int:
    # working_sol (53.19%, 12.98%) -> (131ms, 34.29mb)  time: O(n * n) | space: O(n * n)
    if 1 == n:
        return 0

    @cache
    def check(cur_screen: int, prev_screen: int) -> int:
        if n < cur_screen:
            return 1_000_000
        if n == cur_screen:
            return 0
        # copy the whole string and use it.
        copy_opt: int = 2 + check(cur_screen * 2, cur_screen)
        # add already copied string to the current one.
        paste_opt: int = 1 + check(cur_screen + prev_screen, prev_screen)
        return min(copy_opt, paste_opt)

    return 1 + check(1, 1)


# Time complexity: O(n * n).
# `cur_screen` and `prev_screen` both can have values from `1 -> n` inclusive.
# And we check every combination of them => O(n * n).
# ---------------------------
# Auxiliary space: O(n * n)
# Every option we check is cached with `cache` => O(n * n).


test: int = 3
test_out: int = 3
assert test_out == min_steps(test)

test = 1
test_out = 0
assert test_out == min_steps(test)
