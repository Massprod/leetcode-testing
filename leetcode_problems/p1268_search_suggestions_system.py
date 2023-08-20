# You are given an array of strings products and a string searchWord.
# Design a system that suggests at most three product names from products
#   after each character of searchWord is typed. Suggested products should have common prefix with searchWord.
# If there are more than three products with a common prefix return the three lexicographically minimums products.
# Return a list of lists of the suggested products after each character of searchWord is typed.
# ------------------------
# 1 <= products.length <= 1000
# 1 <= products[i].length <= 3000
# 1 <= sum(products[i].length) <= 2 * 10 ** 4
# All the strings of products are unique.
# products[i] consists of lowercase English letters.
# 1 <= searchWord.length <= 1000
# searchWord consists of lowercase English letters.


class TrieNode:

    def __init__(self):
        self.child: dict[str, TrieNode] = {}
        self.all_paths: list[str] = []


def suggestedProducts(products: list[str], searchWord: str) -> list[list[str]]:
    # working_sol (56.58%, 36.19%) -> (158ms, 23.7mb)  time: O(m * n + n * log n) | space: O(m * n + log n)
    # Creating Trie with all symbols.
    # And for every Node store words from which its build.
    # Cuz if we need to find what Words can be built from some symbol,
    # we can always use Words we used to build this symbol.
    root: TrieNode = TrieNode()
    for product in products:
        node: TrieNode = root
        for symbol in product:
            if symbol in node.child:
                node = node.child[symbol]
                node.all_paths.append(product)
            else:
                node.child[symbol] = TrieNode()
                node = node.child[symbol]
                node.all_paths.append(product)
        node.word_end = True
    # All suggestions, by letters in searchWord.
    suggested: list[list[str]] = []
    last_opener: TrieNode = root

    for y in range(len(searchWord)):
        cur_sym: str = searchWord[y]
        # If symbol present, then we can go deeper
        # and search for others.
        if cur_sym in last_opener.child:
            last_opener = last_opener.child[cur_sym]
            # We need -> ! lexicographically minimums products !
            # So we need to sort, and take only 3 words,
            # for whom this symbol leads.
            suggested.append(sorted(last_opener.all_paths)[:3])
        else:
            # If isn't, we can break and there's no Suggestions possible later.
            for g in range(y, len(searchWord)):
                suggested.append([])
            break
    return suggested


# Time complexity: O( ) -> creating Trie tree with all products stored => O(m * n) -> for every symbol in searchWord
# m - len of one product in products^^| trying to find it in dictionary, if it's present sort and append products ->
# n - len of products_array^^| -> dunno how to calc number of products per symbol correctly => O(k * log k) ->
# k - num of products with some symbol^^| -> but we need to sort it, and it's length is always different ->
#                             -> actually K is always some part of n isn't it? Then can we say O(n * log n) ->
#                             -> cuz every word can start from same first symbol, then it's whole products sorted,
#                             at least for the first node => O(m * n + n * log n)
# Auxiliary space: O(m * n + log n) -> guess, worst case is that all words in products are unique and doesn't have same
#                           symbols, then we will store every symbol of every word in products => O(m * n) ->
#                           -> sorting in_place and storing correct words in suggested ->
#                           -> guess, worst case with it == every string being the same, then n added?
#                           ! All the strings of products are unique. ! <- Incorrect.
#                           Then what can be the worst case here? Dunno, with non_uniques is like w.e?
#                           Can be one symbol with 1 word, or 10 symbols with 10 words for every.
#                           But pretty sure that's always going to be part of input_products, can we say => O(log n)?
# ------------------------
# All correct but slow, cuz I'm rechecking every word from 0 to last symbol everytime.
# How to cull it and start searching from last symbol?
# OK. Now we start searching from last_symbol node. Still slow AF.
# OK. We can just store ALL words we can build from any symbol into the Node. Because it's one some point Node will
# lead to this word, so if we start from this Node we can be 100% sure it's one of the stored words in the End.
# But still slow only 32%. Can I use dictionary? LIke in previous task with Trie, I just stored symbols,
# which actually Used to build from and others is ignored. Actually remove ord() and just check for a symbol?
# Ok. All working, nice progress from 1300ms -> 155ms.
# Looked for best_performances, and they're just slicing prefix and search in sorted array for other half.
# Which is actually simplier, but I guess this task should be about training with Trie.
# And for the second Trie task in life its good practice.
# ------------------------
# Create Trie, add everything from products into it and search like before.
# Only difference is that we need only 3 words and most important is ! lexicographically minimums products ! ->
# -> so for every step we need to choose minimum ORD symbol.
# Well I was using dictionary before to get some sped, and if we need Lexico order I can just use list
# with all symbol ords from either 'a' -> 'z' or 'z' -> to 'a', (122 - ord(sym)) and start search from end.
# It will always give me the lowest ORD and move from it deeper.
# Should be correct. But we need to add everything before which is kinda slow, but it's fine for second Trie task.


test: list[str] = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
test_word: str = "mouse"
test_out: list[list[str]] = [["mobile", "moneypot", "monitor"], ["mobile", "moneypot", "monitor"],
                             ["mouse", "mousepad"], ["mouse", "mousepad"], ["mouse", "mousepad"]]
assert test_out == suggestedProducts(test, test_word)

test = ["havana"]
test_word = "havana"
test_out = [["havana"], ["havana"], ["havana"], ["havana"], ["havana"], ["havana"]]
assert test_out == suggestedProducts(test, test_word)
