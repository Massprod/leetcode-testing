# Given an array of integers citations where citations[i] is the number of citations
#  a researcher received for their ith paper and citations is sorted in ascending order,
#  return the researcher's h-index.
# According to the definition of h-index on Wikipedia:
#  The h-index is defined as the maximum value of h such that the given researcher
#   has published at least h papers that have each been cited at least h times.
# You must write an algorithm that runs in logarithmic time.
# ----------------
# n == citations.length
# 1 <= n <= 10 ** 5
# 0 <= citations[i] <= 1000
# citations is sorted in ascending order.
from random import randint


def h_index(citations: list[int]) -> int:
    # working_sol (56.38%, 83.30%) -> (133ms, 23.2mb)  time: O(log n) | space: O(1)
    # Standard BinarySearch.
    all_papers: int = len(citations)
    l_limit: int = 0
    r_limit: int = all_papers - 1
    while l_limit < r_limit:
        # Index of current paper.
        middle: int = (l_limit + r_limit) // 2 + 1
        # We given sorted array -> we can be 100% sure that there's
        # (all_papers - middle) papers with HIGHER|EQUAL cites than one we check.
        if (all_papers - middle) > citations[middle]:
            l_limit = middle
        else:
            r_limit = middle - 1
    # We find maximum # of papers with HIGHER|EQUAL cites
    #  than our paper == citations[l_limit].
    h_ind: int = all_papers - l_limit
    # But they can have only HIGHER cites ->
    if citations[l_limit] >= h_ind:
        return h_ind
    # -> then we need to exclude it.
    return h_ind - 1


# Time complexity: O(log n) -> standard BS on array => O(log n).
# n - len of input_array^^|
# Auxiliary space: O(1) -> only 4 extra INTs used, none of them depends on input => O(1).
# ----------------
# Should be BS problem, but what we're searching? In first part we just checked for # of papers with correct value.
# Now we have them sorted, so we can use length?
# Like: len(citations) - index == all papers with higher|equal values than we're taken right now.
# So we can just take index, check (len(citations) - index >= citations[index]) if there's more or equal # of
# papers with correct cites, than we can try to make it higher, otherwise lower.
# Should be correct.
# Extra we need to check if paper we found, have same cites as # of papers.


test: list[int] = [0, 1, 3, 5, 6]
test_out: int = 3
assert test_out == h_index(test)

test = [1, 2, 100]
test_out = 2
assert test_out == h_index(test)

test = [
    1, 22, 30, 37, 41, 63, 71, 79, 100, 105, 126, 133, 133, 139, 140, 142, 158,
    159, 176, 186, 187, 187, 195, 199, 206, 214, 234, 242, 254, 258, 268, 274,
    281, 295, 300, 300, 315, 344, 356, 363, 369, 381, 403, 414, 422, 439, 446,
    470, 470, 471, 483, 490, 508, 521, 536, 546, 566, 596, 601, 603, 619, 632,
    634, 635, 636, 666, 670, 684, 684, 705, 709, 719, 719, 723, 727, 730, 739,
    754, 757, 759, 766, 783, 797, 836, 844, 867, 898, 899, 902, 902, 914, 934,
    934, 936, 946, 951, 970, 978, 984, 992
]
test_out = 92
assert test_out == h_index(test)

test = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
test_out = 0
assert test_out == h_index(test)

test = [1]
test_out = 1
assert test_out == h_index(test)

test = [1, 1]
test_out = 1
assert test_out == h_index(test)

test = [0]
test_out = 0
assert test_out == h_index(test)

test = [11, 15]
test_out = 2
assert test_out == h_index(test)

test = sorted([randint(0, 1000) for _ in range(10 ** 3)])
print(test)
