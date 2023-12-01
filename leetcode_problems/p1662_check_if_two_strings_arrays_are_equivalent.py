# Given two string arrays word1 and word2,
#  return true if the two arrays represent the same string, and false otherwise.
# A string is represented by an array if the array elements concatenated in order forms the string.
# --------------------
# 1 <= word1.length, word2.length <= 10 ** 3
# 1 <= word1[i].length, word2[i].length <= 10 ** 3
# 1 <= sum(word1[i].length), sum(word2[i].length) <= 10 ** 3
# word1[i] and word2[i] consist of lowercase letters.


def array_strings_are_equal(word1: list[str], word2: list[str]) -> bool:
    # working_sol (43.23%, 91.22%) -> (42ms, 16.2mb)  time: O(m * k + n * j) | space: O(m * k + n * j)
    return ''.join(word1) == ''.join(word2)


# Time complexity: O(m * k + n * j) <- m - length of input array 'word1',
#                                      n - length of input array 'word2',
#                                      k - average length of strings in 'word1',
#                                      j - average length of strings in 'word2'.
# Auxiliary space: O(m * k + n * j)


test_1: list[str] = ["ab", "c"]
test_2: list[str] = ["a", "bc"]
test_out: bool = True
assert test_out == array_strings_are_equal(test_1, test_2)

test_1 = ["a", "cb"]
test_2 = ["ab", "c"]
test_out = False
assert test_out == array_strings_are_equal(test_1, test_2)


test_1 = ["abc", "d", "defg"]
test_2 = ["abcddefg"]
test_out = True
assert test_out == array_strings_are_equal(test_1, test_2)
