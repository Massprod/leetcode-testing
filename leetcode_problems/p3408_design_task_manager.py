# There is a task management system that allows users to manage their tasks,
#  each associated with a priority. The system should efficiently handle
#  adding, modifying, executing, and removing tasks.
# Implement the TaskManager class:
#  - TaskManager(vector<vector<int>>& tasks) initializes the task manager with a list
#   of user-task-priority triples. Each element in the input list is of the form
#   [userId, taskId, priority], which adds a task to the specified user with the given priority.
#  - void add(int userId, int taskId, int priority) adds a task with the specified taskId
#   and priority to the user with userId. It is guaranteed that taskId does not exist in the system.
#  - void edit(int taskId, int newPriority) updates the priority of the existing taskId
#   to newPriority. It is guaranteed that taskId exists in the system.
#  - void rmv(int taskId) removes the task identified by taskId from the system.
#   It is guaranteed that taskId exists in the system.
#  - int execTop() executes the task with the highest priority across all users.
#   If there are multiple tasks with the same highest priority,
#   execute the one with the highest taskId. After executing, the taskId is removed
#   from the system. Return the userId associated with the executed task.
#   If no tasks are available, return -1.
# Note that a user may be assigned multiple tasks.
# --- --- --- ---
# 1 <= tasks.length <= 10 ** 5
# 0 <= userId <= 10 ** 5
# 0 <= taskId <= 10 ** 5
# 0 <= priority <= 10 ** 9
# 0 <= newPriority <= 10 ** 9
# At most 2 * 10 ** 5 calls will be made in total to add, edit, rmv, and execTop methods.
# The input is generated such that taskId will be valid.
import heapq


class TaskManager:
    # working_solution: (72.07%, 33.21%) -> (495ms, 105.70mb)  Time: O(n * log n) Space: O(n)
    def __init__(self, tasks: list[list[int]]) -> None:
        # { task_id: [user_id, priority]} <- `priority` is negative for the `heapq`
        self.tasks: dict[int, list[int]] = {
            task_id: [user_id, priority]
            for user_id, task_id, priority in tasks
        }
        # [ (priority, task_id) ] <- min heap to get highest priority
        # `task_id` <- is negative to get the `highest` in order
        self.tasks_que: list[tuple[int, int]] = [
            (-1 * priority, -1 * task_id)
            for _, task_id, priority in tasks
        ]
        heapq.heapify(self.tasks_que)

    def add(self, user_id: int, task_id: int, priority: int) -> None:
        # ! It is guaranteed that taskId does not exist in the system !
        self.tasks[task_id] = [user_id, priority]
        heapq.heappush(
            self.tasks_que,
            (-1 * priority, -1 * task_id)
        )

    def edit(self, task_id: int, new_priority: int) -> None:
        # ! It is guaranteed that taskId exists in the system !
        self.tasks[task_id][1] = new_priority
        # Add a new priority task.
        heapq.heappush(
            self.tasks_que,
            (-1 * new_priority, -1 * task_id)
        )

    def rmv(self, task_id: int) -> None:
        # ! It is guaranteed that taskId exists in the system. !        
        self.tasks.pop(task_id)

    def execTop(self) -> int:
        if not self.tasks_que:
            return -1
        task_data: tuple[int, int] = heapq.heappop(self.tasks_que)
        # Task removed => skip.
        # Task changed priority => skip.
        while (
            self.tasks_que
            and
            (
            not self.tasks.get(-1 * task_data[1])             # reverse to original
            or
            -1 * task_data[0] != self.tasks[-1 * task_data[1]][1]  # reverse to original
            )
        ):
            task_data = heapq.heappop(self.tasks_que)
        # If it exist and can be executed => execute.
        task_priority, task_id = -1 * task_data[0], -1 * task_data[1]
        task_record: list[int] = self.tasks.get(task_id, [])
        # If record removed => skip | If record priority changed => skip.
        if not task_record or task_priority != task_record[1]:
            return -1
        user_id: int = task_record[0]
        self.rmv(task_id)
        return user_id


# Time complexity: O(n * log n) <- n - current length of the `self.tasks_que`.
# --- --- --- ---
# Space complexity: O(n)
