# You are given a string s.
# We want to partition the string into as many parts as possible so that each letter appears in at most one part.
# Note that the partition is done so that after concatenating all the parts in order,
#  the resultant string should be s.
# Return a list of integers representing the size of these parts.
# -------------------------
# 1 <= s.length <= 500
# s consists of lowercase English letters.
from random import choice
from string import ascii_lowercase
from collections import defaultdict


def partition_labels(s: str) -> list[int]:
    # working_sol (93.68%, 29.15%) -> (33ms, 16.60mb)  time: O(s) | space: O(s)
    # { symbol: index_of_last_occurrence }
    last_occurs: dict[str, int] = defaultdict(int)
    for index, char in enumerate(s):
        last_occurs[char] = index
    out: list[int] = []
    index: int = 0
    prev_index: int = 0
    while index < len(s):
        # First char of the substring, we should only have 1 in each part.
        # So, we should include every occurrence of it.
        first_char: str = s[index]
        next_start: int = last_occurs[first_char] + 1
        # All symbols within a slice of this char.
        # 'afgdfgerterta' <- we should include all to use 'a'.
        cur_slice: set[str] = set(s[index: next_start])
        cur_slice.remove(first_char)
        index = next_start
        # We check every char last_occurrence and update, with extra chars.
        # Because we need to use all chars inside our slice.
        # And they should be used in the same way as `first_char` <- every char deleted from `s`.
        while cur_slice:
            next_char: str = cur_slice.pop()
            if last_occurs[next_char] + 1 > index:
                cur_slice.update(
                    s[index: last_occurs[next_char] + 1]
                )
                index = last_occurs[next_char] + 1
        # Adjust to get correct length.
        out.append(index - prev_index)
        prev_index = index
    return out


# Time complexity: O(s)
# Traversing `s` once to get all char occurrences => O(s).
# Extra traversing it to get all the slice lengths => O(2 * s).
# -------------------------
# Auxiliary space: O(s)
# In the worst case there's only one duplicate char in `s`, [0] and [-1].
# And whole `s` can be used within one slice.
# `last_occurs` <- allocates space for each char from `s` => O(s - 1).
# `cur_slice` <- allocates space for each char from `s` => O(s).


test: str = "ababcbacadefegdehijhklij"
test_out: list[int] = [9, 7, 8]
assert test_out == partition_labels(test)

test = "eccbbbbdec"
test_out = [10]
assert test_out == partition_labels(test)

test = "qiejxqfnqceocmy"
test_out = [13, 1, 1]
assert test_out == partition_labels(test)

test = ''.join([choice(ascii_lowercase) for _ in range(500)])
print(test)
