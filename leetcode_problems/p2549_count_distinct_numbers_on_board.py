# You are given a positive integer n, that is initially placed on a board.
# Every day, for 10 ** 9 days, you perform the following procedure:
#  - For each number x present on the board,
#    find all numbers 1 <= i <= n such that x % i == 1.
#  - Then, place those numbers on the board.
# Return the number of distinct integers present on the board
#  after 10 ** 9 days have elapsed.
# Note:
#  - Once a number is placed on the board, it will remain on it until the end.
#  - % stands for the modulo operation. For example, 14 % 3 is 2.
# ---------------------------
# 1 <= n <= 100


def distinct_integers(n: int) -> int:
    # working_sol (100.00%, 30.74%) -> (0ms, 17.82mb)  time: O(1) | space: O(1)
    # Only `1` will be placed.
    if 2 >= n:
        return 1
    # After 10 ** 9 days, all the number in range 2 -> n (inclusive) will be added.
    # Except `1`, because it will give us `0` from any value modulus.
    return n - 1


# Time complexity: O(1)
# ---------------------------
# Auxiliary space: O(1)


test: int = 5
test_out: int = 4
assert test_out == distinct_integers(test)

test = 3
test_out = 2
assert test_out == distinct_integers(test)
