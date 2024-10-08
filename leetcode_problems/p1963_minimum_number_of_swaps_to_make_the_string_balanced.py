# You are given a 0-indexed string s of even length n.
# The string consists of exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.
# A string is called balanced if and only if:
#  - It is the empty string, or
#  - It can be written as AB, where both A and B are balanced strings, or
#  - It can be written as [C], where C is a balanced string.
# You may swap the brackets at any two indices any number of times.
# Return the minimum number of swaps to make s balanced.
# ------------------------
# n == s.length
# 2 <= n <= 10 ** 6
# n is even.
# s[i] is either '[' or ']'.
# The number of opening brackets '[' equals n / 2, and the number of closing brackets ']' equals n / 2.


def min_swaps(s: str) -> int:
    # working_sol (84.10%, 26.00%) -> (177ms, 29.26mb)  time: O(s) | space: O(s)
    stack: list[str] = []
    unbalanced: int = 0
    for char in s:
        if '[' == char:
            stack.append(char)
            continue
        # We can either close it correctly.
        if stack:
            stack.pop()
        # Or we will need a swap some open brackets later to close it.
        else:
            unbalanced += 1
    # +1 <- for correct value adjustment => (1 unclosed // 2 = 0, but we need 1)
    return (unbalanced + 1) // 2


# Time complexity: O(s)
# Always traversing all chars from `s` => O(s).
# ------------------------
# Auxiliary space: O(s)
# `stack` <- allocates space for each opened bracket, which in the worst case (s // 2) => O(s // 2)


test: str = "][]["
test_out: int = 1
assert test_out == min_swaps(test)

test = "]]][[["
test_out = 2
assert test_out == min_swaps(test)

test = "[]"
test_out = 0
assert test_out == min_swaps(test)
