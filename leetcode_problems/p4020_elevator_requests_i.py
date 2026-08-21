# You are given an integer n denoting the number of floors in a building,
#  where the floors are numbered from 0 to n - 1.
# You are also given an integer array requests,
#  where requests represents the sequence of floor requests.
# An elevator starts at floor 0 and follows these rules:
#  - The elevator moves one floor per second.
#  - The elevator serves requests in the given order.
#  - If the elevator is already on the requested floor, no movement is needed.
#  - After serving a request, the elevator immediately starts moving toward the next request.
# Return the total time in seconds required to serve all requests.
# --- --- --- ---
# 1 <= n <= 100
# 1 <= requests.length <= 100
# 0 <= requests[i] <= n - 1


def elevator_requests(n: int, requests: list[int]) -> int:
    # working_solution: (100%, 29.98%) -> (0ms, 19.37mb)  Time: O(n) Space: O(1)
    out: int = 0
    floor: int = 0
    for request in requests:
        out += abs(request - floor)
        floor = request

    return out


# Time complexity: O(n)
# --- --- --- ---
# Space complexity: O(1)


test_n: int = 5
test_reqs: list[int] = [2, 1, 4, 3]
test_out: int = 7
assert test_out == elevator_requests(test_n, test_reqs)

test_n = 3
test_reqs = [2, 0, 0]
test_out = 4
assert test_out == elevator_requests(test_n, test_reqs)
