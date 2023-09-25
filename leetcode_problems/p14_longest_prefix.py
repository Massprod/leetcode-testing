# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# ------------------
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.


def longest_prefix(strs: list[str]) -> str:
    # working_sol (67.53%, 98.44%) -> (40ms, 16.2mb)  time: O(n + min(strs)) | space: O(min(strs))
    prefix: str = ''
    # Can't make prefix longer than the shortest string.
    shortest: str = min(strs, key=lambda y: len(y))
    # Check every symbol to being presented in all strings.
    for x in range(len(shortest)):
        for string in strs:
            if shortest[x] != string[x]:
                return prefix
        prefix += shortest[x]
    return prefix


# Time complexity: O(n + min(strs)) -> traverse of whole input array to get minimum sized string => O(n) ->
# n - len of input array^^| -> traverse of this string to get the longest prefix => O(n + min(strs)).
# min(strs) - minimum length string of input array^^|
# Auxiliary space: O(min(strs)) -> worst case == len(prefix) == len(shortest) => O(2 * min(strs)).


test: list[str] = ["flower", "flow", "flight"]
test_out: str = "fl"
assert test_out == longest_prefix(test)

test = ["dog", "racecar", "car"]
test_out = ""
assert test_out == longest_prefix(test)
