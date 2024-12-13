# You are given a 0-indexed string array words.
# Let's define a boolean function isPrefixAndSuffix that takes two strings, str1 and str2:
#  - isPrefixAndSuffix(str1, str2) returns true if str1 is both a prefix and a suffix of str2, and false otherwise.
# For example, isPrefixAndSuffix("aba", "ababa") is true because "aba" is a prefix of "ababa" and also a suffix,
#  but isPrefixAndSuffix("abc", "abcd") is false.
# Return an integer denoting the number of index pairs (i, j) such that i < j,
#  and isPrefixAndSuffix(words[i], words[j]) is true.
# -----------------------
# 1 <= words.length <= 50
# 1 <= words[i].length <= 10
# words[i] consists only of lowercase English letters.
from functools import cache


def count_prefix_suffix_pairs(words: list[str]) -> int:
    # working_sol (15.65%, 5.04%) -> (19ms, 17.44mb)  time: O(n * n * k) | space: O(k)

    @cache
    def is_prefix(check: str, target: str) -> bool:
        slice_size: int = len(check)
        return check == target[-slice_size:]
    
    @cache
    def is_suffix(check: str, target: str) -> bool:
        slice_size: int = len(check)
        return check == target[:slice_size]
    
    out: int = 0
    for _index1 in range(len(words)):
        for _index2 in range(_index1 + 1, len(words)):
            check_str: str = words[_index1]
            target_str: str = words[_index2]
            if (is_prefix(check_str, target_str)
                and is_suffix(check_str, target_str)):
                    out += 1

    return out


# Time complexity: O((n * n) * k) <- n - length of the input array `words`,
#                                    k - average length of strings in `words`.
# Always using every index and check everything after it => O(n * n).
# In the worst case, every string is equal and have max_size => O((n * n) * (2 * k)).
# -----------------------
# Auxiliary space: O(k)
# Same worst case, and we're just using slices 2 times => O(2 * k)


test: list[str] = ["a","aba","ababa","aa"]
test_out: int = 4
assert test_out == count_prefix_suffix_pairs(test)

test = ["pa","papa","ma","mama"]
test_out = 2
assert test_out == count_prefix_suffix_pairs(test)

test = ["abab","ab"]
test_out = 0
assert test_out == count_prefix_suffix_pairs(test)
