# You are given a string s. Simulate events at each second i:
#  - If s[i] == 'E', a person enters the waiting room and takes one of the chairs in it.
#  - If s[i] == 'L', a person leaves the waiting room, freeing up a chair.
# Return the minimum number of chairs needed so that a chair is available for every person who
#  enters the waiting room given that it is initially empty.
# -------------------------
# 1 <= s.length <= 50
# s consists only of the letters 'E' and 'L'.
# s represents a valid sequence of entries and exits.


def minimum_chairs(s: str) -> int:
    # working_sol (95.53%, 65.43%) -> (28ms, 16.46mb)  time: O(s) | space: O(1)
    all_chairs: int = 0
    empty_chairs: int = 0
    # Every 'E' takes a chair if there's not enough empty chairs
    #  we need to have it from the beginning.
    # Every 'L' only frees a chair from use and returns it in a pool.
    for char in s:
        if 'E' == char:
            if empty_chairs:
                empty_chairs -= 1
            else:
                all_chairs += 1
        else:
            empty_chairs += 1
    return all_chairs


# Time complexity: O(s)
# Always using every char from input string `s`, once => O(s).
# -------------------------
# Auxiliary space: O(1)
# Only two constant INTs used, none of them depends on input => O(1).


test: str = "ELEELEELLL"
test_out: int = 3
assert test_out == minimum_chairs(test)

test = "ELELEEL"
test_out = 2
assert test_out == minimum_chairs(test)

test = "EEEEEEE"
test_out = 7
assert test_out == minimum_chairs(test)
