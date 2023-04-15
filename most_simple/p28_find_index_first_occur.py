# Given two strings needle and haystack, return
# the index of the first occurrence of needle in haystack, or -1
# if needle is not part of haystack.
# haystack and needle consist of only lowercase English characters.


def first_occur(haystack: str, needle: str) -> int:
    # working_sol (8.70%, 9.26%)
    if len(needle) > len(haystack):
        return -1

    def in_slice(sliced: str, check: str):
        if len(check) == 0:
            return True
        elif len(sliced) > 0 and sliced[0] == check[0]:
            if in_slice(sliced[1:], check[1:]):
                return True
        return False
    for x in range(len(haystack)):
        if haystack[x] == needle[0]:
            if in_slice(haystack[x + 1:], needle[1:]):
                return x
    return -1


# Rushed solution and didn't think about lengths - failed 2 submits for no reason w.e
# Wanted to solve it with recursion.


test1 = "sadbutsad"
test1_target = "sad"
test1_out = 0
print(first_occur(test1, test1_target))
test2 = "aaa"
test2_target = "aaa"
print(first_occur(test2, test2_target))
test3 = "mississippi"
test3_target = "issipi"
print(first_occur(test3, test3_target))
test4 = "leetcode"
test4_target = "leeto"
print(first_occur(test4, test4_target))
test5 = "hello"
test5_target = "ll"
print(first_occur(test5, test5_target))
