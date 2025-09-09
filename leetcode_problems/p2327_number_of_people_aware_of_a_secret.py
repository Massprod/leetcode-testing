# On day 1, one person discovers a secret.
# You are given an integer delay, which means that each person will share the secret
#  with a new person every day, starting from delay days after discovering the secret.
# You are also given an integer forget, which means that each person will forget
#  the secret forget days after discovering it.
# A person cannot share the secret on the same day they forgot it, or on any day afterwards.
# Given an integer n, return the number of people who know the secret at the end of day n.
# Since the answer may be very large, return it modulo 10 ** 9 + 7.
# --- --- --- ---
# 2 <= n <= 1000
# 1 <= delay < forget <= n
from collections import deque


def people_aware_of_secret(n: int, delay: int, forget: int) -> int:
    # working_solution: (91.24%, 90.51%) -> (3ms, 17.76mb)  Time: O(n) Space: O(n)
    # [ day, number of people ]
    ppl_know: deque[tuple[int, int]] = deque([(1, 1)])
    # [ day, number of people ]
    ppl_shared: deque[tuple[int, int]] = deque([])
    know: int = 1
    share: int = 0
    for day in range(2, n + 1):
        # There's people who know the secret and time to share has come.
        if ppl_know and ppl_know[0][0] == day - delay:
            know -= ppl_know[0][1]
            share += ppl_know[0][1]
            ppl_shared.append(
                ppl_know.popleft()
            )
        # There's people who shared the secret and time to forget has come.
        if ppl_shared and ppl_shared[0][0] == day - forget:
            share -= ppl_shared.popleft()[1]
        # Every day, every person who knows a secret is sharing it.
        if ppl_shared:
            know += share
            ppl_know.append(
                (day, share)
            )
    
    return (know + share) % (10 ** 9 + 7)


# Time complexity: O(n) <- n - input value of the days.
# We simulate all operations on every day that passes => O(n).
# --- --- --- ---
# Space complexity: O(n)
# In the worst case, no secret is discovered.
# `ppl_know` <- allocates space for each day => O(n).
# Or no one forgets them.
# `ppl_shared` <- allocates space for each day => O(2 * n).


test_n: int = 6
test_delay: int = 2
test_forget: int = 4
test_out: int = 5
assert test_out == people_aware_of_secret(test_n, test_delay, test_forget)

test_n = 4
test_delay = 1
test_forget = 3
test_out = 6
assert test_out == people_aware_of_secret(test_n, test_delay, test_forget)
