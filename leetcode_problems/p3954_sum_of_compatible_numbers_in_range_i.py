# You are given two integers n and k.
# A positive integer x is called compatible if it satisfies
#  both of the following conditions:
#  - abs(n - x) <= k
#  - (n & x) == 0
# Return the sum of all compatible integers x.
# Note:
#  - Here, & denotes the bitwise AND operator.
#  - The absolute difference between integers i and j is defined as abs(i - j).
# --- --- --- ---
# 1 <= n <= 100
# 1 <= k <= 100


def sum_of_good_integers(n: int, k: int) -> int:
    # working_solution: (100%, 100%) -> (1ms, 19.16mb)  Time: O(n + k) Space: O(1)
    out: int = 0
    for val in range(max(1, n - k), n + k + 1):
        if 0 == (n & val):
            out += val
    
    return out


# Time complexity: O(n + k)
# --- --- --- ---
# Space complexity: O(1)


test_n: int = 2
test_k: int = 3
test_out: int = 10
assert test_out == sum_of_good_integers(test_n, test_k)

test_n = 5
test_k = 1
test_out = 0
assert test_out == sum_of_good_integers(test_n, test_k)
