# The median is the middle value in an ordered integer list.
# If the size of the list is even, there is no middle value,
#  and the median is the mean of the two middle values.
#  - For example, for arr = [2,3,4], the median is 3.
#  - For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:
#  - MedianFinder() initializes the MedianFinder object.
#  - void addNum(int num) adds the integer num from the data stream to the data structure.
#  - double findMedian() returns the median of all elements so far.
#    Answers within 10 ** -5 of the actual answer will be accepted.
# -----------------------
# -10 ** 5 <= num <= 10 ** 5
# There will be at least one element in the data structure before calling findMedian.
# At most 5 * 10 ** 4 calls will be made to addNum and findMedian.
import heapq
from random import choice, randint


class MedianFinder:
    # working_sol (92.24%, 47.8%) -> (421ms, 38.3mb)

    def __init__(self):
        # Middle -> lowest value. Reversed heap, so we can reach middle in O(1).
        self.left_side: list[int] = []
        # Middle -> highest value.
        self.right_side: list[int] = []
        heapq.heapify(self.left_side)
        heapq.heapify(self.right_side)

    def addNum(self, num: int) -> None:
        # First value.
        if not self.right_side:
            heapq.heappush(self.right_side, num)
            return
        # For correct Median indexing, we need to maintain:
        # Middle -> lowest value for left_side, Middle -> Highest value for right_side.
        if num >= self.right_side[0]:
            heapq.heappush(self.right_side, num)
        else:
            heapq.heappush(self.left_side, num * -1)
        # We need both sides either equal or diff in length == 1.
        # Because we need ODD|EVEN in full, to take correct Median.
        # Left > Right
        if len(self.left_side) - len(self.right_side) == 2:
            heapq.heappush(self.right_side, heapq.heappop(self.left_side) * -1)
        # Right > Left
        elif len(self.right_side) - len(self.left_side) == 2:
            heapq.heappush(self.left_side, heapq.heappop(self.right_side) * -1)

    def findMedian(self) -> float:
        # Full size is ODD.
        if (len(self.left_side) + len(self.right_side)) % 2:
            # Middle on the left side.
            if len(self.left_side) > len(self.right_side):
                return self.left_side[0] * -1
            # Middle on the right side.
            return self.right_side[0]
        # Full size is EVEN.
        return (self.left_side[0] * -1 + self.right_side[0]) / 2


# Time complexity:
#   initiation: O(1)
#   addNum: O(2 * log n + log k) <- n - current elements in heap 'left_side',
#                                   k - current elements in heap 'right_side'.
#           Worst case == everything is higher than first value, so we will add everything into the 'right_side'.
#           We're pushing value into 'right_side' => O(log n).
#           pop() value from 'right_side' and push it into the 'left_side' => O(log n + log k).
#           Or in reverse, everything is lower, so we will do same process but with push in 'left_side' first.
#   findMedian: O(1)
#           Because we're always maintain both heaps 'left_side' with all values lower than values from 'right_side',
#           and their sizes either equal or diff in 1. We can get middle and (middle - 1) in constant time.
# Auxiliary space:
#   classObject: O(n + k)


#                         can't call 'findMedian' on empty stream
test: list[str] = ['MedianFinder'] + ['addNum'] + [choice(['addNum', 'findMedian']) for _ in range(5 * 10 ** 4 - 1)]
test_vals: list[list[int]] = [[randint(-10 ** 5, 10 ** 5)] if option == 'addNum' else [] for option in test]
print(test)
print('!!!!!!!!!!!!!--')
print(test_vals)
