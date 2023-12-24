# We have n buildings numbered from 0 to n - 1.
# Each building has a number of employees.
# It's transfer season, and some employees want to change the building they reside in.
# You are given an array requests where requests[i] = [fromi, toi] represents an employee's request
#  to transfer from building fromi to building toi.
# All buildings are full, so a list of requests is achievable only if for each building,
#  the net change in employee transfers is zero.
# This means the number of employees leaving is equal to the number of employees moving in.
# For example if n = 3 and two employees are leaving building 0, one is leaving building 1,
#  and one is leaving building 2, there should be two employees moving to building 0,
#  one employee moving to building 1, and one employee moving to building 2.
# Return the maximum number of achievable requests.
# ---------------------
# 1 <= n <= 20
# 1 <= requests.length <= 16
# requests[i].length == 2
# 0 <= fromi, toi < n
from random import randint


def maximum_requests(n: int, requests: list[list[int]]) -> int:
    # working_sol (94.70%, 15.23%) -> (379ms, 17.3mb)  time: O(2 ** k * n) | space: O(n)
    # Balanced basic state with all changes == 0.
    basic_state: list[int] = [0 for _ in range(n)]
    # Changes we made should lead as either to `basic_state` or we made some request we can't approve.
    cur_state: list[int] = [0 for _ in range(n)]

    def check(index: int, achievable: int) -> int:
        from_: int
        to_: int
        if index == len(requests):
            if cur_state == basic_state:
                return achievable
            return 0
        max_requests: int = 0
        from_, to_ = requests[index]
        cur_state[from_] -= 1
        cur_state[to_] += 1
        max_requests = max(max_requests, check(index + 1, achievable + 1))  # do request
        cur_state[from_] += 1
        cur_state[to_] -= 1
        # No reasons to skip request, if it's 100% achievable.
        if not from_ == to_:
            max_requests = max(max_requests, check(index + 1, achievable))  # skip request
        return max_requests

    return check(0, 0)


# Time complexity: O(2 ** k * n) <- k - length of input array `requests`, n - input value `n`.
# Worst case: we will have n == 1, and `requests` == [0, 1].
# So, we will check every combination (2 ** k == 2 ** 1) == 2, and for each of them we traverse `cur_state` once.
# Otherwise, we will check all combinations (2 ** k) and only end of the paths will check `cur_state` => O(2 ** n * k).
# Auxiliary space: O(n).
# `basic_state` + `cur_state` both of them with size of `n`.
# And recursion stack will be at max `n` as well.


test: int = 5
test_requests: list[list[int]] = [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]
test_out: int = 5
assert test_out == maximum_requests(test, test_requests)

test = 3
test_requests = [[0, 0], [1, 2], [2, 1]]
test_out = 3
assert test_out == maximum_requests(test, test_requests)

test = 4
test_requests = [[0, 3], [3, 1], [1, 2], [2, 0]]
test_out = 4
assert test_out == maximum_requests(test, test_requests)

test_requests = [[randint(0, 19), randint(0, 19)] for _ in range(16)]
print(test_requests)
