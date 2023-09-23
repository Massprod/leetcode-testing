# You are given an array of words where each word consists of lowercase English letters.
# wordA is a predecessor of wordB if and only if we can insert exactly one letter
#  anywhere in wordA without changing the order of the other characters to make it equal to wordB.
# For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
# A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1,
#  where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on.
# A single word is trivially a word chain with k == 1.
# Return the length of the longest possible word chain with words chosen from the given list of words.
# ----------------------
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 16
# words[i] only consists of lowercase English letters.


def longest_str_chain(words: list[str]) -> int:
    # working_sol (90.96%, 77.76%) -> (117ms, 16.7mb)  time: O(n * log n) | space: O(n + k)
    # All words by themselves == chain of 1.
    chains: dict[str, int] = {word: 1 for word in words}
    # Remove duplicates.
    words = list(set(words))
    # Always use smallest to build from.
    words.sort(key=lambda y: len(y))
    for word in words:
        max_chain: int = 0
        # Delete every symbol and check if there's word to build from.
        for x in range(len(word)):
            one_del: str = word[:x] + word[x + 1:]
            # It's possible that there's multiple chains.
            # We need to choose longest.
            if one_del in chains:
                max_chain = max(max_chain, chains[one_del])
        chains[word] += max_chain
    return max(chains.values())


# Time complexity: O(n * log n) -> worst case == no duplicates -> creating dictionary with all words => O(n) ->
# n - len of input array^^| -> deleting duplicates, by converting into a set and back to list => O(2n) ->
#                           -> sorting in ascending order by length of the words, in place => O(n * log n) ->
#                           -> traversing whole array to slice and check every word, worst case == we  will have
#                           all words with length == 16 == max_constraint => O(n * 16) or O(n * k), k - len of word.
#                           Sorting will dominate everything => O(n * log n).
# Auxiliary space: O(n + k) -> worst case == no duplicates -> extra dictionary with all words stored => O(n) ->
# k - longest word of input array^^| -> and extra string which depends on input, and max_len == 15 => O(k).
# ----------------------
# 83/84 passed, Failed because we can have duplicates.
# In this case we continue to increment stored chain, so we need to delete all of them. Or just store what used.
# But it's better to just delete them and don't bother. Cuz we can't build different chains from same word.
# ----------------------
# !
# Instead of adding a character, try deleting a character to form a chain in reverse.
# !
# Only question, how we can build longest.
# Cuz we can just store everything and use slices of every string to check if it's present and increase counter.
# But how to count it correctly?
# Use smallest? Like we use the smallest string possible, delete symbol from it and check if such string exist.
# Then we will always use the smallest option and build the longest chain.
# What if case like: 'abce' 'abc' 'abd' 'ab' 'bd' 'a' 'd' 'bce'.
# We can build: 'a' -> 'ab' -> 'abd' or 'abc' and 'abce'
# Or: 'bce' -> 'abce'. Which is shorter, but doable. Then we need to take maximum so far?
# Cuz there's multiple chains which can lead to check string.
# Then it's first sort to always use smallest, and then just check deletion of every symbol in a string.
# And if there's multiple chains we can use, choose highest.
# Let's try.


test: list[str] = ["a", "b", "ba", "bca", "bda", "bdca"]
test_out: int = 4
assert test_out == longest_str_chain(test)

test = ["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]
test_out = 5
assert test_out == longest_str_chain(test)

test = ["abcd", "dbqca"]
test_out = 1
assert test_out == longest_str_chain(test)

test = ["abce", "abc", "abd", "ab", "bd", "a", "d", "bce"]
test_out = 4
assert test_out == longest_str_chain(test)
