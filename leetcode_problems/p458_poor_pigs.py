# There are buckets buckets of liquid, where exactly one of the buckets is poisonous.
# To figure out which one is poisonous, you feed some number of (poor) pigs the liquid
#  to see whether they will die or not.
# Unfortunately, you only have minutesToTest minutes to determine which bucket is poisonous.
# You can feed the pigs according to these steps:
#   1. Choose some live pigs to feed.
#   2. For each pig, choose which buckets to feed it.
#    The pig will consume all the chosen buckets simultaneously and will take no time.
#    Each pig can feed from any number of buckets, and each bucket can be fed from by any number of pigs.
#   3. Wait for minutesToDie minutes. You may not feed any other pigs during this time.
#   4. After minutesToDie minutes have passed, any pigs that have been fed the poisonous bucket will die,
#    and all others will survive.
#   5. Repeat this process until you run out of time.
# Given buckets, minutesToDie, and minutesToTest,
#  return the minimum number of pigs needed to figure out which bucket is poisonous within the allotted time.
# --------------------------
# 1 <= buckets <= 1000
# 1 <= minutesToDie <= minutesToTest <= 100


def poor_pigs(buckets: int, minutesToDie: int, minutesToTest: int) -> int:
    # working_sol (75.20%, 74.40%) -> (34ms, 16.1mb)  time: O(n + k + m) | space: O(1)
    # ! Find minimum x such that (T+1)^x >= N !
    # T -> # of tests we can perform in total.
    # x -> # of pigs.
    # N -> # of buckets.
    tests: int = minutesToTest // minutesToDie
    pigs: int = 0
    while (tests + 1) ** pigs < buckets:
        pigs += 1
    return pigs


# Time complexity: O(n + k + m) -> all tests we can perform depends on inputs: 'minutesToDie', 'minutesToTest' ->
# m - input value 'minutesToTest'^^| -> essentially everything depends on all 3 inputs => O(n + k + m).
# k - input value 'minutesToDie'^^|
# n - input value 'buckets'^^|
# Auxiliary space: O(1) -> only 2 constant INTs used, none of them depends on input => O(1).
# --------------------------
# Main idea:
# buckets:
# 1 2 3 4 5 6 7 8
#                 Tests == 1.
# - - - -         pig1
# - -     - -     pig2
# -   -   -   -   pig3
# pig1 will test 1 - 4
# pig2 will test 1 - 2, 5 - 6
# pig3 will test 1, 3, 5, 7
# If pig1 dies then it's something in 1 - 4.
# Because pig2 will cover 1 - 2, if it dies then pig 3 as well, and it's 1 bucket.
# If only pig1 dies => bucket == 4.
# So, we need to cover everything with minimum number of pigs.
# Formula for that:
# (T+1)^x >= N
# T -> # of tests we can perform in total == all_time // time_to_die.
# x -> # of pigs.
# N -> # of buckets.
# We need to find 'x' and it's minimum value it's FIRST TIME we will have (T + 1) ** x >= N.
# And we can find it in reverse with simple ! while (T + 1) ** x < N !.


test: int = 4
test_to_die: int = 15
test_to_test: int = 15
test_out: int = 2
assert test_out == poor_pigs(test, test_to_die, test_to_test)

test = 4
test_to_die = 15
test_to_test = 30
test_out = 2
assert test_out == poor_pigs(test, test_to_die, test_to_test)

test = 1000
test_to_die = 15
test_to_test = 100
test_out = 4
assert test_out == poor_pigs(test, test_to_die, test_to_test)
