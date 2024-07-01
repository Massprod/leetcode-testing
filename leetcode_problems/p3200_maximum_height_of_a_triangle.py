# You are given two integers red and blue representing the count of red and blue colored balls.
# You have to arrange these balls to form a triangle such that the 1st row will have 1 ball,
#  the 2nd row will have 2 balls, the 3rd row will have 3 balls, and so on.
# All the balls in a particular row should be the same color, and adjacent rows should have different colors.
# Return the maximum height of the triangle that can be achieved.
# --------------------------
# 1 <= red, blue <= 100


def max_height_of_triangle(red: int, blue: int) -> int:
    # working_sol (100%, 100%) -> (39ms, 16.45mb)  time: O(red + blue) | O(1)

    def check(_red, _blue, _red_start) -> int:
        row: int = 0
        row_cost: int = 1
        red_left: int = _red
        blue_left: int = _blue
        red_start: bool = _red_start
        while (red_left >= row_cost and red_start) or (blue_left >= row_cost and not red_start):
            if red_start:
                red_left -= row_cost
                red_start = False
            else:
                blue_left -= row_cost
                red_start = True
            row_cost += 1
            row += 1
        return row

    return max(check(red, blue, True), check(red, blue, False))


# Time complexity: O(red + blue)
# Always depleting red and blue until we can build a rows => O(red + blue).
# --------------------------
# Auxiliary space: O(1)


test_red: int = 2
test_blue: int = 4
test_out: int = 3
assert test_out == max_height_of_triangle(test_red, test_blue)

test_red = 2
test_blue = 1
test_out = 2
assert test_out == max_height_of_triangle(test_red, test_blue)

test_red = 1
test_blue = 1
test_out = 1
assert test_out == max_height_of_triangle(test_red, test_blue)

test_red = 10
test_blue = 1
test_out = 2
assert test_out == max_height_of_triangle(test_red, test_blue)

test_red = 99
test_blue = 99
test_out = 18
assert test_out == max_height_of_triangle(test_red, test_blue)
