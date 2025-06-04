# You are given integers n, m, and k.
# There are two logs of lengths n and m units,
#  which need to be transported in three trucks where each truck can carry one log
#  with length at most k units.
# You may cut the logs into smaller pieces, where the cost
#  of cutting a log of length x into logs of length len1 and len2
#  is cost = len1 * len2 such that len1 + len2 = x.
# Return the minimum total cost to distribute the logs onto the trucks.
# If the logs don't need to be cut, the total cost is 0.
# ----------------------------
# 2 <= k <= 10 ** 5
# 1 <= n, m <= 2 * k
# The input is generated such that it is always possible to transport the logs.


def min_cutting_cost(n: int, m: int, k: int) -> int:
    # working_sol (100.00%, 23.05%) -> (0ms, 17.96mb)  time: O(1) | space: O(1)
    # Both higher => can't be transported.
    if k < n and k < m:
        return -1
    out: int = 0
    # Both lower => can be transported.
    if k >= n and k >= m:
        return out
    # We need to cut down to size => `k` => len2 == x - len1.
    # cost = (x - len1) * len1 <- len1 == `k`.
    out = (max(n, m) - k) * k
    
    return out


# Time complexity: O(1)
# Always the same check, nothing depends on the input => O(1).
# ----------------------------
# Auxiliary space: O(1)


test_n: int = 6
test_m: int = 5
test_k: int = 5
test_out: int = 5
assert test_out == min_cutting_cost(test_n, test_m, test_k)

test_n = 4
test_m = 4
test_k = 6
test_out = 0
assert test_out == min_cutting_cost(test_n, test_m, test_k)
