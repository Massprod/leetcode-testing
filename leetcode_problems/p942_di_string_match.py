# A permutation perm of n + 1 integers of all the integers in the range [0, n]
#  can be represented as a string s of length n where:
#  - s[i] == 'I' if perm[i] < perm[i + 1], and
#  - s[i] == 'D' if perm[i] > perm[i + 1].
# Given a string s, reconstruct the permutation perm and return it.
# If there are multiple valid permutations perm, return any of them.
# ------------------------
# 1 <= s.length <= 10 ** 5
# s[i] is either 'I' or 'D'.
from random import choice


def di_string_match(s: str) -> list[int]:
    # working_sol (87.58%, 16.23%) -> (46ms, 17.96mb)  time: O(s) | space: O(s)
    # There's always +1 value to cover the last 'I' or 'D'.
    int_range: list[int] = [val for val in range(0, len(s) + 1)]
    # And the best way to build `perm` is to use
    #  `cur_lowest` and `cur_higher` for 'I' and 'D' from left -> right manner.
    # Because after using `cur_lowest` w.e we meet next is going to be correct:
    #  'II' <- we used 0 and after that next `cur_lowest` is 1.
    #  'DD' <- we used 2, and after that the next `cur_highest` is 1.
    #  etc. can be seen in provided test_cases from the first look.
    min_point: int = 0
    max_point: int = len(int_range) - 1
    out: list[int] = []
    for char in s:
        if 'I' == char:
            out.append(int_range[min_point])
            min_point += 1
        elif 'D' == char:
            out.append(int_range[max_point])
            max_point -= 1
    # And because we always have +1 extra value, we still need to use it after everything else.
    return out + [max_point]


# Time complexity: O(s)
# Always creating `int_range` of size `s + 1` => O(s + 1).
# Extra traversing every char in `s` to get our `perm` => O(s + (s + 1)).
# ------------------------
# Auxiliary space: O(s)
# `int_range` of size `s + 1` => O(s + 1).
# `out` with all the values from `int_range` but in correct order => O(2 * (s + 1)).


test: str = "IDID"
test_out: list[int] = [0, 4, 1, 3, 2]
assert test_out == di_string_match(test)

test = "III"
test_out = [0, 1, 2, 3]
assert test_out == di_string_match(test)

test = "DDI"
test_out = [3, 2, 0, 1]
assert test_out == di_string_match(test)

test = ''.join([choice(['I', 'D']) for _ in range(10 ** 5)])
print(test)
