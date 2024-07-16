# Your friend is typing his name into a keyboard.
# Sometimes, when typing a character c,
#  the key might get long pressed, and the character will be typed 1 or more times.
# You examine the typed characters of the keyboard.
# Return True if it is possible that it was your friends name,
#  with some characters (possibly none) being long pressed.
# -----------------------
# 1 <= name.length, typed.length <= 1000
# name and typed consist of only lowercase English letters.


def is_long_pressed_name(name: str, typed: str) -> bool:
    # working_sol (99.49%, 78.91%) -> (22ms, 16.41mb)  time: O(n) | space: O(1)
    # We can't build `name` from fewer chars than it have.
    if len(typed) < len(name):
        return False
    point_name: int = 0
    point_typed: int = 0
    # We check every char from `name` to be used.
    while point_name < len(name):
        # We still have some chars in `name` not covered, and `typed` is already exhausted.
        # OR
        # We have different chars to start with == we can't use them.
        if point_typed >= len(typed) or name[point_name] != typed[point_typed]:
            return False
        prev_str: str = ''
        # We delete every char from `name`, but we still have something equal to this chars after.
        # Like 'aa' <- 'aaaaa', we're deleting 2 chars `aa` and still need to cover long-pressed ones.
        while point_name < len(name) and point_typed < len(typed) and name[point_name] == typed[point_typed]:
            prev_str = name[point_name]
            point_typed += 1
            point_name += 1
        # For this, we remember `prev_str` and delete everything until we meet different char.
        while point_typed < len(typed) and prev_str == typed[point_typed]:
            point_typed += 1
    # All chars are here and correct, but we still have extra chars in `typed`.
    # And we don't need any extras.
    if point_typed < len(typed):
        return False
    return True


# Time complexity: O(n) <- n - length of the input string `typed`.
# We only check cases when `typed` => `name`, and we are always using every index of it, once => O(n).
# -----------------------
# Auxiliary space: O(1)
# Only 2 constant INT's used, none of them depends on input => O(1).


test: str = "alex"
test_typed: str = "aaleex"
test_out: bool = True
assert test_out == is_long_pressed_name(test, test_typed)

test = "saeed"
test_typed = "ssaaedd"
test_out = False
assert test_out == is_long_pressed_name(test, test_typed)

test = "aab"
test_typed = "aaaaaaaaaaaa"
test_out = False
assert test_out == is_long_pressed_name(test, test_typed)

test = "leelee"
test_typed = "lleeelee"
test_out = True
assert test_out == is_long_pressed_name(test, test_typed)
