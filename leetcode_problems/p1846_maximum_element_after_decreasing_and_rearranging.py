# You are given an array of positive integers arr.
# Perform some operations (possibly none) on arr so that it satisfies these conditions:
#  - The value of the first element in arr must be 1.
#  - The absolute difference between any 2 adjacent elements must be less than or equal to 1.
#    In other words, abs(arr[i] - arr[i - 1]) <= 1 for each i where 1 <= i < arr.length (0-indexed).
#     abs(x) is the absolute value of x.
# There are 2 types of operations that you can perform any number of times:
#  - Decrease the value of any element of arr to a smaller positive integer.
#  - Rearrange the elements of arr to be in any order.
# Return the maximum possible value of an element in arr after performing
#  the operations to satisfy the conditions.
# ---------------------
# 1 <= arr.length <= 10 ** 5
# 1 <= arr[i] <= 10 ** 9
from random import randint


def maximum_element(arr: list[int]) -> int:
    # working_sol (90.61%, 21.55%) -> (409ms, 26.4mb)  time: O(n * log n) | space: O(n)
    # Best case == [1, 2, 3, .... n - 1, n] without duplicates.
    arr.sort()
    # If we have min_value higher|equal to len(arr) then we will always decrease everything.
    # So, we get best case without duplicates == (1 -> len(arr)) and max_value = len(arr).
    if arr[0] >= len(arr):
        return len(arr)
    duplicates: int = 0
    # Current maximum in correct sequence.
    base: int = 1
    for x in range(1, len(arr)):
        # If we have duplicates which is going to be used in correct sequence it's always
        #  -1 from maximum value of len(arr) we could had.
        if arr[x] >= len(arr):
            return len(arr) - duplicates
        if arr[x] == base:
            duplicates += 1
        else:
            base += 1
    return base


# Time complexity: O(n * log n) -> sorting input array => O(n * log n) ->
# n - len of input array 'arr'^^| -> extra traverse of every index of this array => O(n).
# Auxiliary space: O(1) -> only 2 constant INT's used, none of them depends on input => O(1).


test: list[int] = [2, 2, 1, 2, 1]
test_out: int = 2
assert test_out == maximum_element(test)

test = [100, 1, 1000]
test_out = 3
assert test_out == maximum_element(test)

test = [1, 2, 3, 4, 5]
test_out = 5
assert test_out == maximum_element(test)

test = [randint(1, 10 ** 9) for _ in range(10 ** 4)]
# print(test)
