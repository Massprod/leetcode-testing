# Given an array of integers citations where citations[i] is the number
#   of citations a researcher received for their ith paper, return the researcher's h-index.
# According to the definition of h-index on Wikipedia:
#   The h-index is defined as the maximum value of h such that the given researcher
#     has published at least h papers that have each been cited at least h times.
# -------------------
# n == citations.length
# 1 <= n <= 5000
# 0 <= citations[i] <= 1000
from random import randint


def h_index(citations: list[int]) -> int:
    # working_sol (97.40%, 84.68%) -> (38ms, 16.5mb)  time: O(n * log n) | space: O(1)
    # Can be 0 papers with 0 views(cites).
    left_l: int = 0
    # And maximum limit is all papers published.
    right_l: int = len(citations)

    def check(h_ind: int) -> int:
        # h-index == h_papers with h_cites.
        # papers == cites and we need maximum.
        paper_count: int = 0
        for cites in citations:
            if cites >= h_ind:
                paper_count += 1
                # No reason to continue, already satisfied.
                if paper_count >= h_ind:
                    return paper_count
        return paper_count
    # Standard Binary search approach.
    while left_l < right_l:
        # Instead of ceil() just +1.
        middle: int = ((left_l + right_l) // 2) + 1
        # If there's more or equal cites for current h-index == middle ->
        if check(middle) >= middle:
            # -> we can try higher value ->
            left_l = middle
            continue
        # -> or make it lower and recheck.
        right_l = middle - 1
    return left_l


# Time complexity: O(n * log n) -> our maximum limit is len(n) so it's O(n * log n) ->
# n - len of input_array^^|   -> standard BS with extra loop for every check, actually loop can be counted as (log n),
#                             but in the worst case if h_ind == len(citations) we're going for a full loop.
# Auxiliary space: O(1) -> only 4 extra constant INTs used => O(1).
# -------------------
# Should be standard BS problem -> cuz again we're having some Requirement and only 2 limits,
# either it's maximum len as h or 0. And we need to find maximum possible h to satisfy,
# cites == h and papers with such cites == h.


test: list[int] = [3, 0, 6, 1, 5]
test_out: int = 3
assert test_out == h_index(test)

test = [1, 3, 1]
test_out = 1
assert test_out == h_index(test)

test = []
for _ in range(5000):
    test.append(randint(0, 1000))
# print(test)
