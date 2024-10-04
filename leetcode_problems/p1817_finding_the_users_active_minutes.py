# You are given the logs for users' actions on LeetCode, and an integer k.
# The logs are represented by a 2D integer array logs where each logs[i] = [IDi, timei]
#  indicates that the user with IDi performed an action at the minute timei.
# Multiple users can perform actions simultaneously,
#  and a single user can perform multiple actions in the same minute.
# The user active minutes (UAM) for a given user is defined as the number of unique minutes
#  in which the user performed an action on LeetCode.
# A minute can only be counted once, even if multiple actions occur during it.
# You are to calculate a 1-indexed array answer of size k such that, for each j (1 <= j <= k),
#  answer[j] is the number of users whose UAM equals j.
# Return the array answer as described above.
# ------------------------
# 1 <= logs.length <= 10 ** 4
# 0 <= IDi <= 10 ** 9
# 1 <= timei <= 10 ** 5
# k is in the range [The maximum UAM for a user, 10 ** 5].
from collections import defaultdict


def finding_users_active_minutes(logs: list[list[int]], k: int) -> list[int]:
    # working_sol (47.03%, 84.44%) -> (716ms, 26.90mb)  time: O(n) | space: O(n)
    # { user: { minutes when performed } }
    users: dict[int, set[int]] = defaultdict(set)
    for log in logs:
        users[log[0]].add(log[1])
    # { uam : number of users }
    uams: dict[int, int] = defaultdict(int)
    for user in users:
        user_uam: int = len(users[user])
        uams[user_uam] += 1
    # 1 - indexed array
    out: list[int] = [0 for _ in range(k)]
    for uam in uams:
        out[uam - 1] = uams[uam]  # -1 for 1 - indexed array
    return out


# Time complexity: O(n) <- n - length of the input array `logs`.
# In the worst case:
#  - logs all records unique == we're getting `n` users with unique minute performances
# We will traverse `logs` to get them => O(n).
# Extra traversing all unique users == `n` => O(2 * n).
# And traversing all unique `uam` of these users => O(3 * n).
# ------------------------
# Auxiliary space: O(n)
# Same worst case.
# `users` <- allocates space for all unique users == `n` => O(n).
# `uams` <- allocates space for all unique users `uam` => O(2 * n).
# `out` <- always allocates space for `k` values => O(2 * n + k).


test: list[list[int]] = [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]]
test_k: int = 5
test_out: list[int] = [0, 2, 0, 0, 0]
assert test_out == finding_users_active_minutes(test, test_k)

test = [[1, 1], [2, 2], [2, 3]]
test_k = 4
test_out = [1, 1, 0, 0]
assert test_out == finding_users_active_minutes(test, test_k)
