# You are given an integer n.
# Return the total number of commas used when writing all integers from [1, n]
#  (inclusive) in standard number formatting.
# In standard formatting:
#  - A comma is inserted after every three digits from the right.
#  - Numbers with fewer than 4 digits contain no commas.
# --- --- --- ---
# 1 <= n <= 10 ** 5


def count_commas(n: int) -> int:
    # working_solution: (100%, 62.96%) -> (0ms, 19.24mb)  Time: O(1) Space: O(1)
    out: int = n - 999
    return max(out, 0)


# Time complexity: O(1)
# --- --- --- ---
# Space complexity: O(1)


test: int = 1002
test_out: int = 3
assert test_out == count_commas(test)

test = 998
test_out = 0
assert test_out == count_commas(test)
