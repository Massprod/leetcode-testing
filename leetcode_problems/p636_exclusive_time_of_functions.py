# On a single-threaded CPU, we execute a program containing n functions.
# Each function has a unique ID between 0 and n-1.
# Function calls are stored in a call stack: when a function call starts,
#  its ID is pushed onto the stack, and when a function call ends,
#  its ID is popped off the stack. The function whose ID is at the top of the stack
#  is the current function being executed.
# Each time a function starts or ends, we write a log with the ID,
#  whether it started or ended, and the timestamp.
# You are given a list logs, where logs[i] represents the ith log message
#  formatted as a string "{function_id}:{"start" | "end"}:{timestamp}".
# For example, "0:start:3" means a function call with function ID 0 started
#  at the beginning of timestamp 3, and "1:end:2" means a function call
#  with function ID 1 ended at the end of timestamp 2.
# Note that a function can be called multiple times, possibly recursively.
# A function's exclusive time is the sum of execution times for all function calls
#  in the program. For example, if a function is called twice,
#  one call executing for 2 time units and another call executing for 1 time unit,
#  the exclusive time is 2 + 1 = 3.
# Return the exclusive time of each function in an array,
#  where the value at the ith index represents the exclusive time
#  for the function with ID i.
# --- --- --- ---
# 1 <= n <= 100
# 2 <= logs.length <= 500
# 0 <= function_id < n
# 0 <= timestamp <= 10 ** 9
# No two start events will happen at the same timestamp.
# No two end events will happen at the same timestamp.
# Each function has an "end" log for each "start" log.


def exclusive_time(n: int, logs: list[str]) -> list[int]:
    # working_solution: (71.03%, 13.85%) -> (6ms, 19.61mb)  Time: O(m) Space: O(n + m)
    start_time: int
    busy_time: int
    time_spent: int

    out: list[int] = [0 for _ in range(n)]
    # 0 <= function_id < n ! we can ignore -1 for busy_box    
    # [ (process_id, time_start), (process_id, time_end), (-1, time_busy) ]
    stack: list[tuple[int, int]] = []
    events: list[list[str]] = [log.split(":") for log in logs]
    event_start: str = "start"
    for process_id, event, timestamp in events:
        process_id = int(process_id)
        timestamp = int(timestamp)
        if event_start == event:
            stack.append(
                (process_id, timestamp)
            )
            continue
        last_event: int = stack[-1][0]
        # We can't have only `busy_box`, so it's fine to check like this.
        if -1 == last_event and process_id == stack[-2][0]:
            busy_time = stack.pop()[1]
            start_time = stack.pop()[1]
            # All time for task - busy_box
            time_spent = (timestamp - start_time) + 1 - busy_time  # 0 - indexed
            out[process_id] += time_spent
            # Gather all of the CPU busy time.
            run_sum: int = busy_time + time_spent
            while stack and -1 == stack[-1][0]:
                run_sum += stack.pop()[1]
            stack.append(
                (-1, run_sum)
            )
            continue
        if process_id != stack[-1][0]:
            stack.append(
                (process_id, timestamp)
            )
        else:
            start_time = stack.pop()[1]
            time_spent = (timestamp - start_time) + 1  # 0 - indexed
            out[process_id] += time_spent
            if stack:
                # Expend period, when cpu was busy.
                if -1 == stack[-1][0]:
                    stack[-1] = (stack[-1][0], stack[-1][1] + time_spent)
                # Or start a new period.
                else:
                    stack.append(
                        (-1, time_spent)
                    )

    return out


# Time complexity: O(m)
# m - length of the input array `logs`
# --- --- --- ---
# Space complexity: O(n + m)


test_n: int = 2
test_logs: list[str] = [
    "0:start:0", "1:start:2", "1:end:5", "0:end:6"
]
test_out: list[int] = [3, 4]
assert test_out == exclusive_time(test_n, test_logs)

test_n = 1
test_logs = [
    "0:start:0", "0:start:2", "0:end:5", "0:start:6", "0:end:6", "0:end:7"
]
test_out = [8]
assert test_out == exclusive_time(test_n, test_logs)

test_n = 2
test_logs = [
    "0:start:0", "0:start:2", "0:end:5", "1:start:6", "1:end:6", "0:end:7"
]
test_out = [7, 1]
assert test_out == exclusive_time(test_n, test_logs)

test_n = 1
test_logs = [
    "0:start:0", "0:start:1", "0:start:2", "0:end:3", "0:end:4", "0:end:5"
]
test_out = [6]
assert test_out == exclusive_time(test_n, test_logs)
