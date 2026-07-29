# You are given a palindromic string s.
# Return the lexicographically smallest palindromic permutation of s.
# --- --- --- ---
# 1 <= s.length <= 10 ** 5
# s consists of lowercase English letters.
# s is guaranteed to be palindromic.
from collections import Counter


def smallest_palindrome(s: str) -> str:
    # working_solution: (57.14%, 5.36%) -> (254ms, 22.88mb)  Time: O(s * log s) Space: O(s)
    if 1 == len(s):
        return s

    count: dict[str, int] = Counter(s)
    
    c_order: list[str] = sorted(count.keys())
    prefix: list[str] = []
    for char in c_order:
        uses: int = count[char] // 2
        prefix.extend(
            [char for _ in range(uses)]
        )
    suffix: list[str] = prefix[::-1]
    middle: str = '' if 0 == len(s) % 2 else s[len(s) // 2]
    out: str = "".join(prefix + [middle] + suffix)
    
    return out


# Time complexity: O(s * log s)
# --- --- --- ---
# Space complexity: O(s)


test: str= "z"
test_out: str = "z"
assert test_out == smallest_palindrome(test)

test = "babab"
test_out = "abbba"
assert test_out == smallest_palindrome(test)

test = "daccad"
test_out = "acddca"
assert test_out == smallest_palindrome(test)
