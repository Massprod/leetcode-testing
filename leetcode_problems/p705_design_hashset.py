# Design a HashSet without using any built-in hash table libraries.
# Implement MyHashSet class:
#  - void add(key) Inserts the value key into the HashSet.
#  - bool contains(key) Returns whether the value key exists in the HashSet or not.
#  - void remove(key) Removes the value key in the HashSet.
#    If key does not exist in the HashSet, do nothing.
# ---------------------
# 0 <= key <= 10 ** 6
# At most 10 ** 4 calls will be made to add, remove, and contains.


class MyHashSet:
    # working_sol (58.39%, 90.31%) -> (143ms, 21.10mb)
    def __init__(self):
        self.hash_value: int = 100
        self.hash_list: list[list[int]] = [[] for _ in range(self.hash_value)]

    def add(self, key: int) -> None:
        _hash: int = key % self.hash_value
        try:
            self.hash_list[_hash].index(key)
        except ValueError:
            self.hash_list[_hash].append(key)

    def remove(self, key: int) -> None:
        _hash: int = key % self.hash_value
        try:
            self.hash_list[_hash].remove(key)
        except ValueError:
            return

    def contains(self, key: int) -> bool:
        _hash: int = key % self.hash_value
        try:
            self.hash_list[_hash].index(key)
        except ValueError:
            return False
        return True


# Time complexity:
#   Essentially everything is the constant, but it's most basic solution.
#   w.e no reason to bother with it.
#   Because, no idea how to calc collisions correctly.
#   Guess if every value used, will give us a collision we will have O(n) from the array with these values.
#   On all 3 methods.
