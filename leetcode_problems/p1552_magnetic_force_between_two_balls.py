# In the universe Earth C-137, Rick discovered a special form of magnetic force
#  between two balls if they are put in his new invented basket. Rick has n empty baskets,
#  the ith basket is at position[i], Morty has m balls and needs to distribute the balls
#  into the baskets such that the minimum magnetic force between any two balls is maximum.
# Rick stated that magnetic force between two different balls at positions x and y is |x - y|.
# Given the integer array position and the integer m.
# Return the required force.
# -------------------------------
# n == position.length
# 2 <= n <= 10 ** 5
# 1 <= position[i] <= 10 ** 9
# All integers in position are distinct.
# 2 <= m <= position.length
from random import randint


def max_distance(position: list[int], m: int) -> int:
    # working_sol (92.31%, 37.04%) -> (671ms, 30.38mb)  time: O(n * log k) | space: O(n)

    def place_balls(force: int) -> bool:
        # Always start with first position == already placed 1'st ball.
        placed_balls: int = 1
        prev_place: int = position[0]
        for index in range(1, len(position)):
            cur_place: int = position[index]
            if force <= (cur_place - prev_place):
                placed_balls += 1
                prev_place = cur_place
            if m == placed_balls:
                return True
        return False

    position.sort()
    min_force: int = 1
    # `maxForce` we can have is a distance between maximum_position and minimum.
    # But only for 2 balls, and we need `m` => floor by `m - 1`.
    max_force: int = position[-1] // (m - 1)
    out: int = 1
    while min_force <= max_force:
        cur_force: int = (min_force + max_force) // 2
        # We can place them, correctly. But we need `maximum` of lowest options.
        # So, we can try to increase `curForce`.
        if place_balls(cur_force):
            out = max(cur_force, out)
            min_force = cur_force + 1  # cuz, we're using `min <= max` we can't just take `left_l`
        # Otherwise => we need smaller distance.
        else:
            max_force = cur_force - 1
    return out


# Time complexity: O(n * log k) <- n - length of the input array `position`,
#                                  m - input value,
#                                  k == (max(position) // (m - 1)) == floor(max(position) / (m - 1)).
# We're always using BS in range (1 -> k) => O(log k).
# And for every BS check, we're traversing a whole input array `n`
#  to see if we can place balls correctly => O(n * log k).
# -------------------------------
# Auxiliary space: O(n)
# Standard `sort` takes O(n), and everything else is constant INT's which doesnt depends on input.


test: list[int] = [1, 2, 3, 4, 7]
test_m: int = 3
test_out: int = 3
assert test_out == max_distance(test, test_m)

test = [5, 4, 3, 2, 1, 1000000000]
test_m = 2
test_out = 999999999
assert test_out == max_distance(test, test_m)

test = list(set([randint(1, 10 ** 9) for _ in range(10 ** 3)]))
test_m = randint(2, len(test))
print(test)
print(test_m)
