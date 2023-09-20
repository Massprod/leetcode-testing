# Implement the RandomizedSet class:
#   - RandomizedSet() Initializes the RandomizedSet object.
#   - bool insert(int val) Inserts an item val into the set if not present.
#     Returns true if the item was not present, false otherwise.
#   - bool remove(int val) Removes an item val from the set if present.
#     Returns true if the item was present, false otherwise.
#   -int getRandom() Returns a random element from the current set of elements
#    (it's guaranteed that at least one element exists when this method is called).
#    Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works in average O(1) time complexity.
# --------------------------
# -2 ** 31 <= val <= 2 ** 31 - 1
# At most 2 * 10 ** 5 calls will be made to insert, remove, and getRandom.
# There will be at least one element in the data structure when getRandom is called.
from random import choice


class RandomizedSet:
    # working_sol (99.3%, 90.83%) -> (280ms, 63.6mb)

    def __init__(self):
        # Dict of indexes with corresponding values.
        # (index, list_value)
        self.indexes: dict[int, int] = {}
        # List of values.
        self.values: list[int] = []

    def insert(self, val: int) -> bool:
        if val in self.indexes:
            return False
        self.values.append(val)
        self.indexes[val] = len(self.values) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indexes:
            return False
        # Index of deleted value.
        index: int = self.indexes.pop(val)
        if index != (len(self.values) - 1):
            # Reset indexing of changed value
            #  and replace deleted value.
            value: int = self.values.pop()
            self.indexes[value] = index
            self.values[index] = value
            return True
        self.values.pop()
        return True

    def getRandom(self):
        if self.values:
            return choice(self.values)


# Time complexity: all constant => O(1).
# Auxiliary space: O(n) -> object with dict and list of inserted values => O(2n).
#                          Methods are constant O(1).
# --------------------------
# List with values and dictionary to maintain indexing?
# Like dict with values inside of list as keys, and value as index of this list value.
# Then we can just change indexes when deleting == O(1).
# Only question is how to getRandom?
# Ok. Comments say, we're allowed to use standard random library.
