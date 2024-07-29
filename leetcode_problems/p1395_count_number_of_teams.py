# There are n soldiers standing in a line.
# Each soldier is assigned a unique rating value.
# You have to form a team of 3 soldiers amongst them under the following rules:
#  - Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
#  - A team is valid if: (rating[i] < rating[j] < rating[k])
#    or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
# Return the number of teams you can form given the conditions.
# (soldiers can be part of multiple teams).
# ---------------------
# n == rating.length
# 3 <= n <= 1000
# 1 <= rating[i] <= 10 ** 5
# All the integers in rating are unique.
from random import randint


def num_teams(rating: list[int]) -> int:
    # working_sol (59.90%, 66.67%) -> (481ms, 16.70mb)  time: O(n * n) | space: O(1)
    out: int = 0
    for index in range(1, len(rating)):
        left_side_lower: int = 0
        left_side_higher: int = 0
        right_side_lower: int = 0
        right_side_higher: int = 0
        for left_index in range(index):
            if rating[left_index] < rating[index]:
                left_side_lower += 1
            elif rating[left_index] > rating[index]:
                left_side_higher += 1
        for right_index in range(index + 1, len(rating)):
            if rating[right_index] < rating[index]:
                right_side_lower += 1
            elif rating[right_index] > rating[index]:
                right_side_higher += 1
        # Every unique permutation == unique team we can build.
        out += left_side_lower * right_side_higher
        out += left_side_higher * right_side_lower
    return out


# Time complexity: O(n * n) <- n - length of the input array `rating`.
# We're always traversing every index of `rating`.
# And for each index, we're extra traversing `n - 1` indexes to get lower && higher values => O(n * n).
# ---------------------
# Auxiliary space: O(1)
# Only constant INT's used, none of them depends on input => O(1).


test: list[int] = [2, 5, 3, 4, 1]
test_out: int = 3
assert test_out == num_teams(test)

test = [2, 1, 3]
test_out = 0
assert test_out == num_teams(test)

test = [1, 2, 3, 4]
test_out = 4
assert test_out == num_teams(test)

test = list(set([randint(1, 10 ** 5) for _ in range(1000)]))
print(test)
