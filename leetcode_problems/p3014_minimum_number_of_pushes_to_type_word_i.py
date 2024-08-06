# You are given a string word containing distinct lowercase English letters.
# Telephone keypads have keys mapped with distinct collections of lowercase English letters,
#  which can be used to form words by pushing them.
# For example, the key 2 is mapped with ["a","b","c"],
#  we need to push the key one time to type "a",
#  two times to type "b", and three times to type "c" .
# It is allowed to remap the keys numbered 2 to 9 to distinct collections of letters.
# The keys can be remapped to any amount of letters,
#  but each letter must be mapped to exactly one key.
# You need to find the minimum number of times the keys will be pushed to type the string word.
# Return the minimum number of pushes needed to type word after remapping the keys.
# An example mapping of letters to keys on a telephone keypad is given below.
# Note that 1, *, #, and 0 do not map to any letters.
# --------------------------
# 1 <= word.length <= 26
# word consists of lowercase English letters.
# All letters in word are distinct.


def minimum_pushes(word: str) -> int:
    # working_sol (69.18%, 63.99%) -> (34ms, 16.47mb)  time: O(n) | space: O(1)
    # Allowed buttons to use.
    all_buttons: int = 8
    all_chars: int = len(word)
    cur_press: int = 1
    out: int = 0
    while 0 < all_chars:
        if all_buttons <= all_chars:
            all_chars -= all_buttons
        else:
            out += all_chars * cur_press
            break
        out += all_buttons * cur_press
        cur_press += 1
    return out


# Time complexity: O(n) <- n - length of the input string `word`.
# Always using all chars from `word` => O(n).
# --------------------------
# Auxiliary space: O(1)
# Only 4 constant INTs used, none of them depends on input => O(1).


test: str = "abcde"
test_out: int = 5
assert test_out == minimum_pushes(test)

test = "xycdefghij"
test_out = 12
assert test_out == minimum_pushes(test)
