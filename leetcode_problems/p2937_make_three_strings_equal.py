# You are given three strings: s1, s2, and s3.
# In one operation you can choose one of these strings and delete its rightmost character.
# Note that you cannot completely empty a string.
# Return the minimum number of operations required to make the strings equal.
# If it is impossible to make them equal, return -1.
# ------------------------------
# 1 <= s1.length, s2.length, s3.length <= 100
# s1, s2 and s3 consist only of lowercase English letters.


def find_minimum_operations(s1: str, s2: str, s3: str) -> int:
    # working_sol (36.12%, 6.84%) -> (48ms, 16.62mb)  time: O(min(s1, s2, s3)) | space: O(1)
    # First time index not-equal in all 3 strings == end.
    # And we need to take all 3 lengths - end.
    length_1: int = len(s1)
    length_2: int = len(s2)
    length_3: int = len(s3)
    out: int = 0
    end: int = 0
    while end < min(length_1, length_2, length_3):
        if s1[end] != s2[end] or s2[end] != s3[end]:
            break
        end += 1
    if 0 == end:
        return -1
    out += (length_1 - end) + (length_2 - end) + (length_3 - end)
    return out


# Time complexity: O(min(s1, s2, s3))
# Always traversing all indexes of the minimum length string from input strings => O(min(s1, s2, s3)).
# ------------------------------
# Auxiliary space: O(1)
# Only 5 constant INTs used, none of them depends on input => O(1).


test_s1: str = "abc"
test_s2: str = "abb"
test_s3: str = "ab"
test_out: int = 2
assert test_out == find_minimum_operations(test_s1, test_s2, test_s3)

test_s1 = "dac"
test_s2 = "bac"
test_s3 = "cac"
test_out = -1
assert test_out == find_minimum_operations(test_s1, test_s2, test_s3)

test_s1 = "b"
test_s2 = "aba"
test_s3 = "aaccaa"
assert test_out == find_minimum_operations(test_s1, test_s2, test_s3)
