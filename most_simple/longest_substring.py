# Given a string s, find the length of the longest
# substring without repeating characters


# A string U is a substring of a string T if there exist two strings P and S such that
# T = PUS. The empty string is a substring of every string
# P and S can be empty strings
#

def lengthOfLongestSubstring(s: str) -> int:
    speed_test = {}
    for key, value in enumerate(s):
        speed_test[key] = value
    list_len = len(speed_test)
    if list_len == 0:
        return 0
    lengths = []
    symbols = []
    for x in range(list_len):
        symbol = (speed_test[x])
        if list_len - x in lengths:
            break
        for y in range(x + 1, list_len):
            if speed_test[y] not in symbol:
                symbol = symbol + (speed_test[y])
                if y == list_len - 1:
                    symbols.append(symbol)
                    lengths.append(len(symbol))
                    break
            elif speed_test[y] in symbol:
                symbols.append(symbol)
                lengths.append(len(symbol))
                break
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
