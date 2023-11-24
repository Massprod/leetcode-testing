# Given an m x n board of characters and a list of strings words, return all words on the board.
# Each word must be constructed from letters of sequentially adjacent cells,
#  where adjacent cells are horizontally or vertically neighboring.
# The same letter cell may not be used more than once in a word.
# ----------------------
# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] is a lowercase English letter.
# 1 <= words.length <= 3 * 10 ** 4
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# All the strings of words are unique.


def find_words(board: list[list[str]], words: list[str]) -> list[str]:
    # working_sol (87.68%, 80.26%) -> (832ms, 18mb)  time: O((n * m) * (g * k)) | space: O(g + j)
    max_row: int = len(board)
    max_col: int = len(board[0])
    # All symbols we have in 'board', to cull some words from Trie.
    all_symbols: set[str] = set()
    for row_ in range(max_row):
        for col_ in range(max_col):
            all_symbols.add(board[row_][col_])
    out: list[str] = []
    # (symbol: next_node | end of the word with '*' mark)
    trie: dict[str, dict | str] = {}
    any_w: str = '*'
    for word in words:
        cur_node: dict[str, dict | str] = trie
        correct: bool = True
        # Symbol doesn't exist in the 'board' == word as well.
        for symbol in word:
            if symbol not in all_symbols:
                correct = False
        if correct:
            # 1 symbol words, no reasons to bother.
            if len(word) == 1:
                out.append(word)
                continue
            for symbol in word:
                if symbol not in cur_node:
                    cur_node[symbol] = {}
                cur_node = cur_node[symbol]
            cur_node[any_w] = word
    if not trie:
        return out
    options: list[tuple[int, int]] = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(cell: tuple[int, int], node: dict[str, dict | str]) -> None:
        # End of the word found.
        if any_w in node:
            out.append(node[any_w])
            node.pop(any_w)
            # Nothing more we can continue building from here.
            if not node:
                return
        # Mark as visited.
        restore: str = board[cell[0]][cell[1]]
        board[cell[0]][cell[1]] = ''
        for d_row, d_col in options:
            row: int = cell[0] + d_row
            col: int = cell[1] + d_col
            if 0 <= row < max_row and 0 <= col < max_col and board[row][col]:
                cur_sym: str = board[row][col]
                if cur_sym in node:
                    dfs((row, col), node[cur_sym])
                    # Everything found.
                    if not node[cur_sym]:
                        node.pop(cur_sym)
            # All we could build found, no reasons to check other sides.
            if not node:
                board[cell[0]][cell[1]] = restore
                return
        board[cell[0]][cell[1]] = restore

    for row_ in range(max_row):
        for col_ in range(max_col):
            # All words found.
            if not trie:
                break
            if board[row_][col_] in trie:
                dfs((row_, col_), trie[board[row_][col_]])
    return out


# Time complexity: O((n * m) * (g * k)) <- n - height of input matrix 'board', m - length of input matrix 'board' ,
#                                          k - avg len of words inside 'words', g - length of input array 'words'.
# Traversing whole square matrix to get all symbols => O(n * m).
# Checking every symbol in words to be present in matrix => O(g * k).
# Worst case all words will have correct symbols, so we will use them to build Trie => O(g * k).
# Worst case for DFS should be something like we have words == ['a*12'], and we only have 11'a' or something like this.
# We will start DFS from every cell in search almost whole Trie to fail.
# O((n * m) * (g * k))? Like we will search all symbols from input 'words' for every cell of input matrix 'board'.
# ----------------------
# Auxiliary space: O(g + j) <- j - maximum length of words from 'words'.
# Worst case every symbol in matrix is unique => 'all_symbols' will store O(n * m).
# ! words[i] consists of lowercase English letters.!
# Or we can call it constant O(26) and ignore, because there's only 26 symbols in ENG lowercase.
# And set() with 26 symbols is not a problem.
# Worst case for Trie actually the same, because we can have all words maximized for size ! 1 <= words[i].length <= 10 !
# and all of them will have unique symbol sequence, so => O(g * 10) | O(g)?
# Because DFS calls is limited by maximum words length, and we're not creating anything new except inside constants.
# Should be correct to say => O(g + j).
# ----------------------
# Trie + DFS should be ok, but we need to maintain all the words we can find in the Trie.
# Store extra set() with all words we can build from current TrieNode and delete after we find it?
# Should be correct, but I don't need to use class for TrieNode. Cuz it's going to be slow as before.
# And it's better to stick with simple dict.


test: list[list[str]] = [
    ["o", "a", "a", "n"], ["e", "t", "a", "e"],
    ["i", "h", "k", "r"], ["i", "f", "l", "v"]
]
test_words: list[str] = ["oath", "pea", "eat", "rain"]
test_out: list[str] = ["eat", "oath"]
assert sorted(test_out) == sorted(find_words(test, test_words))

test = [["a", "b"], ["c", "d"]]
test_words = ["abcb"]
test_out = []
assert sorted(test_out) == sorted(find_words(test, test_words))

test = [
    ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a"], ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
    ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a"], ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
    ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a"], ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
    ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a"], ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
    ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a"], ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
]
test_words = []
t_word: str = ''
for limit in range(10, 0, -1):
    for _ in range(limit):
        t_word += 'a'
    test_words.append(t_word)
    t_word = ''
assert sorted(test_words) == sorted(find_words(test, test_words))
