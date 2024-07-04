# Given a string s, return true if the s can be palindrome
#  after deleting at most one character from it.
# --------------------------
# 1 <= s.length <= 10 ** 5
# s consists of lowercase English letters.
from random import choice
from string import ascii_lowercase


def valid_palindrome(s: str) -> bool:
    # working_sol (54.87%, 96.42%) -> (103ms, 16.72mb)  time: O(s) | space: O(s)
    def is_pal(string: str) -> bool:
        left_l: int = 0
        right_l: int = len(string) - 1
        while left_l < right_l:
            # We can't delete anymore symbols.
            if string[left_l] != string[right_l]:
                return False
            left_l += 1
            right_l -= 1
        return True

    left: int = 0
    right: int = len(s) - 1
    while left < right:
        # We can delete only once, but in 2 ways.
        if s[left] != s[right]:
            option1: str = s[left + 1: right + 1]
            option2: str = s[left: right]
            # Left or Right value is deleted.
            return is_pal(option1) or is_pal(option2)
        left += 1
        right -= 1
    # Otherwise we can have:
    #  - EVEN palindrome, so we can make it ODD palindrome by deleting one of the middle elements.
    #  - ODD palindrome, we can just take out the middle and have EVEN palindrome.
    return True


# Time complexity: O(s)
# Either traversing whole `s` once, or we delete some symbol and traverse `s` twice => O(2n).
# Not really whole `s` but 2 new strings with size of `s - 1`.
# --------------------------
# Auxiliary space: O(s)
# We're going to create `option1` and `option2` with size `s - 1` both, in the worst case => O(2n).


test: str = "aba"
test_out: bool = True
assert test_out == valid_palindrome(test)

test = "abca"
test_out = True
assert test_out == valid_palindrome(test)

test = "abc"
test_out = False
assert test_out == valid_palindrome(test)

test = 'lcupuupucul'
test_out = True
assert test_out == valid_palindrome(test)

test = ''.join([choice(ascii_lowercase) for _ in range(10 ** 5)])
print(test)
