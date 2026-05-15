# You are given an array of strings chunks.
# Concatenate all strings in chunks in order to form a string s.
# You are also given an array of strings queries.
# A joiner hyphen is a hyphen character '-' in s whose previous and next characters
#  both exist and are lowercase English letters.
# A word is a maximal substring of s consisting only of lowercase English letters
#  and joiner hyphens.
# All other characters, including spaces and hyphens that are not joiner hyphens,
#  are treated as separators.
# Return an integer array ans, where ans[i] is the number of times queries[i]
#  appears as a word in s.
# --- --- --- ---
# 1 <= chunks.length <= 10 ** 5
# 1 <= chunks[i].length <= 10 ** 5
# The total length of all strings in chunks does not exceed 10 ** 5.
# chunks[i] consists only of lowercase English letters, spaces, and '-'.
# 1 <= queries.length <= 10 ** 5
# 1 <= queries[i].length <= 10 ** 5
# The total length of all strings in queries does not exceed 10 ** 5.
# queries[i] consists only of lowercase English letters and '-'.
# queries[i] is a valid word: it does not start or end with '-', and it does not contain two consecutive hyphens.
from collections import defaultdict
from string import ascii_lowercase


def count_word_occurrences(chunks: list[str], queries: list[str]) -> list[int]:
    # working_solution: (68.44%, 88.91%) -> (215ms, 37.56mb)  Time: O(n * m + k * g) Space: O(n * m)
    words: dict[str, int] = defaultdict(int)
    cur_word: list[str] = []
    allowed_sep: str = '-'
    allowed_chars: set[str] = set(ascii_lowercase)
    for chunk in chunks:
        for char in chunk:
            if char in allowed_chars:
                cur_word.append(char)
            elif (
                cur_word
                and allowed_sep == char
                and allowed_sep != cur_word[-1]
            ):
                cur_word.append(char)
            else:
                if not cur_word:
                    continue
                if cur_word[-1] == allowed_sep:
                    cur_word.pop()
                words[''.join(cur_word)] += 1
                cur_word.clear()
    if cur_word:
        if cur_word[-1] == allowed_sep:
            cur_word.pop()
        words[''.join(cur_word)] += 1
    
    out: list[int] = []
    for query in queries:
        out.append(words.get(query, 0))
    
    return out


# Time complexity: O(n * m + k * g)
# n - length of the input array `chunks`
# m - average length of the words in the `chunks`
# k - length of the input array queries
# g - average length of the words in the `queries`
# --- --- --- ---
# Space complexity: O(n * m)


test: list[str] = ["hello wor","ld hello"]
test_queries: list[str] = ["hello","world","wor"]
test_out: list[int] = [2, 1, 0]
assert test_out == count_word_occurrences(test, test_queries)

test = ["a-b a--b ","a-","b"]
test_queries = ["a-b","a","b"]
test_out = [2, 1, 1]
assert test_out == count_word_occurrences(test, test_queries)

test = ["-cat dog- mouse"]
test_queries = ["cat","dog","mouse","cat-dog"]
test_out = [1, 1, 1, 0]
assert test_out == count_word_occurrences(test, test_queries)
