# Given a string s consisting of only the characters 'a' and 'b',
#  return true if every 'a' appears before every 'b' in the string.
# Otherwise, return false.
# ---------------------
# 1 <= s.length <= 100
# s[i] is either 'a' or 'b'.


def check_string(s: str) -> bool:
    # working_sol (89.05%, 62.27%) -> (29ms, 16.45mb)  time: O(s) | space: O(1)
    b_present: bool = False
    for char in s:
        if 'a' == char:
            if b_present:
                return False
        elif 'b' == char:
            b_present = True
    return True


# Time complexity: O(s)
# Always traversing `s`, once => O(s).
# ---------------------
# Auxiliary space: O(1).


test: str = "aaabbb"
test_out: bool = True
assert test_out == check_string(test)

test = "abab"
test_out = False
assert test_out == check_string(test)

test = "bbb"
test_out = True
assert test_out == check_string(test)
