# There are n balls on a table, each ball has a color black or white.
# You are given a 0-indexed binary string s of length n,
#  where 1 and 0 represent black and white balls, respectively.
# In each step, you can choose two adjacent balls and swap them.
# Return the minimum number of steps to group all the black balls to the right
#  and all the white balls to the left.
# -----------------------
# 1 <= n == s.length <= 10 ** 5
# s[i] is either '0' or '1'.


def minimum_steps(s: str) -> int:
    # working_sol (66.87%, 54.03%) -> (94ms, 17.52mb)  time: O(s) | space: O(1)
    # W.e the ball we start moving left -> right.
    # Every ball of another color will be used only once.
    # Because we can move only adjacent balls.
    # Black balls we meet will be move to the right-most position it need
    #  and it's place will be taken by white ball == 1 move.
    out: int = 0
    zeroes: int = 0
    for index in range(len(s) - 1, -1, -1):
        if '0' == s[index]:
            zeroes += 1
        else:
            out += zeroes
    return out


# Time complexity: O(s)
# Always traversing whole input string `s`, once => O(s).
# # -----------------------
# Auxiliary space: O(1)
# Only 2 constant INTs used, none of them depends on input => O(1).


test: str = "101"
test_out: int = 1
assert test_out == minimum_steps(test)

test = "100"
test_out = 2
assert test_out == minimum_steps(test)

test = "0111"
test_out = 0
assert test_out == minimum_steps(test)
