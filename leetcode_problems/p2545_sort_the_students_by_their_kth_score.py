# There is a class with m students and n exams.
# You are given a 0-indexed m x n integer matrix score,
#  where each row represents one student and score[i][j] denotes the score the ith student got in the jth exam.
# The matrix score contains distinct integers only.
# You are also given an integer k. Sort the students (i.e., the rows of the matrix)
#  by their scores in the kth (0-indexed) exam from the highest to the lowest.
# Return the matrix after sorting it.
# --------------------
# m == score.length
# n == score[i].length
# 1 <= m, n <= 250
# 1 <= score[i][j] <= 10 ** 5
# score consists of distinct integers.
# 0 <= k < n


def sort_the_students(score: list[list[int]], k: int) -> list[list[int]]:
    # working_sol (49.10%, 72.63%) -> (323ms, 22.57mb)  time: O(n * log n) | space: O(n)
    score.sort(
        reverse=True,
        key=lambda x: x[k]
    )
    return score


# Time complexity: O(n * log n) <- n - length of the input array `score`.
# We're sorting `score` with builtin `sort`, once => O(n * log n).
# --------------------
# Auxiliary space: O(n)
# `sort` <- takes O(n).


test: list[list[int]] = [[10, 6, 9, 1], [7, 5, 11, 2], [4, 8, 3, 15]]
test_k: int = 2
test_out: list[list[int]] = [[7, 5, 11, 2], [10, 6, 9, 1], [4, 8, 3, 15]]
assert test_out == sort_the_students(test, test_k)

test = [[3, 4], [5, 6]]
test_k = 0
test_out = [[5, 6], [3, 4]]
assert test_out == sort_the_students(test, test_k)
