# There are n cities. Some of them are connected, while some are not.
# If city a is connected directly with city b, and city b is connected directly with city c,
#  then city a is connected indirectly with city c.
# A province is a group of directly or indirectly connected cities and no other cities outside the group.
# You are given an n x n matrix isConnected where isConnected[i][j] = 1
#  if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
# Return the total number of provinces.
# ---------------------
# 1 <= n <= 200
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j] is 1 or 0.
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]


def find_circle_num(isConnected: list[list[int]]) -> int:
    # working_sol (78.91%, 38.26%) -> (209ms, 17.4mb)  time: O(m * n) | space: O(log(m * n))
    row: int = len(isConnected[0])
    col: int = len(isConnected)

    def check(y_: int, x_: int, path: set[tuple[int, int]]) -> None:
        # We need to check both sides of a city.
        for g in range(row):
            # But ignore visited and city itself.
            if g == x_ or (g, g) in path:
                continue
            # Check every possible link and mark it visited.
            if isConnected[y_][g] == 1:
                path.add((g, g))
                isConnected[g][g] = 2
                check(g, g, path)
    # Standard DFS.
    city: int = 0
    provinces: int = 0
    # Every ROW is 1City.
    # [0][0], [1][1] etc.
    while city != col:
        # Ignore if visited -> marked as 2.
        if isConnected[city][city] != 2:
            check(city, city, {(city, city)})
            # We visit every connected city,
            #  so it's only +1 for every check.
            provinces += 1
        city += 1
    return provinces


# Time complexity: O(m * n) -> checking every city(row) and for every row checking all it's indexes => O(m * n).
# m - col of input_matrix^^|
# n - row of input_matrix^^|
# Auxiliary space: O(log(m * n)) -> guess, in the worst case every city is connected, so we're going to check every
#                                diagonal index from [0][0] to [m - 1][n - 1], stack size will be equal to number
#                                of these indexes -> extra all of them stored in a path => O(2 * log(m * n).
# ---------------------
# I was semi_correct on left_side, because it's point to higher Cities -> Yes.
# But we can have 0 city point to like 3, and 3 will point to 2, 6, 3, w.e.
# And 3 city points to a higher ones, when 0 is missing it. So we need to check EVERY part left and right.
# Otherwise, I was missing some edges.
# ---------------------
# Another DFS with graphs, looking same as p841.
# But as I see it we're given BiDirectional edges, and every city is [0][0] -> [1][1] etc. [y + 1][x + 1].
# Like every ROW is a new city, and left|right parts from this city is connected cities.
# And if I understood correctly it's BiDirectional, otherwise why in 1test_case we're given [0, 1] and [1, 0].
# So we can ignore left_side, and try to check right_side if we move from top to bot.
# Or ignore right_side and check left_side if bot to top.
# Need more test_cases, but it's looks like it.
# Take every ROW == City and check his right parts, mark all on path as visited and +1 for counter.
# Ignore visited, and for every unvisited city +1. Should be correct.
# At least left_side, always pointing to higher_row, which we're already going to have checked.


test: list[list[int]] = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
test_out: int = 2
assert test_out == find_circle_num(test)

test = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
test_out = 3
assert test_out == find_circle_num(test)

# test -> Failed -> I was ignoring left_side, take [0][0] city as example and missed lower ones.
#                   Lower cities can have its own connections.
test = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]
test_out = 1
assert test_out == find_circle_num(test)
