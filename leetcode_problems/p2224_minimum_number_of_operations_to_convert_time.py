# You are given two strings current and correct representing two 24-hour times.
# 24-hour times are formatted as "HH:MM", where HH is between 00 and 23,
#  and MM is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.
# In one operation you can increase the time current by 1, 5, 15, or 60 minutes.
# You can perform this operation any number of times.
# Return the minimum number of operations needed to convert current to correct.
# -------------------
# current and correct are in the format "HH:MM"
# current <= correct


def convert_time(current: str, correct: str) -> int:
    # working_sol (75.00%, 29.60%) -> (33ms, 16.63mb)  time: O(n) | space: O(1)
    out: int = 0
    if current == correct:
        return out
    #                      (hours_we_need - hours_we_have) * 60 - minutes_we_have + minutes_we_need
    mins_diff: int = (int(correct[:2]) - int(current[:2])) * 60 - int(current[3:]) + int(correct[3:])
    while mins_diff:
        if mins_diff >= 60:
            out += mins_diff // 60
            mins_diff %= 60
        elif mins_diff >= 15:
            out += mins_diff // 15
            mins_diff %= 15
        elif mins_diff >= 5:
            out += mins_diff // 5
            mins_diff %= 5
        elif mins_diff >= 1:
            out += mins_diff // 1
            mins_diff %= 1
    return out


# Time complexity: O(n) <- n - difference in minutes between `correct` and `current`.
# There's only minutes_difference which affects our timerun.
# And we can't get it just from input, so it's only after calc of `mins_diff`.
# -------------------
# Auxiliary space: O(1)


test_current: str = "02:30"
test_correct: str = "04:35"
test_out: int = 3
assert test_out == convert_time(test_current, test_correct)

test_current = "11:00"
test_correct = "11:01"
test_out = 1
assert test_out == convert_time(test_current, test_correct)
