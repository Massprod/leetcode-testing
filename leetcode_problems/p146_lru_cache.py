# Design a data structure that follows the constraints
#   of a Least Recently Used (LRU) cache.
# Implement the LRUCache class:
#   LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
#   int get(int key) Return the value of the key if the key exists, otherwise return -1.
#   void put(int key, int value) Update the value of the key if the key exists.
#     Otherwise, add the key-value pair to the cache.
#     If the number of keys exceeds the capacity from this operation,
#       evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.
# ------------------
# 1 <= capacity <= 3000
# 0 <= key <= 10 ** 4
# 0 <= value <= 10 ** 5
# At most 2 * 10 ** 5 calls will be made to get and put.


class DoubleLinked:
    # working_sol (23.38%, 85.8%) -> (885ms, 77.6mb)

    def __init__(self, key: int, val: int, prev=None, next=None):
        self.val: int = val
        self.key: int = key
        self.prev: DoubleLinked = prev
        self.next: DoubleLinked = next


class LRUCache:

    def __init__(self, capacity: int):
        # dictionary to store (key, value) pairs
        self.pairs: dict[int, DoubleLinked] = {}
        # set limit
        self.capacity: int = capacity
        # count added until full
        self.counter: int = 1
        # DoubleLinked nodes to store calls ordering
        self.first: DoubleLinked = DoubleLinked(0, 0)
        self.last: DoubleLinked = DoubleLinked(0, 0)
        # Link nodes, to store between them
        self.first.next, self.first.prev = self.last, self.last
        self.last.next, self.last.prev = self.first, self.first

    def get(self, key):
        if key in self.pairs:
            push_key: int = key
            push_val: int = self.pairs[key].val
            # delete existed
            self.delete_node(self.pairs[key])
            # delete and push as freshly used
            pushed: DoubleLinked = self.place_pre_last(push_key, push_val)
            self.pairs[push_key] = pushed
            return pushed.val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity >= self.counter:
            # delete existed
            if key in self.pairs:
                self.delete_node(self.pairs[key])
            else:
                # if it's new count for a limit check
                self.counter += 1
            # create/recreate and push as freshly used
            new_node: DoubleLinked = self.place_pre_last(key, value)
            self.pairs[key] = new_node
            return
        if key in self.pairs:
            # delete existed
            self.delete_node(self.pairs[key])
        else:
            # delete oldest(least recently) used
            # always pushing from right to left,
            # right_most -> fresh | left_most -> oldest (except limiters)
            self.delete_node(self.first.next)
        # create/recreate and push as freshly used
        new_node = self.place_pre_last(key, value)
        self.pairs[key] = new_node
        return

    def place_pre_last(self, key, value: int) -> DoubleLinked:
        # simple reassign of pre_last to a new_node
        new_node: DoubleLinked = DoubleLinked(key, value)
        self.last.prev.next = new_node
        new_node.prev = self.last.prev
        new_node.next = self.last
        self.last.prev = new_node
        return new_node

    def delete_node(self, node: DoubleLinked) -> None:
        # delete key from hash(pairs) and node itself,
        # after connecting his left-right nodes
        node.prev.next, node.next.prev = node.next, node.prev
        del self.pairs[node.key]
        del node


# Time complexity:
#       initiation: O(1) -> doesn't depend on input at all, only sets value of capacity => O(1).
#       delete_node: 0(1) -> always deletes only 1 record from dictionary and given Node itself,
#                            reassign is always the same 2 nodes switch -> doesn't depend on input => O(1).
#       place_pre_last: O(1) -> always same operations: creating new_node, assign it as pre_last,
#                            doesn't depend on input => O(1).
#       put: O(1) -> doesn't depend on input as well, we're always deleting one of the nodes after exceeding limit
#                    or if it's already in a hash_table, extra always creating a new_node => O(1).
#       get: O(1) -> always 2 operations: deleting existed node and push it to as fresh after => O(1).
# ------------------
# Failed commit -> forgot to change counting from everything to only new_nodes, made it first and didn't see after.
# ------------------
# Working correctly, but I'm using most pathetic way with just deleting nodes and recreating them again.
# We can just reassign them if they're already exist, but not going to bother today.


