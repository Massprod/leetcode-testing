# A transformation sequence from word beginWord to word endWord using a dictionary wordList
#   is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
#       Every adjacent pair of words differs by a single letter.
#       Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
#       sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList,
#   return the number of words in the shortest transformation sequence from beginWord to endWord,
#   or 0 if no such sequence exists.
# ------------------------
# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.
from collections import deque, defaultdict


def ladder_length(beginWord: str, endWord: str, wordList: list[str]) -> int:
    pass


test1 = ["hot", "dot", "dog", "lot", "log", "cog"]
test1_begin = "hit"
test1_end = "cog"
test1_out = 5

test2 = ["hot", "dot", "dog", "lot", "log"]
test2_begin = "hit"
test2_end = "cog"
test2_out = 0
