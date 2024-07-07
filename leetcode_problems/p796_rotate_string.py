# Given two strings s and goal,
#  return true if and only if s can become goal after some number of shifts on s.
# A shift on s consists of moving the leftmost character of s to the rightmost position.
# For example, if s = "abcde", then it will be "bcdea" after one shift.
# --------------------------
# 1 <= s.length, goal.length <= 100
# s and goal consist of lowercase English letters.


def rotate_string(s: str, goal: str) -> bool:
    # working_sol (80.12%, 61.61%) -> (31ms, 16.47mb)  time: O(s * (s + n)) | space: O(s + n)
    if len(s) != len(goal) and set(s) != set(goal):
        return False
    for index in range(len(s)):
        if goal == (s[index:] + s[:index]):
            return True
    return False


# Time complexity: O(s * (s + n)) <- n - length of the input string `goal`.
# Always traversing both input strings `s` and `goal` to get all unique values and comparing them => O(s + n).
# For every index in `s` slicing it fully traversing with `goal => O(s * (2s + n)).
# --------------------------
# Auxiliary space: O(s + n)
# Every set we create is, in the worst case, the same size as a string == unique values => O(s + n).
# Slicing also uses space to recreate and slice whole `s` => O(3s + n).


test_s: str = "abcde"
test_goal: str = "cdeab"
test_out: bool = True
assert test_out == rotate_string(test_s, test_goal)

test_s = "abcde"
test_goal = "abced"
test_out = False
assert test_out == rotate_string(test_s, test_goal)
