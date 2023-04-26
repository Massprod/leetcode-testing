# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

def group_anagrams(strs: list[str]) -> list[list[str]]:
    # working_sol (21.46%, 81.97%) -> (118ms, 17.2mb)  time:
    ords = {}
    anagrams = []
    for word in strs:
        summ = ""
        check = "".join(sorted(word))
        for letter in check:
            summ += str(ord(letter))
        if summ in ords.keys():
            ords[summ].append(word)
        else:
            ords[summ] = []
            ords[summ].append(word)
    for key, value in ords.items():
        anagrams.append(value)
    return anagrams



# Main reason why I wanted to use ascii is to skip looping extra time to check current str exists in dict.
# Sums can be equal, so it doesn't work, and now we're extra looping word to sort it.
# Either I drop ascii idea or leaving it like this, cuz we cant check ascii in INT,
# and we need to sort it for a str filter. Because extra sorting is slow.

# Let's just try to count ascii of whole word and filter with dict.
# What I can be missing? What about upper cases?
# Ohh -> ! strs[i] consists of lowercase English letters. !
# If there were uppercase's it could be a fail, cuz 'A' and 'a' different ascii but same letter for the anagram.


test1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
test1_out = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
print(group_anagrams(test1))

test2 = [""]
test2_out = [[""]]
print(group_anagrams(test2))

test3 = ["a"]
test3_out = [["a"]]
print(group_anagrams(test3))

# test4 - failed -> different ascii can summ up to same value. I wanted to do it without extra checks,
#                   but now we need to extra check keys in dict.
test4 = ["cab", "tin", "pew", "duh", "may", "ill", "buy", "bar", "max", "doc"]
test4_out = [["max"], ["buy"], ["doc"], ["may"], ["ill"], ["duh"], ["tin"], ["bar"], ["pew"], ["cab"]]
print(group_anagrams(test4))
