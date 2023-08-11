# You are given the customer visit log of a shop represented by
#   a 0-indexed string customers consisting only of characters 'N' and 'Y':
#     if the ith character is 'Y', it means that customers come at the ith hour
#     whereas 'N' indicates that no customers come at the ith hour.
# If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated as follows:
#   For every hour when the shop is open and no customers come, the penalty increases by 1.
#   For every hour when the shop is closed and customers come, the penalty increases by 1.
# Return the earliest hour at which the shop must be closed to incur a minimum penalty.
# Note that if a shop closes at the jth hour, it means the shop is closed at the hour j.
# ----------------------
# 1 <= customers.length <= 10 ** 5
# customers consists only of characters 'Y' and 'N'.
from random import choice


def best_closing_time(customers: str) -> int:
    # working_sol (66.79%, 93.93%) -> (148ms, 17.22mb)  time: O(n) | space: O(1)
    # [0] <- doesn't have prefix.
    prefix: int = 0
    suffix: int = 0
    # But having all count('Y') as suffix.
    for _ in customers:
        if _ == 'Y':
            suffix += 1
    # Basic closing time == 0,
    best_time: int = 0
    # and basic penalty is suffix of whole array.
    penalty: int = suffix
    # Starting from [1], so we need to consider [0] before.
    # Even if we start from [0] we need some unique check,
    # because [0] never uses prefix.
    # So even if range(0, len(customers), we can't check customers[x] == 'N',
    # because it always should be skipped, better to start from [1] and deal with [0] before.
    # Same goes for closing after last_index.
    if customers[0] == 'N':
        prefix += 1
    else:
        suffix -= 1
    for x in range(1, len(customers)):
        # ! At any index, the penalty is the sum of
        #   prefix count of ‘N’ and suffix count of ‘Y’.!
        cur_penalty: int = suffix + prefix
        # Going from left to right, so it's always minimum index chosen.
        # Only penalties matter.
        if cur_penalty < penalty:
            penalty = cur_penalty
            best_time = x
        if customers[x] == 'N':
            prefix += 1
        if customers[x] == 'Y':
            suffix -= 1
    # If we're closing after last_index, suffix doesn't matter.
    # But all prefix is a penalty.
    if prefix < penalty:
        best_time = len(customers)
    return best_time


# Time complexity: O(n) -> traversing whole input_string once, to count suffix for whole string => O(n) ->
# n - len of input_string^^| -> extra traverse of whole input_string to get all penalties => O(n).
# Auxiliary space: O(1) -> only 5 constant INTs used, none of them depends on input => O(1).
# ----------------------
# HINT -> ! At any index, the penalty is the sum of prefix count of ‘N’ and suffix count of ‘Y’.!
# New kind of problems for me with sum_prefix. So HINTs is good.


test: str = "YYNY"
test_out: int = 2
assert test_out == best_closing_time(test)

test = "NNNNN"
test_out = 0
assert test_out == best_closing_time(test)

test = "YYYY"
test_out = 4
assert test_out == best_closing_time(test)

test = ""
for _ in range(10 ** 5):
    test += choice(['N', 'Y'])
# print(test)
