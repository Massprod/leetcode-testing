# You are given a string s consisting of lowercase letters and an integer k.
# We call a string t ideal if the following conditions are satisfied:
#   t is a subsequence of the string s.
#   The absolute difference in the alphabet order of every two adjacent letters in t is less than or equal to k.
# Return the length of the longest ideal string.
# A subsequence is a string that can be derived from another string by deleting some
#   or no characters without changing the order of the remaining characters.
# Note that the alphabet order is not cyclic.
# For example, the absolute difference in the alphabet order of 'a' and 'z' is 25, not 1.
# ------------------------
# 1 <= s.length <= 10 ** 5
# 0 <= k <= 25
# s consists of lowercase English letters.
from string import ascii_lowercase
from random import choice, randint


def longest_ideal_string(s: str, k: int) -> int:
    # working_sol (54.86%, 58.33%) -> (1867ms, 17.3mb)  time: O(k * n) | space: O(m)
    # All lowercase ASCII symbols:
    all_symbols: dict[int, int] = {}
    for _ in ascii_lowercase:
        all_symbols[ord(_)] = 0
    # Using every symbol to build subsequence from it, with
    # every other symbol available in range ord(symbol) - k or + k.
    # Left side: ord(symbol) - k, inclusive.
    # Right side: ord(symbol) + k, inclusive.
    # Give us all symbols we can use to build correct subseq.
    for sym in s:
        # Can be changed to ord(sym), but it's harder to read. Space tho.
        current_sym: int = ord(sym)
        # Left|Right sides.
        sideway: int = current_sym
        # Building subsequence from currently chosen symbol with all left_side options ->
        while (current_sym - k) <= sideway and sideway >= 97:
            # -> every time we decide, either expand|build(for the first call) subseq with
            # current symbol and new correct symbol ! all_symbols[sideway] + 1 ! or stick
            # to already stored subseq built with this symbol ! all_symbols[current_sym] !.
            # Storing every result in corresponding symbol -> gives us data on
            # what currently maximum_subseq can be built with this symbol included.
            all_symbols[current_sym] = max(all_symbols[current_sym], all_symbols[sideway] + 1)
            # Repeating for every correct symbol.
            # Stored symbols all have correct ASCII for lowercase.
            # So we can just take -1, until 'a' == 97 included.
            sideway -= 1
        # Same for right_side, but because we already have checked:
        # sideway == current_sym <- used for duplicates and first start of symbol subseq.
        # We don't need to check it again.
        sideway = current_sym + 1
        # Same approach but for symbols on the right side.
        while (current_sym + k) >= sideway and sideway <= 122:
            all_symbols[current_sym] = max(all_symbols[current_sym], all_symbols[sideway] + 1)
            sideway += 1

    return max(all_symbols.values())


# Time complexity: O(k * n) -> creating dictionary with all ASCII_lowercase symbols => O(1) -> for every symbol in
# n - len of input_string^^| input_string checking it's left and right sides, in the worst case with k == 14,
# k - ord() limitation^^|    we should check every possible symbol from ord(cur) to ord(cur) - k and ord(cur) + k, inc
#                            so with symbol like 'o' ord('o') == 111, looping for every possible option of 25 symbs ->
#                         -> and string is like 'oooooooooooooooo...etc', should be O(25 * n), but for any symbol ->
#                         -> (ord(cur) - (ord(cur) - k) + 1) * n == (k + 1) * n - left side actions
#                            + (k * n) - right side actions => so it's should be somewhat O(2k * n).
#                            Like 'z' and k == 1, left side is going to be checked for 1 option, and right ignored.
#                            It's not always 2 * k, guess I will stick to O(k * n).
# Auxiliary space: O(m) -> using dictionary with all lower_case ASCII => O(m) -> extra 2 constant INTs used.
# m - number of lower_case ASCII^^|
# ------------------------
# Ok. Working with top_down recursion, but 3200+ ms for max_constraints. What to cull? Or maybe im incorrectly caching.
# Even hits MemoryLimit, time to rebuild.
# ------------------------
# Standard recursion with cache and delete|stay symbol by symbol, but with filtering on last symbol used?
# Like only difference with longest_subsequence is that we can't use ord(x) - ord(y) > k. Let's try.


test: str = "acfgbd"
test_k: int = 2
test_out: int = 4
assert test_out == longest_ideal_string(test, test_k)

test = "abcd"
test_k = 3
test_out = 4
assert test_out == longest_ideal_string(test, test_k)

test = "pvjcci"
test_k = 4
test_out = 2
assert test_out == longest_ideal_string(test, test_k)

test = ""
for _ in range(10 ** 5):
    test += choice(ascii_lowercase)
test_k = randint(0, 25)
# print(test)
# print(test_k)
