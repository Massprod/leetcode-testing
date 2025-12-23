# You are given an integer n.
# Define its mirror distance as: abs(n - reverse(n))​​​​​​​ where reverse(n)
#  is the integer formed by reversing the digits of n.
# Return an integer denoting the mirror distance of n​​​​​​​.
# abs(x) denotes the absolute value of x.
# --- --- --- ---
# 1 <= n <= 10 ** 9


def mirror_distance(n: int) -> int:
    # working_solution: (100%, 97.44%) -> (0ms, 17.09mb)  Time: O(n) Space: O(n)
    return abs(n - int(str(n)[::-1]))


# Time complexity: O(n)
# --- --- --- ---
# Space complexity: O(n)


test: int = 25
test_out: int = 27
assert test_out == mirror_distance(test)

test = 10
test_out = 9
assert test_out == mirror_distance(test)

test = 7
test_out = 0
assert test_out == mirror_distance(test)
