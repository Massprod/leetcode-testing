# You are given three integers x, y, and z, representing the positions of three people on a number line:
#  - x is the position of Person 1.
#  - y is the position of Person 2.
#  - z is the position of Person 3, who does not move.
# Both Person 1 and Person 2 move toward Person 3 at the same speed.
# Determine which person reaches Person 3 first:
#  - Return 1 if Person 1 arrives first.
#  - Return 2 if Person 2 arrives first.
#  - Return 0 if both arrive at the same time.
# Return the result accordingly.
# --------------------------
# 1 <= x, y, z <= 100


def find_closest(x: int, y: int, z: int) -> int:
    # working_sol (100.00%, 59.85%) -> (0ms, 17.79mb)  time: O(1) | space: O(1)
    # They can go in both directions => abs(distance)
    time_x: int = abs(z - x)
    time_y: int = abs(z - y)
    if time_x == time_y:
        return 0
    elif time_x > time_y:
        return 2
    return 1


# Time complexity: O(1)
# --------------------------
# Auxiliary space: O(1)


test_x: int = 2
test_y: int = 7
test_z: int = 4
test_out: int = 1
assert test_out == find_closest(test_x, test_y, test_z)

test_x = 2
test_y = 5
test_z = 6
test_out = 2
assert test_out == find_closest(test_x, test_y, test_z)

test_x = 1
test_y = 5
test_z = 3
test_out = 0
assert test_out == find_closest(test_x, test_y, test_z)
