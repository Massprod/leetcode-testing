# Design a number container system that can do the following:
#  - Insert or Replace a number at the given index in the system.
#  - Return the smallest index for the given number in the system.
# Implement the NumberContainers class:
#  - NumberContainers() Initializes the number container system.
#  - void change(int index, int number) Fills the container at index with the number.
#    If there is already a number at that index, replace it.
#  - int find(int number) Returns the smallest index for the given number,
#    or -1 if there is no index that is filled by number in the system.
# ---------------------------
# 1 <= index, number <= 10 ** 9
# At most 10 ** 5 calls will be made in total to change and find.
import heapq


class NumberContainers:
    # working_sol (70.10%, 97.55%) -> (121ms, 75.60mb)
    #             time: O(n * log n) | space: O(k + m)
    def __init__(self):
        # { number: [ heap with indexes using this number ] }
        self.numbers: dict[int, list[int]] = {}
        # { index: number on it }
        self.indexes: dict[int, int] = {}

    def change(self, index: int, number: int) -> None:
        if number == self.indexes.get(index):
            return
        self.indexes[index] = number
        if self.numbers.get(number):
            heapq.heappush(
                self.numbers[number], index
            )
        else:
            new_heap: list[int] = [index]
            heapq.heapify(new_heap)
            self.numbers[number] = new_heap

    def find(self, number: int) -> int:
        if not self.numbers.get(number):
            return -1
        
        while self.numbers[number]:
            index: int = self.numbers[number][0]
            if number == self.indexes[index]:
                return index
            heapq.heappop(
                self.numbers[number]
            )
        
        return -1


# Time complexity:
#   n - current length of the stored heapq
#   `change`: O(log n)
#       - Always just a push into the heap, or it's creation
#   `find`:   O(n * log n)
#       - In the worst case, all indexes are wrong => we will check all of them.
# ---------------------------
# Auxiliary space: O(k + m) <- k - unique indexes used, m - unique values used.
