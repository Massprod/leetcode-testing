# Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence
#   where each word is a valid dictionary word. Return all such possible sentences in any order.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
# -----------------------------
# 1 <= s.length <= 20  ,  1 <= wordDict.length <= 1000  ,  1 <= wordDict[i].length <= 10
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
# Input is generated in a way that the length of the answer doesn't exceed 105.


def word_break(s: str, wordDict: list[str]) -> list[str]:
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


# Well. 25/26 cases passed, at least it's working with prev_build.


test1 = "catsanddog"
test1_dict = ["cat", "cats", "and", "sand", "dog"]
test1_out = ["cats and dog", "cat sand dog"]
print(word_break(test1, test1_dict))

test2 = "pineapplepenapple"
test2_dict = ["apple", "pen", "applepen", "pine", "pineapple"]
test2_out = ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]
print(word_break(test2, test2_dict))

test3 = "catsandog"
test3_dict = ["cats", "dog", "sand", "and", "cat"]
test3_out = []
print(word_break(test3, test3_dict))

# test4 - failed -> I was adding start_indexes into fail even after exceeding max_length which isn't correct,
#                   because now we're not just returning True or False, but checking every possible way to construct,
#                   and after exceeding length we're just going out from recursion and start is still reusable.
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
for _ in test4_out:
    if _ not in test:
        print(_)
