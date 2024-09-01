# You are given a string time in the form of  hh:mm, where some of the digits
#  in the string are hidden (represented by ?).
# The valid times are those inclusively between 00:00 and 23:59.
# Return the latest valid time you can get from time by replacing the hidden digits.
# -----------------------
# time is in the format hh:mm.
# It is guaranteed that you can produce a valid time from the given string.


def maximum_time(time: str) -> str:
    # working_sol (86.93%, 68.52%) -> (30ms, 16.48mb)  time: O(1) | space: O(1)
    out: list[str] = []
    hidden: str = '?'
    if hidden == time[0]:
        if hidden != time[1] and 3 < int(time[1]):
            out.append('1')
        else:
            out.append('2')
    else:
        out.append(time[0])
    if hidden == time[1]:
        if '1' == time[0] or '0' == time[0]:
            out.append('9')
        elif '2' == time[0] or hidden == time[0]:
            out.append('3')
    else:
        out.append(time[1])
    out.append(time[2])
    if hidden == time[3]:
        out.append('5')
    else:
        out.append(time[3])
    if hidden == time[4]:
        out.append('9')
    else:
        out.append(time[4])
    return ''.join(out)


# Time complexity: O(1)
# `time` is always of the same size, and we always do the same checks => O(1).
# -----------------------
# Auxiliary space: O(1)
# `out` <- always going to be of the same size as `time` => O(1).


test: str = "2?:?0"
test_out: str = "23:50"
assert test_out == maximum_time(test)

test = "0?:3?"
test_out = "09:39"
assert test_out == maximum_time(test)

test = "1?:22"
test_out = "19:22"
assert test_out == maximum_time(test)
