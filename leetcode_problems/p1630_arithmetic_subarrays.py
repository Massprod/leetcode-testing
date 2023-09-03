# A sequence of numbers is called arithmetic if it consists of at least two elements,
#  and the difference between every two consecutive elements is the same.
# More formally, a sequence s is arithmetic if and only if s[i+1] - s[i] == s[1] - s[0] for all valid i.
# For example, these are arithmetic sequences:
#   1, 3, 5, 7, 9
#   7, 7, 7, 7
#   3, -1, -5, -9
# The following sequence is not arithmetic:
#   1, 1, 2, 5, 7
# You are given an array of n integers, nums, and two arrays of m integers each, l and r,
#  representing the m range queries, where the ith query is the range [l[i], r[i]].
# All the arrays are 0-indexed.
# Return a list of boolean elements answer, where answer[i] is true
#  if the subarray nums[l[i]], nums[l[i]+1], ... , nums[r[i]] can be rearranged
#  to form an arithmetic sequence, and false otherwise.
# ----------------
# n == nums.length
# m == l.length
# m == r.length
# 2 <= n <= 500
# 1 <= m <= 500
# 0 <= l[i] < r[i] < n
# -10 ** 5 <= nums[i] <= 10 ** 5


def check_arithmetic_sub(nums: list[int], l: list[int], r: list[int]) -> list[bool]:
    # working_sol (91.61%, 98.90%) -> (158ms, 16.3mb)  time: O(m * (n * log n )) | space: O(n + m)
    ari_seqs: list[bool] = []
    checked: dict[tuple[int, int], bool] = {}
    # ! m == l.length, m == r.length !
    for y in range(len(l)):
        # We allowed to make pairs like:
        #  l == [0, 0, 0] , r == [len(nums] - 1, len(nums] - 1, len(nums] - 1]
        # So it's better to cull reuses. Sorting them and recheck is too much.
        if (l[y], r[y]) in checked:
            ari_seqs.append(checked[l[y], r[y]])
            continue
        # Arithmetic seq is always stays correct when sorted in DESC|ASCE.
        to_check: list[int] = sorted(nums[l[y]: r[y] + 1])
        arithmetic: bool = True
        # ! 0 <= l[i] < r[i] < n ! <- always, at least len == 1.
        if len(to_check) <= 2:
            ari_seqs.append(arithmetic)
            continue
        diff: int = to_check[1] - to_check[0]
        for x in range(2, len(to_check)):
            if (to_check[x] - to_check[x - 1]) != diff:
                arithmetic = False
                break
        ari_seqs.append(arithmetic)
        checked[l[y], r[y]] = arithmetic

    return ari_seqs


# Time complexity: O(m * (n * log n)) -> worst case every left is 0 and every right is len(nums) - 1 indexes ->
# m - len of input l and r^^| -> we will traverse whole input_nums for every pair of indexes => O(m * (n * log n)).
# n - len of input_nums^^|    -> sorting every slice == n * log n, and it's dominates just traverse of n.
#                             Actually we can store already used pairs and reuse them, then worst case is
#                             all L == 0, and R is like [1, 2, 3, 4, 5, ... 500].
#                             Then, can we say O(m * (log n * log n)? Cuz now it's always only some part of n checked.
#                             And because we're sorting on every call should be correct to cull it as well =>
#                             => O(m * log n)?
# Auxiliary space: O(n + m) -> storing every result of index pairs => O(m) -> and saving to reuse this pairs into dict,
#                          worst case they're all unique, so we will have # of tuples == len(l) => O(m) ->
#                          -> sorting and saving slice, which can be in the worst case same as n => O(n).


test: list[int] = [4, 6, 5, 9, 3, 7]
test_l: list[int] = [0, 0, 2]
test_r: list[int] = [2, 3, 5]
test_out: list[bool] = [True, False, True]
assert test_out == check_arithmetic_sub(test, test_l, test_r)

test = [-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10]
test_l = [0, 1, 6, 4, 8, 7]
test_r = [4, 4, 9, 7, 9, 10]
test_out = [False, True, False, False, True, True]
assert test_out == check_arithmetic_sub(test, test_l, test_r)
