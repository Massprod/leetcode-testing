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
from itertools import product
from collections import defaultdict


def find_ladders(beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
    if endWord not in wordList:
        return []
    pairs2: dict[str, list[str]] = defaultdict(list)
    for hm in wordList:
        for j in range(len(hm)):
            bucket: str = f"{hm[:j]}[]{hm[j + 1:]}"
            pairs2[bucket].append(hm)
    pairs: dict[str, set[str]] = defaultdict(set)
    for bucket, neighbours in pairs2.items():
        for word11, word22 in product(neighbours, repeat=2):
            if word11 != word22:
                pairs[word11].add(word22)
                pairs[word22].add(word11)

    def single_diff(word1: str, word2: str) -> bool:
        if word1 in pairs:
            if word2 in pairs[word1]:
                return True
        if word2 in pairs:
            if word1 in pairs[word2]:
                return True
        return False

    def ladder_search(path: list[str]) -> None | bool:
        if min_length[-1] - 1 < len(path):
            path.append(endWord)
            for g in range(1, len(path) - 1):
                if path[g] not in correct_parts:
                    correct_parts[path[g]] = [path[g + 1:]]
                else:
                    correct_parts[path[g]].append(path[g + 1:])
            path.pop()
            return False
        if single_diff(path[-1], endWord):
            path.append(endWord)
            path_length: int = len(path)
            if min_length[-1] > path_length:
                min_length[-1] = path_length
                copy: list[str] = path.copy()
                correct_paths.clear()
                correct_paths.append(copy)
                for g in range(1, len(path) - 1):
                    if path[g] not in correct_parts:
                        correct_parts[path[g]] = [path[g + 1:]]
                    else:
                        correct_parts[path[g]].append(path[g + 1:])
                path.pop()
                return
            elif min_length[-1] == path_length:
                correct_paths.append(path.copy())
                path.pop()
                return
            elif min_length[-1] < path_length:
                path.pop()
                return
        for y in range(len(wordList)):
            word: str = wordList[y]
            if (word != endWord) and (word not in used) and single_diff(path[-1], word):
                if word in correct_parts:
                    for _ in correct_parts[word]:
                        correct_path2: list[str] = path + [word] + _
                        correct_length2: int = len(correct_path2)
                        if correct_length2 < min_length[-1]:
                            min_length[-1] = len(correct_path2)
                            correct_paths.clear()
                            correct_paths.append(correct_path2)
                        elif correct_length2 == min_length[-1]:
                            correct_paths.append(correct_path2)
                    continue
                used.add(word)
                path.append(word)
                ladder_search(path)
                path.pop()
                used.remove(word)

    if single_diff(beginWord, endWord):
        return [[beginWord, endWord]]
    correct_parts: dict[str, list[list[str]]] = {}
    used: set[str] = set()
    min_length: list[int] = [len(wordList)]
    correct_paths: list[list[str]] = []
    for x in range(len(wordList)):
        check: str = wordList[x]
        if (check != endWord) and single_diff(beginWord, check):
            if check in correct_parts:
                for _ in correct_parts[check]:
                    correct_path: list[str] = [beginWord, check] + _
                    correct_length: int = len(correct_path)
                    if correct_length < min_length[-1]:
                        min_length[-1] = len(correct_path)
                        correct_paths.clear()
                        correct_paths.append(correct_path)
                    elif correct_length == min_length[-1]:
                        correct_paths.append(correct_path)
                continue
            used.add(check)
            used.add(beginWord)
            ladder_search([beginWord, check])
            used.clear()
    return correct_paths


# Don't see what im missing, but I need to cull recursion checks, but how?
# -------------------
# Added remembering of already travelled paths, so now if we're going to check first word in
# sequence, and it's already been used in recursion, we will reuse built paths.
# But it's not enough and I need to cull recursion calls.
# -------------------
# Working but hits TimeLimit.
# -------------------
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
print(find_ladders(test2_begin, test2_end, test2))

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