test: list[str] = ["LRUCache", "put", "put", "put", "put", "put", "get", "put", "get", "get", "put", "get", "put",
                   "put", "put",
                   "get", "put", "get", "get", "get", "get", "put", "put", "get", "get", "get", "put", "put", "get",
                   "put", "get",
                   "put", "get", "get", "get", "put", "put", "put", "get", "put", "get", "get", "put", "put", "get",
                   "put", "put",
                   "put", "put", "get", "put", "put", "get", "put", "put", "get", "put", "put", "put", "put", "put",
                   "get", "put",
                   "put", "get", "put", "get", "get", "get", "put", "get", "get", "put", "put", "put", "put", "get",
                   "put", "put",
                   "put", "put", "get", "get", "get", "put", "put", "put", "get", "put", "put", "put", "get", "put",
                   "put", "put",
                   "get", "get", "get", "put", "put", "put", "put", "get", "put", "put", "put", "put", "put", "put",
                   "put"]
test_values: list[list[int]] = [[10], [10, 13], [3, 17], [6, 11], [10, 5], [9, 10], [13], [2, 19], [2], [3], [5, 25],
                                [8],
                                [9, 22],
                                [5, 5], [1, 30], [11], [9, 12], [7], [5], [8], [9], [4, 30], [9, 3], [9], [10], [10],
                                [6, 14],
                                [3, 1],
                                [3], [10, 11], [8], [2, 14], [1], [5], [4], [11, 4], [12, 24], [5, 18], [13], [7, 23],
                                [8],
                                [12],
                                [3, 27], [2, 12], [5], [2, 9], [13, 4], [8, 18], [1, 7], [6], [9, 29], [8, 21], [5],
                                [6, 30],
                                [1, 12],
                                [10], [4, 15], [7, 22], [11, 26], [8, 17], [9, 29], [5], [3, 4], [11, 30], [12],
                                [4, 29], [3],
                                [9], [6],
                                [3, 4], [1], [10], [3, 29], [10, 28], [1, 20], [11, 13], [3], [3, 12], [3, 8], [10, 9],
                                [3, 26], [8],
                                [7], [5], [13, 17], [2, 27], [11, 15], [12], [9, 19], [2, 15], [3, 16], [1], [12, 17],
                                [9, 1],
                                [6, 19],
                                [4], [5], [5], [8, 1], [11, 7], [5, 2], [9, 28], [1], [2, 2], [7, 4], [4, 22], [7, 24],
                                [9, 26],
                                [13, 28], [11, 26]]
test_answers: list[int | None] = [None, None, None, None, None, None, -1, None, 19, 17, None, -1, None, None, None, -1,
                                  None, -1, 5, -1,
                                  12, None, None, 3, 5, 5, None, None, 1, None, -1, None, 30, 5, 30, None, None, None,
                                  -1, None, -1, 24,
                                  None, None, 18, None, None, None, None, -1, None, None, 18, None, None, -1, None,
                                  None, None, None,
                                  None, 18, None, None, -1, None, 4, 29, 30, None, 12, -1, None, None, None, None, 29,
                                  None, None, None,
                                  None, 17, 22, 18, None, None, None, -1, None, None, None, 20, None, None, None, -1,
                                  18, 18, None, None,
                                  None, None, 20, None, None, None, None, None, None, None]

test_case: LRUCache | None = None
for x in range(len(test)):
    if test[x] == "LRUCache":
        test_case = LRUCache(test_values[x][0])
    elif test[x] == "put":
        assert test_answers[x] == test_case.put(test_values[x][0], test_values[x][1])
    elif test[x] == "get":
        assert test_answers[x] == test_case.get(test_values[x][0])
