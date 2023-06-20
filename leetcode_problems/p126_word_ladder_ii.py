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
from collections import deque, defaultdict


def find_ladders(beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
    # semigoogled_solution (84.23%, 43.8%) -> (59ms, 17ms)  time: O(m * (m * g)) | space: O(log(m * g) + m)
    all_prefix_options: dict[str, list[str]] = defaultdict(list)
    for word in wordList:
        for x in range(len(word)):
            # adding every option which differs by 1 symbol
            option: str = f"{word[:x]}*{word[x + 1:]}"
            all_prefix_options[option].append(word)
    # creating graph to store nodes
    graph: dict[str, list[str]] = {beginWord: None}
    # que with nodes to start search from
    que: deque = deque([beginWord])
    # BFS -> first time we find endWord its shortest path to it, so we're breaking search
    end: bool = False
    while que and not end:
        # correct pairs of node we can go from and to, node1 <-> node2 both differs by 1 symbol
        correct_graph: dict[str, list[str]] = defaultdict(list)
        # to check every node in a que, que is changing, and we can't use just ! _ in que !
        # que is holding every node(word) on current level
        for _ in range(len(que)):
            word: str = que.popleft()
            for y in range(len(word)):
                # same approach to find word which differs by 1 symbol
                for option in all_prefix_options[f"{word[:y]}*{word[y + 1:]}"]:
                    if option == endWord:
                        end = True
                    if option not in graph:
                        # we can continue search from this node(word), adding into que
                        if option not in correct_graph:
                            correct_graph[option] = [word]
                            que.append(option)
                            continue
                        # ignore if we already started from this node(word)
                        correct_graph[option].append(word)
        # update/add correct pairs of nodes
        graph.update(correct_graph)
    paths: list[list[str]] = []

    def backtrack(path: list[str], node: str):
        path = path + [node]
        # beginWord leads nowhere so it's always value of None
        if graph[node] is None:
            paths.append(path[::-1])  # list slicing creates new list, no reasons to copy.
            return
        # endWord = [node1, node2] both nodes can lead to beginWord,
        # node1 = [node3, node5] , node5 = [beginWord]
        # we're just taking them one by one until we hit beginWord.
        for next_node in graph[node]:
            backtrack(path, next_node)
    if endWord in graph:
        backtrack([], endWord)
        return paths
    return []


# Time complexity: O(m * (m * g)) -> creating all_prefix_options, looping for every symbol in every node => O(m * g) ->
# m - len of wordList^^|  -> in the worst case every word in wordList will be like: 1 -> 2 -> 3 -> 4 etc -> endWord
# g - len of beginWord^^| so we're having to check every word in wordList and for every word we're checking
#                         all it's symbols to decide if we can use it as correct node or not => O(m * (m * g)) ->
#                         -> if we found correct path leading to a endWord we're doing backtracking to find
#                         all possible path from it to beginWord, in the case if every word was used =>
#                         => O(m) or O(log m), if only part of the words used -> O(m * g) + O(m * (m * g)) + O(m) =>
#                         => O(m * (m * g)).
# Auxiliary space: O(log(m * g) + m) -> creating dictionary with keys: log(m * g), values: log(m) => O(log(m * g))
#                          because there's cases like h*t(hit) <-> h*t(hot) they will be added in the same key ->
#                       -> creating graph(dictionary) with size of m, if we assume worst case is that
#                          we're using all words in wordList, so graph is holding all pairs from beginWord to
#                          endWord and number of pairs is equal to words in wordList => O(m) ->
#                       -> creating dictionary to store all nodes on current level which can be used to go deeper =>
#                       => O(log m) -> backtracking from endWord to beginWord in created graph, for every correct
#                          path leading to a beginWord adding this path into paths, in assumed case it's going to
#                          have only one path but with size of m => O(m), if there's multiple paths than only part
#                          of wordList can be used => O(log m) ->
#                       -> O(log(m * g)) + O(m) + O(log m) + O(m) => O(log(m * g) + m).
# -------------------
# Flow:
#  using defaultdict() to avoid key_errors and extra checks ->
# -> creating dictionary with all_prefix_options (every word with only 1 symbol changed):
#   *it, h*t, hi*, etc. - allowing us to add every other word with same pattern as one_symbol diff pairs ->
# -> we're using BFS to search correct path in all nodes from node==beginWord to node==endWord, for this
#   creating standard graph as dictionary with every node(word), and it's correct pair(one symbol diff word) ->
# -> holding every node we can start search in a que, ignoring one we already checked, starting from beginWord ->
# -> for every node(word) in a que, checking if it's correct option (differs by 1 symbol) go to, if it's correct,
#   and we didn't start from it adding into a que and correct_graph, otherwise only correct_graph ->
# -> repeating search for every node on level, going deeper until we hit node==endWord, breaking on it =>
# => after all of that, we're having all nodes(words) pairs in graph which hold what nodes can be connected between
#   and we can backtrack from endWord to beginWord using this graph ->
# -> creating new path with all nodes from endWord to beginWord if endWord present in graph, otherwise
#   there's no endWord in it and we can't find any path to it.
# -------------------
# Unsolvable without BFS(BreadthFirstSearch) -> https://bradfieldcs.com/algos/graphs/word-ladder/
# As always HARD task which can't be solved if you're not aware of a method.


test1 = ["hot", "dot", "dog", "lot", "log", "cog"]
test1_begin = "hit"
test1_end = "cog"
test1_out = [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]]
print(find_ladders(test1_begin, test1_end, test1))
assert test1_out == find_ladders(test1_begin, test1_end, test1)

