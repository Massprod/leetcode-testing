# An image is represented by an m x n integer grid image
#  where image[i][j] represents the pixel value of the image.
# You are also given three integers sr, sc, and color.
# You should perform a flood fill on the image starting from the pixel image[sr][sc].
# To perform a flood fill, consider the starting pixel,
#  plus any pixels connected 4-directionally to the starting pixel of the same color
#  as the starting pixel, plus any pixels connected 4-directionally
#  to those pixels (also with the same color), and so on.
# Replace the color of all of the aforementioned pixels with color.
# Return the modified image after performing the flood fill.
# ------------------------
# m == image.length
# n == image[i].length
# 1 <= m, n <= 50
# 0 <= image[i][j], color < 2 ** 16
# 0 <= sr < m
# 0 <= sc < n
from collections import deque


def flood_fill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    # working_sol (95.83%, 57.17%) -> (57ms, 16.69mb)  time: O(n * m) | space: O(n * m)
    cur_y: int
    cur_x: int
    if image[sr][sc] == color:
        return image
    # [(dy, dx)] <- 4 directions.
    options: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    # (y, x) <- coordinates of the cell.
    que: deque[tuple[int, int]] = deque([(sr, sc)])
    # Standard BFS.
    visited: set[tuple[int, int]] = {(sr, sc)}
    while que:
        cur_y, cur_x = que.popleft()
        for dy, dx in options:
            option: tuple[int, int] = (cur_y + dy, cur_x + dx)
            if (option not in visited
                    and 0 <= option[0] < len(image)
                    and 0 <= option[1] < len(image[0])
                    and image[option[0]][option[1]] == image[sr][sc]):
                que.append(option)
                visited.add(option)
    for cell in visited:
        image[cell[0]][cell[1]] = color
    return image


# Time complexity: O(n * m) <- n - height of the input matrix `image`, m - length of the input matrix `image`.
# Worst case == everything can be colored.
# So, we will traverse the whole `image`, once with bfs to get all the cells for coloring => O(n * m).
# And extra traverse of the `image` to get color the cells after BFS => O(n * m).
# ------------------------
# Auxiliary space: O(n * m)
# Every cell will be stored in `visited` => O(n * m).
# Extra our `que` will allocate spaces for every cell as well => O(2 * (n * m)).


test: list[list[int]] = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
test_sr: int = 1
test_sc = 1
test_color: int = 2
test_out: list[list[int]] = [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
assert test_out == flood_fill(test, test_sr, test_sc, test_color)

test = [[0, 0, 0], [0, 0, 0]]
test_sr = 0
test_sc = 0
test_color = 0
test_out = [[0, 0, 0], [0, 0, 0]]
assert test_out == flood_fill(test, test_sr, test_sc, test_color)
