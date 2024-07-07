# There are n people standing in a line labeled from 1 to n.
# The first person in the line is holding a pillow initially.
# Every second, the person holding the pillow passes it to the next person standing in the line.
# Once the pillow reaches the end of the line, the direction changes,
#  and people continue passing the pillow in the opposite direction.
# For example, once the pillow reaches the nth person they pass it to the n - 1th person,
#  then to the n - 2th person and so on.
# Given the two positive integers n and time,
#  return the index of the person holding the pillow after time seconds.
# -------------------
# 2 <= n <= 1000
# 1 <= time <= 1000


def pass_the_pillow(n: int, time: int) -> int:
    # working_sol (91.13%, 77.09%) -> (28ms, 16.49mb)  time: O(1) | space: O(1)
    if time < n:
        return time + 1  # we start from 1-st person, + 1 for this.
    full_lines: int = time // (n - 1)  # we start from index == 1, so we already made a 1 move
    last_line: int = time % (n - 1)  # same, we start|end on first|last person, we don't use it.
    if full_lines % 2:
        return n - last_line
    return last_line + 1  # same, +1 for persons array being 1-indexed.


# Time complexity: O(1)
# Always same calculations and same value types => O(1)
# -------------------
# Auxiliary space: O(1)
# Only 2 constant INT's used, none of them depends on input => O(1).


test: int = 4
test_time: int = 5
test_out: int = 2
assert test_out == pass_the_pillow(test, test_time)

test = 3
test_time = 2
test_out = 3
assert test_out == pass_the_pillow(test, test_time)

test = 4
test_time = 9
test_out = 4
assert test_out == pass_the_pillow(test, test_time)

test = 18
test_time = 38
test_out = 5
assert test_out == pass_the_pillow(test, test_time)
