# You have a water dispenser that can dispense cold, warm, and hot water. Every second,
#  you can either fill up 2 cups with different types of water, or 1 cup of any type of water.
# You are given a 0-indexed integer array amount of length 3 where amount[0], amount[1],
#  and amount[2] denote the number of cold, warm, and hot water cups you need to fill respectively.
# Return the minimum number of seconds needed to fill up all the cups.
# ------------------------
# amount.length == 3
# 0 <= amount[i] <= 100


def fill_cups(amount: list[int]) -> int:
    # working_sol (97.39%, 35.83%) -> (27ms, 16.56mb)  time: O(1) | space: O(1)
    amount.sort()
    max_water: int = amount[-1]
    total_water: int = sum(amount)
    # If we use `max_water`, we will take this either one by one.
    # Or we're going to use other temperatures, but still need to cover what's left.
    # And we can combine all the water types: cold | warm | hot.
    # Otherwise, we need to take all water by 2 cups at a time.
    return max(
        max_water, (total_water + 1) // 2
    )


# Time complexity: O(1).
# We got constant sized input, we can call sort() and `sum` constant => O(1).
# ------------------------
# Auxiliary space: O(1)


test: list[int] = [1, 4, 2]
test_out: int = 4
assert test_out == fill_cups(test)

test = [5, 4, 4]
test_out = 7
assert test_out == fill_cups(test)

test = [5, 0, 0]
test_out = 5
assert test_out == fill_cups(test)
