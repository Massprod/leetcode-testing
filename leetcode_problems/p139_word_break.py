# Given a string s and a dictionary of strings wordDict, return true if s can be segmented
#   into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
# -----------------------------
# 1 <= s.length <= 300  ,  1 <= wordDict.length <= 1000  ,  1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.


def word_break(s: str, wordDict: list[str]) -> bool:
    all_symbols: str = "".join(wordDict)
    for _ in s:
        if _ not in all_symbols:
            return False
    all_words: set[str] = set(wordDict)
    path: list[str] = []
    max_len: int = 0
    for _ in all_words:
        max_len = max(max_len, len(_))
    failed: dict[str] = {}

    def check_start(start: int):
        if s[start:] in failed.keys() and failed[s[start:]] is False:
            return False
        if len("".join(path)) == len(s):
            return True
        to_check: str = ""
        for y in range(start, len(s)):
            if len(to_check) > max_len:
                failed[s[start:]] = False
                return False
            to_check += s[y]
            if to_check in all_words:
                path.append(to_check)
                if check_start(y + 1):
                    return True
                path.pop()
        failed[s[start:]] = False
        return False

    return check_start(0)


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


test1 = "leetcode"
test1_dict = ["leet", "code"]
test1_out = True
print(word_break(test1, test1_dict))

test2 = "applepenapple"
test2_dict = ["apple", "pen"]
test2_out = True
print(word_break(test2, test2_dict))

test3 = "catsandog"
test3_dict = ["cats", "dog", "sand", "and", "cat"]
test3_out = False
print(word_break(test3, test3_dict))

# test4 - failed -> I was stupid enough to forget about PATH that we need to clear
#                   element's after returning False, and bad part that I was thinking about that from a start,
#                   but just forgot most import part of the path.
test4 = "aaaaaaa"
test4_dict = ["aaaa", "aaa"]
test4_out = True
print(word_break(test4, test4_dict))

test5 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
test5_dict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
test5_out = False
print(word_break(test5, test5_dict))

test6 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaa" \
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
        "aaaaaaaaaaaaa"
test6_dict = ["aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa", "ba"]
test6_out = False
print(word_break(test6, test6_dict))
