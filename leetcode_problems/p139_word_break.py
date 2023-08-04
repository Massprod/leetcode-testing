# Given a string s and a dictionary of strings wordDict, return true if s can be segmented
#   into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
# -----------------------------
# 1 <= s.length <= 300  ,  1 <= wordDict.length <= 1000  ,  1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.


def word_break(s: str, wordDict: list[str]) -> bool:
    # working_sol (94.45%, 18.55%) -> (35ms, 16.6mb)  time: O(n) | space: O(m + n)
    # If some symbol in 's' isn't present in any word from wordDict,
    # there's no reasons to try.
    # Saving all symbols from all words.
    all_symbols: set[str] = set()
    for word in wordDict:
        for symbol in word:
            if symbol not in all_symbols:
                all_symbols.add(symbol)
    # Check every symbol of 's' to be presented.
    for symbol in s:
        # If there's some symbol which isn't presented in all words
        # we can't create correct sequence at all.
        if symbol not in all_symbols:
            return False
    # For faste access, we need to rebuild input_list into
    # set()|dict() with O(1) search.
    all_words: set[str] = set(wordDict)
    # Current sequence of words.
    path: list[str] = []
    # To cull some calls, we can use max_len ->
    # -> which is maximum length from all the words.
    # There's no reasons to create anything higher,
    # cuz no words with such length we can use.
    max_len: int = 0
    for _ in all_words:
        max_len = max(max_len, len(_))
    # Actually recursion cache, just saving all calls.
    failed: dict[int] = {}

    def check_start(start: int):
        # If cached, we can't build correct sequence.
        if start in failed.keys() and failed[start] is False:
            return False
        # Insta return if correct sequence.
        if len("".join(path)) == len(s):
            return True
        # Current call word.
        to_check: str = ""
        for y in range(start, len(s)):
            # If exceeds max_len we can't use it.
            if len(to_check) > max_len:
                failed[start] = False
                return False
            to_check += s[y]
            # If such word present, we can try to use it.
            if to_check in all_words:
                # Path is storing all words for current sequence.
                path.append(to_check)
                if check_start(y + 1):
                    return True
                # Failed -> delete.
                path.pop()
        # Cache.
        failed[start] = False
        return False

    return check_start(0)


# Time complexity: O(n) -> creating set() with all available symbols in input_dict => O(j * g) ->
# n - len of input_string^^| -> checking every symbol in input_string to be available in input_dict => O(n) ->
# m - len of input_dict^^  | -> creating set of input_dict => O(m) -> getting max_len from all_word => O(m) ->
# g - lens of words in input_dict^^| -> recursion to check every index of input_string => O(n) ->
# j - number of words in input_dict^^| -> O((j * g) + n + m + n) -> O(2n) -> O(n)
# Auxiliary space: O(m + n) -> creating set() with all available symbols in input_dict => O(j * g) ->
#                          -> set() with all_words from input_dict => O(m) -> creating path with all words used =>
#                          => contains words of input_string, with correct path summarized length of these
#                             always equal to n => O(n) -> dictionary with failed start_indexes => worst case
#                             we're going to start from every index from 0 to n - 2, and n - 1 index isn't solvable =>
#                          => O(n - 2) -> O((j * g) + m + n + (n - 2)) -> O(2m + 2n) -> O(m + n)
#                                             ^^all words lengths summarized will leave us with m
# -----------------------------
# Made a fully working but slow solution from a start, and made some speed with breaking options with extra_length,
# and options where's dictionary didn't have all SYMBOLS to make a correct string.
# But what I failed the most important culling part with ignoring paths we already started
# and failed to create correct sequence of words on its path. This part I added only after googling, which is bad.
# But it's still only 20% of solution added to mine.
# !
# Still not good, because I was capable of finding it on my own, better not give up such easily.
# On other hand sitting for hours with 80% working not good either.
# So, for a future use -> try to remember path you already collected and watch for a part which left,
#                         maybe it's better to hold this part not path. !
# -----------------------------
# Ok. Made fully working solution by myself, but failed to see what we need to Remember.
# I was trying to think about how we can remember already used PATH, but after googling a little, found
# that we can just remember PART of a string we didn't complete, and this part is unique.
# If we remember it, we can ignore any cases when we encounter such left PART.
# -----------------------------
# Obviously not enough. How can I scroll it differently? From the highest size word in dict will lead to same problem,
# with repeating same words. Can we destroy original string and recreate it?
# -----------------------------
# Ok. It's working correct but how can I cull some calls?
# Hmm. Don't see how we can cull double calls, because we're allowed to reuse words.
# So we need to re_check same length values on every call, otherwise we're going to miss values.
# Only way I see for now, is same as we did with matrix_word_search -> just check if dict is correct from a start.
# Like check every word in dict to be present in S. No matter if it's correct len and will be used.
# -----------------------------
# Seems working and I don't  see any tricky parts with constraints, so let's try to commit.
# -----------------------------
# Left to right walk with sample_string, which are we increasing for a 1 sign and checking to be present?


test: str = "leetcode"
test_dict: list[str] = ["leet", "code"]
test_out: bool = True
assert test_out == word_break(test, test_dict)

test = "applepenapple"
test_dict = ["apple", "pen"]
test_out = True
assert test_out == word_break(test, test_dict)

test = "catsandog"
test_dict = ["cats", "dog", "sand", "and", "cat"]
test_out = False
assert test_out == word_break(test, test_dict)

# test4 - failed -> I was stupid enough to forget about PATH that we need to clear
#                   element's after returning False, and bad part that I was thinking about that from a start,
#                   but just forgot most import part of the path.
test = "aaaaaaa"
test_dict = ["aaaa", "aaa"]
test_out = True
assert test_out == word_break(test, test_dict)

test = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
test_dict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
test_out = False
assert test_out == word_break(test, test_dict)

test = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaa" \
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
        "aaaaaaaaaaaaa"
test_dict = ["aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa", "ba"]
test_out = False
assert test_out == word_break(test, test_dict)
