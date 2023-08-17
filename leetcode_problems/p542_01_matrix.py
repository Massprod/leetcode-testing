# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
# The distance between two adjacent cells is 1.
# -------------------
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 10 ** 4
# 1 <= m * n <= 10 ** 4
# mat[i][j] is either 0 or 1.
# There is at least one 0 in mat.
from collections import deque


def update_matrix(mat: list[list[int]]) -> list[list[int]]:
    # working_sol (74.35%, 62.50%) -> (574ms, 19.7mb)  time: O(m * n) | space: O(m * n)
    # Store all correctly build cells.
    visited: set[tuple[int, int]] = set()
    col_len: int = len(mat)
    row_len: int = len(mat[0])
    visit_que: deque = deque()
    # First we need to decide from what nodes we can start.
    # And these nodes are neighbours of 0.
    # Cuz they're already having min_distance at all times.
    for y in range(col_len):
        for x in range(row_len):
            if mat[y][x] == 0:
                # No reasons to check 0 after, finding all its neighbours.
                visited.add((y, x))
            # It's faster to find neighbours of 1's being O's.
            # Cuz on median there's more 0 in matrix present.
            elif mat[y][x] == 1:
                if (y - 1) >= 0 and mat[y - 1][x] == 0:
                    visited.add((y, x))
                if (y + 1) < col_len and mat[y + 1][x] == 0:
                    visited.add((y, x))
                if (x - 1) >= 0 and mat[y][x - 1] == 0:
                    visited.add((y, x))
                if (x + 1) < row_len and mat[y][x + 1] == 0:
                    visited.add((y, x))
    # We only care about min_distance, so we need to build from
    # the closest point we can. We stored every neighbour of 0's,
    # into a visit_que it's by default the closest possible points.
    # So we can only start calc from it.
    for _ in visited:
        if mat[_[0]][_[1]] == 0:
            continue
        visit_que.append(_)
    max_neighbour: int = col_len * row_len
    while len(visit_que) > 0:
        # Take not processed cell and check all its neighbours.
        cur_cell: tuple[int, int] = visit_que.popleft()
        y_: int = cur_cell[0]
        x_: int = cur_cell[1]
        # We can't have distance higher than this.
        min_neighbour: int = max_neighbour
        # If there exist left_neighbour ->
        if (y_ - 1) >= 0:
            # -> and it's already set, then we can try to use it ->
            if (y_ - 1, x_) in visited:
                min_neighbour = min(min_neighbour, mat[y_ - 1][x_] + 1)
            # -> otherwise, we need to visit and set it later.
            else:
                visit_que.append((y_ - 1, x_))
        # Same for all other neighbours: right|top|bot.
        if (y_ + 1) < col_len:
            if (y_ + 1, x_) in visited:
                min_neighbour = min(min_neighbour, mat[y_ + 1][x_] + 1)
            else:
                visit_que.append((y_ + 1, x_))
        if (x_ - 1) >= 0:
            if (y_, x_ - 1) in visited:
                min_neighbour = min(min_neighbour, mat[y_][x_ - 1] + 1)
            else:
                visit_que.append((y_, x_ - 1))
        if (x_ + 1) < row_len:
            if (y_, x_ + 1) in visited:
                min_neighbour = min(min_neighbour, mat[y_][x_ + 1] + 1)
            else:
                visit_que.append((y_, x_ + 1))
        # If there was correctly set neighbour we can set this cell,
        # and we're always building from correctly set cells.
        # First cells will have neighbours == 0, and they're actually repeating.
        # Cuz we already know that neighbours of 0 is always min_dist == 1.
        # So I could set them as 1, and start from their neighbours, but
        # we still need to find their neighbours to use, and it's the same process.
        mat[y_][x_] = min_neighbour
        visited.add((y_, x_))

    return mat


# Time complexity: O(m * n) -> traversing to get all neighbours of 0's => O(m * n) -> extra to this
# m - row lenght of input_matrix^^| while loop which going to check every neighbour of 0's found and then
# n - col length of input_matrix^^| check every Neighbour of these checked nodes only once,
#                                   so it's still using every node once after traversing, except 0's => O(m * n).
# Auxiliary space: O(m * n) -> we mark every processed cell with adding them into a visited, in the end
#                              we're always having len(visited) == m * n, so it's => O(m * n) for set.
#                              Extra to this maximum visit_que should not be more than some part of the set ->
#                              -> O(m * n + log(m * n))? In some cases it's only One '1' in the matrix,
#                              better to stick with O(m * n), cuz it's dominating the visit_que anyway.
# -------------------
# Ok. Seems working, but random test_case are always correct. Cuz I don't know how to make them
# harder with big sizes, so it's better to fail and see what could I miss.
# Nice all correct.
# For a future use -> don't try to build checks with just marking nodes,
#   we first need to check nodes which already been marked and expand from them.
# Firstly I was trying to just go from cell to cell and see if their Neighbour is set,
# and if it was I was just setting min(all_neighbours + 1) in this case, I was missing parts
# when some neighbours not even build at this time. So I need to check everything from a que()
# and que is storing all nodes which already been 100% build == Neighbours of 0 and later
# nodes which been build from this marked nodes(que nodes).


test: list[list[int]] = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
test_out: list[list[int]] = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
assert test_out == update_matrix(test)

test = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
test_out = [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
assert test_out == update_matrix(test)

test = [
    [0, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0]
]
test_out = [
    [0, 1, 2, 3, 4, 5, 4], [1, 2, 3, 4, 5, 4, 3],
    [2, 3, 4, 5, 4, 3, 2], [3, 4, 5, 4, 3, 2, 1],
    [4, 5, 4, 3, 2, 1, 0]
]
assert test_out == update_matrix(test)
