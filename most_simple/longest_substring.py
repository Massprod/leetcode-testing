# Given a string s, find the length of the longest
# substring without repeating characters
from itertools import permutations

def lengthOfLongestSubstring(s: str) -> int:
    slice = list(s)
    print(slice)
    sub = ""
    for x in range(1, len(slice) - 1):
        if slice[x] == slice[x+1] and slice[x] not in sub:
            sub += slice[x]
        elif slice[x] != slice[x+1] and slice[x] not in sub:
            sub += slice[x]
    length = len(sub)
    return length

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring(" "))
print(lengthOfLongestSubstring(""))