# In an alien language, surprisingly, they also use English lowercase letters,
#  but possibly in a different order.
# The order of the alphabet is some permutation of lowercase letters.
# Given a sequence of words written in the alien language,
#  and the order of the alphabet, return true if and only if the given words
#  are sorted lexicographically in this alien language.
# -----------------------
# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# order.length == 26
# All characters in words[i] and order are English lowercase letters.


def is_alien_sorted(words: list[str], order: str) -> bool:
    # working_sol (67.63%, 83.46%) -> (39ms, 16.59mb)  time: O(max((m * n), g)) | space: O(n + g)
    if 1 == len(words):
        return True
    cor_order: dict[str, int] = {symbol: index for index, symbol in enumerate(order)}
    ind1: int = 0
    ind2: int = 1
    # Comparing by 1 letter, if they're equal we need to compare next.
    # If all symbols are equal, then string with smaller length should be first.
    while ind2 < len(words):
        word1: str = words[ind1]
        word2: str = words[ind2]
        index: int = 0
        while index < min(len(word2) - 1, len(word1) - 1) and word1[index] == word2[index]:
            index += 1
        if cor_order[word1[index]] == cor_order[word2[index]] and len(word2) < len(word1):
            return False
        if cor_order[word1[index]] > cor_order[word2[index]]:
            return False
        ind1 += 1
        ind2 += 1
    return True


# Time complexity: O(max((m * n), g)) <- m - length of input array `words` , n - average length of words inside `words`
#                                        g - length of input string `order`
# `order` is constant size, and we can have case with `words` only having 1 word and length == 1.
# So, it's better to say => O(max((m * n), g)).
# -----------------------
# Auxiliary space: O(n + g)
# Dictionary `cor_order` with all symbols from original `order` stored in it.
# Extra space for 2 strings from `words`, taking average => O(2n + g).


test: list[str] = ["hello", "leetcode"]
test_order: str = "hlabcdefgijkmnopqrstuvwxyz"
test_out: bool = True
assert test_out == is_alien_sorted(test, test_order)

test = ["word", "world", "row"]
test_order = "worldabcefghijkmnpqstuvxyz"
test_out = False
assert test_out == is_alien_sorted(test, test_order)

test = ["apple", "app"]
test_order = "abcdefghijklmnopqrstuvwxyz"
test_out = False
assert test_out == is_alien_sorted(test, test_order)

test =["ubg", "kwh"]
test_order = "qcipyamwvdjtesbghlorufnkzx"
test_out = True
assert test_out == is_alien_sorted(test, test_order)
