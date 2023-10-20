# You are given a nested list of integers nestedList.
# Each element is either an integer or a list whose elements may also be integers or other lists.
# Implement an iterator to flatten it.
# Implement the NestedIterator class:
#   NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
#   int next() Returns the next integer in the nested list.
#   boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
# -----------------
# 1 <= nestedList.length <= 500
# The values of the integers in the nested list is in the range [-10 ** 6, 10 ** 6].


# Implemented on Leet itself, just for annotation.
class NestedInteger:
    pass
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


class NestedIterator:
    # working_sol (92.68%, 97.2%) -> (54ms, 19.8mb)

    def __init__(self, nestedList: NestedInteger | list):
        self.flattened: list[int] = []

        def flatten(nested: NestedInteger | list) -> None:
            for x in range(len(nested)):
                if nested[x].isInteger():
                    self.flattened.append(nested[x].getInteger())
                else:
                    flatten(nested[x].getList())
        flatten(nestedList)
        self.index: int = -1

    def next(self) -> int:
        self.index += 1
        return self.flattened[self.index]

    def hasNext(self) -> bool:
        if self.index == len(self.flattened) - 1:
            return False
        return True


# Time complexity:
#   initiation: O(n) -> essentially we're just checking every integer inside 'nestedList' no matter if its nested
#     n - len of input 'nestedList'^^| or just single integer => O(n).
#   next: O(1)
#   hasNext: O(1)
# Auxiliary space:
#   initiation: O(n) -> all integers will be placed inside standard list => O(n).
#   next: O(1)
#   hasNext: O(1)
# -----------------
# Because we're already given interface to get integers or lists inside original list.
# It should be just a recursion with going deeper and deeper while we can.
# Guess I don't need to implement it by myself, then it's easy.
