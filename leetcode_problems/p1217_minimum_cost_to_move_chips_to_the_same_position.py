# We have n chips, where the position of the ith chip is position[i].
# We need to move all the chips to the same position.
# In one step, we can change the position of the ith chip from position[i] to:
#  - position[i] + 2 or position[i] - 2 with cost = 0.
#  - position[i] + 1 or position[i] - 1 with cost = 1.
# Return the minimum cost needed to move all the chips to the same position.
# -----------------------
# 1 <= position.length <= 100
# 1 <= position[i] <= 10 ** 9
from random import randint


def min_cost_to_move_chips(position: list[int]) -> int:
    # working_sol (85.95%, 83.86%) -> (32ms, 16.44mb)  time: O(n) | space: O(1)
    # Essentially steps with == 2 is free
    # And only steps with == 1 costs something.
    # So, we can take any value and make w.e steps we want by 2.
    # If it's `even` it's going to become 0, or w.e the value we want.
    # If it's `odd` it's going to become +-1 value of `even` values we end on.
    # And because we need `minimum` cost we need to make less changes.
    # In our case changes are going to be a switch from even to odd.
    # So, every `odd` will be switched to `even` and in reverse.
    # Less values == less cost.
    even_vals: int = 0
    odd_vals: int = 0
    for val in position:
        if val % 2:
            odd_vals += 1
        else:
            even_vals += 1
    return min(even_vals, odd_vals)


# Time complexity: O(n) <- n - length of the input array `position`.
# Always traversing `position`, once => O(n).
# -----------------------
# Auxiliary space: O(1)
# Only 2 constant INT's used, none of them depends on input => O(1).


test: list[int] = [1, 2, 3]
test_out: int = 1
assert test_out == min_cost_to_move_chips(test)

test = [2, 2, 2, 3, 3]
test_out = 2
assert test_out == min_cost_to_move_chips(test)

test = [1, 1000000000]
test_out = 1
assert test_out == min_cost_to_move_chips(test)

test = [randint(1, 10 ** 9) for _ in range(100)]
print(test)
