# You are given two strings, coordinate1 and coordinate2,
#  representing the coordinates of a square on an 8 x 8 chessboard.
# Return true if these two squares have the same color and false otherwise.
# The coordinate will always represent a valid chessboard square.
# The coordinate will always have the letter first (indicating its column),
#  and the number second (indicating its row).
# ---------------------
# coordinate1.length == coordinate2.length == 2
# 'a' <= coordinate1[0], coordinate2[0] <= 'h'
# '1' <= coordinate1[1], coordinate2[1] <= '8'


def check_two_chessboards(coordinate1: str, coordinate2: str) -> bool:
    # working_sol (95.64%, 58.67%) -> (27ms, 16.55mb)  time: O(1) | space: O(1)
    def check_color(column, row) -> int:
        if column % 2:
            if row % 2:
                return 0
            return 1
        else:
            if row % 2:
                return 1
        return 0

    coord1_column, coord1_row = ord(coordinate1[0]) - 97, int(coordinate1[1])
    coord2_column, coord2_row = ord(coordinate2[0]) - 97, int(coordinate2[1])
    # EVEN column + EVEN row == BLACK
    # EVEN column + ODD row == WHITE
    # AND
    # ODD column + EVEN row == white
    # ODD column + ODD row == BLACK
    # 0 == BLACK | 1 == WHITE
    coord1_color: int = check_color(coord1_column, coord1_row)
    coord2_color: int = check_color(coord2_column, coord2_row)
    return coord1_color == coord2_color


# Time complexity: O(1)
# We always check 2 input values with the same actions => O(1)
# ---------------------
# Auxiliary space: O(1)
# And creating the same variables, nothing depends on input => O(1)


test_1: str = "a1"
test_2: str = "c3"
test_out: bool = True
assert test_out == check_two_chessboards(test_1, test_2)

test_1 = "a1"
test_2 = "h3"
test_out = False
assert test_out == check_two_chessboards(test_1, test_2)

test_1 = "d1"
test_2 = "h4"
test_out = False
assert test_out == check_two_chessboards(test_1, test_2)
