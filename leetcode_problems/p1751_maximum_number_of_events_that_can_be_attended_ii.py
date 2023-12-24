# You are given an array of events where events[i] = [startDayi, endDayi, valuei].
# The ith event starts at startDayi and ends at endDayi, and if you attend this event,
#  you will receive a value of valuei.
# You are also given an integer k which represents the maximum number of events you can attend.
# You can only attend one event at a time.
# If you choose to attend an event, you must attend the entire event.
# Note that the end day is inclusive: that is, you cannot attend two events where
#  one of them starts and the other ends on the same day.
# Return the maximum sum of values that you can receive by attending events.
# ------------------------
# 1 <= k <= events.length
# 1 <= k * events.length <= 10 ** 6
# 1 <= startDayi <= endDayi <= 10 ** 9
# 1 <= valuei <= 10 ** 6
from functools import cache
from random import randint


def max_value(events: list[list[int]], k: int) -> int:
    # working_sol (43.50%, 25.80%) -> (1926ms, 256.98mb)  time: O(n * k + n * log n) | space: O(n * k + n)
    events.sort(key=lambda y: y[0])

    @cache
    def bs(target: int) -> int:
        """
        Binary search to get rightmost index with value == target.
        Or where it can be placed without disrupting sorted order.
        bisect.bisect_right() <- similar.
        :param target: value for placement search
        :return: index with correct insert() position
        """
        left: int = 0
        right: int = len(events) - 1
        while left <= right:
            middle: int = (left + right) // 2
            # We need day from which we can start a new event.
            # So it's always higher than target => shift right until we can.
            if events[middle][0] <= target:
                left = middle + 1
            else:
                right = middle - 1
        return left

    @cache
    def check(index: int, visited: int) -> int:
        best_path: int = 0
        # No events left, or we visited our limit == `k`.
        if index == len(events) or visited == k:
            return best_path
        best_path = max(
            # Ignore event and just try next.
            check(index + 1, visited),
            # Visit event and attend nearest, after endDay.
            events[index][2] + check(bs(events[index][1]), visited + 1),
        )
        return best_path

    return check(0, 0)


# Time complexity: O(n * k + n * log n) <- n - length of input array `events`, k - input value `k`.
# We're using @cache for memorisation, and we will at max have (n * k) states of (index, visited).
# So, they will be calculated once. And for each `endDay` we will use BS to get rightmost equal or place where
#  it could be placed without disrupting sorted order in `events`.
# O(n * k + n * log n).
# ------------------------
# Auxiliary space: O(n * k + n).
# For every state we will store its result in @cache + results of BS will be stored as well.
# There's (n * k) states we can have, and in the worst case if every endDay is unique we will have `n` calls to BS.
# O(n * k + n).


test: list[list[int]] = [[1, 2, 4], [3, 4, 3], [2, 3, 1]]
test_k: int = 2
test_out: int = 7
assert test_out == max_value(test, test_k)

test = [[1, 2, 4], [3, 4, 3], [2, 3, 10]]
test_k = 2
test_out = 10
assert test_out == max_value(test, test_k)

test = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]
test_k = 3
test_out = 9
assert test_out == max_value(test, test_k)

# k == 1000, cuz k * length == 10 ** 6 max.
test = [[randint(1, 10 ** 5), randint(10 ** 5 + 1, 10 ** 9), randint(1, 10 ** 6)] for _ in range(10 ** 3)]
print(test)
