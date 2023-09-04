# You are given two 0-indexed integer arrays servers and tasks of lengths n and m respectively.
# servers[i] is the weight of the i server, and tasks[j] is the time needed to process the j-th task in seconds.
# Tasks are assigned to the servers using a task queue.
# Initially, all servers are free, and the queue is empty.
# At second j, the jth task is inserted into the queue (starting with the 0th task being inserted at second 0).
# As long as there are free servers and the queue is not empty,
#  the task in the front of the queue will be assigned to a free server with the smallest weight,
#  and in case of a tie, it is assigned to a free server with the smallest index.
# If there are no free servers and the queue is not empty,
#  we wait until a server becomes free and immediately assign the next task.
# If multiple servers become free at the same time,
#  then multiple tasks from the queue will be assigned in order of insertion
#  following the weight and index priorities above.
# A server that is assigned task j at second t will be free again at second t + tasks[j].
# Build an array ans of length m, where ans[j] is the index of the server the j-th task will be assigned to.
# Return the array ans.
# --------------------
# servers.length == n
# tasks.length == m
# 1 <= n, m <= 2 * 10 ** 5
# 1 <= servers[i], tasks[j] <= 2 * 10 ** 5
import heapq
from random import randint


def assign_tasks(servers: list[int], tasks: list[int]) -> list[int]:
    # working_sol (77.91%, 5.43%) -> (1618ms, 83mb)  time: O(k * log n + n * log n) | space: O(3n + k)
    if len(servers) == 1:
        return [0 for _ in tasks]
    # Servers available to use by weights.
    s_available_weights: list[int] = []
    heapq.heapify(s_available_weights)
    # Indexes of available servers by their weight.
    s_weight_indexes: dict[int, list[int]] = {}
    for x in range(len(servers)):
        weight: int = servers[x]
        if servers[x] in s_weight_indexes:
            heapq.heappush(s_weight_indexes[weight], x)
            continue
        s_weight_indexes[weight] = [x]
        heapq.heapify(s_weight_indexes[weight])
        heapq.heappush(s_available_weights, weight)
    # Task timers stored as: (endtime, weight, index).
    s_task_timer: list[tuple[int, int, int]] = []
    heapq.heapify(s_task_timer)
    cur_time: int = 0
    cur_task: int = 0
    assignments: list[int] = []
    while cur_task != len(tasks):
        while s_task_timer:
            # Free server and add into available, if we can.
            if s_task_timer[0][0] <= cur_time:
                free_server: tuple[int, int, int] = heapq.heappop(s_task_timer)
                free_weight: int = free_server[1]
                free_index: int = free_server[2]
                heapq.heappush(s_available_weights, free_weight)
                heapq.heappush(s_weight_indexes[free_weight], free_index)
            else:
                break
        # Assign server to a task if there's Free one.
        if s_available_weights:
            # Minimal weight.
            server_weight: int = s_available_weights[0]
            # Minimal index, if present.
            if not s_weight_indexes[server_weight]:
                # If not, delete this weight from available.
                heapq.heappop(s_available_weights)
                continue
            server_index: int = heapq.heappop(s_weight_indexes[server_weight])
            task_timer: tuple[int, int, int] = (
                cur_time + tasks[cur_task],  # Time of completion.
                server_weight,  # Weight of server assigned.
                server_index,  # Index of server assigned.
            )
            heapq.heappush(s_task_timer, task_timer)
            assignments.append(server_index)
            cur_task += 1
        else:
            # If no free servers, we should use First server which going to complete set task.
            # Apply weight, index rules to it. Heap is already doing it: (time, weight, index).
            # And increment it's time, so it's going to instantly run another task when prev done.
            task_timer = heapq.heappop(s_task_timer)
            task_timer = (
                task_timer[0] + tasks[cur_task],  # New time of completion.
                task_timer[1],
                task_timer[2],
            )
            heapq.heappush(s_task_timer, task_timer)
            assignments.append(task_timer[2])
            cur_task += 1
        cur_time += 1
    return assignments


