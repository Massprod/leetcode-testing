# You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].
# Implement the SmallestInfiniteSet class:
#   - SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
#   - int popSmallest() Removes and returns the smallest integer contained in the infinite set.
#   - void addBack(int num) Adds a positive integer num back into the infinite set,
#      if it is not already in the infinite set.
# ---------------------------
# 1 <= num <= 1000
# At most 1000 calls will be made in total to popSmallest and addBack.
import heapq


class SmallestInfiniteSet:
    # working_sol (76.69%, 93.50%) -> (112ms, 16.88mb)  time: below | space: O(1)

    def __init__(self):
        # Heapify all Values -> ! 1 <= num <= 1000 !
        self.original: heapq = [num for num in range(1, 1001)]
        heapq.heapify(self.original)
        # Save state of Added|Deleted for all Values.
        self.state: list[bool] = [True for _ in range(1001)]

    def popSmallest(self) -> int:
        # Delete ->
        smallest = heapq.heappop(self.original)
        # -> mark as Deleted.
        self.state[smallest] = False
        return smallest

    def addBack(self, num: int) -> None:
        # If marked as Deleted->
        if not self.state[num]:
            # -> return it ->
            heapq.heappush(self.original, num)
            # -> mark as Added.
            self.state[num] = True


# Time complexity:
#   initial: O(1) -> always creating 2 lists with 1000 and 1001 indexes => O(1).
#
#   popSmallest: O(log m) ->  removing the smallest element from a heapq => O(log m) ->
#   m - current values in heap^^| -> change state of the value => O(1).
#
#   addBack: O(log m) -> adding new value into a heap => O(log m) -> change state of the values => O(1).
#
# Auxiliary space: O(1) -> always creating same lists, and maximum sizes are reached from the start => O(1).
# ---------------------------
# Using heap to maintain order and pop() most left, otherwise I don't know how to maintain correct smallest value.
# Because if we just use set or list, we can't normally maintain smallest, like -> remove 1 - 10 values, add 1,
# smallest will become 1, after that delete 1, and how do we get smallest = 11? Only with min(), or other O(n) method.
# With heap, it's correctly sorted and always smallest value first.


test: list[list[int]] = [[], [2], [], [], [], [1], [], [], []]
test_out: list[int] = [None, None, 1, 2, 3, None, 1, 4, 5]
test_case = SmallestInfiniteSet()
for _ in test[1:]:
    if len(_) == 0:
        assert test_case.popSmallest() >= 1
    elif _[0]:
        assert test_case.addBack(_[0]) is None
