# You are given a positive integer n.
# Return the integer obtained by removing all zeros
#  from the decimal representation of n.
# --- --- --- ---
# 1 <= n <= 10 ** 15


def remove_zeros(n: int) -> int:
    # working_solution: (100%, 96.66%) -> (0ms, 17.57mb)  Time: O(n) Space: O(n)
    stack: list[int] = []
    # Get all the digits (in reverse)
    while n:
        digit: int = n % 10
        if digit:
            stack.append(digit)
        n //= 10

    out: int = 0
    while stack:
        out += stack.pop()
        out *= 10
    # Remove the extra 10. Faster than an index check.
    out //= 10
    return out


# Time complexity: O(n)
# In the worst case there's no `0` in the `n`.
# So, we will traverse every digit of the `n`, twice => O(n).
# --- --- --- ---
# Space complexity: O(n)
# `stack` <- allocates space for each digit of the input value `n` => O(n).


test: int = 1_020_030
test_out: int = 123
assert test_out == remove_zeros(test)

test = 1
test_out = 1
assert test_out == remove_zeros(test)
