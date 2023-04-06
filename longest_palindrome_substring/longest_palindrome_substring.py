# Given a string s, return the longest palindromic substring in s.

# A string U is a substring of a string T if there exist two strings P and S such that
# T = PUS. The empty string is a substring of every string
# P and S can be empty strings
#

def longest_subpal(s: str) -> str:
    s_values = {}
    for key, value in enumerate(s):
        s_values[key] = str(value)
    max_len = len(s_values)
    if max_len == 1:
        return s
    elif max_len == 0:
        return ""
    pal = ""
    pal_list = {}
    pal_len = 0
    for x in range(max_len):
        symbol = (s_values[x])
        if max_len - x == pal_len:
            break
        for y in range(x + 1, max_len):
            symbol = symbol + s_values[y]
            for z in range(len(symbol)):
                if symbol[z] == symbol[(z * -1) - 1]:
                    pal = True
                    continue
                else:
                    pal = False
                    break
            if pal:
                pal_list[len(symbol)] = symbol
    return pal_list[max(pal_list)]



test1 = "babad"
test2 = "cbbd"
test3 = "d"
test4 = "aa"
test5 = "d d"
test6 = "12344321"
test7 = "ac"
print(longest_subpal(test1))
print(longest_subpal(test2))
print(longest_subpal(test3))
print(longest_subpal(""))
print(longest_subpal(test4))
print(longest_subpal(test5))
print(longest_subpal(test6))
print(longest_subpal(test7))
