# Given two version numbers, version1 and version2, compare them.
# Version numbers consist of one or more revisions joined by a dot '.'.
# Each revision consists of digits and may contain leading zeros.
# Every revision contains at least one character.
# Revisions are 0-indexed from left to right, with the leftmost revision being revision 0,
#  the next revision being revision 1, and so on.
# For example 2.5.33 and 0.1 are valid version numbers.
# To compare version numbers, compare their revisions in left-to-right order.
# Revisions are compared using their integer value ignoring any leading zeros.
# This means that revisions 1 and 001 are considered equal.
# If a version number does not specify a revision at an index,
#  then treat the revision as 0.
# For example, version 1.0 is less than version 1.1 because their revision 0s are the same,
#  but their revision 1s are 0 and 1 respectively, and 0 < 1.
# Return the following:
#   If version1 < version2, return -1.
#   If version1 > version2, return 1.
#   Otherwise, return 0.
# ---------------------------
# 1 <= version1.length, version2.length <= 500
# version1 and version2 only contain digits and '.'.
# version1 and version2 are valid version numbers.
# All the given revisions in version1 and version2 can be stored in a 32-bit integer.
from random import randint


def compare_version(version1: str, version2: str) -> int:
    # working_sol (81.16%, 57.93%) -> (31ms, 16.56mb)  time: O(max(m, n)) | space: O(max(m, n))
    left: int
    new_end: int
    num1: int
    num2: int
    out: int = 0
    # Comparing everything, until we run out of one.
    while version1 and version2:
        end1: int = version1.find('.')
        end2: int = version2.find('.')
        if -1 != end1:
            num1 = int(version1[:end1])
            version1 = version1[end1 + 1:]
        else:
            num1 = int(version1)
            version1 = ''
        if -1 != end2:
            num2 = int(version2[:end2])
            version2 = version2[end2 + 1:]
        else:
            num2 = int(version2)
            version2 = ''
        if num1 < num2:
            out = -1
            return out
        elif num1 > num2:
            out = 1
            return out
    # If we ran out of ONE version string, then everything was equal.
    # And now we need to see what's left, if there's only '00000' then they're equal.
    # Otherwise, one of them is Higher.
    while version1:
        new_end = version1.find('.')
        if -1 != new_end:
            left = int(version1[:new_end])
            version1 = version1[new_end + 1:]
        else:
            left = int(version1)
            version1 = ''
        if 0 != left:
            out = 1
            break
    while version2:
        new_end = version2.find('.')
        if -1 != new_end:
            left = int(version2[:new_end])
            version2 = version2[new_end + 1:]
        else:
            left = int(version2)
            version2 = ''
        if 0 != left:
            out = -1
            break
    return out


# Time complexity: O(max(m, n)) <- m - length of input string `version1` , n - length of input string `version2`
# A lot of slicing and search in string, but all of them are Linear.
# ---------------------------
# Auxiliary space: O(max(m, n))
# Worst case: there's no DOTs in string, so we will slice and save whole string.


test_v1: str = "1.01"
test_v2: str = "1.001"
test_out: int = 0
assert test_out == compare_version(test_v1, test_v2)

test_v1 = "1.0"
test_v2 = "1.0.0"
test_out = 0
assert test_out == compare_version(test_v1, test_v2)

test_v1 = "0.1"
test_v2 = "1.1"
test_out = -1
assert test_out == compare_version(test_v1, test_v2)

test_v1 = '1.0'
test_v2 = '1'
test_out = 0
assert test_out == compare_version(test_v1, test_v2)

test_v1 = '1.0.1'
test_v2 = '1'
test_out = 1
assert test_out == compare_version(test_v1, test_v2)

test_v1 = ''
for _ in range(45):
    add: str = ''
    for _ in range(5):
        add += str(randint(0, 9))
    add += '.'
    test_v1 += add
test_v1 += '22'
print(test_v1)
