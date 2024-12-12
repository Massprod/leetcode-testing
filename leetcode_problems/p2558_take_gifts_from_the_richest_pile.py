# You are given an integer array gifts denoting the number of gifts in various piles.
# Every second, you do the following:
#   - Choose the pile with the maximum number of gifts.
#   - If there is more than one pile with the maximum number of gifts, choose any.
#   - Leave behind the floor of the square root of the number of gifts in the pile.
#     Take the rest of the gifts.
# Return the number of gifts remaining after k seconds.
# -------------------------
# 1 <= gifts.length <= 10 ** 3
# 1 <= gifts[i] <= 10 ** 9
# 1 <= k <= 10 ** 3
import heapq
import pyperclip
from random import randint


def pick_gifts(gifts: list[int], k: int) -> int:
    # working_sol: (91.28%, 8.46%) -> (2ms, 17.56mb)  time: O(n * log n + k * log n) | space: O(n)
    # Standard MaxHeap approach.
    heap: list[int] = [value * -1 for value in gifts]
    heapq.heapify(heap)
    while k and heap:
        max_val: int = heapq.heappop(heap) * -1
        # Could be done better :)
        left_over: int = int(max_val ** 0.5)
        heapq.heappush(heap, left_over * -1)
        k -= 1
    return sum(heap) * -1


# Time complexity: O(n * log n + k * log n) <- n - length of the input array `gifts`
# Always creating a `heap` with size of `n` => O(n * log n).
# And then `pop()` and `push()` for `k` times => O(n * log n + k * log n).
# Extra summarize resulted `heap`, in the worst case every value is still there => O(n * log n + k * log n + n).
# -------------------------
# Auxiliary space: O(n)
# `heap` <- allocates space for each value from `gifts` => O(n).


test: list[int] = [25,64,9,4,100]
test_k: int = 4
test_out: int = 29
assert test_out == pick_gifts(test, test_k)

test = [1, 1, 1, 1]
test_k = 4
test_out = 4
assert test_out == pick_gifts(test, test_k)

test = [randint(1, 10 ** 9) for _ in range(10 ** 3)]
pyperclip.copy(test)
