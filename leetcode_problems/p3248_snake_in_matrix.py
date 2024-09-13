# There is a snake in an n x n matrix grid and can move in four possible directions.
# Each cell in the grid is identified by the position: grid[i][j] = (i * n) + j.
# The snake starts at cell 0 and follows a sequence of commands.
# You are given an integer n representing the size of the grid and an array of strings commands
#  where each command[i] is either "UP", "RIGHT", "DOWN", and "LEFT".
# It's guaranteed that the snake will remain within the grid boundaries throughout its movement.
# Return the position of the final cell where the snake ends up after executing commands.
# ---------------------------
# 2 <= n <= 10
# 1 <= commands.length <= 100
# commands consists only of "UP", "RIGHT", "DOWN", and "LEFT".
# The input is generated such the snake will not move outside of the boundaries.


def final_position_of_snake(n: int, commands: list[str]) -> int:
    # working_sol (18.45%, 86.97%) -> (77ms, 16.42mb)  time: O(n * n + k) | space: O(n * n)
    matrix: list[list[int]] = [
        [(row * n) + col for col in range(n)] for row in range(n)
    ]
    snake: list[int] = [0, 0]
    com_moves: dict[str, tuple[int, int]] = {
        'UP': (-1, 0),
        'RIGHT': (0, 1),
        'DOWN': (1, 0),
        'LEFT': (0, -1),
    }
    for command in commands:
        snake[0] += com_moves[command][0]
        snake[1] += com_moves[command][1]
    return matrix[snake[0]][snake[1]]


# Time complexity: O(n * n + k)
# Always creating `n * n` matrix => O(n * n).
# Extra traversing every command from `commands` => O(n * n + k).
# ---------------------------
# Auxiliary space: O(n * n)
# `matrix` <- allocates space for `n * n` cells => O(n * n).


test_n: int = 2
test_commands: list[str] = ["RIGHT", "DOWN"]
test_out: int = 3
assert test_out == final_position_of_snake(test_n, test_commands)

test_n = 3
test_commands = ["DOWN", "RIGHT", "UP"]
test_out = 1
assert test_out == final_position_of_snake(test_n, test_commands)
