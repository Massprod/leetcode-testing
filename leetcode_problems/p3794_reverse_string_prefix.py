# You are given a string s and an integer k.
# Reverse the first k characters of s and return the resulting string.
# --- --- --- ---
# 1 <= s.length <= 100
# s consists of lowercase English letters.
# 1 <= k <= s.length


def reverse_prefix(s: str, k: int) -> str:
    # working_solution: (100%, 100%) -> (0ms, 17.33mb)  Time: O(s) Space: O(s)
    return s[:k][::-1] + s[k:]


# Time complexity: O(s)
# --- --- --- ---
# Space complexity: O(s)


test: str = 'abcd'
test_k: int = 2
test_out: str = 'bacd'
assert test_out == reverse_prefix(test, test_k)

test = 'xyz'
test_k = 3
test_out = 'zyx'
assert test_out == reverse_prefix(test, test_k)

test = 'hey'
test_k = 1
test_out = 'hey'
assert test_out == reverse_prefix(test, test_k)
