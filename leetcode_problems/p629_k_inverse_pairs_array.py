# For an integer array nums, an inverse pair is a pair of integers [i, j]
#  where 0 <= i < j < nums.length and nums[i] > nums[j].
# Given two integers n and k, return the number of different arrays consist
#  of numbers from 1 to n such that there are exactly k inverse pairs.
# Since the answer can be huge, return it modulo 10 ** 9 + 7.
# ------------------
# 1 <= n <= 1000
# 0 <= k <= 1000


def k_inverse_pairs(n: int, k: int) -> int:
    # working_sol (89.29%, 84.29%) -> (183ms, 17.08mb)  time: O(n * k) | space: O(k)
    dp: list[int] = [1] + [0 for _ in range(k)]
    for y in range(n):
        tempo: list[int] = []
        count: int = 0
        for x in range(k + 1):
            count += dp[x]
            if x - y >= 1:
                count -= dp[x - y - 1]
            tempo.append(count)
        dp = tempo
    return dp[k] % (10 ** 9 + 7)


# Time complexity: O(n * k).
# Auxiliary space: O(k)


test_n: int = 3
test_k: int = 0
test_out: int = 1
assert test_out == k_inverse_pairs(test_n, test_k)

test_n = 3
test_k = 1
test_out = 2
assert test_out == k_inverse_pairs(test_n, test_k)
