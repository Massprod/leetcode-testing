# You are given a string s and two distinct lowercase English letters x and y.
# Rearrange the characters of s to construct a new string t such that:
#  - t is a permutation of s.
#  - Every occurrence of y appears before every occurrence of x in t.
# Return any valid string t.
# --- --- --- ---
# 1 <= s.length <= 100
# s consists of lowercase English letters.
# x and y are lowercase English letters.
# x != y


def rearrange_string(s: str, x: str, y: str) -> str:
    # working_solution: (100%, 100%) -> (0ms, 19.23mb)  Time: O(s) Space: O(s)
    out: list [str] = []
    suffix: list[str] = []
    for char in s:
        if x == char:
            suffix.append(char)
            continue
        out.append(char)
    
    out.extend(suffix)
    return "".join(out)


# Time complexity: O(s)
# --- --- --- ---
# Space complexity: O(s)


test_s: str = "aabc"
test_x: str = "a"
test_y: str = "c"
test_out: str = "cbaa"
assert test_out == rearrange_string(test_s, test_x, test_y)

test_s = "dcab"
test_x = "d"
test_y = "b"
test_out = "cabd"
assert test_out == rearrange_string(test_s, test_x, test_y)

test_s = "axe"
test_x = "o"
test_y = "x"
test_out = "axe"
assert test_out == rearrange_string(test_s, test_x, test_y)
