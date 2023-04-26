# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

def group_anagrams(strs: list[str]) -> list[list[str]]:
    ords = {}
    anagrams = []
    for word in strs:
        summ = 0
        for letter in word:
            summ += ord(letter)
        if summ in ords.keys():
            ords[summ].append(word)
        else:
            ords[summ] = []
            ords[summ].append(word)
    for key, value in ords.items():
        anagrams.append(value)
    return anagrams


# strs[i] consists of lowercase English letters.
# Let's just try to count ascii of whole word and filter with dict.
# What I can be missing? What about upper cases?
# Ohh -> ! strs[i] consists of lowercase English letters. !
# If there were uppercase's it could be a fail, cuz A and a different ascii but same letter for the anagram.

test1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
test1_out = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
print(group_anagrams(test1))

test2 = [""]
test2_out = [[""]]
print(group_anagrams(test2))

test3 = ["a"]
test3_out = [["a"]]
print(group_anagrams(test3))
