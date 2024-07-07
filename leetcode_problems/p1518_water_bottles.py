# There are numBottles water bottles that are initially full of water.
# You can exchange numExchange empty water bottles from the market with one full water bottle.
# The operation of drinking a full water bottle turns it into an empty bottle.
# Given the two integers numBottles and numExchange,
#  return the maximum number of water bottles you can drink.
# -------------------------
# 1 <= numBottles <= 100
# 2 <= numExchange <= 100


def num_water_bottles(num_bottles: int, num_exchange: int) -> int:
    # working_sol (52.78%, 79.17%) -> (35ms, 16.50mb)  time: O(n) | space: O(1)
    out: int = 0
    while num_bottles >= num_exchange:
        # Bottle we can drink, but we won't be able to exchange them.
        # But they are still here, and we should consider them in exchange operation.
        cant_be_exchanged: int = num_bottles % num_exchange
        # We ignore them, because it's easier to add them later :)
        out += num_bottles - cant_be_exchanged
        # New bottles + previously left buttons, after exchange operation.
        num_bottles = cant_be_exchanged + (num_bottles // num_exchange)
    out += num_bottles
    return out


# Time complexity: O(n) <- n - input value `num_bottles`.
# Always depleting `num_bottles` until it's lower than `num_exchange` => O(n).
# -------------------------
# Auxiliary space: O(1)
# Only 2 constant INT's used, none of them depends on input => O(1)


test_bottles: int = 9
test_exchange: int = 3
test_out: int = 13
assert test_out == num_water_bottles(test_bottles, test_exchange)

test_bottles = 15
test_exchange = 4
test_out = 19
assert test_out == num_water_bottles(test_bottles, test_exchange)
