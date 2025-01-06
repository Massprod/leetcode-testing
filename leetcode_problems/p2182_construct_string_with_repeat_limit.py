# You are given a string s and an integer repeatLimit.
# Construct a new string repeatLimitedString using the characters of s such that no letter
#  appears more than repeatLimit times in a row. You do not have to use all characters from s.
# Return the lexicographically largest repeatLimitedString possible.
# A string a is lexicographically larger than a string b if in the first position
#  where a and b differ, string a has a letter that appears later in the alphabet
#  than the corresponding letter in b.
# If the first min(a.length, b.length) characters do not differ,
#  then the longer string is the lexicographically larger one.
# --------------------------------
# 1 <= repeatLimit <= s.length <= 10 ** 5
# s consists of lowercase English letters.
import heapq
import pyperclip
from random import choice
from string import ascii_lowercase
from collections import Counter


def repeat_limited_string(s: str, repeatLimit: int) -> str:
    # working_sol: (41.31%, 34.27%) -> (260ms, 19.16mb)  time: O(s * log s) | space: O(s)
    cur_ascii: int
    cur_char: str
    cur_count: int
    # { char: count }
    counted: dict[str, int] = Counter(s)
    # [ (char, uses_left) ]
    heap: list[tuple[int, int]] = []
    heapq.heapify(heap)
    # We can't use chars itself.
    # And we need highest == maxHeap == we need to reverse them.
    # Every char has ascii and it's INT => we can use it in reverse.
    for char, count in counted.items():
        heapq.heappush(
            heap, 
            (ord(char) * -1, count)
        )
    out: list[str] = []
    # We can't use the same char more than `repeatLimit`.
    # So, if we have more occurrences of char than `repeatLimit`.
    # We should skip it and use something else, if we can.
    # Later, we can use it again == push into heap again.
    tempo: tuple[int, int] = (-97, 0)
    while heap:
        cur_ascii, cur_count = heapq.heappop(heap)
        cur_char = chr(cur_ascii * -1)
        # ! Return the lexicographically largest repeatLimitedString possible !
        # We should always use highest char we can.
        # And if we still haven't used previous higher value,
        #  we should only fill the gap with a single lower char.
        if 0 != tempo[1]:
            heapq.heappush(heap, tempo)
            if cur_ascii > tempo[0]:
                out.append(cur_char)
                left_over = cur_count - 1
                tempo = (cur_ascii, max(0, left_over))
                continue
        left_over: int = cur_count - repeatLimit
        cur_string: str = cur_char * min(cur_count, repeatLimit)
        out.append(cur_string)
        tempo = (cur_ascii, max(0, left_over))
    return ''.join(out)


# Time complexity: O(s * log s)
# Counting all chars and their occurrences => O(s).
# Creating a heap with all of these chars and their counts => O(s + s * log s).
# Using every char and their occurences until we can,
#  always push(), pop() at least once => O(s * log s).
# --------------------------------
# Auxiliary space: O(s)
# In the worst case there's only unique chars in `s.`
# `counted` <- allocates space for each unique char => O(s).
# `heap` <- allocates space for each unique char => O(2 * s).
# In the worst case every char will be used.
# `out` <- same size as input string, but with different chars order => O(3 * s).


test: str = "cczazcc"
test_limit: int = 3
test_out: str = "zzcccac"
assert test_out == repeat_limited_string(test, test_limit)

test = "aababab"
test_limit = 2
test_out = "bbabaa"
assert test_out == repeat_limited_string(test, test_limit)

test = ''.join([choice(ascii_lowercase) for _ in range(10 ** 5)])
pyperclip.copy(test)
