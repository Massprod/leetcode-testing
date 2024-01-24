# Given a string s, return the number of segments in the string.
# A segment is defined to be a contiguous sequence of non-space characters.
# -------------------------
# 0 <= s.length <= 300
# s consists of lowercase and uppercase English letters, digits,
#  or one of the following characters "!@#$%^&*()_+-=',.:".
# The only space character in s is ' '.


def count_segments(s: str) -> int:
    # working_sol (79.77%, 54.80%) -> (33ms, 16.44mb)  time: O(n) | space: O(1)
    out: int = 0
    start: bool = False
    # New char => new sequence.
    # Space-char => sequence break.
    for char in s:
        if ' ' != char:
            if not start:
                start = True
                out += 1
        else:
            start = False
    return out


# Time complexity: O(s).
# Single traverse of the whole input string `s` => O(s).
# -------------------------
# Auxiliary space: O(1).
# Nothing depends on input.


test: str = "Hello, my name is John"
test_out: int = 5
assert test_out == count_segments(test)

test = "Hello"
test_out = 1
assert test_out == count_segments(test)
