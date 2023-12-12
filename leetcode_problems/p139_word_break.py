# Given a string s and a dictionary of strings wordDict,
#  return true if s can be segmented
#  into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
# -----------------------------
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.


def word_break(s: str, wordDict: list[str]) -> bool:
    # working_sol (94.45%, 45.61%) -> (35ms, 16.5mb)  time: O(k * m + n * j) | space: O(k * m + n)
    # If some symbol from 's' isn't present in any word from `wordDict`,
    #  there's no reasons to try breaking it.
    # Saving all symbols from all words.
    all_symbols: set[str] = set()
    for word in wordDict:
        for symbol in word:
            if symbol not in all_symbols:
                all_symbols.add(symbol)
    # Check every symbol of `s` to be present.
    for symbol in s:
        if symbol not in all_symbols:
            return False
    # For faster checks, we need to rebuild `wordDict` into set()|dict().
    all_words: set[str] = set(wordDict)
    # Current sequence of words.
    path: list[str] = []
    # To cull some calls, we can use max_len ->
    #  -> which is maximum length from all the words.
    # There's no reasons to check anything higher,
    #  because no words with such length present in `wordDict`.
    max_len: int = 0
    for word in all_words:
        max_len = max(max_len, len(word))
    # Recursion cache.
    failed: dict[int, bool] = {}

    def check_start(start: int) -> bool:
        if start in failed:
            return False
        # Correct path.
        if len(''.join(path)) == len(s):
            return True
        cur_word: str = ''
        for index in range(start, len(s)):
            # If exceeds max_len we can't use it, and higher ones.
            if len(cur_word) > max_len:
                break
            cur_word += s[index]
            if cur_word in all_words:
                path.append(cur_word)
                if check_start(index + 1):
                    return True
                # Last word in sequence(path) Failed -> delete.
                path.pop()
        failed[start] = False
        return False

    return check_start(0)


# Time complexity: O(k * m + n * j) <- n - length of input string `s`,
#                                      j - maximum length of words from `wordDict`,
#                                      k - avg length of words in `wordDict`,
#                                      m - number of words in `wordDict`.
# Creating set `all_symbols` => O(k * m).
# Check every symbol in `s` to be present in given words => O(n).
# Creating set with all words from `wordDict`, because we're given list by default => O(k * m).
# Finding maximum size of word we can create => O(m).
# Recursion with memorization of every call, and we're making calls on every index of `s`.
# Worst case == s = 'a*19 + b', wordDict = ['a', 'aa' ... 'a * 19 + b'].
# We will call recursion on every index to check 'a' and for every call we will check all
#  indexes from (start -> len(s)) == (n - ''.join(path)), can we call it (log n)?
# Essentially there will be 'n' states, but what about loop...
# ! 1 <= s.length <= 300 , 1 <= wordDict[i].length <= 20 !
# So, for 0-index call, we will either check 'j' indexes or if len(s) < 'j' we will only check len(s) indexes.
# O(n * min(j, (len(s) - ''.join(path)))? Maybe.
# But last indexes are still (n - len(''.join(path))), no idea how to calc it.
# O(k * m + n + k * m + m + n * min(j, len(s) - len(''.join(path))))?
# O(k * m + n * j)? Can we just ignore this^^? Like last indexes are just <20, it's like w.e.
# Even constant when we reach last indexes, we're going to check only <20 indexes always.
# Starting from 20 -> 19 -> 18 -> 17 etc.
# So, let's just call it O(k * m + n * j).
# -----------------------------
# Auxiliary space: O(k * m + n)
# Set with all symbols `all_symbols`, assume worst case is all unique => O(k * m).
# Set with all words from `wordDict`, same all words are unique => O(k * m).
# List with used in sequence words `path` will always hold at max strings with summarized  size of `n` => O(n).
# Recursion cache `failed` in the worst case will hold every index of `s` => O(n).
# Recursion stack will be of depth 'n', call for every index s = 'aaa' wordDict = ['a'] => O(n).
# O(2 * k * m + 3 * n).


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
