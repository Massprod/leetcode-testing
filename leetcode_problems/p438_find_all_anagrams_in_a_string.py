# Given two strings s and p, return an array of all the start indices of p's anagrams in s.
# You may return the answer in any order.
# --- --- --- ---
# 1 <= s.length, p.length <= 3 * 10 ** 4
# s and p consist of lowercase English letters.
from collections import Counter


def find_anagrams(s: str, p: str) -> list[int]:
    # working_solution: (33.39%, 10.19%) -> (164ms, 20.06mb)  Time: O(s) Space: O(p + s)
    out: list[int] = []
    if len(p) > len(s):
        return out
    # Always of the same size, and all we care is the char count.
    count_anagram: dict[str, int] = Counter(p)
    s_uniques: set[str] = set(s)
    for char in count_anagram:
        if char in s_uniques:
            continue
        return out
    ind_left: int = 0
    ind_right: int = len(p) - 1
    count_window: dict[str, int] = Counter(s[ind_left: ind_right + 1])
    while ind_right < len(s):
        if count_anagram == count_window:
            out.append(ind_left)
        count_window[s[ind_left]] -= 1
        ind_left += 1
        ind_right += 1
        if ind_right >= len(s):
            break
        count_window[s[ind_right]] += 1
    
    return out


# Time complexity: O(s)
# Traversing `s` and `p` multiple time, but it's linear.
# --- --- --- ---
# Space complexity: O(p + s)
# In the worst case, we get len(s) == len(p)
# `count_anagram` <- allocates space for each chat from `p`.
# `count_window` <- allocates space for each char from `s`.
# `s_uniques` <- allocates space for each char from `s`.


test_s: str = "cbaebabacd"
test_p: str = "abc"
test_out: list[int] = [0, 6]
assert test_out == find_anagrams(test_s, test_p)

test_s = "abab"
test_p = "ab"
test_out = [0, 1, 2]
assert test_out == find_anagrams(test_s, test_p)
