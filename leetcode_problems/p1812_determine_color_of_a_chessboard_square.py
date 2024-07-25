# You are given coordinates, a string that represents the coordinates of a square of the chessboard.
# Return true if the square is white, and false if the square is black.
# The coordinate will always represent a valid chessboard square.
# The coordinate will always have the letter first, and the number second.
# --------------------
# coordinates.length == 2
# 'a' <= coordinates[0] <= 'h'
# '1' <= coordinates[1] <= '8'


def square_is_white(coordinates: str) -> bool:
    # working_sol (98.25%, 96.16%) -> (23ms, 16.34mb)  time: O(1) | space: O(1)
    # evenCol + evenRow => black => False
    # evenCol + oddRow => white => True
    # AND
    # oddCol + evenRow => white => True
    # oddCol + oddRow => black => False
    col: int = ord(coordinates[0]) - 97
    row: int = int(coordinates[1]) - 1  # to make 0-indexed
    if col % 2:
        if row % 2:
            return False
        return True
    else:
        if row % 2:
            return True
        return False


# Time complexity: O(1)
# We always make same operations, no matter the input => O(1).
# --------------------
# Auxiliary space: O(1)
# Only 2 constant INTs used, none of them depends on input => O(1).


test: str = 'a1'
test_out: bool = False
assert test_out == square_is_white(test)

test = 'h3'
test_out = True
assert test_out == square_is_white(test)

test = 'c7'
test_out = False
assert test_out == square_is_white(test)
