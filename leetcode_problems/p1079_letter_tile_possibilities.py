# You have n  tiles, where each tile has one letter tiles[i] printed on it.
# Return the number of possible non-empty sequences of letters you can make using
#  the letters printed on those tiles.
# ---------------------
# 1 <= tiles.length <= 7
# tiles consists of uppercase English letters.
from pyperclip import copy

from collections import Counter

from random import choice

from string import ascii_uppercase


def num_tile_possibilities(tiles: str) -> int:
    # working_sol (8.13%, 96.07%) -> (162ms, 17.70mb)  time: O(2 ** n) | space: O(n)
    chars: dict[str, int] = Counter(tiles)

    def check(avail_chars: dict[str, int]) -> int:
        combinations: int = 0

        for char in ascii_uppercase:
            if 0 == avail_chars[char]:
                continue
            combinations += 1
            # Use and try to build next.
            avail_chars[char] -= 1
            combinations += check(avail_chars)
            # Restore usage option and try to build from next char.
            avail_chars[char] += 1

        return combinations

    return check(chars)


# Time complexity: O(2 ** n) <- n - length of the input string `tiles`.
# Building all the possible combination starting from every char.
# For every char there's 2 options we use it or not => O(2 ** n).
# ---------------------
# Auxiliary space: O(n)
# In the worst case there's only unique chars in `tiles`.
# `chars` <- allocates space for each unique char from `tiles` => O(n).


test: str = "AAB"
test_out: int = 8
assert test_out == num_tile_possibilities(test)

test = "AAABBC"
test_out = 188
assert test_out == num_tile_possibilities(test)

test = "V"
test_out = 1
assert test_out == num_tile_possibilities(test)

test = ''.join([choice(ascii_uppercase) for _ in range(7)])
copy(test)
