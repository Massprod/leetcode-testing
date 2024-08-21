# You are given a string s, where every two consecutive vertical bars '|' are grouped into a pair.
# In other words, the 1st and 2nd '|' make a pair, the 3rd and 4th '|' make a pair, and so forth.
# Return the number of '*' in s, excluding the '*' between each pair of '|'.
# Note that each '|' will belong to exactly one pair.
# -----------------------
# 1 <= s.length <= 1000
# s consists of lowercase English letters, vertical bars '|', and asterisks '*'.
# s contains an even number of vertical bars '|'.


def count_asterisks(s: str) -> int:
    # working_sol (72.29%, 83.14%) -> (34ms, 16.43mb)  time: O(s) | space: O(1)
    out: int = 0
    line_pair: bool = False
    for char in s:
        if '|' == char:
            line_pair = not line_pair
        if not line_pair and '*' == char:
            out += 1
    return out


# Time complexity: O(s)
# Always traversing whole input string `s`, once => O(s).
# -----------------------
# Auxiliary space: O(1).


test: str = "l|*e*et|c**o|*de|"
test_out: int = 2
assert test_out == count_asterisks(test)

test = "iamprogrammer"
test_out = 0
assert test_out == count_asterisks(test)

test = "yo|uar|e**|b|e***au|tifu|l"
test_out = 5
assert test_out == count_asterisks(test)
