# The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
# By listing and labeling all the permutations in order, we get the following sequence for n = 3:
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.
# 1 <= n <= 9 | 1 <= k <= n!

def get_permutation(n: int, k: int) -> str:
    to_permute: list[int] = [_ for _ in range(1, n + 1)]
    permutes: list[list[int]] = []

    def rec_permute(to_check: list[int], start_ind: int = 0):
        if start_ind == len(to_check):
            permutes.append(to_check.copy())
            return
        for x in range(start_ind, len(to_check)):
            if to_check[x] == to_check[start_ind] and start_ind != x:
                continue
            to_check[x], to_check[start_ind] = to_check[start_ind], to_check[x]
            rec_permute(to_check, start_ind + 1)
            to_check[x], to_check[start_ind] = to_check[start_ind], to_check[x]
    rec_permute(to_permute, 0)
    permutes.sort()
    k_permute: str = ""
    for _ in permutes[k - 1]:
        k_permute += str(_)
    return k_permute

# Used p47 solution to create unique permutations, but there was used unordered set() and now using list -> slower.
# --------------------------------
# This descriptions...
# ! The set [1, 2, 3, ..., n] contains a total of n! unique permutations !
# Where's this set??
# Should I create it?? For what??
# Can I use list with 1 - n values??
# I'm only given n -> which is last number of sequence from 1 to n.


test1_n = 3
test1_k = 3
test1_out = "213"
assert test1_out == get_permutation(test1_n, test1_k)
print(get_permutation(test1_n, test1_k))

test2_n = 4
test2_k = 9
test2_out = "2314"
assert test2_out == get_permutation(test2_n, test2_k)
print(get_permutation(test2_n, test2_k))

test3_n = 3
test3_k = 1
test3_out = "123"
assert test3_out == get_permutation(test3_n, test3_k)
print(get_permutation(test3_n, test3_k))

test4_n = 9
test4_k = 1
test4_out = "123456789"
assert test4_out == get_permutation(test4_n, test4_k)
print(get_permutation(test4_n, test4_k))

# test5 - failed -> most certain, because I was not sorting list, and wanted to just stop search at K permutation.
#               ! By listing and labeling all the permutations in order, we get the following sequence !
#               ^^ it can be solved like this, but then I need to find every possible permutation, and 100% sure
#                  time limit is here.
test5_n = 3
test5_k = 5
test5_out = "312"
assert test5_out == get_permutation(test5_n, test5_k)
print(get_permutation(test5_n, test5_k))

# test6 - failed -> Yep. Time_limit, cuz there's no way it's just repeating of p47, and I need to find way to stop
#                   recursion at some moment. Already tried to simple count of adding unique_permutes and stop at k.
test6_n = 9
test6_k = 206490
test6_out = "619754832"
print(get_permutation(test6_n, test6_k))

# test7 - failed -> Time_limit, if I stop permutations at some point my solution isn't going to work,
#                   cuz there's either other solution with correct order of permutations or IDK.
#                   Because it's obviously going to work with full list of all_unique_permutations in ascending order.
test7_n = 9
test7_k = 219601
test7_out = "647123589"
print(get_permutation(test7_n, test7_k))
