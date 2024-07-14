# You are given an array of integers stones where stones[i] is the weight of the ith stone.
# We are playing a game with the stones. On each turn,
#  we choose the heaviest two stones and smash them together.
# Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
#   - If x == y, both stones are destroyed, and
#   - If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.
# Return the weight of the last remaining stone.
# If there are no stones left, return 0.
# ----------------------
# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000
import heapq
from random import randint


def last_stone_weight(stones: list[int]) -> int:
    # working_sol (71.83%, 22.98%) -> (34ms, 16.58mb)  time: O(n * log n) | space: O(n)
    heap: list[int] = [val * -1 for val in stones]
    heapq.heapify(heap)
    while 1 < len(heap):
        heavier: int = heapq.heappop(heap)
        heavy: int = heapq.heappop(heap)
        if heavy != heavier:
            heavier -= heavy
            heapq.heappush(heap, heavier)
    return heapq.heappop(heap) * -1 if heap else 0


# Time complexity: O(n * log n) <- n - length of the input string `stones`.
# Reversing values of `stones` to build a `minHeap` => O(n).
# Building a `heap` with size of `stones` => O(log n).
# `heappop` takes O(log n) for every operation, and we're exhausting every value from `heap` => O(n * log n).
# ----------------------
# Auxiliary space: O(n)
# We're always allocating space for the `heap` with a size of `stones` => O(n).


test: list[int] = [2, 7, 4, 1, 8, 1]
test_out: int = 1
assert test_out == last_stone_weight(test)

test = [1]
test_out = 1
assert test_out == last_stone_weight(test)

test = [randint(1, 1000) for _ in range(30)]
print(test)
