# You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].
# Implement the SmallestInfiniteSet class:
#   SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
#   int popSmallest() Removes and returns the smallest integer contained in the infinite set.
#   void addBack(int num) Adds a positive integer num back into the infinite set,
#       if it is not already in the infinite set.
# ---------------------------
# 1 <= num <= 1000
# At most 1000 calls will be made in total to popSmallest and addBack.
import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.original: heapq = [num for num in range(1, 1001)]
        heapq.heapify(self.original)
        self.removed: set[int] = set()

    def popSmallest(self) -> int:
        smallest = heapq.heappop(self.original)
        self.removed.add(smallest)
        return smallest

    def addBack(self, num: int) -> None:
        if num in self.removed:
            heapq.heappush(self.original, num)


# Using heap to maintain order and pop() most left, otherwise I don't know how to maintain correct smallest value.
# Because if we just use set or list, we can't normally maintain smallest, like -> remove 1 - 10 values, add 1,
# smallest will become 1, after that delete 1, and how do we get smallest = 11? Only with min(), or other O(n) method.
# With heap, it's correctly sorted and always smallest value first.


test1 = [[], [2], [], [], [], [1], [], [], []]
test1_out = [None, None, 1, 2, 3, None, 1, 4, 5]
test = SmallestInfiniteSet()
for _ in test1[1:]:
    if len(_) == 0:
        assert test.popSmallest() >= 1
    elif _[0]:
        assert test.addBack(_[0]) is None
