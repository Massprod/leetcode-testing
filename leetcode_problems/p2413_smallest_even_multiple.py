# Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.
# ----------------
# 1 <= n <= 150


def smallest_even_multiple(n: int) -> int:
    # working_sol (79.89%, 98.14%) -> (34ms, 16mb)  time: O(1) | space: O(1)
    # (even % 2) == 0 => multiple of 2 by itself.
    # And we can get even with: (even * 1)
    # (odd % 2) != 0 -> the closest number in this case:
    # (odd * 2) % 2 == 0.
    if n % 2 == 0:
        return n
    return n * 2

# Time complexity: O(1) -> no matter the input only 2 actions, either multiply by 2 or just return => O(1).
# Auxiliary space: O(1) -> nothing extra used.
# ----------------
# Every even number => even % 2 == 0. So it's multiple of 2 by itself, and we can get this by even * 1.
# Insta return any even, and for odd we can just =>  odd * 2, and it's closest we can get.
# Cuz (odd * 1) % 2 != 0, and closest number we can get is (odd * 2) % 2 == 0.


test: int = 5
test_out: int = 10
assert test_out == smallest_even_multiple(test)

test = 6
test_out = 6
assert test_out == smallest_even_multiple(test)

test = 133
test_out = 266
assert test_out == smallest_even_multiple(test)
