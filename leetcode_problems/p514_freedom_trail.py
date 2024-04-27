# In the video game Fallout 4, the quest "Road to Freedom" requires players to reach a metal dial
#  called the "Freedom Trail Ring" and use the dial to spell a specific keyword to open the door.
# Given a string ring that represents the code engraved on the outer ring and another string key
#  that represents the keyword that needs to be spelled,
#  return the minimum number of steps to spell all the characters in the keyword.
# Initially, the first character of the ring is aligned at the "12:00" direction.
# You should spell all the characters in key one by one by rotating ring clockwise
#  or anticlockwise to make each character of the string key aligned at the "12:00" direction
#  and then by pressing the center button.
# At the stage of rotating the ring to spell the key character key[i]:
#  1. You can rotate the ring clockwise or anticlockwise by one place,
#     which counts as one step. The final purpose of the rotation is to align one of ring's
#     characters at the "12:00" direction, where this character must equal key[i].
#  2. If the character key[i] has been aligned at the "12:00" direction,
#     press the center button to spell, which also counts as one step.
#     After the pressing, you could begin to spell the next character in the key (next stage).
#     Otherwise, you have finished all the spelling.
# ------------------------
# 1 <= ring.length, key.length <= 100
# ring and key consist of only lower case English letters.
# It is guaranteed that key could always be spelled by rotating ring.
import heapq
from random import choice
from string import ascii_lowercase
from collections import defaultdict


def find_rotate_steps(ring: str, key: str) -> int:
    # working_sol (56.47%, 65.49%) -> (121ms, 16.79mb)  time: O(n * k * log(n * k)) | space: O(n * k + n)
    steps: int
    key_index: int
    ring_index: int

    def get_distance(index1: int, index2: int) -> int:
        distance: int = 0
        if index1 == index2:
            return distance
        steps_between: int = abs(index1 - index2)
        steps_around: int = len(ring) - steps_between
        distance = min(steps_around, steps_between)
        return distance

    occurrences: dict[str, list[int]] = defaultdict(list)
    for index, char in enumerate(ring):
        occurrences[char].append(index)
    # (steps, key index, ring index)
    heap: list[tuple[int, int, int]] = []
    heapq.heapify(heap)
    heapq.heappush(heap, (0, 0, 0))
    # (key_index, ring_index)
    visited: set[tuple[int, int]] = set()
    steps: int = 0
    # Standard Dijkstra's algo
    while heap:
        steps, ring_index, key_index = heapq.heappop(heap)
        if len(key) == key_index:
            break
        if (ring_index, key_index) in visited:
            continue
        visited.add((ring_index, key_index))
        for option in occurrences[key[key_index]]:
            new_steps: int = steps + get_distance(ring_index, option) + 1
            heapq.heappush(heap, (new_steps, option, key_index + 1))
    return steps


# Time complexity: O(n * k * log(n * k)) <- n - length of input string `ring`, k - length of input string `key`
# At max `heap` will store (n * k) elements and we will check every1 push | pop in heapq is log => O(n * k * log(n * k).
# Standard Dijkstra
# ------------------------
# Auxiliary space: O(n * k + n)
# At max `heap` allocates all options we use => O(n * k).
# Same for visited => O(n * k).
# And `occurrences` will store all chars from `ring`, with their index => O(2n)


test_ring: str = "godding"
test_key: str = "gd"
test_out: int = 4
assert test_out == find_rotate_steps(test_ring, test_key)

test_ring = "godding"
test_key = "godding"
test_out = 13
assert test_out == find_rotate_steps(test_ring, test_key)

test_ring = "htixplottp"
test_key = "poitttpotp"
test_out = 27
assert test_out == find_rotate_steps(test_ring, test_key)

test_ring = ''.join([choice(ascii_lowercase) for _ in range(10)])
test_key = ''.join([choice(test_ring) for _ in range(10)])
print(test_ring)
print(test_key)
