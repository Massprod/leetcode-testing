# You are given a 2D integer array drones, where drones[i] = [xi, yi, rangei]
#  represents the x-coordinate, y-coordinate, and travel range of the ith drone.
# You are also given an integer array target = [tx, ty],
#  representing the coordinates of the target.
# A drone drones[i] can reach the target if the Manhattan distance between
#  its coordinates and the target coordinates is less than or equal to its rangei.
# Return the index of the reachable drone with the minimum Manhattan distance to the target.
# If there is a tie, return the smallest index.
# If no drone can reach the target, return -1.
# --- --- --- ---
# 1 <= drones.length <= 100
# drones[i] = [xi, yi, rangei]
# target = [tx, ty]
# -25 <= xi, yi, tx, ty <= 25
# 1 <= rangei <= 100


def nearest_drone(drones: list[list[int]], target: list[int]) -> int:
    # working_solution: (100%, 79.85%) -> (0ms, 19.25mb)  Time: O(n) Space: O(1)
    out: int = -1
    cur_best: int = 1_000
    for index, d_data in enumerate(drones):
        d_x, d_y, d_range = d_data[0], d_data[1], d_data[2]
        m_d: int = abs(d_x - target[0]) + abs(d_y - target[1])
        if m_d <= d_range and cur_best > m_d:
            out = index
            cur_best = m_d
    
    return out


# Time complexity: O(n)
# n - length of the input array `drones`
# --- --- --- ---
# Space complexity: O(1)


test_drones: list[list[int]] = [[0, 0, 8], [2, 2, 9]]
test_target: list[int] = [3, 4]
test_out: int = 1
assert test_out == nearest_drone(test_drones, test_target)

test_drones = [[2, 1, 5], [4, 4, 5], [6, 6, 8]]
test_target = [5, 5]
test_out = 1
assert test_out == nearest_drone(test_drones, test_target)

test_drones = [[4, 4, 5]]
test_target = [8, 6]
test_out = -1
assert test_out == nearest_drone(test_drones, test_target)
