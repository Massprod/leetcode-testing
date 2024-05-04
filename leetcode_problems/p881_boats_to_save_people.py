# You are given an array people where people[i] is the weight of the ith person,
#  and an infinite number of boats where each boat can carry a maximum weight of limit.
# Each boat carries at most two people at the same time, provided the sum of the weight
#  of those people is at most limit.
# Return the minimum number of boats to carry every given person.
# -------------------------
# 1 <= people.length <= 5 * 10 ** 4
# 1 <= people[i] <= limit <= 3 * 10 ** 4
from random import randint


def num_rescue_boats(people: list[int], limit: int) -> int:
    # working_sol (40.82%, 93.50%) -> (354ms, 23.25mb)  time: O(n * log n) | space: O(n)
    new_boat: int
    people.sort()
    left: int = 0
    right: int = len(people) - 1
    out: int = 0
    # ! Each boat carries at most two people ! <- Reason of failure
    # Best tactic is to fill as much weight as we can.
    # So, we can just take maximum weight and try to add smaller weights to it.
    while left <= right:
        ppl: int = 0
        cur_boat: int = 0
        while ppl < 2 and (new_boat := cur_boat + people[right]) <= limit:
            cur_boat += new_boat
            right -= 1
            ppl += 1
        while ppl < 2 and (new_boat := cur_boat + people[left]) <= limit:
            cur_boat += new_boat
            left += 1
            ppl += 1
        out += 1
    return out


# Time complexity: O(n * log n) <- n - length of an input array `people`.
# Always sorting `people` with standard `sort()` => O(n * log n).
# And traversing the whole array again to get all of the boats => O(n).
# -------------------------
# Auxiliary space: O(n)
# Standard `sort()` takes O(n), and we use only 6 constant INT's => O(n + 6).


test: list[int] = [1, 2]
test_limit: int = 3
test_out: int = 1
assert test_out == num_rescue_boats(test, test_limit)

test = [3, 2, 2, 1]
test_limit = 3
test_out = 3
assert test_out == num_rescue_boats(test, test_limit)

test = [3, 5, 3, 4]
test_limit = 5
test_out = 4
assert test_out == num_rescue_boats(test, test_limit)

test = [3, 2, 3, 2, 2]
test_limit = 6
test_out = 3
assert test_out == num_rescue_boats(test, test_limit)

test_limit = randint(1, 3 * 10 ** 4)
test = [randint(1, test_limit) for _ in range(5 * 10 ** 4)]
print(test)
print(f'-----------------\n{test_limit}')