test2 = ["hot", "dot", "dog", "lot", "log"]
test2_begin = "hit"
test2_end = "cog"
test2_out = []
print(find_ladders(test2_begin, test2_end, test2))
assert test2_out == find_ladders(test2_begin, test2_end, test2)

test3 = ["hot", "dot", "dog", "lot", "log", "cog", "mog"]
test3_begin = "hit"
test3_end = "cog"
test3_out = [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]]
print(find_ladders(test3_begin, test3_end, test3))
assert test3_out == find_ladders(test3_begin, test3_end, test3)

# test4 - Failed -> I was trying to speed things up and assumed that we can ignore double checks,
#                   but we can't ignore double checks inside a recursion, because it gives us different paths.
test4 = ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]
test4_begin = "red"
test4_end = "tax"
test4_out = [["red", "ted", "tad", "tax"], ["red", "ted", "tex", "tax"], ["red", "rex", "tex", "tax"]]
print(find_ladders(test4_begin, test4_end, test4))
assert test4_out == find_ladders(test4_begin, test4_end, test4)

# test5 - Failed -> I was incorrect on checking 2 words, focused on recursion too much,
#                   and I can actually use sets(), because we're checking every index anyway.
test5 = ["lest", "leet", "lose", "code", "lode", "robe", "lost"]
test5_begin = "leet"
test5_end = "code"
test5_out = [["leet", "lest", "lost", "lose", "lode", "code"]]
print(find_ladders(test5_begin, test5_end, test5))
assert test5_out == find_ladders(test5_begin, test5_end, test5)

test6 = ["kid", "tag", "pup", "ail", "tun", "woo", "erg", "luz", "brr", "gay", "sip", "kay", "per", "val", "mes", "ohs",
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
         "aim"]
test6_begin = "cet"
test6_end = "ism"
print(find_ladders(test6_begin, test6_end, test6))
test6_out = [['cet', 'cot', 'con', 'ion', 'inn', 'ins', 'its', 'ito', 'ibo', 'ibm', 'ism'],
             ['cet', 'cat', 'can', 'ian', 'inn', 'ins', 'its', 'ito', 'ibo', 'ibm', 'ism']
             ]
assert test6_out == find_ladders(test6_begin, test6_end, test6)

test7 = ["hot", "dog"]
test7_begin = "hot"
test7_end = "dog"
test7_out = []
print(find_ladders(test7_begin, test7_end, test7))
assert test7_out == find_ladders(test7_begin, test7_end, test7)
