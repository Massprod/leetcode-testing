# Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence
#   where each word is a valid dictionary word. Return all such possible sentences in any order.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
# -----------------------------
# 1 <= s.length <= 20  ,  1 <= wordDict.length <= 1000  ,  1 <= wordDict[i].length <= 10
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
# Input is generated in a way that the length of the answer doesn't exceed 105.


def word_break(s: str, wordDict: list[str]) -> list[str]:
    pass


test1 = "catsanddog"
test1_dict = ["cat", "cats", "and", "sand", "dog"]
test1_out = ["cats and dog", "cat sand dog"]

test2 = "pineapplepenapple"
test2_dict = ["apple", "pen", "applepen", "pine", "pineapple"]
test2_out = ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]

test3 = "catsandog"
test3_dict = ["cats", "dog", "sand", "and", "cat"]
test3_out = []
