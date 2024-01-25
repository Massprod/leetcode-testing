# Given the coordinates of two rectilinear rectangles in a 2D plane,
#  return the total area covered by the two rectangles.
# The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-right corner (ax2, ay2).
# The second rectangle is defined by its bottom-left corner (bx1, by1) and its top-right corner (bx2, by2).
# ------------------------------
# -10 ** 4 <= ax1 <= ax2 <= 10 ** 4
# -10 ** 4 <= ay1 <= ay2 <= 10 ** 4
# -10 ** 4 <= bx1 <= bx2 <= 10 ** 4
# -10 ** 4 <= by1 <= by2 <= 10 ** 4


def compute_area(ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
    # working_sol (74.40%, 61.28%) -> (49ms, 16.6mb)  time: O(1) | space: O(1)
    # Whole area they're covering with overlapping area.
    a_length: int = ax2 - ax1
    a_height: int = ay2 - ay1
    a_area: int = a_length * a_height
    b_length: int = bx2 - bx1
    b_height: int = by2 - by1
    b_area: int = b_length * b_height
    # But in this case overlapping area is counted twice, we need to find it and exclude.
    out: int = a_area + b_area
    overlap_length: int = min(bx2, ax2) - max(bx1, ax1)
    overlap_height: int = min(by2, ay2) - max(by1, ay1)
    # Or they can be distinct and don't have overlapping area.
    if overlap_length > 0 and overlap_height > 0:
        out -= overlap_height * overlap_length
    return out


# Time complexity: O(1).
# If input is correct, we're always doing same actions no matter what => O(1).
# ------------------------------
# Auxiliary space: O(1).
# Everything used is constant, and doesn't depend on input => O(1)


test_ax1: int = -3
test_ay1: int = 0
test_ax2: int = 3
test_ay2: int = 4
test_bx1: int = 0
test_by1: int = -1
test_bx2: int = 9
test_by2: int = 2
test_out: int = 45
assert test_out == compute_area(test_ax1, test_ay1, test_ax2, test_ay2, test_bx1,test_by1, test_bx2, test_by2)

test_ax1 = -2
test_ay1 = -2
test_ax2 = 2
test_ay2 = 2
test_bx1 = -1
test_by1 = -2
test_bx2 = 2
test_by2 = 2
test_out = 16
assert test_out == compute_area(test_ax1, test_ay1, test_ax2, test_ay2, test_bx1,test_by1, test_bx2, test_by2)
