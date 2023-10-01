# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
#   - Starting with any positive integer, replace the number by the sum of the squares of its digits.
#   - Repeat the process until the number equals 1 (where it will stay),
#        or it loops endlessly in a cycle which does not include 1.
#   - Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.
# -----------------------
# 1 <= n <= 2 ** 31 - 1


def is_happy(n: int) -> bool:
    # working_sol (70.84%, 85.31%) -> (40ms, 16.1mb)  time: O(n) | space: O(n)
    while True:
        check: str = str(n)
        n = 0
        # Replace 'n' with summ of the squares.
        for value in check:
            n += int(value) ** 2
        # There's 2 unique cases when it's not a loop.
        if n == 1 or n == 7:
            return True
        # Always ends in a loop.
        elif 1 < n < 10:
            return False


# Time complexity: O(n) -> no idea how to calculate all combinations we will get until hit limits,
# n - input value 'n'^^|   but obviously if our n is getting higher than we're checking more and more options ->
#                          -> like, for n == 1 it's insta return, but for n == 8 it's 5+ checks etc. ->
#                          -> leaving this as O(n), because it's not growing exponentially for sure ->
#                          -> we can tell that based on runtime with maximum_constraint(2 ** 31 - 1) and 1
#                          almost the same runtime.
# Auxiliary space: O(n) -> extra string with all digits, depends on input 'n' => O(n).
# -----------------------
# Lmao, this task is actually about checking if there's cycle or not with Floyd method.
# No wonder I didn't understand why there's extra 7 to check :) But my intuitively made solution still works.
# Won't be rebuilding this, because mine is still working correctly. Calling it a lucky guess on breaks.
# -----------------------
# Maybe there's some way to use digital_root? But it's summ of all digits how we can get them one by one and power()?
# -----------------------
# It was expected to other than 1 and 10 fail with loop, but this extra 7 is not obvious at all.
# Unique case which can't be seen without failing or extra math_info on that, I made it with brute_forcing,
# without research, so I guess there's some other methods explaining it.
# -----------------------
# Hmm. all except 7 is correct for my solution, but only 7 is unique in case of less than 10.
# I was thinking every value except 1 will be endless loop but here's extra 7, maybe something more but other's is
# ending in a loop. Guess I will just check for 1 and 7, and find extra info on that after.
# -----------------------
# Guess there's TLE for standard manipulations with power(), so either I insta look for extra info
# or fail TimeLimit first. Prefer to fail first, maybe im wrong. But don't see any bit_methods I know.


test: int = 19
test_out: bool = True
assert test_out == is_happy(test)

test = 2
test_out = False
assert test_out == is_happy(test)

test = 2 ** 31 - 1
test_out = False
assert test_out == is_happy(test)

test = 1111111
test_out = True
assert test_out == is_happy(test)
