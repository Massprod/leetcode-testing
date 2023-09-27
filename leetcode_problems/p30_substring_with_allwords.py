# You are given a string s and an array of strings words.
# All the strings of words are of the same length.
# A concatenated substring in s is a substring that contains
#  all the strings of any permutation of words concatenated.
# For example, if words = ["ab","cd","ef"],
#  then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab"
#  are all concatenated strings.
# "acdbef" is not a concatenated substring because it is not
#  the concatenation of any permutation of words.
# Return the starting indices of all the concatenated substrings in s.
# You can return the answer in any order.
# ----------------
# 1 <= s.length <= 10 ** 4
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 30
# s and words[i] consist of lowercase English letters.
from collections import Counter


def sub_indexes(s: str, words: list[str]) -> list[int]:
    # working_sol (98.37%, 98.37%) -> (71ms, 16.8mb)  time: O(n * k) | space: O(n + k)
    # All words have same length.
    max_len: int = len(words[0])
    # Counter of all words occurrences.
    all_words: dict[str, int] = Counter(words)
    # Currently used words in substring.
    used_words: dict[str, int] = {}
    start_indexes: list[int] = []
    # We're using sliding window of (max_len) size.
    # So, we need to check only 0 -> max_len - 1, start indexes.
    # Because everything else will be covered:
    # 0 -> 29, 29 -> 58 | 1 -> 30, 30 -> 59 etc.
    for x in range(max_len):
        # Words used in current substring.
        count: int = 0
        used_words.clear()
        # Substring start point.
        start: int = x
        # Substring end point == y.
        for y in range(x, len(s), max_len):
            cur_word: str = s[y: y + max_len]
            # Expand.
            if cur_word in all_words:
                if cur_word in used_words:
                    used_words[cur_word] += 1
                    count += 1
                    # Delete exceed usages to maintain correct substring.
                    while used_words[cur_word] > all_words[cur_word]:
                        first_word: str = s[start: start + max_len]
                        used_words[first_word] -= 1
                        count -= 1
                        # Shift the start on to the next word, after every deletion.
                        start += max_len
                else:
                    used_words[cur_word] = 1
                    count += 1
                # All set == correct start point.
                # But we still can check others.
                if count == len(words):
                    start_indexes.append(start)
            # Incorrect word in substring == reset substring.
            # Skip this word and try starting a new substring after it.
            else:
                count = 0
                start = y + max_len
                used_words.clear()
    return start_indexes


# Time complexity: O(k * n) -> we start building windows(substrings) only from (0 -> max_len - 1) indexes ->
# n - len of input array == words^^| -> for every substring we traverse almost whole input string -> for 0 is whole,
# k - len of words in words^^| for 1 is len(s) - 1 .. len(s) - 30, but worst case == we're using all indexes ->
#                              -> once to expand and once we shrink, they can be used twice => O(k * 2n).
# Auxiliary space: O(n + k) -> two dictionaries with all words from input array -> string with max size = k => O(n + k).


test: str = "barfoothefoobarman"
test_words: list[str] = ["foo", "bar"]
test_out: list[int] = [0, 9]
assert sub_indexes(test, test_words) == test_out

test = "wordgoodgoodgoodbestword"
test_words = ["word", "good", "best", "good"]
test_out = [8]
assert sub_indexes(test, test_words) == test_out
