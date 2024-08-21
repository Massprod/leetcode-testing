# You are given an array of strings words and a string pref.
# Return the number of strings in words that contain pref as a prefix.
# A prefix of a string s is any leading contiguous substring of s.
# -------------------------
# 1 <= words.length <= 100
# 1 <= words[i].length, pref.length <= 100
# words[i] and pref consist of lowercase English letters.


def prefix_count(words: list[str], pref: str) -> int:
    # working_sol (93.69%, 54.67%) -> (36ms, 16.70mb)  time: O(n * k) | space: O(1)
    out: int = 0
    for word in words:
        # Or we can count chars with 2 pointers, but w.e
        if word.startswith(pref):
            out += 1
    return out


# Time complexity: O(n * k) <- n - length of the input array `words`, k - average length of word in `words`.
# In the worst case, every word is going to have `pref`.
# We traverse every word in `words` and `pref` in it => O(n * k).
# -------------------------
# Auxiliary space: O(1).


test: list[str] = ["pay", "attention", "practice", "attend"]
test_pref: str = "at"
test_out: int = 2
assert test_out == prefix_count(test, test_pref)

test = ["leetcode", "win", "loops", "success"]
test_pref = "code"
test_out = 0
assert test_out == prefix_count(test, test_pref)
