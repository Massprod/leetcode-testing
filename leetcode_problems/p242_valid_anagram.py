# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.
# ------------------------
# 1 <= s.length, t.length <= 5 * 10 ** 4
# s and t consist of lowercase English letters.
# ------------------------
# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?


def is_anagram(s: str, t: str) -> bool:
    # working_sol (8.37%, 69.14%) -> (83ms, 16.8mb)  time: O(n) | space: O(n)
    if len(t) != len(s):
        return False
    to_check: dict[int] = {}
    for _ in t:
        if ord(_) not in to_check:
            to_check[ord(_)] = 1
            continue
        to_check[ord(_)] += 1
    for symbol in s:
        if ord(symbol) not in to_check:
            return False
        to_check[ord(symbol)] -= 1
        if to_check[ord(symbol)] < 0:
            return False
    for key in to_check:
        if to_check[key] != 0:
            return False
    return True


# Time complexity: O(n) -> below.
# n - len of input_string^^|
# Auxiliary space: O(n) -> extra dictionary of size n => O(n)
# ------------------------
# Strange that top_tiers is sorting, and it's faster, but yeah python sorted() taking care of all characters.
# Mine should be => O(n + n + n) -> creating dictionary of size n => O(n), checking every symbol in s => O(n) ->
#                                -> checking every key in dictionary again => O(n) -> O(3n).
# With sorting => O(2 * (n * log n) + n) -> sorting with sorted() => O(n * (log n)) ->
#                                        -> doing it twice => O(2 * (n * (log n)) ->
#                                        -> and check after sorting => O(n) -> O((2 * (n * log n)) + n).
# W.e all of this valid, but sorted() is faster for like 15%.
# Guess im incorrect with BigO, or dictionary operations taking more time for extra checks than i think.
# ------------------------
# Wait, why all these extras? I could just create 2 dictionaries from for x in range() and check them equal or not.
# Nah. Both working with similar speed, but in some cases it's better to check every value one by one,
# because if there's break at half_way (used symbols more than present in t) insta returning False.
# But in cases with correct anagram it's faster to just check 2 dictionaries. W.e both valid.
# ------------------------
# Well first I see is simple O(n * n) to check every value from s in t.
# Second is that we can build dictionary with key as t values, and values as encounters of them.
# ^^Should be faster, because dict look_ups is O(1) not O(n) for lists.
# With considering follow_up, we can store not just symbols but ord(symbol) to simply get their code.
# Guess in this case it's faster to convert every symbol in s into their ord(s) and store into 1 dict,
# and store ord(t) in another. Same check every single one of them, or just scroll through s and convert on a go.
# But as I previously tried to check list of STRINGs with another dict(INTs),
# it was faster to convert whole list into INTs first and then compare them, than converting on a way.


test1 = "anagram"
test1_t = "nagaram"
test1_out = True
print(is_anagram(test1, test1_t))
assert test1_out == is_anagram(test1, test1_t)

test2 = "rat"
test2_t = "car"
test2_out = False
print(is_anagram(test2, test2_t))
assert test2_out == is_anagram(test2, test2_t)

test3 = "◁◐╡☎♠✝✘✘✘✘™™™✍✍✍"
test3_t = "◁✘◐╡™✍☎✘™✍✍✘♠✝✘™"
test3_out = True
print(is_anagram(test3, test3_t))
assert test3_out == is_anagram(test3, test3_t)
