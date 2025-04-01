# You are given an array rectangles where rectangles[i] = [li, wi]
#  represents the ith rectangle of length li and width wi.
# You can cut the ith rectangle to form a square with a side length of k if both
#  k <= li and k <= wi. For example, if you have a rectangle [4,6],
#  you can cut it to get a square with a side length of at most 4.
# Let maxLen be the side length of the largest square you can obtain
#  from any of the given rectangles.
# Return the number of rectangles that can make a square with a side length of maxLen.
# ----------------------
# 1 <= rectangles.length <= 1000
# rectangles[i].length == 2
# 1 <= li, wi <= 10 ** 9
# li != wi


def count_good_rectangles(rectangles: list[list[int]]) -> int:
    # working_sol (98.74%, 65.33%) -> (153ms, 18.38mb)  time: O(n) | space: O(1)
    out: int = 0
    max_square: int = 0
    for length, width in rectangles:
        cur_square: int = min(length, width)
        if cur_square == max_square:
            out += 1
        elif cur_square > max_square:
            out = 1
            max_square = cur_square
    
    return out


# Time complexity: O(n) <- n - length of the input array `rectangles`.
# Always traversing whole input array `rectangles`, once => O(n).
# ----------------------
# Auxiliary space: O(1)


test: list[list[int]] = [[5, 8], [3, 9], [5, 12], [16, 5]]
test_out: int = 3
assert test_out == count_good_rectangles(test)

test = [[2, 3], [3, 7], [4, 3], [3, 7]]
test_out = 3
assert test_out == count_good_rectangles(test)
