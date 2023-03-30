# Given a string s, find the length of the longest
# substring without repeating characters


# A string U is a substring of a string T if there exist two strings P and S such that
# T = PUS. The empty string is a substring of every string
# P and S can be empty strings
#

def lengthOfLongestSubstring(s: str) -> int:
    string_list = list(s)
    if len(string_list) == 0:
        return 0
    lengths = []
    sub = []
    test = {}
    for key, value in enumerate(string_list):
        test[key] = value
    indexes = []
    symbols = []
    for key2, value2 in test.items():
        if value2 not in symbols:
            indexes.append(key2)
            symbols.append(value2)
            if len(symbols) == len(string_list):
                sub.append(symbols)
        elif value2 in symbols:
            sub.append(symbols)
            indexes = [key2]
            symbols = [value2]
    for _ in sub:
        lengths.append(len(_))
    # print(test)
    # print(sub)
    # print(lengths)
    return max(lengths)


print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring(" "))
print(lengthOfLongestSubstring(""))
print(lengthOfLongestSubstring("aa"))
print(lengthOfLongestSubstring("aabb"))
print(lengthOfLongestSubstring("au"))
