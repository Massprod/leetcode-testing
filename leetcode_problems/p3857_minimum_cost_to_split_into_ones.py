# You are given an integer n.
# In one operation, you may split an integer x into two positive integers a and b
#  such that a + b = x.
# The cost of this operation is a * b.
# Return an integer denoting the minimum total cost required
#  to split the integer n into n ones.
# --- --- --- ---
# 1 <= n <= 500


def min_cost(n: int) -> int:
    # working_solution: (37.27%, 64.72%) -> (3ms, 19.24mb)  Time: O(n) Space: O(1)
    # Best approach is to always split into `1 * (n - 1)`
    out: int = 0
    while 1 != n:
        a, b = 1, n - 1
        out += a * b
        n -= 1
    
    return out


# Time complexity: O(n)
# --- --- --- ---
# Space complexity: O(1)


test: int = 3
test_out: int = 3
assert test_out == min_cost(test)

test = 4
test_out = 6
assert test_out == min_cost(test)
