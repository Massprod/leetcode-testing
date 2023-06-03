# Given a string s and a dictionary of strings wordDict, return true if s can be segmented
#   into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
# -----------------------------
# 1 <= s.length <= 300  ,  1 <= wordDict.length <= 1000  ,  1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.


def word_break(s: str, wordDict: list[str]) -> bool:
    all_words: set[str] = set(wordDict)
    path: list[str] = []

    def check_start(start: int):
        if len("".join(path)) == len(s):
            return True
        to_check: str = ""
        for y in range(start, len(s)):
            to_check += s[y]
            if to_check in all_words:
                path.append(to_check)
                if check_start(y + 1):
                    return True
        return False

    return check_start(0)


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
