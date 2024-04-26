# You have a lock in front of you with 4 circular wheels.
# Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'.
# The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'.
# Each move consists of turning one wheel one slot.
# The lock initially starts at '0000', a string representing the state of the 4 wheels.
# You are given a list of deadends dead ends, meaning if the lock displays any of these codes,
#  the wheels of the lock will stop turning and you will be unable to open it.
# Given a target representing the value of the wheels that will unlock the lock,
#  return the minimum total number of turns required to open the lock, or -1 if it is impossible.
# -------------------------------
# 1 <= deadends.length <= 500
# deadends[i].length == 4
# target.length == 4
# target will not be in the list deadends.
# target and deadends[i] consist of digits only.
from collections import deque


def open_lock(deadends: list[str], target: str) -> int:
    # working_sol (91.79%, 80.21%) -> (288ms, 17.97mb)  time: O(4 * (d + 10 ** 4)) | space: O(4 * (d + 10 ** 4))
    cur_comb: str
    turns: int
    turn_left: dict[str, str] = {
        '0': '1',
        '1': '2',
        '2': '3',
        '3': '4',
        '4': '5',
        '5': '6',
        '6': '7',
        '7': '8',
        '8': '9',
        '9': '0',
    }
    turn_right: dict[str, str] = {
        '0': '9',
        '1': '0',
        '2': '1',
        '3': '2',
        '4': '3',
        '5': '4',
        '6': '5',
        '7': '6',
        '8': '7',
        '9': '8',
    }
    fast_deadends: set[str] = set(deadends)
    # Lock initially starts at '0000'.
    initial_state: str = '0000'
    if target in fast_deadends or initial_state in fast_deadends:
        return -1
    # [(state, turns)]
    que: deque[tuple[str, int]] = deque([(initial_state, 0)])
    visited: set[str] = {initial_state}
    while que:
        cur_comb, turns = que.popleft()
        if target == cur_comb:
            return turns
        for turn_option in range(4):
            # Right turn of the wheel.
            new_comb: str = cur_comb[:turn_option] + turn_right[cur_comb[turn_option]] + cur_comb[turn_option + 1:]
            if new_comb not in visited and new_comb not in fast_deadends:
                que.append((new_comb, turns + 1))
                visited.add(new_comb)
            # Left turn of the wheel.
            new_comb = cur_comb[:turn_option] + turn_left[cur_comb[turn_option]] + cur_comb[turn_option + 1:]
            if new_comb not in visited and new_comb not in fast_deadends:
                que.append((new_comb, turns + 1))
                visited.add(new_comb)
    return -1


# Time complexity: O(4 * (d + 10 ** 4)) <- d - length of an input array `deadends`.
# -------------------------------
# Auxiliary space: O(4 * (d + 10 ** 4))
# -------------------------------
# Explanation in editorial, it's too good, and I failed complexity desc by myself...


test_deadends: list[str] = ["0201", "0101", "0102", "1212", "2002"]
test_target: str = "0202"
test_out: int = 6
assert test_out == open_lock(test_deadends, test_target)

test_deadends = ["8888"]
test_target = "0009"
test_out = 1
assert test_out == open_lock(test_deadends, test_target)

test_deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
test_target = "8888"
test_out = -1
assert test_out == open_lock(test_deadends, test_target)

test_deadends = ["0000"]
test_target = "8888"
test_out = -1
assert test_out == open_lock(test_deadends, test_target)
