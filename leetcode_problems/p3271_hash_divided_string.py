# You are given a string s of length n and an integer k, where n is a multiple of k.
# Your task is to hash the string s into a new string called result,
#  which has a length of n / k.
# First, divide s into n / k substrings, each with a length of k.
# Then, initialize result as an empty string.
# For each substring in order from the beginning:
#  - The hash value of a character is the index of that character in the English
#   alphabet (e.g., 'a' → 0, 'b' → 1, ..., 'z' → 25).
#  - Calculate the sum of all the hash values of the characters in the substring.
#  - Find the remainder of this sum when divided by 26, which is called hashedChar.
#  - Identify the character in the English lowercase alphabet
#   that corresponds to hashedChar.
#  - Append that character to the end of result.
# Return result.
# --------------------------
# 1 <= k <= 100
# k <= s.length <= 1000
# s.length is divisible by k.
# s consists only of lowercase English letters.
from string import ascii_lowercase


def string_has(s: str, k: int) -> str:
    # working_sol (78.19%, 76.67%) -> (15ms, 17.82mb)  time: O(s) | space: O(s)
    out: list[str] = []
    # ! s.length is divisible by k. !
    for start in range(0, len(s), k):
        slice_sum: int = 0
        # We either create a map for a -> 0 and other chars.
        # Or, we save space and just calc +97 -97 when we needed.
        for char_index in range(start, start + k):
            char: str = s[char_index]
            char_hash: int = ord(char)
            slice_sum += char_hash - 97
        out.append(chr((slice_sum % 26) + 97))
    
    return ''.join(out)


# Time complexity: O(s)
# Always traversing every char of the input string `s`, once => O(s)
# --------------------------
# Auxiliary space: O(s)
# In the worst case `k` == 1.
# `out` <- allocates space for each char from 1 sized slices => O(s).


test: str = 'abcd'
test_k: int = 2
test_out: str = 'bf'
assert test_out == string_has(test, test_k)

test = 'mxz'
test_k = 3
test_out = 'i'
assert test_out == string_has(test, test_k)
