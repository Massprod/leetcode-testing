# Given an integer n (in base 10) and a base k,
#  return the sum of the digits of n after converting n from base 10 to base k.
# After converting, each digit should be interpreted as a base 10 number,
#  and the sum should be returned in base 10.
# ---------------------
# 1 <= n <= 100
# 2 <= k <= 10


def sum_base(n: int, k: int) -> int:
    # working_sol (42.60%, 79.19%) -> (36ms, 16.42mb)  time: O(n) | space: O(1)
    if 10 == k:
        return sum([int(digit) for digit in str(n)])
    new_digit: int
    new_base: str = ''
    while n:
        new_digit = n % k
        new_base = str(new_digit) + new_base
        n //= k
    old_base: int = int(new_base)
    out: str = ''
    while old_base:
        new_digit = old_base % 10
        out = str(new_digit) + out
        old_base //= 10
    return sum([int(digit) for digit in out])


# Time complexity: O(n)
# Always depleting `n` to 0 => O(n).
# ---------------------
# Auxiliary space: O(1).


test_n: int = 34
test_k: int = 6
test_out: int = 9
assert test_out == sum_base(test_n, test_k)

test_n = 10
test_k = 10
test_out = 1
assert test_out == sum_base(test_n, test_k)
