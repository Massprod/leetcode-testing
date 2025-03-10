# You are given two arrays of integers, fruits and baskets, each of length n,
#  where fruits[i] represents the quantity of the ith type of fruit,
#  and baskets[j] represents the capacity of the jth basket.
# From left to right, place the fruits according to these rules:
#  - Each fruit type must be placed in the leftmost available basket with
#    a capacity greater than or equal to the quantity of that fruit type.
#  - Each basket can hold only one type of fruit.
#  - If a fruit type cannot be placed in any basket, it remains unplaced.
# Return the number of fruit types that remain unplaced
#  after all possible allocations are made.
# ------------------------
# n == fruits.length == baskets.length
# 1 <= n <= 100
# 1 <= fruits[i], baskets[i] <= 1000


def num_of_unplaced_fruits(fruits: list[int], baskets: list[int]) -> int:
    # working_sol (100.00%, 100.00%) -> (25ms, 18.03mb)  time: O(n ** 2) | space: O(1)
    # There's some BS vodoo, but I don't see it.
    # And there's no reason to bother for an easy...
    out: int = 0
    for fruit_ind in range(len(fruits)):
        fruit_type: int = fruits[fruit_ind]
        for basket_ind in range(len(baskets)):
            basket_size: int = baskets[basket_ind]
            if basket_size >= fruit_type:
                baskets[basket_ind], fruits[fruit_ind] = 0, 0
                break
        if 0 != fruits[fruit_ind]:
            out += 1
    
    return out


# Time complexity: O(n * n) <- n - length of the input arrays `fruits`, `baskets`
# Standard double loop check... => O(n ** 2).
# ------------------------
# Auxiliary space: O(1)


test: list[int] = [4, 2, 5]
test_baskets: list[int] = [3, 5, 4]
test_out: int = 1
assert test_out == num_of_unplaced_fruits(test, test_baskets)

test = [3, 6, 1]
test_baskets = [6, 4, 7]
test_out = 0
assert test_out == num_of_unplaced_fruits(test, test_baskets)
