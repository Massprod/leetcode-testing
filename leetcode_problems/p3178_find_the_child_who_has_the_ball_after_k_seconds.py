# You are given two positive integers n and k.
# There are n children numbered from 0 to n - 1 standing in a queue in order from left to right.
# Initially, child 0 holds a ball and the direction of passing the ball is towards the right direction.
# After each second, the child holding the ball passes it to the child next to them.
# Once the ball reaches either end of the line, i.e. child 0 or child n - 1, the direction of passing is reversed.
# Return the number of the child who receives the ball after k seconds.
# ------------------------------
# 2 <= n <= 50
# 1 <= k <= 50


def number_of_child(n: int, k: int) -> int:
    # working_sol (79.91%, 81.23%) -> (32ms, 16.41mb)  time: O(1) | space: O(1)
    # (n - 1) <- because first|last person insta passes it
    full_circles: int = k // (n - 1)
    moves_left: int = k % (n - 1)
    if full_circles % 2:
        return (n - 1) - moves_left
    return moves_left


# Time complexity: O(1).
# ------------------------------
# Auxiliary space: O(1).


test_n: int = 3
test_k: int = 5
test_out: int = 1
assert test_out == number_of_child(test_n, test_k)

test_n = 5
test_k = 6
test_out = 2
assert test_out == number_of_child(test_n, test_k)

test_n = 4
test_k = 2
test_out = 2
assert test_out == number_of_child(test_n, test_k)
