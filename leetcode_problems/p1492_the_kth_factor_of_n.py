# You are given two positive integers n and k. A factor of an integer n is defined
#       as an integer i where n % i == 0.
# Consider a list of all factors of n sorted in ascending order,
#       return the kth factor in this list or return -1 if n has less than k factors.
# --------------------
# 1 <= k <= n <= 1000
# Follow up:
# Could you solve this problem in less than O(n) complexity?


def kth_factor(n: int, k: int) -> int:
    # working_sol (81.66%, 67.78%) -> (43, 16.3mb)  time: O(n) | space: O(1)
    if k == 1:
        return 1
    factor_count: int = 1
    for x in range(2, n + 1):
        if n % x == 0:
            factor_count += 1
        if factor_count == k:
            return x
    return -1


# Time complexity: O(n) -> in the worst case, there's no kth factor, so we're doing full (2 to n + 1) loop => O(n).
# n - input_value of n^^|
#                  Θ(log n) -> on media it's breaking on some part of the loop from (2 to n + 1) => O(log n).
#                  Ω(1) -> k == 1, insta return.
# Auxiliary space: O(1) -> one extra constant INT, doesn't depend on input => O(1).
# !
# But, for larger values of n there will come a point where this approach is faster than the brute-force loop. !
# Only found some stack_overflow topic about this, and even there's brute_force is better in most cases. Hmm.
# --------------------
# No idea about big_math methods to solve this, but basic is to loop from 1 - n and calc n % value == 0,
# and count every factor we find. Return factor on encounter counter == k.
# On median, it should be less than O(n), but they want us to do this as worst case O(n) ->
# guess I will fail TimeLimit, and only after that, search for this less than O(n) solution.


test1 = 12
test1_k = 3
test1_out = 3
assert test1_out == kth_factor(test1, test1_k)

test2 = 7
test2_k = 2
test2_out = 7
assert test2_out == kth_factor(test2, test2_k)

test3 = 4
test3_k = 4
test3_out = -1
assert test3_out == kth_factor(test3, test3_k)
