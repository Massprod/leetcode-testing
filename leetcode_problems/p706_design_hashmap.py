# Design a HashMap without using any built-in hash table libraries.
# Implement the MyHashMap class:
#   MyHashMap() initializes the object with an empty map.
#   void put(int key, int value) inserts a (key, value) pair into the HashMap.
#    If the key already exists in the map, update the corresponding value.
#   int get(int key) returns the value to which the specified key is mapped,
#    or -1 if this map contains no mapping for the key.
#   void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
# ---------------------
# 0 <= key, value <= 10 ** 6
# At most 10 ** 4 calls will be made to put, get, and remove.


class ListNode:

    def __init__(self, key: int, val: int):
        self.key: int = key
        self.val: int = val
        self.next: ListNode | None = None


class MyHashMap:
    # working_sol (190ms, 20.1mb) -> (78.95%, 48.8%)
    def __init__(self):
        self.size: int = 1024
        self.hashmap: list[ListNode | None] = [None for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        id: int = key % self.size
        # No collision.
        if not self.hashmap[id]:
            self.hashmap[id] = ListNode(key, value)
            return
        # Collision.
        head: ListNode = self.hashmap[id]
        while head:
            # Already exist.
            if key == head.key:
                head.val = value
                return
            # Not exist.
            if not head.next:
                head.next = ListNode(key, value)
                return
            head = head.next

    def get(self, key: int) -> int:
        id: int = key % self.size
        head: ListNode = self.hashmap[id]
        while head:
            if key == head.key:
                return head.val
            head = head.next
        return -1

    def remove(self, key: int) -> None:
        id: int = key % self.size
        head: ListNode = self.hashmap[id]
        # Not exist.
        if not head:
            return
        # Reassign to next Node.
        if head.key == key:
            self.hashmap[id] = head.next
            return
        while head.next:
            if head.next.key == key:
                head.next = head.next.next
                return
            head = head.next


# Time complexity:
#       initialization: O(1) -> always constant, we're not changing size => O(1).
#       put: O(n) -> worst case == every value we add will collide, then we need to traverse all added before => O(n).
#        n - number of collisions(keys)^^|
#       get: O(n) -> same worst case and complexity as put()
#       remove: O(n) -> worst case == always removing last collided key, then we will traverse n - 1 of them => O(n).
# Auxiliary space:
#       Every method except object itself is O(1).
#       We store LinkedLists on indexes, for every (key, value) pair we will create new Node => O(n).
#        n - number of added pairs.
# ---------------------
# Small constraints, so it can be done with just a list.
# But it's better to build more correct version with linked lists or lists in list and hash_calc.
