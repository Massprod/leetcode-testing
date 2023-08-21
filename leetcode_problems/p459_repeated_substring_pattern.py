# Given a string s, check if it can be constructed by taking a substring
#   of it and appending multiple copies of the substring together.
# ---------------
# 1 <= s.length <= 10 ** 4
# s consists of lowercase English letters.


def repeated_sub_pat(s: str) -> bool:
    # working_sol (54.57%, 46.1%) -> (62ms, 16.5mb)  time: O((n // 2) * √n) | space: O(n)
    # We can use only prefix.
    # Otherwise, we will miss some letters|symbols.
    prefix: str = ''
    # Only care about half, cuz maximum SUB which can be
    # multiplied to get S is half of the S.
    for x in range(len(s) // 2):
        # Build prefix ->
        prefix += s[x]
        # -> check if it can be multiplied to get len(S) ->
        if len(s) % len(prefix) == 0:
            # -> check if it's correct string after multiplying.
            repeats = len(s) // len(prefix)
            if (prefix * repeats) == s:
                return True
    return False


# Time complexity: O((n // 2) * √n) -> traverse half or the input string with constructing prefix for every index ->
# n - len of input_string^^| -> extra build check string with some divisor of n, and max divisor of number is √num ->
#                            -> O((n // 2) * √n).
# Auxiliary space: O(n) -> we're not saving, but still building and checking (prefix * repeats) == s,
#                          and in the worst case it will be same size as n => O(n).
# ---------------
# Check every prefix of being s % len(sub) == 0  size? Like we only care about prefixes,
# cuz if we can't use prefix than we're going to miss something.
# It's slow, but is there better way? Don't see better for now, try this one.
# Ok. We need only half to consider, cuz otherwise it's always can be possible to use whole string,
# but we need substring which can be taken multiple time, not once.
# And maximum sub which can be taken at least twice is half.


test: str = "abab"
test_out: bool = True
assert test_out == repeated_sub_pat(test)

test = "aba"
test_out = False
assert test_out == repeated_sub_pat(test)

test = "abcabcabcabc"
test_out = True
assert test_out == repeated_sub_pat(test)
