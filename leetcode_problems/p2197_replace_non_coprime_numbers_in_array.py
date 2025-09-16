# You are given an array of integers nums. Perform the following steps:
#  1. Find any two adjacent numbers in nums that are non-coprime.
#  2. If no such numbers are found, stop the process.
#  3. Otherwise, delete the two numbers and replace them with their LCM (Least Common Multiple).
#  4. Repeat this process as long as you keep finding two adjacent non-coprime numbers.
# Return the final modified array. It can be shown that replacing adjacent
#  non-coprime numbers in any arbitrary order will lead to the same result.
# The test cases are generated such that the values in the final array are less
#  than or equal to 10 ** 8.
# Two values x and y are non-coprime if GCD(x, y) > 1 where GCD(x, y)
#  is the Greatest Common Divisor of x and y.
# --- --- --- ---
# 1 <= nums.length <= 10 ** 5
# 1 <= nums[i] <= 10 ** 5
# The test cases are generated such that the values in the final array are less
#  than or equal to 10 ** 8.
from math import gcd


def replace_non_comprimes(nums: list[int]) -> list[int]:
    # working_solution: (71.74%, 59.78%) -> (121ms, 31.59mb)  Time: O(n) Space: O(n)
    # LCM = A * B / GCD(A, B)
    stack: list[int] = [nums[0]]
    for index in range(1, len(nums)):
        lcm_val: int 
        val1: int = stack[-1]
        val2: int = nums[index]
        gcd_val: int = gcd(val1, val2)
        if not (gcd_val > 1):
            stack.append(val2)
            continue
        lcm_val = (val1 * val2) // gcd_val
        stack.pop()
        while gcd_val > 1 and stack:
            val1 = stack[-1]
            gcd_val = gcd(val1, lcm_val)
            new_lcm_val: int = (val1 * lcm_val) // gcd_val
            if gcd_val > 1:
                stack.pop()
                lcm_val = new_lcm_val
        stack.append(lcm_val)

    return stack


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing the whole input array `nums`, at most twice => O(2 * n).
# --- --- --- ---
# Space complexity: O(n)
# In the worst case, there' 0 `non-coprime` numbers.
# `stack` <- allocates space for each value from the `nums` => O(n).


test: list[int] = [6, 4, 3, 2, 7, 6, 2]
test_out: list[int] = [12, 7, 6]
assert test_out == replace_non_comprimes(test)

test = [2, 2, 1, 1, 3, 3, 3]
test_out = [2, 1, 1, 3]
assert test_out == replace_non_comprimes(test)
