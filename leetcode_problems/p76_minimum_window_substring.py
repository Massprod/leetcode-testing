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
    # working_sol (21.69%, 65.61%) -> (301ms, 17mb)  time: O(n + (n - j) * m) | space: O(m)
    if len(t) > len(s):
        return ""
    chars: dict[str] = {}
    cur_chars: dict[str] = {}
    extras: dict[str] = {}
    for char in t:
        if char not in chars:
            chars[char] = 1
            cur_chars[char] = 0
            extras[char] = 0
            continue
        chars[char] += 1
    left: int = 0
    right: int = 0
    min_sub: str = ""
    whole: bool = False
    used: int = 0
    while right != len(s) + 1 and left < len(s):
        if used >= len(t):
            for key in cur_chars:
                if cur_chars[key] >= chars[key]:
                    whole = True
                    continue
                if chars[key] > cur_chars[key]:
                    whole = False
                    break
        if whole:
            if len(min_sub) > len(s[left: right]) or len(min_sub) == 0:
                min_sub = s[left: right]
                if len(min_sub) == len(t):
                    return min_sub
            if s[left] in cur_chars:
                cur_chars[s[left]] -= 1
                used -= 1
                whole = False
            left += 1
            continue
        while left < len(s) and ((s[left] not in cur_chars) or ((cur_chars[s[left]] - chars[s[left]]) > 0)):
            if (s[left] in cur_chars) and ((cur_chars[s[left]] - chars[s[left]]) > 0):
                cur_chars[s[left]] -= 1
                used -= 1
                whole = False
            left += 1
        if (right < len(s)) and (s[right] in cur_chars):
            cur_chars[s[right]] += 1
            used += 1
        right += 1
    return min_sub


# Time complexity: O(n + (n - j) * m) ->
#   -> traversing whole symbols_string, and creating 3 dictionaries with equal size => O(m) ->
#   -> traversing whole input_string from 0 to end with right_pointer, in the worst case,
#      and (n - m) with left_pointer => O(n + (n - m)) ->
#   -> for every index on this path checking every KEY in cur_chars + chars + cur_chars, every check is O(1) but
#      for every KEY is still should be O(m) => O((n - j) * 3m) ->
#   -> O(m + n + (n - m) + (n - j) * 3m) => O(2n + (n - j) * 3m) =>  O(n + (n - j) * m)
# ^^ m - len of symbols_string | n - len of input_string | j - number of unique subs with WHOLE in it ^^
# --------------------------
# ^^After sleeping on this task, it's not so bad in the end if I just add extra check to cull some calls
# on check if WHOLE or not, now it's 308ms instead of 800, still not 120ms like top_tiers, but I'm fine with that.
# And now it's not (n * m) -> ((n - j) * m) <- where's j is number of unique substrings
#                                              with correct number of search_values.
# Don't know how to calculate this j. Worst case should be like -> s = "aacbcaacbcaacbca", t = "aba" ->
# -> "aacb" gives us WHOLE but not same length as t, so we're going to check more ->
# -> so after that we're checking every index from 3 to 15 is calling check on WHOLE, so it's still O((n - j) * m).
# But in the best case, like -> s = "aacbcddddddddd", t = "aba" -> we're getting "aacb" ->
# -> and after shifting left side by 1 index, it's never going to get (used >= len(t)), so it's just 1 check.
# Better than it was, but still can be changed to check less, maybe I will come up with something later.
# --------------------------
# Auxiliary space: O(m) -> 3 dictionaries of the same size == m => O(3m) -> extra constants,
#                          and string with the size == m in the worst case => O(m) -> O(4m) -> O(m)
# --------------------------
# Sheesh. Hard without extra info and only using HINT as guidance, evolving.
# Dunno about O(n + m), but at least I made a correctly working solution.
# Actually we're making it in ONE_WAY walk O(n), but with every step we're checking too much data
# in dictionaries, so if we can't call dictionary operations as O(1), in this case I doubt that.
# Because search in dictionary is O(1) but we're checking every KEY. Plus there's top solutions with <200ms,
# when mine is 801ms. So if they're O(n + m) mine is something O(n + m * n) ->
# -> we're checking every index once, but every KEY in dictionaries will be checked, on every index step.
# --------------------------
# Don't think changing extras from list to dict is going to change anything, but if there's
# a 100 extra it's going to be faster. Well let's try this one as well.
# Otherwise, I need to find how to check all_symbols used or not faster.
# Well well well, working in this 266 test_case, 1 to go :)
# --------------------------
# Sadly 265/267 cases passed, now it's TimeGate, but at least I made working solution,
# without extra info(google/gpt). There's a lot of extra checks, and maybe I will find how to cull them.
# What about length?
# While doing heavy_lifting I forgot that we can just cull any input with incorrect length.
# Nah, not the case, but still good to implement.
# Another one I see is that we can insta return if we found min_sub with equal length to t,
# because t == min_sub is IDEAL option, no reasons to search anything else.
# --------------------------
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
assert test1_out == min_window(test1, test1_t)

test2 = "a"
test2_t = "a"
test2_out = "a"
print(min_window(test2, test2_t))
assert test2_out == min_window(test2, test2_t)

test3 = "a"
test3_t = "aa"
test3_out = ""
print(min_window(test3, test3_t))
assert test3_out == min_window(test3, test3_t)

test4 = "A"
test4_t = "a"
test4_out = ""
print(min_window(test4, test4_t))
assert test4_out == min_window(test4, test4_t)

test5 = "acbbaca"
test5_t = "aba"
test5_out = "baca"
print(min_window(test5, test5_t))
assert test5_out == min_window(test5, test5_t)
