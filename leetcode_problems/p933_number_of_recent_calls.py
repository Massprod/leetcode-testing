# You have a RecentCounter class which counts the number of recent requests within a certain time frame.
# Implement the RecentCounter class:
#   RecentCounter() Initializes the counter with zero recent requests.
#   int ping(int t) Adds a new request at time t, where t represents some time in milliseconds,
#     and returns the number of requests that has happened in the past 3000 milliseconds (including the new request).
#   Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
# It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.
# ----------------
# 1 <= t <= 10 ** 9
# Each test case will call ping with strictly increasing values of t.
# At most 10 ** 4 calls will be made to ping.
from collections import deque


class RecentCounter:
    # working_sol (91.57%, 66.44%) -> (219ms, 21.59mb)
    def __init__(self):
        self.ping_que: deque = deque()

    def ping(self, t: int) -> int:
        self.ping_que.append(t)
        while not (t - 3000) <= self.ping_que[0] <= t:
            self.ping_que.popleft()
        return len(self.ping_que)


# Time complexity:
#   init: O(1) -> always constant.
#   ping: O(n) -> worst case, we're getting ping with value higher than everything stored so far,
#                 so we're going to delete everything from ping_que except this new_value => O(n).
#   n - len of ping_que, before current call^^|
# Auxiliary space:
#   init: O(3000) -> always constant, maximum stores 3000 values at the time.
#   ping: O(1) -> worst case, we're always calling in this range from 1, to 3000 inclusive.
#                 Actually it's just maximum of 3000 values stored, but it can be dropped to 1 at any time.
#                 And not even ping() stores it, so it's just object of this class with O(3000) ?
# ----------------
# No reasons to bother with test_cases, cuz we always guaranteed with ->
# ! guaranteed that every call to ping uses a strictly larger value of t than the previous call ! ->
# -> so we don't need to filter anything except outdated values in deque, delete them and return len(what's left).
