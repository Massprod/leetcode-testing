# You are given a positive integer num.
# You may swap any two digits of num that have the same parity
#  (i.e. both odd digits or both even digits).
# Return the largest possible value of num after any number of swaps.
# ---------------------
# 1 <= num <= 10 ** 9
import heapq
from collections import deque


def largest_integer(num: int) -> int:
    # working_sol (79.01%, 58.49%) -> (31ms, 16.54mb)  time: O(n * log n) | space: O(n)
    # Because we can switch for w.e time we want.
    # We can just take maximum ODD|EVEN and place them in front.
    # Always replacing lower values with the same parity.
    odds: list[int] = []
    evens: list[int] = []
    heapq.heapify(odds)
    heapq.heapify(evens)
    # True == even | False == odd
    correct: deque[int | bool] = deque([])
    while num:
        digit: int = num % 10
        if digit % 2:
            heapq.heappush(odds, digit * -1)
            correct.appendleft(False)
        else:
            heapq.heappush(evens, digit * -1)
            correct.appendleft(True)
        num //= 10
    for index, option in enumerate(correct):
        if option is True:
            correct[index] = heapq.heappop(evens) * -1
        else:
            correct[index] = heapq.heappop(odds) * -1
    out: int = 0
    for digit in correct:
        out += digit
        out *= 10
    return out // 10


# Time complexity: O(n * log n) <- n - number of digits in `num`
# Always placing every digit in a heaps and in the worst case, there's only one type of digits,
#  so we're going to have heap of size `n` => O(n * log n).
# Always taking every digit and double traversing them => O(n * log n + 2 * n).
# ---------------------
# Auxiliary space: O(n)
# `correct` <- always of the size `n` => O(n).
# `odds` && `evens` <- always stores `n` digits in them => O(2 * n).


test: int = 1234
test_out: int = 3412
assert test_out == largest_integer(test)

test = 65875
test_out = 87655
assert test_out == largest_integer(test)
