# You are given two integers numBottles and numExchange.
# numBottles represents the number of full water bottles that you initially have.
# In one operation, you can perform one of the following operations:
#  - Drink any number of full water bottles turning them into empty bottles.
#  - Exchange numExchange empty bottles with one full water bottle.
#    Then, increase numExchange by one.
# Note that you cannot exchange multiple batches of empty bottles
#  for the same value of numExchange. For example, if numBottles == 3
#  and numExchange == 1, you cannot exchange 3 empty water bottles for 3 full bottles.
# Return the maximum number of water bottles you can drink.
# --- --- --- ---
# 1 <= numBottles <= 100 
# 1 <= numExchange <= 100


def max_bottles_drunk(numBottles: int, numExchange: int) -> int:
    # working_solution: (59.44%, 90.00%) -> (39ms, 17.60mb)  Time: O(n) Space: O(1)
    out: int = numBottles
    empty: int = numBottles
    while empty >= numExchange:
        out += 1
        empty += 1
        empty = empty - numExchange
        numExchange += 1
    
    return out


# Time complexity: O(n) <- n - `numBottles`.
# --- --- --- ---
# Space complexity: O(1)


test_bottles: int = 13
test_exchange: int = 6
test_out: int = 15
assert test_out == max_bottles_drunk(test_bottles, test_exchange)

test_bottles = 10
test_exchange = 3
test_out = 13
assert test_out == max_bottles_drunk(test_bottles, test_exchange)
