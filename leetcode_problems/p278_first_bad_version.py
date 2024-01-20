# You are a product manager and currently leading a team to develop a new product. Unfortunately,
#  the latest version of your product fails the quality check.
# Since each version is developed based on the previous version,
#  all the versions after a bad version are also bad.
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
#  which causes all the following ones to be bad.
# You are given an API bool isBadVersion(version) which returns whether version is bad.
# Implement a function to find the first bad version.
# You should minimize the number of calls to the API.
# ----------------------
# 1 <= bad <= n <= 2 ** 31 - 1


def isBadVersion(bad: int) -> bool:
    global test_out
    return test_out <= bad


def first_bad_version(n: int) -> int:
    # working_sol (90.84%, 57.75%) -> (30ms, 16.48mb)  time: O(log n) | space: O(1)
    # ! Suppose you have n versions [1, 2, ..., n] !
    left: int = 1
    right: int = n
    while left <= right:
        middle: int = (left + right) // 2
        if isBadVersion(middle):
            right = middle - 1
        else:
            left = middle + 1
    return left


# Time complexity: O(log n).
# Standard BS algo.
# Auxiliary space: O(1)


test: int = 5
test_out: int = 4
assert test_out == first_bad_version(test)

test = 1
test_out = 1
assert test_out == first_bad_version(test)
