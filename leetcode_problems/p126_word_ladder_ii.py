# A transformation sequence from word beginWord to word endWord using a dictionary wordList
#  is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
#   - Every adjacent pair of words differs by a single letter.
#   - Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
#   - sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList,
#  return all the shortest transformation sequences from beginWord to endWord,
#  or an empty list if no such sequence exists.
# Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk]
# -------------------
# 1 <= beginWord.length <= 5
# endWord.length == beginWord.length
# 1 <= wordList.length <= 500
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.
# The sum of all shortest transformation sequences does not exceed 10 ** 5.
from collections import deque


def find_ladders(beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
    # working_sol (92.42%, 43.68%) -> (47ms, 17mb)  time: O(n * k + (n - 2) * m) | space: O(n * k + ((n - 2) * m) * k)
    # We're not guaranteed that endWord in wordList.
    # But, we're guaranteed no duplicates == no reasons to change it to set().
    if endWord not in wordList:
        return []
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
    end: bool = False
    # (word: [words to whom we can travel from it])
    # Extra used as visited check.
    dfs_graph: dict[str, list[str]] = {}
    # Copy of 'dfs_graph', but we can't ignore words while level traverse isn't complete.
    # We need temporary storage like this:
    # (lot: hot) <- if we add this into 'dfs_graph' instantly.
    # Then we will ignore other words from whom we can come into 'lot'.
    # So, we first record every 'edge' + words from whom we can come to this 'edge' on level,
    #  and only after add this in 'dfs_graph' + mark as visited.
    level_graph: dict[str, list[str]] = {}
    while que:
        word: str = que.popleft()
        if not word:
            dfs_graph.update(level_graph)
            level_graph = {}
            if end:
                break
            if que:
                que.append(None)
            continue
        # Check every other word with only 1 symbol difference.
        for x in range(len(word)):
            option = f'{word[:x]}*{word[x + 1:]}'
            if option in graph:
                for edge in graph[option]:
                    # Visited.
                    if edge in dfs_graph:
                        continue
                    # (word <-> edge)
                    # Visited, but only on current level.
                    # So, we can have multiple words this 'edge' leading to.
                    if edge in level_graph:
                        level_graph[edge].append(word)
                    else:
                        level_graph[edge] = [word]
                        que.append(edge)
                    # Last level we need to proceed.
                    if edge == endWord:
                        end = True
    paths: list[list[str]] = []

    def dfs(node: str, path: list[str]) -> None:
        # Standard DFS, from 'endWord' -> 'beginWord'.
        if node == beginWord:
            path = path + [beginWord]
            # We need 'beginWord' -> 'endWord' sequence == reverse.
            paths.append(path[::-1])
            return
        if node in dfs_graph:
            for new_node in dfs_graph[node]:
                dfs(new_node, path + [node])

    dfs(endWord, [])
    return paths


# Time complexity: O(n * k + (n - 2) * m) -> worst case == every word have unique 'option's => O(n * k) ->
# n - len of input array 'wordList'^^|  -> standard BFS with check of all words and their options => O(2 * (n * k)) ->
# k - len of input string 'beginWord'^^|-> worst cast == everything is differs by 1 symbol ->
# m - len of shortest seq^^|            -> dfs will check every path and in case like:
#                                       begin and end words will have all neighbour differ by 1 symbol ->
#                                       -> begin + word1|word2|word4| etc. |wordN + endWord => O((n - 2) * m).
#                                        ! (n - 2) # of sequences, m - length of every sequence (dfs depth) !
# Auxiliary space: O(n * k + ((n - 2) * m) * k) -> we will store every unique word 'option's in 'graph' => O(n * k) ->
#                           -> extra que with all words allocated => O(n) ->
#                           -> worst case == begin and end words will have all neighbour differ by 1 symbol ->
#                           -> begin + word1|word2|word4| etc. |wordN + endWord <- sequence like this ->
#                           -> so, 'level_graph' will be a copy of 'dfs_graph' and size of 'n' => O(2n) ->
#                           -> array 'paths' will store (m * (n - 2)) paths in this case => O((n - 2) * m * k).
#                           ! (n - 2) # of sequences, m - length of every sequence, k - length of every word !
#                           -> extra recursion stack with max size 'n' when using every word in sequence => O(n).


test: list[str] = ["hot", "dot", "dog", "lot", "log", "cog"]
test_begin: str = "hit"
test_end: str = "cog"
test_out: list[list[str]] = [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]]
assert sorted(test_out) == sorted(find_ladders(test_begin, test_end, test))

test = ["hot", "dot", "dog", "lot", "log"]
test_begin = "hit"
test_end = "cog"
test_out = []
assert sorted(test_out) == sorted(find_ladders(test_begin, test_end, test))

test = ["hot", "dot", "dog", "lot", "log", "cog", "mog"]
test_begin = "hit"
test_end = "cog"
test_out = [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]]
assert sorted(test_out) == sorted(find_ladders(test_begin, test_end, test))

test = ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]
test_begin = "red"
test_end = "tax"
test_out = [["red", "ted", "tad", "tax"], ["red", "ted", "tex", "tax"], ["red", "rex", "tex", "tax"]]
assert sorted(test_out) == sorted(find_ladders(test_begin, test_end, test))

test = ["lest", "leet", "lose", "code", "lode", "robe", "lost"]
test_begin = "leet"
test_end = "code"
test_out = [["leet", "lest", "lost", "lose", "lode", "code"]]
assert sorted(test_out) == sorted(find_ladders(test_begin, test_end, test))

