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
import math


def get_permutation(n: int, k: int) -> str:
    numbers = [_ for _ in range(1, n + 1)]
    permutation = ''
    k -= 1  # for 0 - based indexing
    for x in range(n):
        n -= 1
        fact = math.factorial(n)
        index = int(k / fact)
        k = k % fact
        permutation += str(numbers[index])
        numbers.pop(index)
    return permutation

# Ok. Brute solution is fine, but there's no way to make it faster without rebuild.
# Google_time:
# The first position of an n length sequence is occupied by each of the numbers from 1 to n
# exactly n! / n that is (n-1)! number of times and in ascending order.
# So the first position of the kth sequence will be occupied by the number present at
#   index = k / (n-1)!(according to 1-based indexing).
#   index = (k - 1) / (n - 1)! (according to 0-based indexing) <- using this one.
# The currently found number can not occur again, so it is removed from the original n numbers
# and now the problem reduces to finding the ( k % (n-1)! )th permutation sequence of the remaining n-1 numbers.
# This process can be repeated until we have only one number left
# which will be placed in the first position of the last 1-length sequence.
# The factorial values involved here can be very large as compared to k.
# So, the trick used to avoid the full computation of such large factorials
# is that as soon as the product n * (n-1) * … becomes greater than k,
# we no longer need to find the actual factorial value.
# ----------------------------------------
# There's just no way to solve it for me without knowing this ^^
# Especially:
#   ! The first position of an n length sequence is occupied by each of the numbers from 1 to n
#     exactly n! / n that is (n-1)! number of times and in ascending order. !


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

test5_n = 3
test5_k = 5
test5_out = "312"
assert test5_out == get_permutation(test5_n, test5_k)
print(get_permutation(test5_n, test5_k))

test6_n = 9
test6_k = 206490
test6_out = "619754832"
assert test6_out == get_permutation(test6_n, test6_k)
print(get_permutation(test6_n, test6_k))

test7_n = 9
test7_k = 219601
test7_out = "647123589"
assert test7_out == get_permutation(test7_n, test7_k)
print(get_permutation(test7_n, test7_k))
