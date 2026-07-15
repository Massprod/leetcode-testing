# You are given two valid times startTime and endTime,
#  each represented as a string in the format "HH:MM:SS".
# Return the number of seconds that have elapsed from startTime to endTime.
# --- --- --- ---
# startTime.length == 8
# endTime.length == 8
# startTime and endTime are valid times in the format "HH:MM:SS"
# 00 <= HH <= 23
# 00 <= MM <= 59
# 00 <= SS <= 59
# endTime is not earlier than startTime


def seconds_between_time(startTime: str, endTime: str) -> int:
    # working_solution: (100%, 63.39%) -> (0ms, 19.23mb)  Time: O(n) Space: O(1)
    def get_seconds(time: str) -> int:
        hours: int = int(time[:2])
        minutes: int = int(time[3:5])
        seconds: int = int(time[6:])
        out: int = hours * 60 * 60 + minutes * 60 + seconds
        
        return out
    
    seconds_start: int = get_seconds(startTime)
    seconds_end: int = get_seconds(endTime)

    return seconds_end - seconds_start


# Time complexity: O(n)
# n - length of the input strings `startTime` or `endTime`
# --- --- --- ---
# Space complexity: O(1)


test_start: str = '01:00:00'
test_end: str = '01:00:25'
test_out: int = 25
assert test_out == seconds_between_time(test_start, test_end)

test_start = '12:34:56'
test_end = '13:00:00'
test_out = 1504
assert test_out == seconds_between_time(test_start, test_end)
