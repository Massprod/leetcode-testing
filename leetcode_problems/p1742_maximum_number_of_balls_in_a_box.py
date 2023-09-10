# You are working in a ball factory where you have n balls numbered from lowLimit up to highLimit
#  inclusive (i.e., n == highLimit - lowLimit + 1), and an infinite number of boxes
#  numbered from 1 to infinity.
# Your job at this factory is to put each ball in the box with a number equal to the sum of digits
#  of the ball's number.
# For example, the ball number 321 will be put in the box number 3 + 2 + 1 = 6
#  and the ball number 10 will be put in the box number 1 + 0 = 1.
# Given two integers lowLimit and highLimit, return the number of balls in the box with the most balls.
# --------------------
# 1 <= lowLimit <= highLimit <= 10 ** 5


def count_balls(lowLimit: int, highLimit: int) -> int:
    # working_sol (95.69%, 72.97%) -> (232ms, 16.26mb)  time: O(n * log n) | space: O(K)
    boxes: dict[int, int] = {}
    # Standard digits sum.
    for x in range(lowLimit, highLimit + 1):
        cur_sum: int = 0
        while x:
            cur_sum += x % 10
            x //= 10
        if cur_sum not in boxes:
            boxes[cur_sum] = 1
            continue
        boxes[cur_sum] += 1
    return max(boxes.values())


# Time complexity: O(n * log n) -> for every ball taking its digits sum => O(n * log n).
# n - ball numbers to use == range(lowLimit, highLimit + 1)^^|
# Auxiliary space: O(K) -> for every unique sum store its digits sum, in case like (1, 9) store everything,
#                       so it should be O(n), but for higher it can be less or more like 71 and 17 ->
#                       -> better to stick with K == unique sums => O(K).


test_high: int = 10
test_low: int = 1
test_out: int = 2
assert test_out == count_balls(test_low, test_high)

test_high = 15
test_low = 5
test_out = 2
assert test_out == count_balls(test_low, test_high)

test_high = 28
test_low = 19
test_out = 2
assert test_out == count_balls(test_low, test_high)

test_high = 11111
test_low = 999
test_out = 681
assert test_out == count_balls(test_low, test_high)
