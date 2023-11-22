# Design a data structure that supports adding new words
#  and finding if a string matches any previously added string.
# Implement the WordDictionary class:
#   - WordDictionary() Initializes the object.
#   - void addWord(word) Adds word to the data structure, it can be matched later.
#   - bool search(word) Returns true if there is any string in the data structure
#     that matches word or false otherwise.
#     word may contain dots '.' where dots can be matched with any letter.
# -------------------
# 1 <= word.length <= 25
# word in addWord consists of lowercase English letters.
# word in search consist of '.' or lowercase English letters.
# There will be at most 2 dots in word for search queries.
# At most 10 ** 4 calls will be made to addWord and search.


class WordDictionary:
    # working_sol (92.77%, 92.8%) -> (1262ms, 58mb)

    def __init__(self):
        # It's x2 faster to just use dictionary, instead of separate Class for Trie.
        self.root: dict[str, dict | bool] = {'end': False}

    def addWord(self, word: str) -> None:
        node: dict[str, dict | bool] = self.root
        for sym in word:
            if sym not in node:
                node[sym] = {'end': False}
            node = node[sym]
        node['end'] = True

    def search(self, word: str) -> bool:

        def dfs(index: int, cur_node: dict[str, dict | bool]):
            if index == len(word):
                return cur_node['end']
            if word[index] != '.':
                if word[index] in cur_node:
                    return dfs(index + 1, cur_node[word[index]])
                return False
            else:
                # Wildcard == check everything except 'end'.
                # Because we still have symbols to check, and we don't care about other words ending here.
                for sym in cur_node:
                    if sym != 'end' and dfs(index + 1, cur_node[sym]):
                        return True
                return False

        return dfs(0, self.root)


# Time complexity:
#   initiation: O(1).
#   addWord: O(n) -> adding every symbol in dictionary(Trie) => O(n).
#       n - len of input 'word'^^|
#   search: O(m) -> worst case == ['a.bcdefg.j'] but max sized for 25 + all words added was like:'a*bcdefg*z'(* == any)
#       m - all symbols of currently added unique words^^| so, we will visit every symbol we added into a Trie.
# Auxiliary space:
#   class object: O(m)
#   search: O(n) -> w.e the case we will always have only 'n' recursion calls, for every index of 'word' => O(n).
