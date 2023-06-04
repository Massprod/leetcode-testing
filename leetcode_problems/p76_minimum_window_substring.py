# Given two strings s and t of lengths m and n respectively, return the minimum window substring
#   of s such that every character in t (including duplicates) is included in the window.
#   If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.
# --------------------------
# m == s.length  ,  n == t.length  ,  1 <= m, n <= 10 ** 5
# s and t consist of uppercase and lowercase English letters.
# --------------------------
# Follow up: Could you find an algorithm that runs in O(m + n) time?


def min_window(s: str, t: str) -> str:
    pass


test1 = "ADOBECODEBANC"
test1_t = "ABC"
test1_out = "BANC"

test2 = "a"
test2_t = "a"
test2_out = "a"

test3 = "a"
test3_t = "aa"
test3_out = ""
