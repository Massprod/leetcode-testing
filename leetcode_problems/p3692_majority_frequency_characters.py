# You are given a string s consisting of lowercase English letters.
# The frequency group for a value k is the set of characters
#  that appear exactly k times in s.
# The majority frequency group is the frequency group that contains
#  the largest number of distinct characters.
# Return a string containing all characters in the majority frequency group,
#  in any order.
# If two or more frequency groups tie for that largest size,
#  pick the group whose frequency k is larger.
# --- --- --- ---
# 1 <= s.length <= 100
# s consists only of lowercase English letters.
from collections import Counter, defaultdict


def majority_frequency_group(s: str) -> str:
    # working_solution: (74.84%, 77.99%) -> (3ms, 17.75mb)  Time: O(s) Space: O(s)
    frequencies = Counter(s)
    
    groups: dict[int, list[str]] = defaultdict(list)
    for char, frequency in frequencies.items():
        groups[frequency].append(char)
    
    out: list[str] = []
    max_freq: int = 0
    for frequency, chars in groups.items():
        cur_len: int = len(chars)
        if cur_len > len(out):
            out = chars
            max_freq = frequency
        elif len(out) == cur_len and max_freq < frequency:
            out = chars
            max_freq = frequency
    
    return ''.join(out)


# Time complexity: O(s)
# In the worst case, all chars are unique.
# We will traverse whole `s`, once => O(s).
# Extra traverse every char and it's frequency to group them => O(2 * s).
# Extra traversing all chars to get the maximum group => O(3 * s).
# --- --- --- ---
# Space complexity: O(s)
# `frequencies` <- allocates space for each char of the `s` => O(s).
# `groups` <- allocates space for each char of the `s` => O(2 * s).


test: str = "aaabbbccdddde"
test_out: str = "ab"
assert test_out == majority_frequency_group(test)

test = "abcd"
test_out = "abcd"
assert test_out == majority_frequency_group(test)

test = "pfpfgi"
test_out = "pf"
assert test_out == majority_frequency_group(test)
