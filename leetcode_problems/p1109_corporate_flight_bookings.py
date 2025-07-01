# There are n flights that are labeled from 1 to n.
# You are given an array of flight bookings bookings,
#  where bookings[i] = [firsti, lasti, seatsi] represents a booking for flights
#  firsti through lasti (inclusive) with seatsi seats reserved for each flight in the range.
# Return an array answer of length n, where answer[i]
#  is the total number of seats reserved for flight i.
# -------------------------
# 1 <= n <= 2 * 10 ** 4
# 1 <= bookings.length <= 2 * 10 ** 4
# bookings[i].length == 3
# 1 <= firsti <= lasti <= n
# 1 <= seatsi <= 10 ** 4


def corp_flight_bookings(bookings: list[list[int]], n: int) -> list[int]:
    # working_sol (78.12%, 15.57%) -> (23ms, 29.15mb)  time: O(m) | space: O(n)
    out: list[int] = [0 for _ in range(n)]
    for start, end, value in bookings:
        out[start - 1] += value
        if end < n:
            out[end] -= value
    for index in range(1, n):
        out[index] += out[index - 1]

    return out


# Time complexity: O(m) <- m - length of the input array `bookings`.
# Traversing the whole input array `bookings`, once => O(m).
# -------------------------
# Auxiliary space: O(n)
# `out` <- allocates space for `n` values => O(n).


test: list[list[int]] = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
test_n: int = 5
test_out: list[int] = [10, 55, 45, 25, 25]
assert test_out == corp_flight_bookings(test, test_n)

test = [[1, 2, 10], [2, 2, 15]]
test_n = 2
test_out = [10, 25]
assert test_out == corp_flight_bookings(test, test_n)
