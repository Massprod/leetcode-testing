# Given a string s consisting of lowercase English letters,
#  return the first letter to appear twice.
# Note:
#  - A letter a appears twice before another letter b if the second occurrence
#   of a is before the second occurrence of b.
#  - s will contain at least one letter that appears twice.
# -------------------------
# 2 <= s.length <= 100
# s consists of lowercase English letters.
# s has at least one repeated letter.


def repeated_character(s: str) -> str:
    # working_sol (96.19%, 54.55%) -> (26ms, 16.44mb)  time: O(s) | space: O(s)
    appeared: set[str] = set()
    for char in s:
        if char in appeared:
            return char
        appeared.add(char)
    return ''


# Time complexity: O(s)
# Always traversing whole `s`, once => O(s).
# -------------------------
# Auxiliary space: O(s)
# In the worst case, every char except the last one is unique.
# `appeared` <- will allocate space for `len(s) - 1` chars => O(s - 1).


test: str = "abccbaacz"
test_out: str = "c"
assert test_out == repeated_character(test)

test = "abcdd"
test_out = "d"
assert test_out == repeated_character(test)
