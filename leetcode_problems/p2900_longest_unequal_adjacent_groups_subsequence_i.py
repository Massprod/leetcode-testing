# You are given a string array words and a binary array groups both of length n,
#  where words[i] is associated with groups[i].
# Your task is to select the longest alternating subsequence from words.
# A subsequence of words is alternating if for any two consecutive strings
#  in the sequence, their corresponding elements in the binary array groups differ.
# Essentially, you are to choose strings such that adjacent elements have
#  non-matching corresponding bits in the groups array.
# Formally, you need to find the longest subsequence of an array of indices
#  [0, 1, ..., n - 1] denoted as [i0, i1, ..., ik-1],
#  such that groups[ij] != groups[ij+1] for each 0 <= j < k - 1 and
#  then find the words corresponding to these indices.
# Return the selected subsequence.
# If there are multiple answers, return any of them.
# Note: The elements in words are distinct.
# -----------------------------
# 1 <= n == words.length == groups.length <= 100
# 1 <= words[i].length <= 10
# groups[i] is either 0 or 1.
# words consists of distinct strings.
# words[i] consists of lowercase English letters.]
from random import choice, randint

from string import ascii_lowercase


def get_longest_subsequence(words: list[str], groups: list[int]) -> list[str]:
    # working_sol (100.00%, 69.38%) -> (0ms, 17.71mb)  time: O(n) | space: O(n * m)
    # `groups` are binary.
    # We don't care about anything, except alternating.
    # Indexing doesnt matter and we need maximum length.
    # Just start building from the [0] and use everything we can.
    # If we start from `1` it will give us maximum length if we ever meet `0`,
    #  no matter how many `1` before.
    # Same for `0` start.
    out: list[str] = [words[0]]
    cur_bit: int = groups[0]
    for index in range(1, len(groups)):
        if cur_bit != groups[index]:
            out.append(words[index])
            cur_bit = groups[index]
    
    return out


# Time complexity: O(n) <- n - length of the input array `groups`.
# Always traversing `groups`, once => O(n).
# -----------------------------
# Auxiliary space: O(n * m) <- m - average string length in `words`.
# In the worst case every string from `words` can be used => O(n * m).


test: list[str] = ['e', 'a', 'b']
test_groups: list[int] = [0, 0, 1]
test_out: list[str] = ['e', 'b']
assert test_out == get_longest_subsequence(test, test_groups)

test = ['a', 'b', 'c', 'd']
test_groups = [1, 0, 1, 1]
test_out = ['a', 'b', 'c']
assert test_out == get_longest_subsequence(test, test_groups)

used: set[str] = set()
test = []
while 100 != len(test):
    test_str: str = ''.join([choice(ascii_lowercase) for _ in range(randint(1, 10))])
    if test_str in used:
        continue
    used.add(test_str)
    test.append(test_str)
test_groups = [randint(0, 1) for _ in range(100)]
print(test, '\n---\n', test_groups)
