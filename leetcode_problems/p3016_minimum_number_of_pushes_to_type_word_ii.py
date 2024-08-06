# You are given a string word containing lowercase English letters.
# Telephone keypads have keys mapped with distinct collections of lowercase English letters,
#  which can be used to form words by pushing them.
# For example, the key 2 is mapped with ["a","b","c"],
#  we need to push the key one time to type "a", two times to type "b", and three times to type "c" .
# It is allowed to remap the keys numbered 2 to 9 to distinct collections of letters.
# The keys can be remapped to any amount of letters,
#  but each letter must be mapped to exactly one key.
# You need to find the minimum number of times the keys will be pushed to type the string word.
# Return the minimum number of pushes needed to type word after remapping the keys.
# An example mapping of letters to keys on a telephone keypad is given below.
# Note that 1, *, #, and 0 do not map to any letters.
# ------------------------
# 1 <= word.length <= 10 ** 5
# word consists of lowercase English letters.
from random import choice
from collections import Counter
from string import ascii_lowercase


def minimum_pushes(word: str) -> int:
    # working_sol (97.61%, 36.75%) -> (130ms, 17.65mb)  time: O(n * log n) | space: O(n)
    # { char: occurrences }
    char_occurs: dict[str, int] = Counter(word)
    # All buttons we can use.
    all_buttons: int = 8
    # Current cost to get a char we need.
    cur_press: int = 1
    used_buttons: int = 0
    out: int = 0
    # Essentially, all we need is to get most occurred chars and use them first.
    count: list[int] = sorted(char_occurs.values(), reverse=True)
    for occur in count:
        out += occur * cur_press
        used_buttons += 1
        # And because we can only use 8 buttons, we will get `cur_press` == cost
        #  increased by 1 for every new cycle.
        if all_buttons <= used_buttons:
            used_buttons = 0
            cur_press += 1
    return out


# Time complexity: O(n * log n) <- n - length of the input string `word`
# Always traversing whole `word` to get chars and their occurrences => O(n).
# In the worst case, every char is unique, and we're sorting whole `word` string => o(n + n * log n).
# Extra traversing all of these chars to count button presses => O(n + n + n * log n).
# ------------------------
# Auxiliary space: O(n)
# Same worst case.
# `char_occurs` <- will hold {STR:INT} for every char in `word` => O(n).
# `count` <- will hold every char from `word` => O(2 * n).


test: str = "abcde"
test_out: int = 5
assert test_out == minimum_pushes(test)

test = "xyzxyzxyzxyz"
test_out = 12
assert test_out == minimum_pushes(test)

test = "aabbccddeeffgghhiiiiii"
test_out = 24
assert test_out == minimum_pushes(test)

test = ''.join([choice(ascii_lowercase) for _ in range(10 ** 5)])
print(test)
