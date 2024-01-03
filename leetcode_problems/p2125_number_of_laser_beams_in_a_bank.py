# Anti-theft security devices are activated inside a bank.
# You are given a 0-indexed binary string array bank representing the floor plan of the bank,
#  which is an m x n 2D matrix. bank[i] represents the ith row,
#  consisting of '0's and '1's. '0' means the cell is empty,
#  while'1' means the cell has a security device.
# There is one laser beam between any two security devices if both conditions are met:
#   - The two devices are located on two different rows: r1 and r2, where r1 < r2.
#   - For each row i where r1 < i < r2, there are no security devices in the ith row.
# Laser beams are independent, i.e., one beam does not interfere nor join with another.
# Return the total number of laser beams in the bank.
# ------------------
# m == bank.length
# n == bank[i].length
# 1 <= m, n <= 500
# bank[i][j] is either '0' or '1'.
from random import choice


def number_of_beams(bank: list[str]) -> int:
    # working_sol (98.89%, 12.99%) -> (79ms, 19.4mb)  time: O(n * m) | space: O(1)
    # Every laser on prev_row is always points to every laser on closest row with lasers.
    # So, it's just first -> last row walk with multiplying of '1' on rows.
    out: int = 0
    prev_row: int = bank[0].count('1')
    for row in range(1, len(bank)):
        cur_row: int = bank[row].count('1')
        if cur_row:
            out += prev_row * cur_row
            prev_row = cur_row
    return out


# Time complexity: O(n * m) <- n - length of input array `bank`, m - length of inside strings.
# Traversing whole array `bank` and count() on every string => O(n * m).
# ------------------
# Auxiliary space: O(1).
# Nothing extra, only 3 constant INTs none of them depends on input => O(1).


test: list[str] = ["011001", "000000", "010100", "001000"]
test_out: int = 8
assert test_out == number_of_beams(test)

test = ["000", "111", "000"]
test_out = 0
assert test_out == number_of_beams(test)

test = [''.join([choice(['0', '1']) for _ in range(500)]) for _ in range(500)]
print(test)
