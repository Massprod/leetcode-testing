# There is a special typewriter with lowercase English letters 'a' to 'z' arranged in a circle with a pointer.
# A character can only be typed if the pointer is pointing to that character.
# The pointer is initially pointing to the character 'a'.
# Each second, you may perform one of the following operations:
#  - Move the pointer one character counterclockwise or clockwise.
#  - Type the character the pointer is currently on.
# Given a string word, return the minimum number of seconds to type out the characters in word.
# -------------------------
# 1 <= word.length <= 100
# word consists of lowercase English letters.


def min_time_to_type(word: str) -> int:
    # working_sol (82.18%, 29.81%) -> (32ms, 16.56mb)  time: O(n) | space: O(1)
    out: int = 0
    cur_char: str = 'a'
    for next_char in word:
        ord_cur: int = ord(cur_char)
        ord_next: int = ord(next_char)
        if ord_cur == ord_next:
            out += 1
            continue
        counter_clock_distance: int = abs(ord_cur - ord_next) % 26
        clock_distance: int = 26 - counter_clock_distance
        cur_char = next_char
        out += min(clock_distance, counter_clock_distance) + 1
    return out


# Time complexity: O(n) <- n - length of the input string `word`.
# Always traversing `word`, once => O(n).
# -------------------------
# Auxiliary space: O(1)
# Nothing depending on input is used => O(1).


test: str = "abc"
test_out: int = 5
assert test_out == min_time_to_type(test)

test = "bza"
test_out = 7
assert test_out == min_time_to_type(test)

test = "zjpc"
test_out = 34
assert test_out == min_time_to_type(test)
