# Design a stack that supports increment operations on its elements.
# Implement the CustomStack class:
#  - CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack.
#  - void push(int x) Adds x to the top of the stack if the stack has not reached the maxSize.
#  - int pop() Pops and returns the top of the stack or -1 if the stack is empty.
#  - void inc(int k, int val) Increments the bottom k elements of the stack by val.
#    If there are less than k elements in the stack, increment all the elements in the stack.
# --------------------------
# 1 <= maxSize, x, k <= 1000
# 0 <= val <= 100
# At most 1000 calls will be made to each method of increment, push and pop each separately.


class CustomStack:
    # working_sol (62.59%, 87.29%) -> (88ms, 17.43mb)
    def __init__(self, maxSize: int):
        self.stack: list[int] = []
        self.size: int = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.size:
            self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        for index in range(min(k, len(self.stack))):
            self.stack[index] += val


# Time complexity:
#   `push`: O(1)
#   `pop`: O(1)
#   `increment`: O(k)
# Auxiliary space:
#   `init`|`classObject`: O(n) <- n - appended elements.
