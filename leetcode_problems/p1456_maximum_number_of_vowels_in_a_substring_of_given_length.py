# Given a string s and an integer k, return the maximum number
#        of vowel letters in any substring of s with length k.
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
# --------------------------
# 1 <= s.length <= 10 ** 5  ,  1 <= k <= s.length
# s consists of lowercase English letters.


def max_vowels(s: str, k: int) -> int:
    k_sub_indexes: set = set()
    tempo: list[int] = []
    vowels: dict[str] = {
        "a": True,
        "e": True,
        "i": True,
        "o": True,
        "u": True,
        "max": 0,
    }

    def new_combine(left_to_use: int, start: int = 0, end: int = len(s), ) -> None:
        if left_to_use == 0:
            k_sub_indexes.add(tuple(sorted(tempo)))
            return
        for num in range(start, end):
            if num in tempo:
                break
            tempo.append(num)
            new_combine(left_to_use - 1, start + 1, end)
            tempo.clear()
            return

    for _ in range(len(s)):
        new_combine(k, start=_)
    for tup in k_sub_indexes:
        current_vowels: int = 0
        for index in tup:
            if s[index] in vowels:
                current_vowels += 1
        if current_vowels > vowels["max"]:
            vowels["max"] = current_vowels
    return vowels["max"]


# Bad part I was thinking we should use every SUBSET, and rebuild previously made recursion for that.
# But after than I see that only substrings...W.e still made this working, but I will need to cull some parts.


test1 = "abciiidef"
test1_k = 3
test1_out = 3
print(max_vowels(test1, test1_k))

test2 = "aeiou"
test2_k = 2
test2_out = 2
print(max_vowels(test2, test2_k))

test3 = "leetcode"
test3_k = 3
test3_out = 2
print(max_vowels(test3, test3_k))
