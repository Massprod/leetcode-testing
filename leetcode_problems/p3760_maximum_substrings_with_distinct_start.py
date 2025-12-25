# You are given a string s consisting of lowercase English letters.
# Return an integer denoting the maximum number of substrings you can split s
#  into such that each substring starts with a distinct character
#  (i.e., no two substrings start with the same character).
# --- --- --- ---
# 1 <= s.length <= 10 ** 5
# s consists of lowercase English letters.


def max_distinct(s: str) -> int:
    # working_solution: (75.04%, 94.37%) -> (15ms, 17.99mb)  Time: O(s) Space: O(s)
    # No matter what substring we're going to use.
    # It's always the number of unique values in the string.
    # Because, we can only start with the unique value :)
    return len(set(s))


# Time complexity: O(s)
# --- --- --- ---
# Space complexity: O(s)


test: str = 'abab'
test_out: int = 2
assert test_out == max_distinct(test)

test = 'abcd'
test_out = 4
assert test_out == max_distinct(test)

test = 'aaaa'
test_out = 1
assert test_out == max_distinct(test)
