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
    word_list: set[str] = set(wordList)
    if endWord not in wordList:
        return []

    def single_diff(word1: str, word2: str) -> bool:
        count: int = 0
        for x in range(len(word1)):
            if count > 1:
                return False
            elif word1[x] != word2[x]:
                count += 1
        if count == 1:
            return True
        return False

    def ladder_search(path: list[str]) -> None:
        if min_length[-1] - 1 < len(path):
            return
        if single_diff(path[-1], endWord):
            path.append(endWord)
            path_length: int = len(path)
            if min_length[-1] > path_length:
                min_length[-1] = path_length
                correct_paths.clear()
                correct_paths.append(path.copy())
                path.pop()
                return
            elif min_length[-1] == path_length:
                correct_paths.append(path.copy())
                path.pop()
                return
            elif min_length[-1] < path_length:
                path.pop()
                return
        for word in word_list:
            if (word not in used) and single_diff(path[-1], word):
                used.add(word)
                path.append(word)
                ladder_search(path)
                path.pop()
                used.remove(word)

    if single_diff(beginWord, endWord):
        return [[beginWord, endWord]]
    used: set[str] = set()
    min_length: list[int] = [len(word_list)]
    correct_paths: list[list[str]] = []
    for check in word_list:
        if single_diff(beginWord, check):
            used.add(check)
            used.add(beginWord)
            ladder_search([beginWord, check])
            used.clear()
    return correct_paths


# Rushed commit and forgot about part with different lengths, if we meet something smaller
# we should fully clear correct_paths.
# -------------------
# What about case when beginWord is 1 letter changed endWord?
# can we just return it => [beginWord, endWord]
# Yeah, tested this case, it's correct assumption.
# -------------------
# No info on what position endWord will have, so I assume that it can be any position.
# So we obliged to check every possible index to find this and build ladder using any other words.
# We can ignore any starting words we already checked.
# Like in test1 -> started with HOT there's ro reasons to check DOR + HOT after HOT ->
# -> so it's only left to right walk to find ladder, everything we already started from can be ignored.
# -------------------
# No idea about TimeLimit, but I can solve it with recursion.
# If I hit TLE than rebuild, but let's try recursion first.


test1 = ["hot", "dot", "dog", "lot", "log", "cog"]
test1_begin = "hit"
test1_end = "cog"
test1_out = [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]]
print(find_ladders(test1_begin, test1_end, test1))

test2 = ["hot", "dot", "dog", "lot", "log"]
test2_begin = "hit"
test2_end = "cog"
test2_out = []

test3 = ["hot", "dot", "dog", "lot", "log", "cog", "mog"]
test3_begin = "hit"
test3_end = "cog"
test3_out = [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]]
print(find_ladders(test3_begin, test3_end, test3))

# test4 - Failed -> I was trying to speed things up and assumed that we can ignore double checks,
#                   but we can't ignore double checks inside a recursion, because it gives us different paths.
test4 = ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]
test4_begin = "red"
test4_end = "tax"
test4_out = [["red", "ted", "tad", "tax"], ["red", "ted", "tex", "tax"], ["red", "rex", "tex", "tax"]]
print(find_ladders(test4_begin, test4_end, test4))

# test5 - Failed -> I was incorrect on checking 2 words, focused on recursion too much,
#                   and I can actually use sets(), because we're checking every index anyway.
test5 = ["lest", "leet", "lose", "code", "lode", "robe", "lost"]
test5_begin = "leet"
test5_end = "code"
test5_out = [["leet", "lest", "lost", "lose", "lode", "code"]]
print(find_ladders(test5_begin, test5_end, test5))
