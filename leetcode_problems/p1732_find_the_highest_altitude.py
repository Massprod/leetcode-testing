# There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes.
# The biker starts his trip on point 0 with altitude equal 0.
# You are given an integer array gain of length n where gain[i] is the net gain in altitude
#   between points i and i + 1 for all (0 <= i < n). Return the highest altitude of a point.
# -------------------
# n == gain.length
# 1 <= n <= 100
# -100 <= gain[i] <= 100


def largest_altitude(gain: list[int]) -> int:
    # working_sol (96.45%, 26.6%) -> (36ms, 16.3mb)  time: O(n) | space: O(1)
    altitude: int = 0
    max_altitude: int = 0
    for _ in gain:
        altitude += _
        max_altitude = max(altitude, max_altitude)
    return max_altitude


# Time complexity: O(n) -> traversing whole input array once => O(n).
# n - len of input_list^^|
# Auxiliary space: O(1) -> 2 constant INTs both doesn't depend on input => O(1)


test1 = [-5, 1, 5, 0, -7]
test1_out = 1
print(largest_altitude(test1))
assert test1_out == largest_altitude(test1)

test2 = [-4, -3, -2, -1, 4, 3, 2]
test2_out = 0
print(largest_altitude(test2))
assert test2_out == largest_altitude(test2)
