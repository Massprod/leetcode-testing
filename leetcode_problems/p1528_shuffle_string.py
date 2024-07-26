# You are given a string s and an integer array indices of the same length.
# The string s will be shuffled such that the character at the ith position
#  moves to indices[i] in the shuffled string.
# Return the shuffled string.
# --------------------
# s.length == indices.length == n
# 1 <= n <= 100
# s consists of only lowercase English letters.
# 0 <= indices[i] < n
# All values of indices are unique.


def restore_string(s: str, indices: list[int]) -> str:
    # working_sol (74.45%, 67.39%) -> (51ms, 16.42mb)  time: O(s) | space: O(s)
    out: list[str] = ['' for _ in s]
    for index, target in enumerate(indices):
        out[target] = s[index]
    return ''.join(out)


# Time complexity: O(s)
# Always traversing every char in `s` => O(s).
# Always creating an array `out` of size `s` => O(2 * s).
# --------------------
# Auxiliary space: O(s)
# `out` <- always of the same size as `s` => O(s).


test: str = "codeleet"
test_indices: list[int] = [4, 5, 6, 7, 0, 2, 1, 3]
test_out: str = "leetcode"
assert test_out == restore_string(test, test_indices)

test = "abc"
test_indices = [0, 1, 2]
test_out = "abc"
assert test_out == restore_string(test, test_indices)
