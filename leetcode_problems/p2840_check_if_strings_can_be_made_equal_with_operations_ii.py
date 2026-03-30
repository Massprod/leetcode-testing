# You are given two strings s1 and s2, both of length n, consisting of lowercase English letters.
# You can apply the following operation on any of the two strings any number of times:
#  - Choose any two indices i and j such that i < j and the difference j - i is even,
#    then swap the two characters at those indices in the string.
# Return true if you can make the strings s1 and s2 equal, and false otherwise.
# --- --- --- ---
# n == s1.length == s2.length
# 1 <= n <= 10 ** 5
# s1 and s2 consist only of lowercase English letters.
from collections import defaultdict


def check_strings(s1: str, s2: str) -> bool:
    # working_solution: (41.04%, 95.52%) -> (155ms, 19.95mb)  Time: O(s1 + s2) Space: O(s1 + s2)
    # `odd` - `odd` = `even`   <- we can use any `odd` index after `odd` index
    # `odd` - `even` = `odd`
    # `even` - `even` = `even` <- we can use any `even` index after `even` index
    # `even` - `odd` = `odd`
    # We're not limited on actions, so we can swap any `even` and `odd`.
    # So, `even` s1 == s2 and `odd` s1 == s2
    str1_even: dict[str, int] = defaultdict(int)
    str1_odd: dict[str, int] = defaultdict(int)
    for index, value in enumerate(s1):
        if index % 2:
            str1_odd[value] += 1
        else:
            str1_even[value] += 1
    str2_even: dict[str, int] = defaultdict(int)
    str2_odd: dict[str, int] = defaultdict(int)
    for index, value in enumerate(s2):
        if index % 2:
            str2_odd[value] += 1
        else:
            str2_even[value] += 1
    
    return str1_even == str2_even and str1_odd == str2_odd


# Time complexity: O(s1 + s2)
# --- --- --- ---
# Space complexity: O(s1 + s2)


test_s1: str = "abcdba"
test_s2: str = "cabdab"
test_out: bool = True
assert test_out == check_strings(test_s1, test_s2)

test_s1 = "abe"
test_s2 = "bea"
test_out = False
assert test_out == check_strings(test_s1, test_s2)
