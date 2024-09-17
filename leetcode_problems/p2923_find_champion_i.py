# There are n teams numbered from 0 to n - 1 in a tournament.
# Given a 0-indexed 2D boolean matrix grid of size n * n.
# For all i, j that 0 <= i, j <= n - 1 and i != j team i is stronger
#  than team j if grid[i][j] == 1, otherwise, team j is stronger than team i.
# Team a will be the champion of the tournament if there is no team b that is stronger than team a.
# Return the team that will be the champion of the tournament.
# -------------------------
# n == grid.length
# n == grid[i].length
# 2 <= n <= 100
# grid[i][j] is either 0 or 1.
# For all i grid[i][i] is 0.
# For all i, j that i != j, grid[i][j] != grid[j][i].
# The input is generated such that if team a is stronger
#  than team b and team b is stronger than team c, then team a is stronger than team c.


def find_champion(grid: list[list[int]]) -> int:
    # working_sol (62.15%, 54.50%) -> (428ms, 16.96mb)  time: O(n * n) | space: O(n)
    strongest: int = 0
    weaker: set[int] = set()

    def gather_weaker(team_row: int) -> None:
        for other_team in range(len(grid[team_row])):
            if grid[team_row][other_team]:
                weaker.add(other_team)

    for team in range(len(grid)):
        if team not in weaker:
            strongest = team
            gather_weaker(team)
    return strongest


# Time complexity: O(n * n) <- n - length | height of the input square matrix `grid`.
# In the worst case, every `team_row` is going to have all `0` columns.
# So, we will traverse the whole input matrix, and only the last row & column value is going to have 1 => O(n * n).
# -------------------------
# Auxiliary space: O(n)
# `weaker` <- allocates space for weaker teams, and they can be only 1 row of the weaker teams.
# We will either skip them and add later, or we will get a team with all `1`s row => O(n).


test: list[list[int]] = [[0, 1], [0, 0]]
test_out: int = 0
assert test_out == find_champion(test)

test = [[0, 0, 1], [1, 0, 1], [0, 0, 0]]
test_out = 1
assert test_out == find_champion(test)
