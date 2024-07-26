# A string s can be partitioned into groups of size k using the following procedure:
#  - The first group consists of the first k characters of the string,
#    the second group consists of the next k characters of the string, and so on.
#    Each character can be a part of exactly one group.
#  - For the last group, if the string does not have k characters remaining,
#    a character fill is used to complete the group.
# Note that the partition is done so that after removing the fill character
#  from the last group (if it exists) and concatenating all the groups in order,
#  the resultant string should be s.
# Given the string s, the size of each group k and the character fill,
#  return a string array denoting the composition of every group s has
#  been divided into, using the above procedure.
# ----------------------------
# 1 <= s.length <= 100
# s consists of lowercase English letters only.
# 1 <= k <= 100
# fill is a lowercase English letter.


def divide_string(s: str, k: int, fill: str) -> list[str]:
    # working_sol (70.20%, 76.75%) -> (34ms, 16.48mb)  time: O(s + (k - 1)) | space: O(s + (k - 1))
    out: list[str] = []
    start: int = 0
    while start < len(s):
        out.append(s[start: start + k])
        start += k
    while len(out[-1]) < k:
        out[-1] += fill
    return out


# Time complexity: O(s + (k - 1))
# Always slicing whole `s` in groups => O(s).
# Extra (k - 1) elements added to `out[-1]` in the worst case => O(s + (k - 1))
# ----------------------------
# Auxiliary space: O(s + (k - 1))
# Same worst-case, we're only going to have 1 element for the last group => O(s + (k - 1)).


test: str = "abcdefghi"
test_k: int = 3
test_fill: str = "x"
test_out: list[str] = ["abc", "def", "ghi"]
assert test_out == divide_string(test, test_k, test_fill)

test = "abcdefghij"
test_k = 3
test_fill = "x"
test_out = ["abc", "def", "ghi", "jxx"]
assert test_out == divide_string(test, test_k, test_fill)
