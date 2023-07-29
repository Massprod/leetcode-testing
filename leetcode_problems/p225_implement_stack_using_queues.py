# Implement a last-in-first-out (LIFO) stack using only two queues.
# The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).
# Implement the MyStack class:
#   void push(int x) Pushes element x to the top of the stack.
#   int pop() Removes the element on the top of the stack and returns it.
#   int top() Returns the element on the top of the stack.
#   boolean empty() Returns true if the stack is empty, false otherwise.
# Notes:
# You must use only standard operations of a queue,
#   which means that only push to back, peek/pop from front, size and is empty operations are valid.
# ------------------
# 1 <= x <= 9
# At most 100 calls will be made to push, pop, top, and empty.
# All the calls to pop and top are valid.
# ------------------
# Follow-up: Can you implement the stack using only one queue?


class MyStack:
    # working_sol (93.87%, 95.21%) -> (37ms, 16.28mb)

    def __init__(self):
        self.stack: list[int] = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        if len(self.stack) == 0:
            return True
        return False


# Time complexity:
#   initiation: O(1) -> always empty list.
#   push: O(1) -> always just append.
#   pop: O(1) -> always just list.pop().
#   top: O(1) -> always just list[-1].
#   empty: O(1) -> simple check for len of a list.
# ------------------
# Follow-up: Can you implement the stack using only one queue?
# What? It basically just list with [-1] pop or just returned. Why there's more than 1 que?
# Don't get this follow_up like what does it even mean if we're allowed to use list?
# And even if I use deque, it's even simplier and still only ONE. Hard question is how we can do this with 2 ques?
