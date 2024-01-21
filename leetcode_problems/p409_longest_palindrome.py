# Given a string s which consists of lowercase or uppercase letters,
#  return the length of the longest palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
# ----------------------
# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.
from random import choice
from collections import Counter
from string import ascii_letters


def longest_palindrome(s: str) -> int:
    # working_sol (87.81%, 57.49%) -> (33ms, 16.56mb)  time: O(s) | space: O(s)
    all_chars: dict[str, int] = Counter(s)
    out: int = 0
    middle_used: bool = False
    for char, occurrences in all_chars.items():
        # Even -> we can use them all.
        if 0 == occurrences % 2:
            out += occurrences
        # Odd -> we can use only occurrences - 1.
        else:
            # But, 1 of them can be placed in the middle. Once.
            if not middle_used:
                out += occurrences
                middle_used = True
            else:
                out += occurrences - 1
    return out


# Time complexity: O(s).
# Traversing input string `s` once to get all characters and their occurrences => O(s).
# Worst case: all chars are unique.
# Traversing all these chars again, to get maximum size of the palindrome => O(s).
# ----------------------
# Auxiliary space: O(s).
# We're using dict `all_chars` to store all chars present in `s`.
# Worst case: all chars are unique. So, we will store all of them => O(s).


test: str = "abccccdd"
test_out: int = 7
assert test_out == longest_palindrome(test)

test = "a"
test_out = 1
assert test_out == longest_palindrome(test)

test = "AAAAAAAAAaa"
test_out = 11
assert test_out == longest_palindrome(test)

test = ''.join([choice(ascii_letters) for _ in range(2000)])
print(test)
