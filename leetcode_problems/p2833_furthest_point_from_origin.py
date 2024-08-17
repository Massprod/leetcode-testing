# You are given a string moves of length n consisting only of characters 'L', 'R', and '_'.
# The string represents your movement on a number line starting from the origin 0.
# In the ith move, you can choose one of the following directions:
#  - move to the left if moves[i] = 'L' or moves[i] = '_'
#  - move to the right if moves[i] = 'R' or moves[i] = '_'
# Return the distance from the origin of the furthest point you can get to after n moves.
# --------------------------
# 1 <= moves.length == n <= 50
# moves consists only of characters 'L', 'R' and '_'.
from collections import Counter
from random import choice


def furthest_distance_from_origin(moves: str) -> int:
    # working_sol (68.58%, 71.53%) -> (35ms, 16.45mb)  time: O(n) | space: O(n)
    # W.e the path we travel, we still will either end in the middle
    #  or some left|right shifted position.
    # And the best tactic to move furthest, is to continue traveling
    #  in the same direction we shifted.
    all_moves: dict[str, int] = Counter(moves)
    start_pos: int = abs(all_moves['R'] - all_moves['L'])
    end_pos: int = start_pos + all_moves['_']
    return end_pos


# Time complexity: O(n) <- n - length of the input string `moves`.
# Always traversing whole `moves`, once => O(n).
# --------------------------
# Auxiliary space: O(n)
# In the worst case there's only 3 chars = ['R', 'L', '_'].
# So, every char from `moves` is stored in `all_moves` => O(n).


test: str = "L_RL__R"
test_out: int = 3
assert test_out == furthest_distance_from_origin(test)

test = "_R__LL_"
test_out = 5
assert test_out == furthest_distance_from_origin(test)

test = "_______"
test_out = 7
assert test_out == furthest_distance_from_origin(test)

test = ''.join([choice(['R', 'L', '_']) for _ in range(50)])
print(test)
