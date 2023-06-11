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
# At most 3 * 10 ** 4 calls will be made to push, pop, top, and getMin.


class MinStack:

    def __init__(self):
        self.min_stack: list[tuple[int, int]] = []
        self.min_val: int | None = None

    def push(self, val: int) -> None:
        if self.min_val is None or self.min_val > val:
            self.min_val = val
        self.min_stack.append((val, self.min_val))

    def pop(self) -> None:
        self.min_stack.pop()
        if len(self.min_stack) == 0:
            self.min_val = None
        else:
            self.min_val = self.min_stack[-1][1]

    def top(self) -> int:
        return self.min_stack[-1][0]

    def getMin(self) -> int:
        return self.min_stack[-1][1]


# !
# Methods pop, top and getMin operations will always be called on non-empty stacks. !
# ^^This is why I ignore every check we actually should do, because pop() on empty is error, etc.
# --------------------
# It's all should be easy except this part -> retrieves the minimum element in the stack.
# Should we delete this and return, or just return?
# If we need to return and leave it be, then it's just list[0], but if it's removing than I should use deque().
# This wording is confusing, but I will assume that's just a return of value and nothing extra.


def t(test_case: list[str], test_vals: list, test_out: list) -> None:
    test: MinStack | None = None
    for x in range(len(test_case)):
        if test_case[x] == "MinStack":
            test = MinStack()
        elif test_case[x] == "push":
            test.push(test_vals[x][0])
        elif test_case[x] == "getMin":
            assert test_out[x] == test.getMin()
        elif test_case[x] == "pop":
            test.pop()
        elif test_case[x] == "top":
            assert test_out[x] == test.top()


test1 = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
test1_vals = [[], [-2], [0], [-3], [], [], [], []]
test1_out = [None, None, None, None, -3, None, 0, -2]
t(test1, test1_vals, test1_out)

# test2 - failed -> Ok. I considered case with empty stack refreshing of min_val, but didn't see most important
#                   case that we should change min_val on every pop(). Shame.
test2 = ["MinStack", "push", "push", "getMin", "getMin", "push", "getMin", "getMin", "top", "getMin", "pop", "push",
         "push", "getMin", "push", "pop", "top", "getMin", "pop"]
test2_vals = [[], [-10], [14], [], [], [-20], [], [], [], [], [], [10], [-7], [], [-7], [], [], [], []]
test2_out = [None, None, None, -10, -10, None, -20, -20, -20, -20, None, None, None, -10, None, None, -7, -10, None]
t(test2, test2_vals, test2_out)
