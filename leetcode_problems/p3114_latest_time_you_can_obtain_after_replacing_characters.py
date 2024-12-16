# You are given a string s representing a 12-hour format time where some of the digits
#  (possibly none) are replaced with a "?".
# 12-hour times are formatted as "HH:MM", where HH is between 00 and 11, and MM is between 00 and 59.
# The earliest 12-hour time is 00:00, and the latest is 11:59.
# You have to replace all the "?" characters in s with digits such that the time we obtain
#  by the resulting string is a valid 12-hour format time and is the latest possible.
# Return the resulting string.
# ----------------------------
# s.length == 5
# s[2] is equal to the character ":".
# All characters except s[2] are digits or "?" characters.
# The input is generated such that there is at least one time between "00:00" and "11:59"
#  that you can obtain after replacing the "?" characters.


def find_latest_time(s: str) -> str:
    # working_sol (37.98%, 23.76%) -> (40ms, 17.13mb)  time: O(1) | space: O(1)
    out: list[str] = list(s)
    hidden: str = '?'
    h_first: str = s[0]
    h_second: str = s[1]
    m_first: str = s[3]
    m_second: str = s[4]
    if hidden == h_first and hidden == h_second:
        out[0], out[1] = '1', '1'
    elif hidden == h_first:
        if 1 < int(h_second):
            out[0] = '0'
        else:
            out[0] = '1'
    elif hidden == h_second:
        if 1 == int(h_first):
            out[1] = '1'
        else:
            out[1] = '9'
    if hidden == m_first:
        out[3] = '5'
    if hidden == m_second:
        out[4] = '9'
    return ''.join(out)


# Time complexity: O(1)
# Always the same checks => O(1).
# ----------------------------
# Auxiliary space: O(1)
# Always the same input type/size => O(1)


test: str = "1?:?4"
test_out: str = "11:54"
assert test_out == find_latest_time(test)

test = "0?:5?"
test_out = "09:59"
assert test_out == find_latest_time(test)