# Time complexity: O(k * log n + n * log n) -> for every weight in servers adding weight into a heap, and for every
# n - len of servers_array^^| weight creating heap with all indexes assigned to it => O(n) -> for every task presented
# k - len of tasks_array^^|   essentially doing same heappush() and heappop() which is O(log n) for servers,
#                             and O(log k) for tasks -> guess worst case is 10 servers and 10 ** 5 tasks,
#                             and tasks will end only on last task, so for every task except last we're doing
#                             O((k - 1) * log n) and for last index we're extra freeing all servers =>
#                             => O(n * (log n + log n + log n)), server tasks, weights and indexes heaps are equal size
#                             O((k - 1) * log n + n * log n), and last task is going to be pushed as available,
#                             heappop() from all server weights O(log n) and O(1) for pushing as a new task_timer,
#                             at this moment task_timers are empty => O(k * log n + n * log n), should be correct.
# Auxiliary space: O(3n + k) -> heap with all server weights stored => O(n) ->
#                    -> dictionary with all indexes of servers as keys and heaps with their weight as values => O(n) ->
#                    -> s_task_timer: heap with at maximum size of all servers => O(n) ->
#                    -> assignments: list with all servers assigned to a tasks, size of input_task_array => O(k).
# --------------------
# Even explanation of this guy is ridiculous. Like even with tasks saved in some backlog,
#  and assigning them instantly when some server is freed still Fails.
# Googled that we can just increment already stored time. Which is logical, but this description is garba...
# We can assign them all instantly, but we can assign them to the fastest server as continuation.
# So everything, except instant reuse of servers was correct, and for reuse of freed servers we can just take
#  servers which going to be freed first (there's can be multiple) filter them on weight and just add time.
# Extra, didn't know that heap is sorting tuple not just by 0 value, but all of them ->
# -> so we can just save (time, weight, index), instead of (time, index, weight) and extra filter them on weight.
# Actually instead of dictionaries to filter weight, now I can easily use a heap. Maybe rebuild later.
# --------------------
# !
# Failing this test case means you're incrementing time when you don't need to.
# Consider the following (much simpler) scenario:
#   servers:
#   [1, 20, 300]
#
#   tasks:
#   [10, 9, 8, 1, 1, 1]
#
# The first 3 tasks come in-- going to server 0, server 1, and then server 2 respectively.
# All 3 of these will finish simultaneously at time = 10 sec.
# At this point, the last 3 tasks are all waiting to be launched (they are "backlogged", not streaming in).
# The correct answer is that at time = 10, you launch all 3 "backlogged" tasks immediately (one on each server).
# However, if you're not handling this case (and incrementing time when you don't need to),
#  the 4th task will be assigned to server 0... server 0 will finish that task in 1 sec,
#  and then the 5th (and similarly the 6th) task will run on server 0.
# This larger test case ends up being impacted by the above scenario, just in a much more complex situation.
# !
# Ok. This is why im failing, when multiple servers are freed at the same time, we need to add multiple tasks at once.
# --------------------
# All easy. But how to correctly maintain weight check for max_constraints.
# Like if I just use sorted set() with all weights it could be O(n) for every second check.
# Heap should be faster, but I will need to delete weights from it and return after task is complete.
# So first dict with available indexes into a heap as values, and keys == weights.
# Second dict with end times of tasks as keys and tuple[weight, index] for returning.
# And maintain heap with all weights, should be correct. Let's try.


test: list[int] = [3, 3, 2]
test_tasks: list[int] = [1, 2, 3, 2, 1, 2]
test_out: list[int] = [2, 2, 0, 2, 1, 2]
assert test_out == assign_tasks(test, test_tasks)

test = [5, 1, 4, 3, 2]
test_tasks = [2, 1, 2, 4, 5, 2, 1]
test_out = [1, 4, 1, 4, 1, 3, 2]
assert test_out == assign_tasks(test, test_tasks)

test = [5, 5, 9, 9, 9, 5, 10]
test_tasks = [9, 9, 9, 6, 7, 3, 1, 10, 8, 6, 8, 9, 5, 7, 8, 3, 7, 3, 3, 7]
test_out = [0, 1, 5, 2, 3, 4, 6, 6, 4, 0, 1, 5, 2, 3, 0, 4, 2, 6, 1, 4]
assert test_out == assign_tasks(test, test_tasks)

test = [1, 20, 300]
test_tasks = [10, 9, 8, 1, 1, 1]
test_out = [0, 1, 2, 0, 1, 2]
assert test_out == assign_tasks(test, test_tasks)

test = [randint(1, 2 * 10 ** 5) for _ in range(randint(1, 10 ** 1))]
test_tasks = [randint(1, 2 * 10 ** 5) for _ in range(randint(1, 10 ** 3))]
print(test)
print('--------------')
print(test_tasks)
