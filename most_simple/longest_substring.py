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
    symbols = []
    symbol = []
    for x in range(len(string_list)):
        symbol.append(string_list[x])
        for y in range(x + 1, len(string_list)):
            if string_list[y] not in symbol:
                symbol.append(string_list[y])
                if y == len(string_list) - 1:
                    symbols.append(symbol)
                    symbol = []
                    break
            elif string_list[y] in symbol:
                symbols.append(symbol)
                symbol = []
                break
    for _ in symbols:
        lengths.append(len(_))
    if len(lengths) == 0:
        return 1
    return max(lengths)


print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring(" "))
print(lengthOfLongestSubstring(""))
print(lengthOfLongestSubstring("aa"))
print(lengthOfLongestSubstring("aabb"))
print(lengthOfLongestSubstring("au"))
print(lengthOfLongestSubstring("aab"))
print(lengthOfLongestSubstring("dvdf"))
