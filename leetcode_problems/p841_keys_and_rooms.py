# There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0.
# Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.
# When you visit a room, you may find a set of distinct keys in it.
# Each key has a number on it, denoting which room it unlocks,
#  and you can take all of them with you to unlock the other rooms.
# Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i,
#  return true if you can visit all the rooms, or false otherwise.
# ----------------
# n == rooms.length
# 2 <= n <= 1000
# 0 <= rooms[i].length <= 1000
# 1 <= sum(rooms[i].length) <= 3000
# 0 <= rooms[i][j] < n
# All the values of rooms[i] are unique.
from random import randint


def can_visit_all(rooms: list[list[int]]) -> bool:
    # working_sol (94.14%, 33.83%) -> (65ms, 17.3mb)  time: O(n) | space: O(n)
    # ! all the rooms are locked except for room 0 ! =>
    # => [0] always True.
    visited: list[bool] = [True] + [False for _ in range(len(rooms) - 1)]

    def check(room: int, path: set[int]) -> None:
        # Standard DFS, with going as deep as we can.
        # With skipping cycles or repeated rooms,
        #  by recording path we travel.
        if room != 0 and visited[room]:
            return
        # W.e the way we get in the room,
        #  it's Visited anyway.
        visited[room] = True
        # Check every key presented in this room.
        for key in rooms[room]:
            # Except ones, we already used.
            if key not in path:
                path.add(key)
                check(key, path)

    check(0, {0})
    return False not in visited

# Time complexity: O(n) -> only visiting every room|index once => O(n).
# n - len of input_array^^|
# Auxiliary space: O(n) -> every room can lead to another like 0 -> 1 -> 2 -> 3...etc, so stack will be a size of n ->
#                       -> extra to recursion stack we're creating array with same size n => O(n).
# ----------------
# Only being doing DFS with dailies and actually most of them for Cycle search.
# So it's first task for DFS from 75 study. I guess it's the same but when I find visited room,
#  all I need to do is just mark everything on path as True|Visited in adjacency list.
# Extra check if False present and return True|False depending on it. Let's try.


test: list[list[int]] = [[1], [2], [3], []]
test_out: bool = True
assert test_out == can_visit_all(test)

test = [[1, 3], [3, 0, 1], [2], [0]]
test_out = False
assert test_out == can_visit_all(test)
