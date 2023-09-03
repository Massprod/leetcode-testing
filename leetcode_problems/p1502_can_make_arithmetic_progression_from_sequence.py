# A sequence of numbers is called an arithmetic progression
#  if the difference between any two consecutive elements is the same.
# Given an array of numbers arr, return true if the array can be rearranged
#  to form an arithmetic progression.
# Otherwise, return false.
# ----------------------
# 2 <= arr.length <= 1000
# -10 ** 6 <= arr[i] <= 10 ** 6


def can_make_arith(arr: list[int]) -> bool:
    # working_sol (96.61%, 79.27%) -> (38ms, 16.4mb)  time: O(n * log n) | space: O(1)
    arr.sort()
    diff: int = arr[1] - arr[0]
    for x in range(2, len(arr)):
        if (arr[x] - arr[x - 1]) != diff:
            return False
    return True


# Time complexity: O(n * log n) -> sorting input_array, in place => O(n * log n) -> traversing it whole => O(n).
# n - len of input_array^^|
# Auxiliary space: O(1) -> sorting in place and extra constant INT used => O(1).


test: list[int] = [3, 5, 1]
test_out: bool = True
assert test_out == can_make_arith(test)

test = [1, 2, 4]
test_out = False
assert test_out == can_make_arith(test)
