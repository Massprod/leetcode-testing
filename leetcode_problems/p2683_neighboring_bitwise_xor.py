# A 0-indexed array derived with length n is derived by computing the bitwise XOR (⊕)
#  of adjacent values in a binary array original of length n.
# Specifically, for each index i in the range [0, n - 1]:
#  - If i = n - 1, then derived[i] = original[i] ⊕ original[0].
#  - Otherwise, derived[i] = original[i] ⊕ original[i + 1].
# Given an array derived, your task is to determine whether there exists
#  a valid binary array original that could have formed derived.
# Return true if such an array exists or false otherwise.
#  - A binary array is an array containing only 0's and 1's
# --------------------
# n == derived.length
# 1 <= n <= 10 ** 5
# The values in derived are either 0's or 1's


def does_valid_array_exist(derived: list[int]) -> bool:
    # working_sol (91.24%, 24.82%) -> (24ms, 22.45mb)  time: O(n) | space: O(1) 
    # !
    # The xor-sum of the derived array should be 0
    #  since there is always a duplicate occurrence of each element.
    # !
    return 0 == sum(derived) % 2


# Time complexity: O(n) <- n - length of the input array `derived`
# `sum` traverse whole `derived`, once => O(n).
# --------------------
# Auxiliary space: O(1)


test: list[int] = [1, 1, 0]
test_out: bool = True
assert test_out == does_valid_array_exist(test)

test = [1, 1]
test_out = True
assert test_out == does_valid_array_exist(test)

test = [1, 0]
test_out = False
assert test_out == does_valid_array_exist(test)
