# You are given a positive integer days representing the total number of days
#  an employee is available for work (starting from day 1).
# You are also given a 2D array meetings of size n where, meetings[i] = [start_i, end_i]
#  represents the starting and ending days of meeting i (inclusive).
# Return the count of days when the employee is available
#  for work but no meetings are scheduled.
# Note: The meetings may overlap.
# --------------------------
# 1 <= days <= 10 ** 9
# 1 <= meetings.length <= 10 ** 5
# meetings[i].length == 2
# 1 <= meetings[i][0] <= meetings[i][1] <= days


def count_days(days: int, meetings: list[list[int]]) -> int:
    # working_sol (57.25%, 86.51%) -> (179ms, 52.68mb)  time: O(n * log n) | space: O(n)
    # We can either merge all ranges and count how many free days bettwen them.
    # Or, because while we're merging we already check for overlaps.
    # We can just ignore these overlaps and count empty days directly.
    out: int = 0
    prev_range_end: int = 0
    meetings.sort()

    for start, end in meetings:
        # +1 because we don't need ranges which starts on the prev end.
        # Like: [1, 2], [3, 5] <- no free days.
        if start > prev_range_end + 1:
            # -1 because we don't need to include the next range start.
            # Like: [1, 2], [4, 5] <- 4 is excluded => -1
            out += start - prev_range_end - 1
        prev_range_end = max(prev_range_end, end)

    # Ranges might not cover every day.
    # So, we need to check for the extra free days.
    leftovers: int = days - prev_range_end
    return out + leftovers


# Time complexity: O(n * log n) <- n - length of the input array `meetings`
# Always sorting `meetings`, once => O(n * log n).
# Extra traversing whole input array `meetings`, once => O((n * log n) + n).
# --------------------------
# Auxiliary space: O(n)
# `sort` <- takes O(n) => O(n).
# Extra 3 constant INTs, none of them depends on input.


test_days: int = 10
test_meetings: list[list[int]] = [[5, 7], [1, 3], [9, 10]]
test_out: int = 2
assert test_out == count_days(test_days, test_meetings)

test_days = 5
test_meetings = [[2, 4], [1, 3]]
test_out = 1
assert test_out == count_days(test_days, test_meetings)

test_days = 6
test_meetings = [[1, 6]]
test_out = 0
assert test_out == count_days(test_days, test_meetings)
