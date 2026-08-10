# You are given an integer n, representing n light bulbs arranged in a line
#  and indexed from 0 to n - 1.
# You are also given an integer brightness and a 2D integer array intervals,
#  where intervals[i] = [starti, endi] represents an inclusive time interval
#  during which the lighting requirement must be satisfied.
# At each time unit, every bulb can independently be either on or off.
# A bulb that is on illuminates its own position and its adjacent positions,
#  if they exist.
# The total illumination at a time unit is the number of illuminated positions.
# Each position is counted at most once.
# For every integer time unit covered by at least one interval in intervals,
#  the total illumination must be at least brightness.
# At time units not covered by any interval, all bulbs may remain off.
# Each bulb that is on consumes 1 unit of energy for that time unit.
# Return an integer denoting the minimum total energy required.
# --- --- --- ---
# 1 <= n <= 10 ** 6
# 1 <= brightness <= n
# 1 <= intervals.length <= 10 ** 5
# intervals[i] == [starti, endi]
# 0 <= starti <= endi <= 10 ** 9
from math import ceil


def min_energy(n: int, brightness: int, intervals: list[list[int]]) -> int:
    # working_solution: (41.18%, 29.22%) -> (90ms, 57.48mb)  Time: O(m * log m) Space: O(m)
    # Basically 1 buld, light 3 cells.
    # We got `n` cells, so ceil(n / 3) == what we need to be `on` to cover everything.
    # But, we only need to cover the `brightness`.
    out: int = 0
    req_bulbs: int = ceil(brightness / 3)
    merged_intervals: list[list[int]] = []
    for interval in sorted(intervals, key=lambda x: x[0]):
        if merged_intervals:
            if (
                merged_intervals[-1][1] <= interval[1]
                and
                merged_intervals[-1][1] >= interval[0]
            ):
                merged_intervals[-1][1] = interval[1]
            elif (
                    merged_intervals[-1][0] == interval[0]
                    and
                    merged_intervals[-1][1] >= interval[1]
            ):
                continue
            elif (
                merged_intervals[-1][1] >= interval[0]
                and
                merged_intervals[-1][1] >= interval[1]
            ):
                continue
            else:
                merged_intervals.append(interval)
        else:
            merged_intervals.append(interval)
    
    for interval in merged_intervals:
        out += req_bulbs * ((interval[1] - interval[0])+ 1)
    
    return out


# Time complexity: O(m * log m)
# m - length of the input array `intervals`
# --- --- --- ---
# Space complexity: O(m)


test_n: int = 5
test_brightness: int = 5
test_intervals: list[list[int]] = [[6, 12]]
test_out: int = 14
assert test_out == min_energy(test_n, test_brightness, test_intervals)

test_n = 2
test_brightness = 1
test_intervals = [[0, 0], [2, 2]]
test_out = 2
assert test_out == min_energy(test_n, test_brightness, test_intervals)

test_n = 4
test_brightness = 2
test_intervals =[[1, 3], [2, 4]]
test_out = 4
assert test_out == min_energy(test_n, test_brightness, test_intervals)

test_n = 738235
test_brightness = 635017
test_intervals = [
     [880012,962435],[880012,984965],[880012,966345],[880012,959020],[880012,954813],
     [880012,891751],[880012,924920],[880012,998728],[880012,943084],[880012,909394],
     [880012,949521],[880012,966713],[880012,883519],[880012,930005],[880012,939543],
     [880012,960371],[880012,955023],[880012,929936],[880012,940539]
]
test_out: int = 25129183541
assert test_out == min_energy(test_n, test_brightness, test_intervals)
