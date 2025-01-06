# You are given a 2D array events which represents a sequence of events where
#  a child pushes a series of buttons on a keyboard.
# Each events[i] = [indexi, timei] indicates that the button
#  at index indexi was pressed at time timei.
#  - The array is sorted in increasing order of time.
#  - The time taken to press a button is the difference in time between
#    consecutive button presses.
#    The time for the first button is simply the time at which it was pressed.
# Return the index of the button that took the longest time to push.
# If multiple buttons have the same longest time,
#  return the button with the smallest index.
# -----------------------
# 1 <= events.length <= 1000
# events[i] == [indexi, timei]
# 1 <= indexi, timei <= 10 ** 5
# The input is generated such that events is sorted in increasing order of timei.


def button_with_longest_time(events: list[list[int]]) -> int:
    # working_sol: (100.00%, 71.27%) -> (0ms, 17.66mb)  time: O(n) | space: O(1)
    pushed_index: int
    pushed_time: int
    pushed_index, pushed_time = events[0]
    for index in range(1, len(events)):
        new_time: int = events[index][1] - events[index - 1][1]
        if pushed_time < new_time:
            pushed_index, pushed_time = events[index][0], new_time
        elif pushed_time == new_time:
            pushed_index = min(pushed_index, events[index][0])
    return pushed_index


# Time complexity: O(n) <- n - length of the input array `events`
# Always traversing whole input array `events`, once => O(n).
# -----------------------
# Auxiliary space: O(1)
# Only 2 constant INTs used, none of them depends on input => O(1).


test: list[list[int]] = [[1,2],[2,5],[3,9],[1,15]]
test_out: int = 1
assert test_out == button_with_longest_time(test)

test = [[10,5],[1,7]]
test_out = 10
assert test_out == button_with_longest_time(test)
