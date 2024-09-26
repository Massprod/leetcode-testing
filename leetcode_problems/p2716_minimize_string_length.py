# Given a string s, you have two types of operation:
# 1. Choose an index i in the string, and let c be the character in position i.
#    Delete the closest occurrence of c to the left of i (if exists).
# 2. Choose an index i in the string, and let c be the character in position i.
#    Delete the closest occurrence of c to the right of i (if exists).
# Your task is to minimize the length of s by performing the above operations zero or more times.
# Return an integer denoting the length of the minimized string.
# ------------------------
# 1 <= s.length <= 100
# s contains only lowercase English letters


def minimize_string_length(s: str) -> int:
    # working_sol (72.21%, 75.00%) -> (46ms, 16.44mb)  time: O(s) | space: O(s)
    return len(set(s))


# Time complexity: O(s)
# Always converting `s` to `set` => O(s).
# ------------------------
# Auxiliary space: O(s)
# In the worst case, there's only unique strings in `s`.
# `set` we create is going to have all unique strings from `s` => O(s).


test: str = "aaabc"
test_out: int = 3
assert test_out == minimize_string_length(test)

test = "cbbd"
test_out = 3
assert test_out == minimize_string_length(test)

test = "baadccab"
test_out = 4
assert test_out == minimize_string_length(test)
