# You would like to make dessert and are preparing to buy the ingredients.
# You have n ice cream base flavors and m types of toppings to choose from.
# You must follow these rules when making your dessert:
#   - There must be exactly one ice cream base.
#   - You can add one or more types of topping or have no toppings at all.
#   - There are at most two of each type of topping.
# You are given three inputs:
#  - baseCosts, an integer array of length n, where each baseCosts[i]
#     represents the price of the ith ice cream base flavor.
#  - toppingCosts, an integer array of length m, where each toppingCosts[i] is the price of one of the ith topping.
#  - target, an integer representing your target price for dessert.
# You want to make a dessert with a total cost as close to target as possible.
# Return the closest possible cost of the dessert to target.
# If there are multiple, return the lower one.
# --------------------
# n == baseCosts.length
# m == toppingCosts.length
# 1 <= n, m <= 10
# 1 <= baseCosts[i], toppingCosts[i] <= 10 ** 4
# 1 <= target <= 10 ** 4
from random import randint


def closest_cost(baseCosts: list[int], toppingCosts: list[int], target: int) -> int:
    # working_sol (99.65%, 52.11%) -> (40ms, 17mb)  time: O(m * n) | space: O(m * n)
    cur_closest: list[int] = [0]
    cur_distance: list[int | float] = [float('inf')]
    recur_cache: dict[tuple[int, int]: int] = {}

    def check(index: int, cur_cost: int) -> bool | None:
        # Standard caching.
        if (index, cur_cost) in recur_cache:
            return False
        # If we found a target, we don't care about anything else.
        if cur_cost == target:
            cur_closest[0] = cur_cost
            return True
        # Otherwise, we need closest.
        # So we calc distance from cost to our target for every option.
        distance: int = abs(target - cur_cost)
        # If we find something lower, we need to use it.
        if distance < cur_distance[0]:
            cur_distance[0] = distance
            cur_closest[0] = cur_cost
        # If we find something equal on distance, we need lowest ->
        # -> ! If there are multiple, return the lower one !
        if distance == cur_distance[0]:
            cur_closest[0] = min(cur_cost, cur_closest[0])
        # And there's no reason to keep searching after we calculate,
        #  first distance which was Higher than Target.
        # Because everything else will only make it Higher ->
        # ! 1 <= baseCosts[i], toppingCosts[i] <= 10 ** 4 !
        if cur_cost > target:
            return False
        for x in range(index, len(toppingCosts)):
            # Checking every option.
            use_top: int = toppingCosts[x]
            # ! add one or more types of topping
            #   or have no toppings at all !
            if check(x + 1, cur_cost + use_top):
                return True
            if check(x + 1, cur_cost):
                return True
            # ! at most two of each type of topping !
            if check(x + 1, cur_cost + use_top * 2):
                return True
        recur_cache[index, cur_cost] = False
    # Check every base.
    for base in baseCosts:
        if check(0, base):
            break
    return cur_closest[0]


# Time complexity: O(m * n) -> for every index in bases we're checking every index in topps, but x3 times for index,
# m - len of bases_array^^| can we say => O(m * 3n)? Like for every index in bases there will be a calls with pairs:
# n - len of topps_array^^| (topp_index, cur_cost) (topp_index, cur_cost + top_cost) (topp_index, cur_cost + 2*top_cost)
#                           Again caching can eliminate some of them, but still should be correct to say O(m * n).
# Auxiliary space: O(m * n) -> every call is stored => O(m * n) -> everything else is totally dominated by it.
# --------------------
# Ok. Brute force is working 8004ms. Caching helps -> 763ms. What else can be done?
# Stop searching when we already met something higher?
# Like I don't need higher values and calc of distance will be already done.
# 8004 -> 40ms. Simple cache for top_down + culling when cost is higher is enough.
# Expected something tricky, but task is just do what u told with some recursion optimisation.


test_base: list[int] = [1, 7]
test_costs: list[int] = [3, 4]
test_target: int = 10
test_out: int = 10
assert test_out == closest_cost(test_base, test_costs, test_target)

test_base = [2, 3]
test_costs = [4, 5, 100]
test_target = 18
test_out = 17
assert test_out == closest_cost(test_base, test_costs, test_target)

test_base = [3, 10]
test_costs = [2, 5]
test_target = 9
test_out = 8
assert test_out == closest_cost(test_base, test_costs, test_target)

test_base = []
test_costs = []
for _ in range(10):
    test_base.append(randint(1, 10 ** 4))
    test_costs.append(randint(1, 10 ** 4))
test_target = randint(1, 10 ** 4)
print(test_base)
print(test_costs)
print(test_target)
