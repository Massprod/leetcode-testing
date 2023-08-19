# A trie (pronounced as "try") or prefix tree is a tree data structure
#   used to efficiently store and retrieve keys in a dataset of strings.
# There are various applications of this data structure, such as autocomplete and spellchecker.
# Implement the Trie class:
#   Trie() Initializes the trie object.
#   void insert(String word) Inserts the string word into the trie.
#   boolean search(String word) Returns true if the string word is in the trie
#     (i.e., was inserted before), and false otherwise.
#   boolean startsWith(String prefix) Returns true if there is a previously inserted string word
#     that has the prefix 'prefix', and false otherwise.
# -----------------
# 1 <= word.length, prefix.length <= 2000
# word and prefix consist only of lowercase English letters.
# At most 3 * 10 ** 4 calls in total will be made to insert, search, and startsWith.


class TrieNode:

    def __init__(self):
        self.child: dict[str: TrieNode] = {'end': False}


class Trie:
    # working_sol (74.74%, 19.6%) -> (155ms, 34.9mb)

    def __init__(self):
        self.root: TrieNode = TrieNode()

    def insert(self, word: str) -> None:
        # Store every symbol in nodes,
        # and mark end of the word.
        node: TrieNode = self.root
        for sym in word:
            if sym in node.child:
                node = node.child[sym]
            else:
                node.child[sym] = TrieNode()
                node = node.child[sym]
        node.child['end'] = True

    def search(self, word: str) -> bool:
        # Go deeper for every symbol if it's present,
        # otherwise there's no such word and symbol.
        search_node: TrieNode = self.root
        for sym in word:
            if sym in search_node.child:
                search_node = search_node.child[sym]
            else:
                return False
        return search_node.child['end']

    def startsWith(self, prefix: str) -> bool:
        # Same as search, but we don't need it's to be.
        # 'end' <- whole word. We only need some part of it,
        # and if part is present we can return True.
        search_node: TrieNode = self.root
        for sym in prefix:
            if sym in search_node.child:
                search_node = search_node.child[sym]
            else:
                return False
        return True


# Time complexity:
#   insert: O(n) -> store every symbol one by one in nodes => O(n).
#   search: O(n) -> search every symbol one by one in stored nodes => O(n).
#   startsWith: O(n) -> same as search, but we're not searching for the 'end' => O(n).
#   n - len of input word|prefix^^|
# Auxiliary space:
#   insert: O(n) -> store every symbol into a dictionary as a new Node, if it's not presented already => O(n).
#   search: O(1) -> only using existing nodes => O(1).
#   startsWith: O(1) -> only using existing nodes => O(1).
# -----------------
# First encounter with Trie -> ! https://www.geeksforgeeks.org/trie-insert-and-search/ !
# And we don't need to use list with all alphabet, cuz we can store them in dictionary and search by this.
