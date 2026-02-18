# You are given an array bulbs of integers between 1 and 100.
# There are 100 light bulbs numbered from 1 to 100. All of them
#  are switched off initially.
# For each element bulbs[i] in the array bulbs:
#  - If the bulbs[i]th light bulb is currently off, switch it on.
#  - Otherwise, switch it off.
# Return the list of integers denoting the light bulbs that are on in the end,
#  sorted in ascending order. If no bulb is on, return an empty list.
# --- --- --- ---
# 1 <= bulbs.length <= 100
# 1 <= bulbs[i] <= 100


def toggle_Light_bulbs(bulbs: list[int]) -> list[int]:
    # working_solution: (100%, 96.56%) -> (0ms, 19.28mb)  Time: O(n) Space: O(1)
    # Initially `off` == `negative`
    all_bulbs: list[int] = [-1 * _ for _ in range(101)]
    for bulb in bulbs:
        all_bulbs[bulb] *= -1
    
    out: list[int] = [bulb for bulb in all_bulbs if 0 < bulb]
    return out


# Time complexity: O(n)
# n - lengt of the input array `bulbs`
# --- --- --- ---
# Space complexity: O(1)


test: list[int] = [10, 30, 20, 10]
test_out: list[int] = [20, 30]
assert test_out == toggle_Light_bulbs(test)

test = [100, 100]
test_out = []
assert test_out == toggle_Light_bulbs(test)