test = [
    "kid", "tag", "pup", "ail", "tun", "woo", "erg", "luz", "brr", "gay", "sip", "kay", "per", "val", "mes", "ohs",
    "now", "boa", "cet", "pal", "bar", "die", "war", "hay", "eco", "pub", "lob", "rue", "fry", "lit", "rex", "jan",
    "cot", "bid", "ali", "pay", "col", "gum", "ger", "row", "won", "dan", "rum", "fad", "tut", "sag", "yip", "sui",
    "ark", "has", "zip", "fez", "own", "ump", "dis", "ads", "max", "jaw", "out", "btu", "ana", "gap", "cry", "led",
    "abe", "box", "ore", "pig", "fie", "toy", "fat", "cal", "lie", "noh", "sew", "ono", "tam", "flu", "mgm", "ply",
    "awe", "pry", "tit", "tie", "yet", "too", "tax", "jim", "san", "pan", "map", "ski", "ova", "wed", "non", "wac",
    "nut", "why", "bye", "lye", "oct", "old", "fin", "feb", "chi", "sap", "owl", "log", "tod", "dot", "bow", "fob",
    "for", "joe", "ivy", "fan", "age", "fax", "hip", "jib", "mel", "hus", "sob", "ifs", "tab", "ara", "dab", "jag",
    "jar", "arm", "lot", "tom", "sax", "tex", "yum", "pei", "wen", "wry", "ire", "irk", "far", "mew", "wit", "doe",
    "gas", "rte", "ian", "pot", "ask", "wag", "hag", "amy", "nag", "ron", "soy", "gin", "don", "tug", "fay", "vic",
    "boo", "nam", "ave", "buy", "sop", "but", "orb", "fen", "paw", "his", "sub", "bob", "yea", "oft", "inn", "rod",
    "yam", "pew", "web", "hod", "hun", "gyp", "wei", "wis", "rob", "gad", "pie", "mon", "dog", "bib", "rub", "ere",
    "dig", "era", "cat", "fox", "bee", "mod", "day", "apr", "vie", "nev", "jam", "pam", "new", "aye", "ani", "and",
    "ibm", "yap", "can", "pyx", "tar", "kin", "fog", "hum", "pip", "cup", "dye", "lyx", "jog", "nun", "par", "wan",
    "fey", "bus", "oak", "bad", "ats", "set", "qom", "vat", "eat", "pus", "rev", "axe", "ion", "six", "ila", "lao",
    "mom", "mas", "pro", "few", "opt", "poe", "art", "ash", "oar", "cap", "lop", "may", "shy", "rid", "bat", "sum",
    "rim", "fee", "bmw", "sky", "maj", "hue", "thy", "ava", "rap", "den", "fla", "auk", "cox", "ibo", "hey", "saw",
    "vim", "sec", "ltd", "you", "its", "tat", "dew", "eva", "tog", "ram", "let", "see", "zit", "maw", "nix", "ate",
    "gig", "rep", "owe", "ind", "hog", "eve", "sam", "zoo", "any", "dow", "cod", "bed", "vet", "ham", "sis", "hex",
    "via", "fir", "nod", "mao", "aug", "mum", "hoe", "bah", "hal", "keg", "hew", "zed", "tow", "gog", "ass", "dem",
    "who", "bet", "gos", "son", "ear", "spy", "kit", "boy", "due", "sen", "oaf", "mix", "hep", "fur", "ada", "bin",
    "nil", "mia", "ewe", "hit", "fix", "sad", "rib", "eye", "hop", "haw", "wax", "mid", "tad", "ken", "wad", "rye",
    "pap", "bog", "gut", "ito", "woe", "our", "ado", "sin", "mad", "ray", "hon", "roy", "dip", "hen", "iva", "lug",
    "asp", "hui", "yak", "bay", "poi", "yep", "bun", "try", "lad", "elm", "nat", "wyo", "gym", "dug", "toe", "dee",
    "wig", "sly", "rip", "geo", "cog", "pas", "zen", "odd", "nan", "lay", "pod", "fit", "hem", "joy", "bum", "rio",
    "yon", "dec", "leg", "put", "sue", "dim", "pet", "yaw", "nub", "bit", "bur", "sid", "sun", "oil", "red", "doc",
    "moe", "caw", "eel", "dix", "cub", "end", "gem", "off", "yew", "hug", "pop", "tub", "sgt", "lid", "pun", "ton",
    "sol", "din", "yup", "jab", "pea", "bug", "gag", "mil", "jig", "hub", "low", "did", "tin", "get", "gte", "sox",
    "lei", "mig", "fig", "lon", "use", "ban", "flo", "nov", "jut", "bag", "mir", "sty", "lap", "two", "ins", "con",
    "ant", "net", "tux", "ode", "stu", "mug", "cad", "nap", "gun", "fop", "tot", "sow", "sal", "sic", "ted", "wot",
    "del", "imp", "cob", "way", "ann", "tan", "mci", "job", "wet", "ism", "err", "him", "all", "pad", "hah", "hie",
    "aim",
]
test_begin = "cet"
test_end = "ism"
test_out = [
    ['cet', 'cot', 'con', 'ion', 'inn', 'ins', 'its', 'ito', 'ibo', 'ibm', 'ism'],
    ['cet', 'cat', 'can', 'ian', 'inn', 'ins', 'its', 'ito', 'ibo', 'ibm', 'ism'],
]
assert sorted(test_out) == sorted(find_ladders(test_begin, test_end, test))

test = ["hot", "dog"]
test_begin = "hot"
test_end = "dog"
test_out = []
assert sorted(test_out) == sorted(find_ladders(test_begin, test_end, test))
