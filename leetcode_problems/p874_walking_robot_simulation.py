# A robot on an infinite XY-plane starts at point (0, 0) facing north.
# The robot can receive a sequence of these three possible types of commands:
#  - -2: Turn left 90 degrees.
#  - -1: Turn right 90 degrees.
#  - 1 <= k <= 9: Move forward k units, one unit at a time.
# Some of the grid squares are obstacles.
# The ith obstacle is at grid point obstacles[i] = (xi, yi).
# If the robot runs into an obstacle, then it will instead stay
#  in its current location and move on to the next command.
# Return the maximum Euclidean distance that the robot ever gets
#  from the origin squared (i.e. if the distance is 5, return 25).
# Note:
#  - North means +Y direction.
#  - East means +X direction.
#  - South means -Y direction.
#  - West means -X direction.
#  - There can be obstacle in [0,0].
# -----------------------
# 1 <= commands.length <= 10 ** 4
# commands[i] is either -2, -1, or an integer in the range [1, 9].
# 0 <= obstacles.length <= 10 ** 4
# -3 * 10 ** 4 <= xi, yi <= 3 * 10 ** 4
# The answer is guaranteed to be less than 2 ** 31.


def robot_sim(commands: list[int], obstacles: list[list[int]]) -> int:
    # working_sol (44.18%, 80.18%) -> (290ms, 23.22mb)  time: O(n + k) | space: O(k)
    dy: int
    dx: int
    # { direction: (left_turn, right_turn) }
    dirs: dict[str, tuple[str, str]] = {
        'n': ('w', 'e'),
        'w': ('s', 'n'),
        's': ('e', 'w'),
        'e': ('n', 's'),
    }
    # { direction: (dy, dx) }
    dir_steps: dict[str, tuple[int, int]] = {
        'n': (1, 0),
        'w': (0, -1),
        's': (-1, 0),
        'e': (0, 1),
    }
    cur_face: str = 'n'
    # [y, x]
    cur_coords: list[int] = [0, 0]
    # Original `obstacles` given in format (x, y) <- we need to reverse.
    fast_obstacles: set[tuple[int, ...]] = {
        (obstacle[1], obstacle[0]) for obstacle in obstacles
    }
    out: int = 0
    for command in commands:
        if 0 > command:
            cur_face = dirs[cur_face][command]
            continue
        dy, dx = dir_steps[cur_face][0], dir_steps[cur_face][1]
        for step in range(command):
            new_y = cur_coords[0] + dy
            new_x = cur_coords[1] + dx
            if (new_y, new_x) in fast_obstacles:
                break
            cur_coords[0], cur_coords[1] = new_y, new_x
            out = max(
                out,
                cur_coords[0] ** 2 + cur_coords[1] ** 2
            )
    return out


# Time complexity: O(n + k) <- n - length of the input array `commands`, k - length of the input array `obstacles`.
# Always using every pair of `obstacles` to get correct block tuples => O(k).
# Executing every command from `commands`, and because we're having `1 <= k <= 9`
#  we can count it as a constant => O(n + k).
# -----------------------
# Auxiliary space: O(k)
# `fast_obstacles` <- always of the same size as `obstacles` => O(k).


test: list[int] = [4, -1, 3]
test_obs: list[list[int]] = []
test_out: int = 25
assert test_out == robot_sim(test, test_obs)

test = [4, -1, 4, -2, 4]
test_obs = [[2, 4]]
test_out = 65
assert test_out == robot_sim(test, test_obs)

test = [6, -1, -1, 6]
test_obs = []
test_out = 36
assert test_out == robot_sim(test, test_obs)
