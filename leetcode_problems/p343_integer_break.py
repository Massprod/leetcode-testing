# Given an integer n, break it into the sum of k positive integers, where k >= 2,
#  and maximize the product of those integers.
# Return the maximum product you can get.
# ----------------------
# 2 <= n <= 58


def integer_break(n: int) -> int:
    # working_sol (75.93%, 58.98%) -> (37ms, 16.26mb)  time: O(n * n) | space: O(n)
    recur_cache: dict[int, int] = {}

    def check(num: int) -> int:
        # ((3 - 2) * 3) highest, no reasons to check.
        if num <= 3:
            return num
        if num in recur_cache:
            return recur_cache[num]
        max_: int = num
        for x in range(2, num):
            max_ = max(max_, x * check(num - x))
        recur_cache[num] = max_
        return max_
    # 3 -> 2 * 1 == 3, 1 * 1 == 2.
    # 1 can't be split == 0.
    if n <= 3:
        return n - 1
    return check(n)


# Time complexity: O(n * n) -> 'n' states and for every state loop (2 -> n) => O(n * n).
# n - input value 'n'^^|
# Auxiliary space: O(n) -> dictionary with all 'n' states => O(n) -> extra stack with same size in worst case => O(n).
# ----------------------
# Skip <= 3, cuz it always the same.
# No reasons to check (num - 1) -> we can always get at least num as product from EVEN and num + 1 from ODD:
# 4 -> 2 + 2 => 2 * 2 == 4
# 5 -> 2 + 3 => 2 * 3 == 6.
# So just check everything from (2 -> num) and use highest.


test: int = 2
test_out: int = 1
assert test_out == integer_break(test)

test = 10
test_out = 36
assert test_out == integer_break(test)
