# You are given a string s.
# You can perform the following process on s any number of times:
#  - Choose an index i in the string such that there is at least one character
#    to the left of index i that is equal to s[i],
#    and at least one character to the right that is also equal to s[i].
#  - Delete the closest character to the left of index i that is equal to s[i].
#  - Delete the closest character to the right of index i that is equal to s[i].
# Return the minimum length of the final string s that you can achieve.
# ---------------------
# 1 <= s.length <= 2 * 10 ** 5
# s consists only of lowercase English letters.
from collections import Counter


def minimum_length(s: str) -> int:
    # working_sol (14.60%, 32.70%) -> (295ms, 18.89mb)  time: O(s) | space: O(s)
    # { char: occurrences }
    chars: dict[str, int] = Counter(s)
    # Essentially, we only care about deleting both chars (left and right).
    # And we can delete them, only if there's at least 3 occurrences of a char in `s`.
    out: int = 0
    for char in s:
        if char in chars:
            if chars[char] % 2:
                out += 1
                del chars[char]
            else:
                out += 2
                del chars[char]
    return out



# Time complexity: O(s)
# Always traversing whole input string to count all chars and their occurrences => O(s).
# In the worst case, every char in `s` is unique.
# We will traverse all the chars again => O(2 * s).
# ---------------------
# Auxiliary space: O(s)
# `chars` <- allocates space for all unique chars from `s` => O(s).


test: str = "abaacbcbb"
test_out: int = 5
assert test_out == minimum_length(test)

test = "aa"
test_out = 2
assert test_out == minimum_length(test)
