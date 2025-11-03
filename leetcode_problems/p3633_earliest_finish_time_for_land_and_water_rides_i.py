# You are given two categories of theme park attractions: land rides and water rides.
# Land rides
#   landStartTime[i] – the earliest time the ith land ride can be boarded.
#   landDuration[i] – how long the ith land ride lasts.
# Water rides
#   waterStartTime[j] – the earliest time the jth water ride can be boarded.
#   waterDuration[j] – how long the jth water ride lasts.
# A tourist must experience exactly one ride from each category, in either order.
#   A ride may be started at its opening time or any later moment.
#   If a ride is started at time t, it finishes at time t + duration.
#   Immediately after finishing one ride the tourist may board the other
#    (if it is already open) or wait until it opens.
# Return the earliest possible time at which the tourist can finish both rides.
# --- --- --- ---
# 1 <= n, m <= 100
# landStartTime.length == landDuration.length == n
# waterStartTime.length == waterDuration.length == m
# 1 <= landStartTime[i], landDuration[i], waterStartTime[j], waterDuration[j] <= 1000


def earliest_finish_time(
    landStartTime: list[int],
    landDuration: list[int],
    waterStartTime: list[int],
    waterDuration: list[int],
) -> int:
    # working_solution: (55.51%, 94.06%) -> (322ms, 17.79mb)  Time: O(n * m) Space: O(1)
    out: int = 100_000
    # Land starts.
    for index in range(len(landStartTime)):
        land_start: int = landStartTime[index]
        land_duration: int = landDuration[index]
        land_end: int = land_start + land_duration
        for w_index in range(len(waterStartTime)):
            water_start: int = waterStartTime[w_index]
            if water_start < land_end:
                water_duration: int = waterDuration[w_index]
                water_end: int = land_end + water_duration
            else:
                water_duration: int = waterDuration[w_index]
                water_end: int = water_start + water_duration
            out = min(water_end, out)
    # Water starts.
    for w_index in range(len(waterStartTime)):
        water_start: int = waterStartTime[w_index]
        water_duration: int = waterDuration[w_index]
        water_end: int = water_start + water_duration
        for index in range(len(landStartTime)):
            land_start: int = landStartTime[index]
            if land_start < water_end:
                land_duration: int = landDuration[index]
                land_end: int = water_end + land_duration
            else:
                land_duration: int = landDuration[index]
                land_end: int = land_start + land_duration
            out = min(land_end, out)

    return out


# Time complexity: O(n * m) <- n - length of the input arrays `landStartTime` & `landDuration`,
#                              m - length of the input arrays `waterStartTime` & `waterDuration`.
# We double looping on both array => O(2 * n * m).
# --- --- --- ---
# Space complexity: O(1)


test_land_start: list[int] = [2, 8]
test_land_duration: list[int] = [4, 1]
test_water_start: list[int] = [6]
test_water_duration: list[int] = [3]
test_out: int = 9
assert test_out == earliest_finish_time(
    test_land_start,
    test_land_duration,
    test_water_start,
    test_water_duration,
)

test_land_start = [5]
test_land_duration = [3]
test_water_start = [1]
test_water_duration = [10]
test_out = 14
assert test_out == earliest_finish_time(
    test_land_start,
    test_land_duration,
    test_water_start,
    test_water_duration,
)
