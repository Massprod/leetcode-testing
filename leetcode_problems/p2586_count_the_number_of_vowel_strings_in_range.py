# You are given a 0-indexed array of string words and two integers left and right.
# A string is called a vowel string if it starts with a vowel character
#  and ends with a vowel character where vowel characters are 'a', 'e', 'i', 'o', and 'u'.
# Return the number of vowel strings words[i] where i belongs to the inclusive range [left, right].
# -------------------------
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 10
# words[i] consists of only lowercase English letters.
# 0 <= left <= right < words.length


def vowel_strings(words: list[str], left: int, right: int) -> int:
    # working_sol (66.07%, 73.57%) -> (67ms, 16.73mb)  time: O(right - left) | space: O(1)
    vowels: set[str] = {'a', 'e', 'i', 'o', 'u'}
    out: int = 0
    for index in range(left, right + 1):
        if words[index][0] in vowels and words[index][-1] in vowels:
            out += 1
    return out


# Time complexity: O(right - left)
# Always traversing `right - left` indexes, inclusive => O(right - left).
# -------------------------
# Auxiliary space: O(1).
# Constant INT and constant set `vowels` is used, none of them depends on input => O(1).


test: list[str] = ["are", "amy", "u"]
test_left: int = 0
test_right: int = 2
test_out: int = 2
assert test_out == vowel_strings(test, test_left, test_right)

test = ["hey", "aeo", "mu", "ooo", "artro"]
test_left = 1
test_right = 4
test_out = 3
assert test_out == vowel_strings(test, test_left, test_right)
