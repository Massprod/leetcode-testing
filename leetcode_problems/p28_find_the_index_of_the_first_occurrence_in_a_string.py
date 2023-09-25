# Given two strings needle and haystack,
#  return the index of the first occurrence of needle in haystack,
#  or -1 if needle is not part of haystack.
# -------------------
# 1 <= haystack.length, needle.length <= 10 ** 4
# haystack and needle consist of only lowercase English characters.


def first_occur(haystack: str, needle: str) -> int:
    # working_sol (66.45%, 98.32%) -> (37ms, 16.09mb)  time: O((log n) * k) | space: O(1)
    # Can't be inside lower string.
    if len(needle) > len(haystack):
        return -1
    # (index + len(needle) == string with len == needle.
    slice_range: int = len(needle)
    # After this index, everything will be smaller than (needle).
    max_index: int = len(haystack) - len(needle)
    index: int = 0
    while index <= max_index:
        if haystack[index] == needle[0]:
            if haystack[index: index + slice_range] == needle:
                return index
        index += 1
    return -1


# Time complexity: O((log n) * k) -> worst case == every symbol is starting symbol == needle[0] ->
# n - len of input string 'haystack'^^| -> we will check some part of the array, depend on size of the needle ->
# k - len of input string 'needle'^^|   -> and for every index doing slice of needle size => O((log n) * k).
# Auxiliary space: O(1) -> only 3 constant INTs used, none of them depend on input => O(1).


test: str = "sadbutsad"
test_target: str = "sad"
test_out: int = 0
assert test_out == first_occur(test, test_target)

test = "aaa"
test_target = "aaa"
test_out = 0
assert test_out == first_occur(test, test_target)

test = "mississippi"
test_target = "issipi"
test_out = -1
assert test_out == first_occur(test, test_target)

test = "leetcode"
test_target = "leeto"
test_out = -1
assert test_out == first_occur(test, test_target)

test = "hello"
test_target = "ll"
test_out = 2
assert test_out == first_occur(test, test_target)
