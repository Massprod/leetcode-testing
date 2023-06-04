# Given two strings s and t of lengths m and n respectively, return the minimum window substring
#   of s such that every character in t (including duplicates) is included in the window.
#   If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.
# --------------------------
# m == s.length  ,  n == t.length  ,  1 <= m, n <= 10 ** 5
# s and t consist of uppercase and lowercase English letters.
# --------------------------
# Follow up: Could you find an algorithm that runs in O(m + n) time?


def min_window(s: str, t: str) -> str:
    chars: dict[str] = {}
    cur_chars: dict[str] = {}
    for char in t:
        if char not in chars:
            chars[char] = 1
            cur_chars[char] = 0
            continue
        chars[char] += 1
    left: int = 0
    right: int = 0
    min_sub: str = ""
    whole: bool = False
    extras: list[str] = []
    while right != len(s) + 1 and left < len(s):
        for key in cur_chars:
            if chars[key] == cur_chars[key]:
                whole = True
            if chars[key] != cur_chars[key]:
                whole = False
                break
        if not whole:
            for key in cur_chars:
                if cur_chars[key] > chars[key]:
                    extras.append(key)
        if whole:
            if len(min_sub) > len(s[left: right]) or len(min_sub) == 0:
                min_sub = s[left: right]
            if s[left] in cur_chars:
                cur_chars[s[left]] -= 1
            left += 1
            continue
        while (s[left] not in cur_chars) or (s[left] in extras):
            if s[left] in extras:
                cur_chars[s[left]] -= 1
                extras.remove(s[left])
            left += 1
        if (right != len(s)) and (s[right] in cur_chars):
            cur_chars[s[right]] += 1
        right += 1
    return min_sub


# Ok. I need to fail, because I'm kinda stuck with thinking that's correct need more test_cases.
# --------------------------
# Creating two dictionaries because copying is taking the same time, and I want to use counter and limiter.
# And without copying should be O(m) not O(2m).
# --------------------------
# !
# s and t consist of uppercase and lowercase English letters. !
# Should we differentiate them? Because "a" can be equal to "A" or not, no info on that.
# !
# such that every character in t (including duplicates) is included in the window !
# Only this. Hmm. Guess there's would be no reasons to put UPPER and LOWER cases as constraints,
# if we shouldn't differentiate them.
# I will stick to this, and search for UPPER and LOWER cases as different characters.
# Tested with test case s = "A" and t = "a", correct output from them is "".
# So yes we should differentiate them.


test1 = "ADOBECODEBANC"
test1_t = "ABC"
test1_out = "BANC"
print(min_window(test1, test1_t))

test2 = "a"
test2_t = "a"
test2_out = "a"
print(min_window(test2, test2_t))

test3 = "a"
test3_t = "aa"
test3_out = ""
print(min_window(test3, test3_t))
