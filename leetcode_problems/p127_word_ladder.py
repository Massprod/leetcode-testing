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
    # working_sol (57.93%, 7.98%) -> (158ms, 22mb)  time: O(m * (m * g)) | space: O((log(m * g) + (log m)) + m)
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

    def backtrack(path: list[str], node: str):
        path = path + [node]
        # beginWord leads nowhere so it's always value of None
        if graph[node] is None:  # list slicing creates new list, no reasons to copy.
            return len(path)
        # endWord = [node1, node2] both nodes can lead to beginWord,
        # node1 = [node3, node5] , node5 = [beginWord]
        # we're just taking them one by one until we hit beginWord.
        for next_node in graph[node]:
            return backtrack(path, next_node)

    if endWord in graph:
        return backtrack([], endWord)
    return 0


# Time complexity: O(m * (m * g)) -> creating all_prefix_options, looping for every symbol in every node => O(m * g) ->
# g - len of beginWord^^| -> in the worst case every word in wordList will be like: 1 -> 2 -> 3 -> 4 etc -> endWord
# m - len of wordList^^|  so we're having to check every word in wordList and for every word we're checking
#                         all it's symbols to decide if we can use it as correct node or not => O(m * (m * g)) ->
#                         -> if we found correct path leading to a endWord we're doing backtracking to find
#                         all possible path from it to beginWord, in the case if every word was used, on diff paths =>
#                         => O(m) or O(log m), if only part of the wordList used ->
#                         -> O(m * g) + O(m * (m * g)) + O(m) => O(m * (m * g)).
#                            ^^Exactly the same as p126, except we're breaking from backtracking on 1 path.
# Auxiliary space: O((log(m * g) + (log m)) + m) -> creating dictionary with keys: log(m * g), values: (log m) =>
#                       => O(log(m * g) + (log m))
#                          because there's cases like h*t(hit) <-> h*t(hot) they will be added in the same key ->
#                       -> creating graph(dictionary) with size of m, if we assume worst case is that
#                          we're using all words in wordList, so graph is holding all pairs from beginWord to
#                          endWord and number of pairs is equal to words in wordList => O(m) ->
#                       -> creating dictionary to store all nodes on current level which can be used to go deeper =>
#                       => O(log m) -> backtracking from endWord to beginWord in created graph, we're not going
#                          to store any of the paths, but recursion will still have a stack with size of m or log m =>
#                       => O(m) or O(log m) if we're only using part of wordList ->
#                       -> O((log(m * g) + (log m)) + O(m) + O(log m) + O(m) =>
#                       => O((log(m * g) + (log m)) + O(m)).
#                            ^^Exactly the same as p126, except we're breaking from backtracking on 1 path,
#                              and not storing any paths.
# ------------------------
# Same solution as p126, just returning length instead of paths.
# BFS(BreadthFirstSearch) always giving as shortest path. No need to extra checks.


test1 = ["hot", "dot", "dog", "lot", "log", "cog"]
test1_begin = "hit"
test1_end = "cog"
test1_out = 5
assert test1_out == ladder_length(test1_begin, test1_end, test1)

test2 = ["hot", "dot", "dog", "lot", "log"]
test2_begin = "hit"
test2_end = "cog"
test2_out = 0
assert test2_out == ladder_length(test2_begin, test2_end, test2)
