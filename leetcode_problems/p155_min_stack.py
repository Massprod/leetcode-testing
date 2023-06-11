# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the MinStack class:
#   MinStack() initializes the stack object.
#   void push(int val) pushes the element val onto the stack.
#   void pop() removes the element on the top of the stack.
#   int top() gets the top element of the stack.
#   int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.
# --------------------
# -2 ** 31 <= val <= 2 ** 31 - 1
# Methods pop, top and getMin operations will always be called on non-empty stacks.
# At most 3 * 104 calls will be made to push, pop, top, and getMin.


class MinStack:

    def __init__(self):
        pass

    def push(self, val: int) -> None:
        pass

    def pop(self) -> None:
        pass

    def top(self) -> int:
        pass

    def getMin(self) -> int:
        pass


test1 = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
test1_val = [[], [-2], [0], [-3], [], [], [], []]
test1_out = [None, None, None, None, -3, None, 0, -2]
