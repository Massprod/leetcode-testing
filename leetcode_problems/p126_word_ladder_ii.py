# A transformation sequence from word beginWord to word endWord using a dictionary
#   wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
#     - Every adjacent pair of words differs by a single letter.
#     - Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
#     - sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList,
#   return all the shortest transformation sequences from beginWord to endWord,
#   or an empty list if no such sequence exists. Each sequence should be returned
#   as a list of the words [beginWord, s1, s2, ..., sk]
# -------------------
# 1 <= beginWord.length <= 5
# endWord.length == beginWord.length
# 1 <= wordList.length <= 500
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.
# The sum of all shortest transformation sequences does not exceed 10 ** 5.


def find_ladders(beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
    pass


test1 = ["hot", "dot", "dog", "lot", "log", "cog"]
test1_begin = "hit"
test1_end = "cog"
test1_out = [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]]

test2 = ["hot", "dot", "dog", "lot", "log"]
test2_begin = "hit"
test2_end = "cog"
test2_out = []
