# You are given a 0-indexed string s consisting of only lowercase English letters,
#  where each letter in s appears exactly twice. You are also given a 0-indexed integer array distance of length 26.
# Each letter in the alphabet is numbered from 0 to 25 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, ... , 'z' -> 25).
# In a well-spaced string, the number of letters between the two occurrences of the ith letter is distance[i].
# If the ith letter does not appear in s, then distance[i] can be ignored.
# Return true if s is a well-spaced string, otherwise return false.
# --------------------------
# 2 <= s.length <= 52
# s consists only of lowercase English letters.
# Each letter appears in s exactly twice.
# distance.length == 26
# 0 <= distance[i] <= 50


def check_distance(s: str, distance: list[int]) -> bool:
    # working_sol (42.83%, 29.70%) -> (46ms, 16.56mb)  time: O(s) | space: O(s)
    chars: dict[str, int] = {}
    for index, char in enumerate(s):
        if char in chars:
            chars[char] = abs(chars[char] - index) - 1
        else:
            chars[char] = index
    for char, dist in chars.items():
        if distance[ord(char) - 97] != dist:
            return False
    return True


# Time complexity: O(s)
# Always traversing whole input string `s`, once => O(s).
# Extra traversing `s / 2` chars to check their distances => O(s + s / 2).
# --------------------------
# Auxiliary space: O(s)
# `chars` <- always allocates space for `s / 2` chars from `s` => O(s).


test: str = "abaccb"
test_dist: list[int] = [1, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
test_out: bool = True
assert test_out == check_distance(test, test_dist)

test = "aa"
test_dist = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
test_out = False
assert test_out == check_distance(test, test_dist)
