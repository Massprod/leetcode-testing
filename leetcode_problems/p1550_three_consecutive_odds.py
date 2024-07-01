# Given an integer array arr,
#  return true if there are three consecutive odd numbers in the array.
# Otherwise, return false.
# ---------------------------
# 1 <= arr.length <= 1000
# 1 <= arr[i] <= 1000
from random import randint


def three_cons_odds(arr: list[int]) -> bool:
    # working_sol (85.64%, 93.64%) -> (42ms, 16.58mb)  time: O(n) | space: O(1)
    count: int = 0
    for val in arr:
        if val % 2:
            count += 1
        else:
            count = 0
        if 3 == count:
            return True
    return False


# Time complexity: O(n) <- n - length of the input array `arr`.
# In the worst case, we're going to traverse the whole `arr`, once => O(n).
# ---------------------------
# Auxiliary space: O(1)


test: list[int] = [2, 6, 4, 1]
test_out: bool = False
assert test_out == three_cons_odds(test)

test = [1, 2, 34, 3, 4, 5, 7, 23, 12]
test_out = True
assert test_out == three_cons_odds(test)

test = [randint(1, 1000) for _ in range(1000)]
print(test)
