# Given a string s and a dictionary of strings wordDict, return true if s can be segmented
#   into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
# -----------------------------
# 1 <= s.length <= 300  ,  1 <= wordDict.length <= 1000  ,  1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.


def word_break(s: str, wordDict: list[str]) -> bool:
    pass


test1 = "leetcode"
test1_dict = ["leet", "code"]
test1_out = True

test2 = "applepenapple"
test2_dict = ["apple", "pen"]
test2_out = True

test3 = "catsandog"
test3_dict = ["cats", "dog", "sand", "and", "cat"]
test3_out = False
