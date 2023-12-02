# You are given an array of strings words and a string chars.
# A string is good if it can be formed by characters from chars
#  (each character can only be used once).
# Return the sum of lengths of all good strings in words.
# -----------------------
# 1 <= words.length <= 1000
# 1 <= words[i].length, chars.length <= 100
# words[i] and chars consist of lowercase English letters.
from random import choice
from string import ascii_lowercase
from collections import Counter


def count_characters(words: list[str], chars: str) -> int:
    # working_sol (86.96%, 83.2%) -> (100ms, 16.78mb)  time: O(n * m + k) | space: O(n + k)
    # {symbol: # of occurrences}
    all_syms: dict[str, int] = Counter(chars)
    out: int = 0
    # We can have duplicates and even 1 word repeated for ! 1 <= words.length <= 1000 !.
    # So, it's better to ignore them if already checked.
    correct: set[str] = set()
    incorrect: set[str] = set()
    for word in words:
        if word in correct:
            out += len(word)
            continue
        elif word in incorrect:
            continue
        # Same goes for symbols we check.
        # We can have words like: 'aaaaaaa...aaa', and count() is O(n).
        syms_checked: set[str] = set()
        for sym in word:
            if sym in syms_checked:
                continue
            # Every symbol should be present, and it's occurrences <= occurrences in 'chars'.
            if not (sym in all_syms and word.count(sym) <= all_syms[sym]):
                incorrect.add(word)
                break
            syms_checked.add(sym)
        else:
            correct.add(word)
            out += len(word)
    return out


# Time complexity: O(n * m + k) <- n - length of input array 'words',
#                                  m - average length of word inside 'words',
#                                  k - length of input string 'chars'.
# Counter() on 'chars' to get all characters present.
# Worst case == every word is maximum sized == 100, and all their symbols presented in 'chars' + all words unique.
# We will traverse all words in the 'words' and all their symbols.
# !
# Only question is count(). Because if we have duplicates we will ignore them, but does it traverse all string?
# Yep O(n) for count() <- n - length of input string.
# And I don't get it what test_cases they have, because if we traverse full string
#  why it's slower to ignore duplicated symbols.
# Cuz my solution with just count() on every symbols is 81ms and with extra culling is 100ms.
# But it should be faster with duplicates 100%.
# !
# But we can ignore already used symbols, so we always check at max all lowercase ENG symbols == 26.
# ! words[i] and chars consist of lowercase English letters !.
# Well, then it should be: O(n * (26 * m) + k)? OR O(n * m + k), if we ignore constant.
# Because we call count() on every index in word, and if docs I found correct every call is O(m).
# -----------------------
# Auxiliary space: O(n + k)
# 'all_syms' every symbol of 'chars' with INT as value.
# 'correct' or 'incorrect' no matter the case they both will store every word from 'words' if summarized.
# 'syms_checked' is at max going to have size of 26, so it's somewhat constant.


test: list[str] = ["cat", "bt", "hat", "tree"]
test_chars: str = "atach"
test_out = 6
assert test_out == count_characters(test, test_chars)

test = ["hello", "world", "leetcode"]
test_chars = "welldonehoneyr"
test_out = 10
assert test_out == count_characters(test, test_chars)

test = [''.join([choice(ascii_lowercase) for _ in range(100)]) for _ in range(1000)]
test_chars = ''.join([choice(ascii_lowercase) for _ in range(100)])
print(test)
print('\n!!!!!!\n')
print(test_chars)
