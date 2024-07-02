# Given two strings a and b, return the length of the longest uncommon subsequence
#  between a and b. If no such uncommon subsequence exists, return -1.
# An uncommon subsequence between two strings is a string that is a
#  subsequence of exactly one of them.
# ---------------------------
# 1 <= a.length, b.length <= 100
# a and b consist of lower-case English letters.


def find_lus_length(a: str, b: str) -> int:
    # working_sol (92.99%, 60.26%) -> (28ms, 16.43mb)  time: O(a + b) | space: O(1)
    if a == b:
        return -1
    # We can use the whole string as subsequence.
    # And if they differ by at least 1 symbol and suppose still one of them contains another, like:
    # a == 'aab' , b == 'caab` <- we can just take highest,
    #  because it'd for sure have distinct char, and it's longer :)
    return max(len(a), len(b))


# Time complexity O(a + b)
# Always traversing both strings `a` and `b` to compare them => O(a + b)
# ---------------------------
# Auxiliary space: O(1)
# Nothing extra used.


test_a: str = "aba"
test_b: str = "cdc"
test_out: int = 3
assert test_out == find_lus_length(test_a, test_b)

test_a = "aaa"
test_b = "bbb"
test_out = 3
assert test_out == find_lus_length(test_a, test_b)

test_a = "aaa"
test_b = "aaa"
test_out = -1
assert test_out == find_lus_length(test_a, test_b)
