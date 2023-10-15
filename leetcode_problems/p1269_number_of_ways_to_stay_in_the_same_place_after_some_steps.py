# You have a pointer at index 0 in an array of size arrLen.
# At each step, you can move 1 position to the left, 1 position to the right in the array,
#  or stay in the same place (The pointer should not be placed outside the array at any time).
# Given two integers steps and arrLen, return the number of ways such that your pointer is still at index 0
#  after exactly steps steps.
# Since the answer may be too large, return it modulo 10 ** 9 + 7.
# --------------------
# 1 <= steps <= 500
# 1 <= arrLen <= 10 ** 6


def num_ways(steps: int, arrLen: int) -> int:
    # working_sol (25.55%, 8.89%) -> (543ms, 122.5mb)  time: O(n * min(n, m)) | space: O(n * min(n, m))
    recur_cache: dict[tuple[int, int], int] = {}

    def check(index: int, steps_left: int) -> int:
        if not (0 <= index < arrLen):
            return 0
        if (index, steps_left) in recur_cache:
            return recur_cache[index, steps_left]
        # ! pointer is still at index 0 after exactly ## steps !
        if steps_left == 0:
            if index == 0:
                return 1
            return 0
        ways: int = 0
        ways += check(index, steps_left - 1)  # stay in place
        ways += check(index + 1, steps_left - 1)  # move right
        ways += check(index - 1, steps_left - 1)  # move left
        recur_cache[index, steps_left] = ways
        return ways

    return check(0, steps) % (10 ** 9 + 7)


# Time complexity: O(n * min(n, m)) -> limited on (index, steps_left) calls, like: if we have less steps than arrLen
# n - input value 'steps'^^|  then we will only get (n * n) states, and (n * m) otherwise ->
# m - input value 'arrLen'^^| -> because indexes are limited from (0 -> (arrLen - 1)) => O(n * min(n, m)).
# Auxiliary space: O(n * min(n, m)) -> using dictionary as cache and store every call state => O(n * min(n, m)).
# --------------------
# ! 1 <= steps <= 500 ! Low constraints and tag DP.
# So it should be at least Top-down recursion.
# We only care about steps, and we can have 3 options:
# stay == 1 step
# move_left == 1 step
# move_right == 1 step.
# Just 3 options with limiting index in range of 0 -> (arrLen - 1).
# Let's try.


test: int = 3
test_len: int = 2
test_out: int = 4
assert test_out == num_ways(test, test_len)

test = 2
test_len = 4
test_out = 2
assert test_out == num_ways(test, test_len)

test = 4
test_len = 2
test_out = 8
assert test_out == num_ways(test, test_len)

test = 500
test_len = 1000000
test_out = 374847123
assert test_out == num_ways(test, test_len)
