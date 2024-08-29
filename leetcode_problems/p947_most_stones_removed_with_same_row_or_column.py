# On a 2D plane, we place n stones at some integer coordinate points.
# Each coordinate point may have at most one stone.
# A stone can be removed if it shares either the same row
#  or the same column as another stone that has not been removed.
# Given an array stones of length n where stones[i] = [xi, yi]
#  represents the location of the ith stone,
#  return the largest possible number of stones that can be removed.
# --------------------------
# 1 <= stones.length <= 1000
# 0 <= xi, yi <= 10 ** 4
# No two stones are at the same coordinate point.


def remove_stones(stones: list[list[int]]) -> int:
    # working_sol (20.05%, 32.33%) -> (691ms, 17.74mb)  time: O(n * n) | space: O(n * n)
    # [ nodes: [ edges ] ]
    graph: list[list[int]] = [[] for _ in stones]
    for stone_ind in range(len(stones)):
        for diff_stone_ind in range(stone_ind + 1, len(stones)):
            if (stones[stone_ind][0] == stones[diff_stone_ind][0]
                    or stones[stone_ind][1] == stones[diff_stone_ind][1]):
                graph[stone_ind].append(diff_stone_ind)
                graph[diff_stone_ind].append(stone_ind)

    def check_connected(_stone_ind: int) -> None:
        nonlocal visited
        nonlocal graph
        for edge in graph[_stone_ind]:
            if edge not in visited:
                visited.add(edge)
                check_connected(edge)

    out: int = 0
    visited: set[int] = set()
    # Find all connected blocks with standard DFS.
    for stone in range(len(stones)):
        if stone not in visited:
            visited.add(stone)
            check_connected(stone)
            out += 1
    # We found every connected block,
    #  but we need # of stones we can remove.
    # And if we delete a stones from the block:
    # ! A stone can be removed if it shares either the same row or the same column
    #   as another stone that has not been removed. !
    # ^^We will always have One stone left, because it's no longer shares connection with some1.
    # So, we only care about how many blocks we deleted from original.
    # Deleted blocks == # of stones left == everything else is deleted:
    return len(stones) - out


# Time complexity: O(n * n) <- n - length of the input array `stones`.
# Always building a graph with nested loop => O(n * n).
# Extra traversing every Node with DFS => O(n * n + n).
# --------------------------
# Auxiliary space: O(n * n).
# In the worst case, every stone is going to be on the same row|column.
# So, all of them are going to be stored in `graph` => O(n * n).
# [index: [(n - 1) edges] -> [index: [(n - 2) edges]] ... etc.
# `visited` <- always stores every stone(index) from `stones` => O(n * n + n).


test: list[list[int]] = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
test_out: int = 5
assert test_out == remove_stones(test)

test = [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]
test_out = 3
assert test_out == remove_stones(test)

test = [[0, 0]]
test_out = 0
assert test_out == remove_stones(test)
