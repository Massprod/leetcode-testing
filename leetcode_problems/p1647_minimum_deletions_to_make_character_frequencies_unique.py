# A string s is called good if there are no two different characters in s that have the same frequency.
# Given a string s, return the minimum number of characters you need to delete to make s good.
# The frequency of a character in a string is the number of times it appears in the string.
# For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.
# -----------------------
# 1 <= s.length <= 10 ** 5
# s contains only lowercase English letters.
from string import ascii_lowercase
from random import choice
from collections import Counter


def min_deletions(s: str) -> int:
    # working_sol (91.33%, 93.71%) -> (108ms, 17.05mb)  time: O(n * k) | space: O(n)
    # collections.Counter() <- x2 on counting speed.
    # So it's better to use it. If we allowed.
    all_symbols: dict[str, int] = Counter(s)
    deleted: int = 0
    # Greedy approach.
    # We will delete every symbol occurrences until there's
    #  only one pair of (symbol: occurrences).
    checked_occurrences: set[int] = set()
    for sym, occurs in all_symbols.items():
        # Remember # of occurrences we already set for Any symbol.
        if occurs not in checked_occurrences:
            checked_occurrences.add(occurs)
        # If there's another symbol with same # of occurrences.
        else:
            cur_occurs: int = occurs
            # Delete symbol occurrences, until occurrence number is unique.
            # Or it's completely deleted from a string, cur_occurs == 0.
            while cur_occurs > 0 and cur_occurs in checked_occurrences:
                deleted += 1
                cur_occurs -= 1
            checked_occurrences.add(cur_occurs)

    return deleted


# Time complexity: O(n * k) -> traversing whole input_string once, to get all symbols and their occurrences => O(n) ->
# k - number of occurrences^^| -> worst case, every symbol is unique and having same occurrences ->
# n - len of input_string^^| -> then for every symbol we will change its occurrences from max to max - 1, max - 2 etc.
#                            but last symbol will be fully deleted, so it should be => O(n * k)
# Auxiliary space: O(n) -> dictionary with all symbols stored, with every symbol being unique -> store everything,
#                          extra set with occurrences, so we need unique occurrences as well =>
#                          => worst case == all unique, and all occurrences unique as well => O(2n).
# -----------------------
# Ok. Mine solution with counting values in a string is like X2 on speed vs Counter().
# So it's better to use builtin python Counter(), to count occurrences in future.
# https://docs.python.org/3/library/collections.html#collections.Counter
# Essentially the same, but faster and give another usefully methods to use.
# -----------------------
# Count every symbol occurrences, and delete ones with same occurrences, until they become unique?
# Hint:
# ! Iterate on the alphabet characters, keep decreasing
#   the frequency of the current character until it reaches a value that has not appeared before. !
# Yep. Correct idea, but I missed part with decreasing frequency order.
# Actually we don't need decreasing frequencies, all we need is delete duplicates of occurrences.


test: str = "aab"
test_out: int = 0
assert test_out == min_deletions(test)

test = "aaabbbcc"
test_out = 2
assert test_out == min_deletions(test)

test = "ceabaacb"
test_out = 2
assert test_out == min_deletions(test)

# test -> Failed -> I was counting deleted symbol which already == 0.
#                   And we need to ignore after all symbol occurrences deleted.
test = "bbcebab"
test_out = 2
assert test_out == min_deletions(test)

test = ''
for _ in range(10 ** 3):
    test += choice(ascii_lowercase)
print(test)
