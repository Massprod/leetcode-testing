# Given a string s, return true if s is a good string, or false otherwise.
# A string s is good if all the characters that appear in s
#  have the same number of occurrences (i.e., the same frequency).
# -------------------
# 1 <= s.length <= 1000
# s consists of lowercase English letters.
from collections import Counter


def are_occurrences_equal(s: str) -> bool:
    # working_sol (94.14%, 15.00%) -> (29ms, 16.68mb)   time: O(s) | space: O(s)
    # {char: occurrences}
    occurs: dict[str, int] = Counter(s)
    first_occ: int = 0
    for occ in occurs.values():
        if not first_occ:
            first_occ = occ
        elif occ != first_occ:
            return False
    return True


# Time complexity: O(s).
# In the worst case every char is unique.
# So, we're going to traverse whole `s` twice => O(2 * s).
# -------------------
# Auxiliary space: O(s)
# Every char is unique and will be stored in `occurs` => O(s).
# Extra storage will all `values` from `occurs` => O(2 * s).


test: str = "abacbc"
test_out: bool = True
assert test_out == are_occurrences_equal(test)

test = "aaabb"
test_out = False
assert test_out == are_occurrences_equal(test)
