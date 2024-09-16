# Given a list of 24-hour clock time points in "HH:MM" format,
#  return the minimum minutes difference between any two time-points in the list.
# --------------------------
# 2 <= timePoints.length <= 2 * 10 ** 4
# timePoints[i] is in the format "HH:MM".


def find_min_difference(timePoints: list[str]) -> int:
    # working_sol (97.00%, 79.74%) -> (57ms, 19.57mb)  time: O(n * log n) | space: O(n)
    # Convert everything to minutes.
    new_times: list[int] = [
        int(point[:2]) * 60 + int(point[3:]) for point in timePoints
    ]
    # Sort in ascending order.
    new_times.sort()
    out: int = 24 * 60
    # Now we can just check all adj_pair, because it's always the smallest distance.
    for index in range(1, len(new_times)):
        out = min(out, new_times[index] - new_times[index - 1])
    # Extra, we need to compare edge values in reverse.
    # `24 * 60 == minutes in day` - `highest time` == time to reach 24:00
    # `24 * 60 + `lowest time` time after 24:00 == 24 * 60 - highest time + lowest time
    out = min(out, 24 * 60 - new_times[-1] + new_times[0])
    return out


# Time complexity: O(n * log n) <- n - length of the input array `timePoints`.
# We're given every index of the same size, so we can count it as constant.
# Converting every value to minutes + sorting it => O((n * log n) + n).
# Extra traversing new array of the same size, once => O(2 * n + n * log n).
# --------------------------
# Auxiliary space: O(n)
# `new_times` <- allocates space for each index of `timePoints` => O(n).
# `sort` <- takes O(n) => O(2 * n).


test: list[str] = ["23:59", "00:00"]
test_out: int = 1
assert test_out == find_min_difference(test)

test = ["00:00", "23:59", "00:00"]
test_out = 0
assert test_out == find_min_difference(test)
