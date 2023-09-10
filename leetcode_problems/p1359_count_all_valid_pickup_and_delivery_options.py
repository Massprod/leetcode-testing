# Given n orders, each order consist in pickup and delivery services.
# Count all valid pickup/delivery possible sequences such that delivery(i)
#  is always after of pickup(i).
# Since the answer may be too large, return it modulo 10^9 + 7.
# --------------------
# 1 <= n <= 500
from math import factorial


def count_orders(n: int) -> int:
    # working_sol (5.11%, 5.53%) -> (1179ms, 600.52mb)  time: O(n ** 3) | space: O(n * n)
    recur_cache: dict[tuple[int, int], int] = {}

    def check(picks: int, deliv: int) -> int:
        if (picks, deliv) in recur_cache:
            return recur_cache[picks, deliv]
        # If we don't have anything to pick up,
        #  then all we need is to place Deliveries.
        # We don't care about their placement and there's -> n!
        #  sequence permutations to do this.
        if picks == 0:
            return factorial(deliv)
        pairs: int = 0
        # We can't pick up over given limit.
        if (picks - 1) >= 0:
            # Pick up and deliver later.
            pairs += picks * check(picks - 1, deliv + 1)
        # Or deliver more than given.
        if (deliv - 1) >= 0:
            # Deliver now and pick up later.
            pairs += deliv * check(picks, deliv - 1)
        recur_cache[picks, deliv] = pairs
        return pairs

    return check(n, 0) % (10 ** 9 + 7)


# Time complexity: O(n ** 3) -> we're checking every pair of (picks, deliv) which is (n..0 * 0...n) => O(n * n) ->
# n - input value^^| -> and in the worst case, we will calculate factorial(n), checked this part and for any input_n,
#                       always calculating factorial() for all n values from n -> 1.
#                       So worst case should be O(n ** 3), and median Θ(n * n * log n).
# Auxiliary space: O(n * n) -> cache_dictionary to store all pairs and their results => O(n * n) ->
#                           -> stack of recursion at max == n, (picks - 1, deliv + 1) and we can't go negative => O(n).
# --------------------
# Hint:
# ! Use the permutation and combination theory to add one (P, D) pair each time until n pairs. !
# So it's some Math problem, and I don't know theory.
#   1) At any stage we can do P pickups and D deliveries.
#      Let's denote the stage as [P;D]
#   2) At first we can only do n pickups and no deliveries yet : [n,0]
#   3) At every next stage we can do a pickup thus [P,D] -> [P-1, D+1] or do a delivery:[P,D] -> [P, D-1]
#      (every new pickup leads to the number of deliveries increasing, and number of available pickups decreasing;
#      every delivery only leads to the number of pickups decreasing)
#   4) Now what?
#     4a. How many different pickups we can do at any stage? P
#     4b. How many different deliveries? D
#     4c. So (from 3, 4a and 4b) the ans([P,D]) = P * ans([P-1,D+1]) + D * ans([P, D-1])
#   5) Obvious corner cases:
#     5a. [1,0] = 1
#     5b. [0,n] = n! (we need to count every order of deliveries - all permutations of
#                     n numbers - well it is combinatorics, but this is unavoidable)
#   6) Memorizing ans[p,d] is an obvious step.
#     6a. You can do it bottom-up iteratively or top-down recursively
#     6b. Both ways it will be pretty slow
# --------------------
# Ok. Only questionable part is, why we do -> ! P * ans([P-1,D+1]) !?
# Assuming that we have 5 variants to Pickup from, then we will take (P-1) and we can take 5 options?
# Like P1??D1 -> P2 or P3 or P4 etc. so we need to multiply on all these options.
# We're taking all of them at once, same goes for Deliveries.
# Math solution:
# (2n!) / 2 ** n


test: int = 1
test_out: int = 1
assert test_out == count_orders(test)

test = 2
test_out = 6
assert test_out == count_orders(test)

test = 3
test_out = 90
assert test_out == count_orders(test)

test = 200
test_out = 880584563
assert test_out == count_orders(test)
