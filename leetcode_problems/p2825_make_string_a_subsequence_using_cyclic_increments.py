# You are given two 0-indexed strings str1 and str2.
# In an operation, you select a set of indices in str1,
#  and for each index i in the set, increment str1[i] to the next character cyclically.
# That is 'a' becomes 'b', 'b' becomes 'c', and so on, and 'z' becomes 'a'.
# Return true if it is possible to make str2 a subsequence of str1
#  by performing the operation at most once, and false otherwise.
# Note: A subsequence of a string is a new string that is formed from the original string
#  by deleting some (possibly none) of the characters without disturbing
#  the relative positions of the remaining characters.
# -------------------------
# 1 <= str1.length <= 10 ** 5
# 1 <= str2.length <= 10 ** 5
# str1 and str2 consist of only lowercase English letters.


def can_make_subsequence(str1: str, str2: str) -> bool:
    # working_sol (29.86%, 31.28%) -> (92ms, 17.62mb)  time: O(max(n, m)) | space: O(1)
    # We need to preserve order => 2 pointers.
    point_1: int = 0
    point_2: int = 0
    while point_1 < len(str1) and point_2 < len(str2):
        str1_target: str = str1[point_1]
        str2_value: str = str2[point_2]
        # We can use it as it is.
        if str1_target == str2_value:
            point_2 += 1
        else:
            # We need to switch value to next ord of `str1_target`.
            # Or we can reverse to prev ord of `str2_value`.
            str2_ascii: int = ord(str2_value)
            switch_char: str = chr(str2_ascii - 1) if str2_ascii != 97 else 'z'
            # Can be used, after switch.
            if switch_char == str1_target:
                point_2 += 1
        point_1 += 1
    # All chars covered, or we still need to convert something.
    return point_2 == len(str2)


# Time complexity: O(max(n, m)) <- n - length of the input string `str1`, m - length of the input string `str2`.
# Always traversing one of the input strings => O(max(n, m)).
# -------------------------
# Auxiliary space: O(1)
# Only constant values used, none of them depends on input => O(1).


test_1: str = "abc"
test_2: str = "ad"
test_out: bool = True
assert test_out == can_make_subsequence(test_1, test_2)

test_1 = "zc"
test_2 = "ad"
test_out = True
assert test_out == can_make_subsequence(test_1, test_2)

test_1 = "ab"
test_2 = "d"
test_out = False
assert test_out == can_make_subsequence(test_1, test_2)

test_1 = "eao"
test_2 = "ofa"
test_out = False
assert test_out == can_make_subsequence(test_1, test_2)
