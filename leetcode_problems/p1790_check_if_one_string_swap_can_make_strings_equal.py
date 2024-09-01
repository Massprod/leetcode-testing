# You are given two strings s1 and s2 of equal length.
# A string swap is an operation where you choose two indices in a string (not necessarily different)
#  and swap the characters at these indices.
# Return true if it is possible to make both strings equal by performing at most one string swap
#  on exactly one of the strings.
# Otherwise, return false.
# --------------------------
# 1 <= s1.length, s2.length <= 100
# s1.length == s2.length
# s1 and s2 consist of only lowercase English letters.


def are_almost_equal(s1: str, s2: str) -> bool:
    # working_sol (89.86%, 96.86%) -> (29ms, 16.36mb)  time: O(s1) | space: O(1)
    correct: bool = False
    diff_count: int = 0
    diff_s1: str = ''
    diff_s2: str = ''
    for index in range(len(s1)):
        if s1[index] != s2[index]:
            diff_count += 1
            if 2 < diff_count:
                return False
            elif not diff_s1:
                diff_s1 = s1[index]
                diff_s2 = s2[index]
            elif diff_s1:
                if s1[index] == diff_s2 and s2[index] == diff_s1:
                    correct = True
    if correct or 0 == diff_count:
        return True
    return False


# Time complexity: O(s1)
# Always check all the indexes from both input strings `s1` & `s2` => O(s1 * 2).
# --------------------------
# Auxiliary space: O(1)
# Only constant variables used, none of them depends on input => O(1).


test_1: str = "bank"
test_2: str = "kanb"
test_out: bool = True
assert test_out == are_almost_equal(test_1, test_2)

test_1 = "attack"
test_2 = "defend"
test_out = False
assert test_out == are_almost_equal(test_1, test_2)

test_1 = "kelb"
test_2 = "kelb"
test_out = True
assert test_out == are_almost_equal(test_1, test_2)

test_1 = "aa"
test_2 = "ac"
test_out = False
assert test_out == are_almost_equal(test_1, test_2)
