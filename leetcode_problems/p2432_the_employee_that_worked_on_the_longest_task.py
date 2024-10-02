# There are n employees, each with a unique id from 0 to n - 1.
# You are given a 2D integer array logs where logs[i] = [idi, leaveTimei] where:
#  - idi is the id of the employee that worked on the ith task, and
#  - leaveTimei is the time at which the employee finished the ith task. All the values leaveTimei are unique.
# Note that the ith task starts the moment right after the (i - 1)th task ends, and the 0th task starts at time 0.
# Return the id of the employee that worked the task with the longest time.
# If there is a tie between two or more employees, return the smallest id among them.
# ------------------------
# 2 <= n <= 500
# 1 <= logs.length <= 500
# logs[i].length == 2
# 0 <= idi <= n - 1
# 1 <= leaveTimei <= 500
# idi != idi+1
# leaveTimei are sorted in a strictly increasing order.


def hardest_worker(n: int, logs: list[list[int]]) -> int:
    # working_sol (80.10%, 95.92%) -> (251ms, 16.46mb)  time: O(m) | space: O(1)
    worker: int = logs[0][0]
    longest: int = logs[0][1]
    for index in range(1, len(logs)):
        cur_time: int = logs[index][1] - logs[index - 1][1]
        cur_worker: int = logs[index][0]
        if cur_time > longest:
            worker = cur_worker
            longest = cur_time
        elif cur_time == longest:
            worker = min(worker, cur_worker)
    return worker


# Time complexity: O(m) <- m - length of the input array `logs`.
# Always traversing whole input array `logs`, once => O(m)
# ------------------------
# Auxiliary space: O(1).


test_n: int = 10
test_logs: list[list[int]] = [[0, 3], [2, 5], [0, 9], [1, 15]]
test_out: int = 1
assert test_out == hardest_worker(test_n, test_logs)

test_n = 26
test_logs = [[1, 1], [3, 7], [2, 12], [7, 17]]
test_out = 3
assert test_out == hardest_worker(test_n, test_logs)

test_n = 2
test_logs = [[0, 10], [1, 20]]
test_out = 0
assert test_out == hardest_worker(test_n, test_logs)
