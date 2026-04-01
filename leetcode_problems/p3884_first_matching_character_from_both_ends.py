# You are given a string s of length n consisting of lowercase English letters.
# Return the smallest index i such that s[i] == s[n - i - 1].
# If no such index exists, return -1.
# --- --- --- ---
# 1 <= n == s.length <= 100
# s consists of lowercase English letters.


def first_matching_index(s: str) -> int:
    # working_solution: (100%, 62.64%) -> (0ms, 19.27mb)  Time: O(s) Space: O(1)
    len_s: int = len(s)
    for index in range(len_s):
        if s[index] != s[len_s - index - 1]:
            continue
        return index

    return -1


# Time complexity: O(s)
# --- --- --- ---
# Space complexity: O(1)


test: str = "abcacbd"
test_out: int = 1
assert test_out == first_matching_index(test)

test = "abc"
test_out = 1
assert test_out == first_matching_index(test)

test = "abcdab"
test_out = -1
assert test_out == first_matching_index(test)
