# In a string s of lowercase letters,
#  these letters form consecutive groups of the same character.
# For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".
# A group is identified by an interval [start, end],
#  where start and end denote the start and end indices (inclusive) of the group.
# In the above example, "xxxx" has the interval [3,6].
# A group is considered large if it has 3 or more characters.
# Return the intervals of every large group sorted in increasing order by start index.
# ----------------------
# 1 <= s.length <= 1000
# s contains lowercase English letters only.
from random import choice
from string import ascii_lowercase


def large_group_positions(s: str) -> list[list[int]]:
    # working_sol (97.31%, 85.47%) -> (30ms, 16.43mb)  time: O(s) | space: O(s)
    out: list[list[int]] = []
    cur_group: list[int] = [0, 0]
    cur_group_char: str = s[0]
    for index in range(1, len(s)):
        if s[index] == cur_group_char:
            cur_group[1] += 1
        else:
            if 2 <= cur_group[1] - cur_group[0]:
                out.append([cur_group[0], cur_group[1]])
            cur_group[0], cur_group[1] = index, index
            cur_group_char = s[index]
    if 2 <= cur_group[1] - cur_group[0]:
        out.append(cur_group)
    return out


# Time complexity: O(s)
# Always traversing input string `s`, once => O(s).
# ----------------------
# Auxiliary space: O(s)
# W.e the size, in the worst case, every 3 consecutive symbols will change, and we can use them.
# So, essentially we're going to have (s / 3) ranges => O(s/3).


test: str = "abbxxxxzzy"
test_out: list[list[int]] = [[3, 6]]
assert test_out == large_group_positions(test)

test = "abc"
test_out = []
assert test_out == large_group_positions(test)

test = "abcdddeeeeaabbbcd"
test_out = [[3, 5], [6, 9], [12, 14]]
assert test_out == large_group_positions(test)

test = ''.join([choice(ascii_lowercase) for _ in range(1000)])
print(test)
