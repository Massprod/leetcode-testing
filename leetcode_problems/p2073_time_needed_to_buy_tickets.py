# There are n people in a line queuing to buy tickets, where the 0th person is
#  at the front of the line and the (n - 1)th person is at the back of the line.
# You are given a 0-indexed integer array tickets of length n where the number of tickets
#  that the ith person would like to buy is tickets[i].
# Each person takes exactly 1 second to buy a ticket.
# A person can only buy 1 ticket at a time and has to go back to the end of the line
#  (which happens instantaneously) in order to buy more tickets.
# If a person does not have any tickets left to buy, the person will leave the line.
# Return the time taken for the person at position k (0-indexed) to finish buying tickets.
# -------------------------
# n == tickets.length
# 1 <= n <= 100
# 1 <= tickets[i] <= 100
# 0 <= k < n
from random import randint
from collections import Counter


def time_required(tickets: list[int], k: int) -> int:
    # working_sol (69.89%, 51.83%) -> (43ms, 16.57mb)  time: O(n * log n) | space: O(n)
    cur_min: int
    min_ppl: int
    # To make it easier, we need to place our Buyer in the of the line.
    out: int = 0
    # So, if he is not at the End, place him there.
    if 99 != k:
        for _ in range(k + 1):
            tickets[_] -= 1
            out += 1
    # Now we know, that there's len(tickets) ppl in the line (including our Buyer).
    # And we are at the End, so everyone will buy tickets before us.
    # {number of tickets: number of persons which wants it}
    all_ppl: dict[int, int] = Counter(tickets)
    # But, some of them might be already out, because they were in front of Buyer and needed only 1 ticket.
    if 0 in all_ppl:
        all_ppl.pop(0)
    order: list[tuple[int, int]] = [(num_of_tickets, num_of_ppl) for num_of_tickets, num_of_ppl in all_ppl.items()]
    order.sort(key=lambda x: x[0])
    cur_ppl: int = sum(all_ppl.values())  # Current # of ppl in the line.
    prev_min: int = 0  # Time already spend in the line.
    cur_ind: int = 0
    bought_tickets: int = tickets[k]  # Tickets our Buyer wants, after 1 round.
    # Line will never change, except when someone is out from it (bought enough).
    # If we know how many ppl in the line, and we know how many tickets we can get before someone is out.
    # We can call it a ROUND and just calc as: (ppl in the line * time before first will go out)
    while bought_tickets and cur_ind < len(order):
        cur_min, min_ppl = order[cur_ind]
        # cur_min == Time we need to buy all tickets for these persons, if we count from 0.
        round_time: int = cur_min - prev_min
        bought_tickets -= round_time
        # Because we're at the End of the line, we will wait through all ppl in front us.
        # Until, some of them are not satisfied.
        out += cur_ppl * round_time
        prev_min = cur_min  # Current time we spend in the line.
        cur_ppl -= min_ppl  # PPl left in the line.
        cur_ind += 1
    out += bought_tickets
    return out


# Time complexity: O(n * log n) <- n - length of input array `tickets`.
# Worst case: every value in `tickets` will be unique.
# So, we will add all of them in `all_ppl` and sort after => O(n * log n).
# Everything except sorting, is linear.
# -------------------------
# Auxiliary space: O(n)
# Same worst case, sort() will take `n` space as standard.
# And extra dictionary with all uniques `all_ppl`.
# And list `order` with same size == n, with all unique values counted => O(3n).


test: list[int] = [2, 3, 2]
test_k: int = 2
test_out: int = 6
assert test_out == time_required(test, test_k)

test = [5, 1, 1, 1]
test_k = 0
test_out = 8
assert test_out == time_required(test, test_k)

test = [randint(1, 100) for _ in range(100)]
print(test)
