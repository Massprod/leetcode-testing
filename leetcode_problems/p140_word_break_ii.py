# Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence
#   where each word is a valid dictionary word. Return all such possible sentences in any order.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
# -----------------------------
# 1 <= s.length <= 20  ,  1 <= wordDict.length <= 1000  ,  1 <= wordDict[i].length <= 10
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
# Input is generated in a way that the length of the answer doesn't exceed 105.


def word_break(s: str, wordDict: list[str]) -> list[str]:
    # working_sol (41.42%, 28.56%) -> (44ms, 16.4mb)  time: O(2 ** (log n)) | space: O(m + n + (K * n))
    all_symbols: set[str] = set()
    path: list[str] = []
    paths: list[[list[str]]] = []
    for _ in wordDict:
        for symbol in _:
            if symbol not in all_symbols:
                all_symbols.add(symbol)
    for _ in s:
        if _ not in all_symbols:
            return path
    all_words: set[str] = set(wordDict)
    max_len: int = 0
    for _ in all_words:
        max_len = max(max_len, len(_))
    failed: dict[int] = {}

    def check_start(start: int):
        if start in failed.keys() and failed[start] is False:
            return False
        if len("".join(path)) == len(s):
            to_append: str = " ".join(path.copy())
            paths.append(to_append)
            return True
        fail: bool = True
        to_check: str = ""
        for y in range(start, len(s)):
            if len(to_check) > max_len:
                if fail:
                    failed[start] = False
                return False
            to_check += s[y]
            if to_check in all_words:
                fail = False
                path.append(to_check)
                check_start(y + 1)
                path.pop()
        if fail:
            failed[start] = False

    check_start(0)
    return paths


# Time complexity: O(2 ** (log n)) -> creating set() with all available symbols in input_dict => O(j * g) ->
# n - len of input_string^^| -> checking every symbol in input_string to be available in input_dict => O(n) ->
# m - len of input_dict^^  | -> creating set of input_dict => O(m) -> getting max_len from all_word => O(m) ->
# g - lens of words in input_dict^^| -> recursion to check every substring in input_string => O(2 ** (log n)) ->
# j - number of words in input_dict^^| -> O((j * g) + n + m + 2 ** n) -> O(2 ** (log n))
#                                 ! 99% sure it's incorrect for the recursion^^,
#                                   but still didn't find how to calc them correctly.
#                                   Leaving it as default for all substrings O(2 ** n)
#                                   We're only using combinations for nCg for every g in input_dict !
# Auxiliary space: O(O(m + n + (K * n))) -> creating set() with all available symbols in input_dict => O(j * g) ->
#                         -> set() with all_words from input_dict => O(m) -> creating path with all words used =>
#                         => contains words of input_string, with correct path summarized length of these
#                            always equal to n => O(n) -> dictionary with failed start_indexes => worst case
#                            we're going to start from every index from 0 to n - 2, and n - 1 index isn't solvable =>
#                         => O(n - 2) -> O((j * g) + m + n + (n - 2)) -> O(2m + 2n) -> O(m + n)
#                                             ^^all words lengths summarized will leave us with m
# K - num of correct paths^^| Now we're creating extra PATHS, containing all correct paths we found ->
#                         -> every path is at max of len(n) but number of these paths unknown, let it be some int-K ->
#                         -> O(K * n) => O(m + n + (K * n))
# -----------------------------
# Ok. Rebuild p139 solution to save path, and don't skip indexes we're already visited but not failed.
# -----------------------------
# Well. 25/26 cases passed, at least it's working with prev_build.


test1 = "catsanddog"
test1_dict = ["cat", "cats", "and", "sand", "dog"]
test1_out = ["cats and dog", "cat sand dog"]
test = word_break(test1, test1_dict)
assert len(test1_out) == len(test)
for _ in test1_out:
    assert _ in test
del test

test2 = "pineapplepenapple"
test2_dict = ["apple", "pen", "applepen", "pine", "pineapple"]
test2_out = ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]
test = word_break(test2, test2_dict)
assert len(test2_out) == len(test)
for _ in test2_out:
    assert _ in test
del test

test3 = "catsandog"
test3_dict = ["cats", "dog", "sand", "and", "cat"]
test3_out = []
test = word_break(test3, test3_dict)
assert len(test3_out) == len(test)
for _ in test3_out:
    assert _ in test
del test

# test4 - failed -> I was adding start_indexes into failed even after exceeding max_length which isn't correct,
#                   because now we're not just returning True or False, but checking every possible way to construct,
#                   and after exceeding length we're just going out from recursion, and start_index is still reusable.
test4 = "aaaaaaaa"
test4_dict = ["aaaa", "aa", "a"]
test4_out = [
    "a a a a a a a a", "aa a a a a a a", "a aa a a a a a", "a a aa a a a a", "aa aa a a a a", "aaaa a a a a",
    "a a a aa a a a", "aa a aa a a a", "a aa aa a a a", "a aaaa a a a", "a a a a aa a a", "aa a a aa a a",
    "a aa a aa a a", "a a aa aa a a", "aa aa aa a a", "aaaa aa a a", "a a aaaa a a", "aa aaaa a a",
    "a a a a a aa a", "aa a a a aa a", "a aa a a aa a", "a a aa a aa a", "aa aa a aa a", "aaaa a aa a",
    "a a a aa aa a", "aa a aa aa a", "a aa aa aa a", "a aaaa aa a", "a a a aaaa a", "aa a aaaa a",
    "a aa aaaa a", "a a a a a a aa", "aa a a a a aa", "a aa a a a aa", "a a aa a a aa", "aa aa a a aa",
    "aaaa a a aa", "a a a aa a aa", "aa a aa a aa", "a aa aa a aa", "a aaaa a aa", "a a a a aa aa",
    "aa a a aa aa", "a aa a aa aa", "a a aa aa aa", "aa aa aa aa", "aaaa aa aa", "a a aaaa aa", "aa aaaa aa",
    "a a a a aaaa", "aa a a aaaa", "a aa a aaaa", "a a aa aaaa", "aa aa aaaa", "aaaa aaaa",
]
test = word_break(test4, test4_dict)
assert len(test4_out) == len(test)
for _ in test4_out:
    assert _ in test
del test
