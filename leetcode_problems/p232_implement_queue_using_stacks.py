# Implement a first in first out (FIFO) queue using only two stacks.
# The implemented queue should support all the functions of a normal queue
#  (push, peek, pop, and empty).
# Implement the MyQueue class:
#  - void push(int x) Pushes element x to the back of the queue.
#  - int pop() Removes the element from the front of the queue and returns it.
#  - int peek() Returns the element at the front of the queue.
#  - boolean empty() Returns true if the queue is empty, false otherwise.
# Notes:
#  - You must use only standard operations of a stack,
#     which means only push to top, peek/pop from top, size, and is empty operations are valid.
#  - Depending on your language, the stack may not be supported natively.
#    You may simulate a stack using a list or deque (double-ended queue)
#     as long as you use only a stack's standard operations.
# ------------------------
# 1 <= x <= 9
# At most 100 calls will be made to push, pop, peek, and empty.
# All the calls to pop and peek are valid.
# ------------------------
# Follow-up: Can you implement the queue such that each operation
#  is amortized O(1) time complexity?
# In other words, performing n operations will take overall O(n) time
#  even if one of those operations may take longer.


class MyQueue:
    # working_sol (92.05%, 58.97%) -> (30ms, 16.53mb)  time: O(1) | space: O(n)
    def __init__(self):
        self.all_vals: list[int] = []
        self.front: int = 0

    def push(self, x: int) -> None:
        self.all_vals.append(x)

    def pop(self) -> int:
        # ! All the calls to pop and peek are valid. !
        # So, we don't need to check if we still have elements to pop().
        cur_front: int = self.all_vals[self.front]
        self.front += 1
        return cur_front

    def peek(self) -> int:
        return self.all_vals[self.front]

    def empty(self) -> bool:
        return self.front == len(self.all_vals)


# Time complexity:
#   All constant O(1).
# Auxiliary space:
#   Nothing takes extra space, except object of Class itself.
#   And it's size depends on added elements, linearly == O(n).

# Not doing test_cases, it's longer than actual task.
