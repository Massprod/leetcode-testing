# Given a string s and an integer k, return the maximum number
#        of vowel letters in any substring of s with length k.
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
# --------------------------
# 1 <= s.length <= 10 ** 5  ,  1 <= k <= s.length
# s consists of lowercase English letters.


def max_vowels(s: str, k: int) -> int:
    # working_sol (58.30%, 69.85%) -> (196ms, 17.2mb)  time: O(n) | space: O(1)
    vowels: dict[str] = {
        "a": True,
        "e": True,
        "i": True,
        "o": True,
        "u": True,
        "max": 0,
    }
    left: int = 0
    right: int = k - 1
    start_vowels: int = 0
    for symbol in s[left:right + 1]:
        if symbol in vowels:
            start_vowels += 1
    vowels["max"] = start_vowels
    while right != (len(s) - 1):
        if s[left] in vowels:
            prev_left: bool = True
        else:
            prev_left: bool = False
        left += 1
        right += 1
        if s[right] in vowels:
            right_correct: bool = True
        else:
            right_correct = False
        if right_correct and prev_left:
            vowels["max"] = max(vowels["max"], start_vowels)
            continue
        if right_correct and not prev_left:
            start_vowels += 1
            vowels["max"] = max(vowels["max"], start_vowels)
            continue
        if not right_correct and prev_left:
            start_vowels -= 1
            vowels["max"] = max(vowels["max"], start_vowels)
            continue
    return vowels["max"]


# Time complexity: O(n) -> creating dictionary with all vowel_letters => O(m), doesn't depend on input, culling it ->
# n - len of input_string^^| -> checking every index in input_string from 0 to K (inclusive), in the worst case k==n =>
# m - num of vowel_letters^^| => O(k), ! but in this case we're ending function on this step! ->
# K - size of substring^^|   -> checking every index in input_string from (K + 1), to (len(s) - 1) (inclusive) =>
#                            => O(n - k) -> in a summ we're just checking whole input_string => O(n)
# Auxiliary space: O(1) -> creating dictionary with all vowel_letters + extra max_key => O(m + 1) ->
#                          -> 5 extra constants, 3 INTs and 2 bools => O(5) -> none of these depends on input,
#                             so it can be called constant space O(1) or O(m), because we're still creating
#                             these dictionary from scratch. But it's constant value and doesn't depend on input,
#                             so why don't just call it constant?
# --------------------------
# Ok. I made correct version, but too slow for big constraint because it was checking every K size substrings.
# What I failed to understand is that we can use WINDOW method and check every substring by changing position
# of that WINDOW. But I didn't google which is Good. Actually didn't google only because there was a HINT on leetcode,
# still can be counted as my_solution. And now after correct commit I can google for some extra info on WINDOW method.
# --------------------------
# left change -> if from correct to incorrect vowels -1,
#                if from correct to correct vowels -1,
#                if from incorrect to correct vowels +0,
# right change -> if from correct to incorrect and left from correct to incorrect -1
#                 if from correct to correct and left from correct to correct +1
#                 if from correct to correct and left from correct to incorrect +0
# actually we need only check left for -> if from correct -> it's -1
#                             right for -> if to incorrect and left from correct -> it's -1
# --------------------------
# Ok. I missed hard p76, and didn't check a hint. There's no way to break time_limit without using a window.
# Time to learn window_methods.


test1 = "abciiidef"
test1_k = 3
test1_out = 3
print(max_vowels(test1, test1_k))
assert test1_out == max_vowels(test1, test1_k)

test2 = "aeiou"
test2_k = 2
test2_out = 2
print(max_vowels(test2, test2_k))
assert test2_out == max_vowels(test2, test2_k)

test3 = "leetcode"
test3_k = 3
test3_out = 2
print(max_vowels(test3, test3_k))
assert test3_out == max_vowels(test3, test3_k)
