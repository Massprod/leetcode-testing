# A transformation sequence from word beginWord to word endWord using a dictionary wordList
#  is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
#   - Every adjacent pair of words differs by a single letter.
#   - Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
#   - sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList,
#  return the number of words in the shortest transformation sequence from beginWord to endWord,
#  or 0 if no such sequence exists.
# ------------------------
# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.
from collections import deque


def ladder_length(beginWord: str, endWord: str, wordList: list[str]) -> int:
    # working_sol (80.48%, 42.36%) -> (126ms, 19.82mb)  time: O(n * k) | space: O(n * k)
    # We're not guaranteed that endWord in wordList.
    # But, we're guaranteed no duplicates == no reasons to change it to set().
    if endWord not in wordList:
        return 0
    # (1sym_diff: [all words with 1sym_diff])
    graph: dict[str, list[str]] = {}
    for word in wordList:
        for x in range(len(word)):
            option: str = f'{word[:x]}*{word[x + 1:]}'
            if option in graph:
                graph[option].append(word)
            else:
                graph[option] = [word]
    # Standard BFS with delimiter.
    que: deque[str | None] = deque([beginWord, None])
    visited: set[str] = set()
    # beginWord -> always first word in sequence len(seq) == 1.
    length: int = 1
    while que:
        word: str = que.popleft()
        if not word:
            if que:
                que.append(None)
            length += 1
            continue
        if word in visited:
            continue
        visited.add(word)
        # Check every other word with only 1 symbol difference.
        for x in range(len(word)):
            option = f'{word[:x]}*{word[x + 1:]}'
            if option in graph:
                for edge in graph[option]:
                    if edge == endWord:
                        return length + 1
                    que.append(edge)
    return 0


# Time complexity: O(n * k) -> all words are equal size + worst case == every word have unique 'option's => O(n * k) ->
# n - len of input array 'wordList'^^|  -> standard BFS with check of all words and their options => O(2 * (n * k)).
# k - len of input string 'beginWord'^^|
# Auxiliary space: O(n * k) -> same worst case -> we will store every unique word 'option's in 'graph' => O(n * k) ->
#                           -> extra que with all words allocated => O(n) -> and set 'visited' in worst case O(n - 1).


test: list[str] = ["hot", "dot", "dog", "lot", "log", "cog"]
test_begin: str = "hit"
test_end: str = "cog"
test_out: int = 5
assert test_out == ladder_length(test_begin, test_end, test)

test = ["hot", "dot", "dog", "lot", "log"]
test_begin = "hit"
test_end = "cog"
test_out = 0
assert test_out == ladder_length(test_begin, test_end, test)
