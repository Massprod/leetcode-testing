# You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.
# You start your journey from building 0 and move to the next building by possibly using bricks or ladders.
# While moving from building i to building i+1 (0-indexed),
#  - If the current building's height is greater than or equal to the next building's height,
#     you do not need a ladder or bricks.
#  - If the current building's height is less than the next building's height,
#     you can either use one ladder or (h[i+1] - h[i]) bricks.
# Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.
# ------------------------
# 1 <= heights.length <= 10 ** 5
# 1 <= heights[i] <= 10 ** 6
# 0 <= bricks <= 10 ** 9
# 0 <= ladders <= heights.length
import heapq
from random import randint


def furthest_building(heights: list[int], bricks: int, ladders: int) -> int:
    # working_sol (78.95%, 70.90%) -> (426ms, 31.00mb)  time: O(n * log n) | space: O(n)
    # Most optimal way:
    #  Use bricks on the lowest differences, and use ladders on highest ones.
    # [Bricks we need to cover diff in heights]
    height_diffs: list[int] = []
    heapq.heapify(height_diffs)
    out: int = 0
    for x in range(len(heights) - 1):
        if heights[x] >= heights[x + 1]:
            out += 1
        else:
            bricks_needed: int = heights[x + 1] - heights[x]
            heapq.heappush(height_diffs, bricks_needed)
            # If we have ladder, try use it first.
            if ladders:
                ladders -= 1
                out += 1
            # If we don't have ladders, but used them before.
            # Try to replace already used ladder with LOWEST bricks cost with bricks,
            #  and place this ladder on HIGHER height diff.
            elif height_diffs:
                lowest_cost: int = height_diffs[0]
                # We have enough bricks to free previously used ladder.
                # Free it and instantly use.
                if lowest_cost <= bricks:
                    bricks -= heapq.heappop(height_diffs)
                    out += 1
                    continue
                # We don't have enough bricks to free any used ladder,
                #  and we don't have enough bricks to cover currently needed height diff.
                if bricks_needed > bricks:
                    break
                # Or we have enough, just cover this diff with bricks.
                bricks -= bricks_needed
                out += 1
            # If we don't have ladders at all, just use bricks while we can.
            elif bricks_needed <= bricks:
                out += 1
                bricks -= bricks_needed
            # No ladders, no bricks => can't do anything.
            else:
                break
    return out


# Time complexity: O(n * log n) <- n - length of input array `heights`.
# Worst case: ladders == heights.length, and all houses will be higher than previous.
# We will have (n - 1) brick costs stored in `height_diffs`, and we traverse (n - 1) indexes of `heights`.
# heappush() == Logarithmic, and we use it on every index. And heap `height_diffs` at max size == n - 1.
# O(n * log n)
# ------------------------
# Auxiliary space: O(n)
# Worst case: ladders == heights.length, and all houses will be higher than previous.
# We will never heappop() anything from `height_diffs` and in the end it's size == n - 1.


test: list[int] = [4, 2, 7, 6, 9, 14, 12]
test_bricks: int = 5
test_ladders: int = 1
test_out: int = 4
assert test_out == furthest_building(test, test_bricks, test_ladders)

test = [4, 12, 2, 7, 3, 18, 20, 3, 19]
test_bricks = 10
test_ladders = 2
test_out = 7
assert test_out == furthest_building(test, test_bricks, test_ladders)

test = [14, 3, 19, 3]
test_bricks = 17
test_ladders = 0
test_out = 3
assert test_out == furthest_building(test, test_bricks, test_ladders)

test = [1, 5, 1, 2, 3, 4, 10000]
test_bricks = 4
test_ladders = 1
test_out = 5
assert test_out == furthest_building(test, test_bricks, test_ladders)

test = [randint(1, 10 ** 6) for _ in range(10 ** 3)]
print(test)
