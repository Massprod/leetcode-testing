# There is a one-dimensional garden on the x-axis.
# The garden starts at the point 0 and ends at the point n. (i.e The length of the garden is n).
# There are n + 1 taps located at points [0, 1, ..., n] in the garden.
# Given an integer n and an integer array ranges of length n + 1 where ranges[i] (0-indexed)
#  means the i-th tap can water the area [i - ranges[i], i + ranges[i]] if it was open.
# Return the minimum number of taps that should be open to water the whole garden,
#  If the garden cannot be watered return -1.
# --------------------------
# 1 <= n <= 10 ** 4
# ranges.length == n + 1
# 0 <= ranges[i] <= 100
from random import randint


def min_taps(n: int, ranges: list[int]) -> int:
    # working_sol (77.62%, 55.71%) -> (130ms, 16.8mb)  time: O(n) | space: O(n)
    # Maximum distance on the right side from a Tap which can be covered,
    #  if Tap is ON. Every index is a place of a Tap in the Garden.
    taps_coverage: list[int] = [0 for _ in range(len(ranges))]
    for x in range(len(ranges)):
        # !  [i - ranges[i], i + ranges[i]] !
        # So we can use every Tap as an interval,
        #  starting at point [i - ranges[i] and ending at [i + ranges[i]].
        # Then we can use index == start as a starting point and record
        #  end point of the interval, starting from this Tap(index).
        start: int = max(0, x - ranges[x])
        end: int = min(len(ranges) - 1, x + ranges[x])
        # All we need is to save END points we can reach from this Tap.
        # We need to cover maximum distance possible from any Tap.
        taps_coverage[start] = max(taps_coverage[start], end)

    # If there's a correct way to cover whole Garden,
    #  it always uses at least 1 tap. Default == 1.
    taps_on: int = 1
    # This Tap is going to cover from its position to the END point saved.
    cur_tap_end: int = taps_coverage[0]
    # Maximum distance we can cover if we start from any Tap we met so far.
    max_coverage: int = taps_coverage[0]
    for tap_point in range(1, len(taps_coverage)):
        # Tap is unreachable.
        # We're trying to start from a Tap which position(index) is higher,
        #  than maximum distance we could cover.
        if tap_point > max_coverage:
            return -1
        # If we start from a Tap which index(position) is higher than previous Tap reach.
        # Then this Tap interval intersects with previous Tap, but Tap(start) isn't inside of it.
        if tap_point > cur_tap_end:
            taps_on += 1
            # We should continue from this Tap.
            cur_tap_end = max_coverage
        # If Tap are reachable.
        # Always updating maximum distance we can cover from this Tap.
        max_coverage = max(max_coverage, taps_coverage[tap_point])

    return taps_on


# Time complexity: O(n) -> creating list with same size as input_array => O(n) -> populating this list with,
# n - len of input_array^^| correct end_points for every starting_point(Tap) => O(n) ->
#                           -> traversing this array again to find number of tap_points which intersects
#                           with previous intervals but not inside of them => O(n).
# Auxiliary space: O(n) -> fully copying input array indexes(size) and populating with the same type: INTs => O(n).
# --------------------------
# Ok. First we need to cover everything after and before every tap.
# Otherwise, answer to test with [0, 0, 0, 0] should be 4, and it's 0 cuz we can't cover space between them.
# So it's essentially task to find an overlapping interval from 0 to n, and count the biggest parts of it.
# Only problem is how?
# Hints:
# -> ! Create intervals of the area covered by each tap, sort intervals by the left end. !
# -> ! We need to cover the interval [0, n]. we can start with the first interval and out of all intervals
#      that intersect with it, we choose the one that covers the farthest point to the right. !
# -> ! What if there is a gap between intervals that is not covered ?
#      we should stop and return -1 as there is some interval that cannot be covered. !


test_n: int = 5
test: list[int] = [3, 4, 1, 1, 0, 0]
test_out: int = 1
assert test_out == min_taps(test_n, test)

test_n = 3
test = [0, 0, 0, 0]
test_out = -1
assert test_out == min_taps(test_n, test)

test = [randint(0, 100) for _ in range(randint(1, 10 ** 4))]
print(test)
test_n = len(test) - 1
print('-----------')
print(test_n)
