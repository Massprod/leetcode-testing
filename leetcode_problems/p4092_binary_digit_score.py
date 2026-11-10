# You are given two integers a and b.
# Let s1 and s2 be the number of set bits in the binary representations of a and b, respectively.
# The score of these integers is defined as follows:
#  - If s1 >= s2, the score is s1 * s2.
#  - Otherwise, the score is s2 / s1 using integer division.
# Return an integer representing the score of a and b.
# --- --- --- ---
# 1 <= a, b <= 100


def calculate_score(a: int, b: int) -> int:
    # working_solution: (100%, 73.56%) -> (0ms, 19.13mb)  Time: O(1) Space: O(1)
    b_count_a: int = bin(a)[2:].count('1')
    b_count_b: int = bin(b)[2:].count('1')

    return b_count_a * b_count_b if b_count_a >= b_count_b else b_count_b // b_count_a


# Time complexity: O(1)
# --- --- --- ---
# Space complexity: O(1)


test_a: int = 14
test_b: int = 6
test_out: int = 6
assert test_out == calculate_score(test_a, test_b)

test_a = 5
test_b = 15
test_out = 2
assert test_out == calculate_score(test_a, test_b)

test_a = 10
test_b = 12
test_out = 4
assert test_out == calculate_score(test_a, test_b)
