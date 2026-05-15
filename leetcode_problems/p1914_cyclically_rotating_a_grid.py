# You are given an m x n integer matrix grid​​​, where m and n are both even integers,
#  and an integer k.
# The matrix is composed of several layers, which is shown in the below image,
#  where each color is its own layer:
# A cyclic rotation of the matrix is done by cyclically rotating each layer in the matrix.
# To cyclically rotate a layer once, each element in the layer will take the place
#  of the adjacent element in the counter-clockwise direction.
# An example rotation is shown below:
# Return the matrix after applying k cyclic rotations to it.
# --- --- --- ---
# m == grid.length
# n == grid[i].length
# 2 <= m, n <= 50
# Both m and n are even integers.
# 1 <= grid[i][j] <= 5000
# 1 <= k <= 10 ** 9

def rotate_grid(grid: list[list[int]], k: int) -> list[list[int]]:
    # working_solution: (20.55%, 24.66%) -> (125ms, 19.7mb)  Time: O(n * m) Space: O(n + m)
    # [(dy, dx)] -> [down, right, top, left]
    travel_directions: list[tuple[int, int]] = [
        (1, 0), (0, 1), (-1, 0), (0, -1)
    ]
    shift: int = 0
    # Every time we `shift` to the new circle, we will have less cells to use.
    # Always lower by `x2`, so we need to calculate actual rotation we need to make.
    # Exclude full circles.
    # Circles we need to travel.
    limit: int = min(len(grid) // 2, len(grid[0]) // 2)
    while shift < limit:
        y: int = 0 + shift
        x: int = 0 + shift
        cur_circle: list[int] = [grid[y][x]]
        limit_end_vertical: int = len(grid) - shift
        limit_end_horizontal: int = len(grid[0]) - shift
        limit_start_vertical: int = 0 + shift
        limit_start_horizontal: int = 0 + shift
        direction: int = 0
        while 4 > direction:
            dy, dx = travel_directions[direction]
            new_y, new_x = y + dy, x + dx
            if (not (limit_start_vertical <= new_y < limit_end_vertical)
                or not (limit_start_horizontal <= new_x < limit_end_horizontal)):
                direction += 1
                continue
            y, x = new_y, new_x
            cur_circle.append(
                grid[y][x]
            )
        # `if` more costly, than removing an extra value from a full circle
        cur_circle.pop()
        y = 0 + shift
        x = 0 + shift
        pivot: int = k % len(cur_circle)
        cur_circle = cur_circle[len(cur_circle) - pivot:] + cur_circle[:len(cur_circle) - pivot]
        direction = 0
        index: int = 0
        grid[y][x] = cur_circle[index]
        index += 1
        while index < len(cur_circle):
            dy, dx = travel_directions[direction]
            new_y, new_x = y + dy, x + dx
            if (not (limit_start_vertical <= new_y < limit_end_vertical)
                or not (limit_start_horizontal <= new_x < limit_end_horizontal)):
                direction += 1
                continue
            y, x = new_y, new_x
            grid[y][x] = cur_circle[index]
            index += 1
        shift +=1
    
    return grid


# Time complexity: O(n * m)
# n - legnth of the input matrix `grid`
# m - height of the input matrix `grid`
# --- --- --- ---
# Space complexity: O((n + m) * 2)
# First circle is stored in the `cur_circle` and we allocate space for each of its value.


test: list[list[int]] = [
    [40, 10],
    [30, 20]
]
test_k: int = 1
test_out: list[list[int]] = [
    [10, 20],
    [40, 30]
]
assert test_out == rotate_grid(test, test_k)

test = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
test_k = 2
test_out: list[list[int]] = [
    [3, 4, 8, 12],
    [2, 11, 10, 16],
    [1, 7, 6, 15],
    [5, 9, 13, 14]
]
assert test_out == rotate_grid(test, test_k)
