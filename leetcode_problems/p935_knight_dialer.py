# The chess knight has a unique movement, it may move two squares vertically and one square horizontally,
#  or two squares horizontally and one square vertically (with both forming the shape of an L).
# ---------------------
# Given an integer n, return how many distinct phone numbers of length n we can dial.
# You are allowed to place the knight on any numeric cell initially and then you should perform
#  n - 1 jumps to dial a number of length n.
# All jumps should be valid knight jumps.
# As the answer may be very large, return the answer modulo 10 ** 9 + 7.
# ----------------
# 1 <= n <= 5000


def knight_dialer(n: int) -> int:
    # working_sol (35.83%, 15.56%) -> (2038ms, 86.8mb)  time: O(n) | space: O(n)
    recur_cache: dict[tuple[int, int], int] = {}
    # {cell: [cells we can reach from it]}
    options: dict[int, list[int]] = {
        1: [8, 6],
        2: [7, 9],
        3: [4, 8],
        4: [3, 9, 0],
        5: [],
        6: [1, 7, 0],
        7: [2, 6],
        8: [1, 3],
        9: [4, 2],
        0: [4, 6],
    }

    def dfs(jumps_left: int, cur_cell: int) -> int:
        if not jumps_left:
            return 1
        if (jumps_left, cur_cell) in recur_cache:
            return recur_cache[jumps_left, cur_cell]
        dials: int = 0
        for option in options[cur_cell]:
            dials += dfs(jumps_left - 1, option)
        recur_cache[jumps_left, cur_cell] = dials
        return dials

    out: int = 0
    for cell in range(10):
        # ! you should perform n - 1 jumps to dial a number of length n !
        out += dfs(n - 1, cell)
    return out % (10 ** 9 + 7)


# Time complexity: O(n) -> due to memorization we only calculate every state once, but we have 10 starting cells =>
# n - input value 'n'^^|   => O(10 * n).
# Auxiliary space: O(n) -> using dict 'recur_cache' to memorize every state we calculated + recursion stack is at max
#                          will have only 'n' calls => O(2n).


test: int = 1
test_out: int = 10
assert test_out == knight_dialer(test)

test = 2
test_out = 20
assert test_out == knight_dialer(test)

test = 500
test_out = 84202957
assert test_out == knight_dialer(test)
