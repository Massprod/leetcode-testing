# You are given an array of n strings strs, all of the same length.
# The strings can be arranged such that there is one on each line, making a grid.
#  - For example, strs = ["abc", "bce", "cae"] can be arranged as follows:
#    - abc
#    - bce
#    - cae
# You want to delete the columns that are not sorted lexicographically.
# In the above example (0-indexed), columns 0 ('a', 'b', 'c')
#  and 2 ('c', 'e', 'e') are sorted, while column 1 ('b', 'c', 'a') is not, so you would delete column 1.
# Return the number of columns that you will delete.
# -----------------------
# n == strs.length
# 1 <= n <= 100
# 1 <= strs[i].length <= 1000
# strs[i] consists of lowercase English letters.


def min_deletion_size(strs: list[str]) -> int:
    # working_sol (62.53%, 57.66%) -> (114ms, 17.10mb)  time: O(n) | space: O(1)
    out: int = 0
    if 1 == len(strs):
        return out
    # ! all of the same length !
    for column in range(len(strs[0])):
        for row in range(1, len(strs)):
            if strs[row - 1][column] > strs[row][column]:
                out += 1
                break
    return out


# Time complexity: O(n * k) <- n - length of the input array `strs`, k - length of the words inside `strs`.
# In the worst case, there are no columns to delete.
# So, we're going to traverse every word in `strs` and every char in all of the words => O(n * k).
# -----------------------
# Auxiliary space: O(1)
# Only one constant INT is used => O(1).


test: list[str] = ["cba", "daf", "ghi"]
test_out: int = 1
assert test_out == min_deletion_size(test)

test = ["a", "b"]
test_out = 0
assert test_out == min_deletion_size(test)

test = ["zyx", "wvu", "tsr"]
test_out = 3
assert test_out == min_deletion_size(test)
