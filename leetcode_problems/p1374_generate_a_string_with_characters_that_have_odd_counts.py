# Given an integer n, return a string with n characters
#  such that each character in such string occurs an odd number of times.
# The returned string must contain only lowercase English letters.
# If there are multiples valid strings, return any of them.
# --------------------
# 1 <= n <= 500


def generate_the_string(n: int) -> str:
    # working_sol (64.23%, 31.75%) -> (34ms, 16.55mb)  time: O(n) | space: O(n)
    # We don't care about anything, except using odd # of chars.
    # So, we can just take 1 char to fill everything for `odd` `n`
    # And we need one different char for an `even` `n`.
    if n % 2:
        return 'a' * n
    return 'a' * (n - 1) + 'b'


# Time complexity: O(n)
# W.e the case we're still using 'a`, `n` or (`n` - 1) times => O(n).
# --------------------
# Auxiliary space: O(n).
# Return can be ignored, but we still can count its space.
# And her size is equal to `n` in both cases => O(n).
