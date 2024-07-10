# Given a string s and a character c that occurs in s,
#  return an array of integers answer where answer.length == s.length
#  and answer[i] is the distance from index i to the closest occurrence of character c in s.
# The distance between two indices i and j is abs(i - j),
#  where abs is the absolute value function.
# ---------------------
# 1 <= s.length <= 10 ** 4
# s[i] and c are lowercase English letters.
# It is guaranteed that c occurs at least once in s.
from random import choice
from string import ascii_lowercase


def shortest_to_char(s: str, c: str) -> list[int]:
    # working_sol (89.79%, 29.69%) -> (36ms, 16.63mb)  time: O(s) | space: O(s)
    highest: int = 10 ** 5
    out: list[int] = [highest for _ in s]
    for index, char in enumerate(s):
        if c != char:
            continue
        # Two pointers == check both directions from `c`.
        out[index] = 0
        cur_index: int = index - 1
        while cur_index >= 0:
            cur_dist: int = abs(cur_index - index)
            if out[cur_index] <= cur_dist or s[cur_index] == c:
                break
            out[cur_index] = cur_dist
            cur_index -= 1
        cur_index = index + 1
        while cur_index < len(s):
            cur_dist = abs(cur_index - index)
            if out[cur_index] <= cur_dist or s[cur_index] == c:
                break
            out[cur_index] = cur_dist
            cur_index += 1
    return out


# Time complexity: O(s)
# Essentially we're always traversing every index to start from, and rechecking every other index, once => O(2n).
# ---------------------
# Auxiliary space: O(s)
# Always creating an array `out` with the size of `s` => O(s).


test_s: str = "loveleetcode"
test_c: str = "e"
test_out: list[int] = [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
assert test_out == shortest_to_char(test_s, test_c)

test_s = "aaab"
test_c = "b"
test_out = [3, 2, 1, 0]
assert test_out == shortest_to_char(test_s, test_c)

test_s = ''.join([choice(ascii_lowercase) for _ in range(10 ** 4)])
test_c = choice(ascii_lowercase)
print(test_s, '\n\n', test_c)
