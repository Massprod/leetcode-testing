# Design an iterator that supports the peek operation
#  on an existing iterator in addition to the hasNext and the next operations.
# Implement the PeekingIterator class:
#  - PeekingIterator(Iterator<int> nums) Initializes the object with the given integer iterator iterator.
#  - int next() Returns the next element in the array and moves the pointer to the next element.
#  - boolean hasNext() Returns true if there are still elements in the array.
#  - int peek() Returns the next element in the array without moving the pointer.
# Note: Each language may have a different implementation of the constructor and Iterator,
#  but they all support the int next() and boolean hasNext() functions.
# -----------------------------
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 1000
# All the calls to next and peek are valid.
# At most 1000 calls will be made to next, hasNext, and peek.


class PeekingIterator:
    # working_sol (50.43%, 13.75%) -> (37ms, 16.81mb)
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.peeked: bool = False
        self.peeked_value: int | bool = False

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.peeked:
            self.peeked = True
            self.peeked_value = self.iterator.next()
            return self.peeked_value
        return self.peeked_value

    def next(self):
        """
        :rtype: int
        """
        if self.peeked:
            self.peeked = False
            return self.peeked_value
        return self.iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.peeked:
            return True if self.peeked_value else False
        return self.iterator.hasNext()


# Time complexity:
#   `peek`: O(1)
#   `next`: O(1)
#   `hasNext`: O(1)
# Auxiliary space:
#   `peek`: O(1)
#   `next`: O(1)
#   `hasNext`: O(1)
