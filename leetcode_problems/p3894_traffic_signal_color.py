# You are given an integer timer representing the remaining time (in seconds)
#  on a traffic signal.
# The signal follows these rules:
#  - If timer == 0, the signal is "Green"
#  - If timer == 30, the signal is "Orange"
#  - If 30 < timer <= 90, the signal is "Red"
# Return the current state of the signal.
# If none of the above conditions are met, return "Invalid".
# --- --- --- ---
# 0 <= timer <= 1000


def traffic_signal(timer: int) -> str:
    # working_solution: (100%, 100%) -> (1ms, 19.30mb)  Time: O(1) Space: O(1)
    if 0 == timer:
        return 'Green'
    elif 30 == timer:
        return 'Orange'
    elif 30 < timer <= 90:
        return 'Red'

    return 'Invalid'


# Time complexity: O(1)
# --- --- --- ---
# Space complexity: O(1)


test: int = 60
test_out: str = 'Red'
assert test_out == traffic_signal(test)

test = 5
test_out = 'Invalid'
assert test_out == traffic_signal(test)
