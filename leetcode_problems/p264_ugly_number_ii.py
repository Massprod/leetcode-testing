# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
# Given an integer n, return the nth ugly number.
# -----------------
# 1 <= n <= 1690
import heapq


def nth_ugly_number(n: int) -> int:
    # working_sol (52.61%, 36.75%) -> (107ms, 16.67mb)  time: O(n * log m) | space: O(m)
    heap: list[int] = [1]
    heapq.heapify(heap)
    used: set[int] = {1}
    count: int = 1
    options: list[int] = [2, 3, 5]
    while n != count:
        # We always take currently minimum ugly_number.
        # And we stop when the next ugly_number is `n`th.
        cur_ugly: int = heapq.heappop(heap)
        for option in options:
            next_ugly = cur_ugly * option
            if next_ugly not in used:
                heapq.heappush(heap, next_ugly)
                used.add(next_ugly)
        count += 1
    return heapq.heappop(heap)


# Time complexity: O(n * log m) <- m - length of the `heap` == unique ugly numbers.
# Count every option for a `cur_ugly` until we get to the `n`th => O(n * log m).
# -----------------
# Auxiliary space: O(m)
# `heap` <- always allocates space for all unique ugly numbers so far => O(m).
# `used` <- always allocates space for all unique ugly numbers => O(m).


test: int = 10
test_out: int = 12
assert test_out == nth_ugly_number(test)

test = 1
test_out = 1
assert test_out == nth_ugly_number(test)
