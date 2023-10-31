# You are given an integer array pref of size n.
# Find and return the array arr of size n that satisfies:
#   pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].
# Note that ^ denotes the bitwise-xor operation.
# It can be proven that the answer is unique.
# ---------------------
# 1 <= pref.length <= 10 ** 5
# 0 <= pref[i] <= 10 ** 6
from random import randint


def find_array(pref: list[int]) -> list[int]:
    # working_sol (71.45%, 57.35%) -> (661ms, 36.36mb)  time: O(n) | space: O(n)
    # pref[0] == array[0], because there's no prefix for 0 index.
    array: list[int] = [pref[0]]
    # We can reuse prefixes:
    #  pref[1] = | 5 ^ 7 = 2 |
    #  pref[2] = | 5 ^ 7 | ^ array[2] = 0 -> array[2] = 0 ^ 2
    #  pref[3] = | 5 ^ 7 ^ 2 | ^ array[3] = 3 -> array[3] = 3 ^ 0 etc.
    for x in range(1, len(pref)):
        array.append(pref[x] ^ pref[x - 1])
    return array


# Time complexity: O(n) -> using n indexes of input array 'pref' => O(n).
# n - len of input array 'pref'^^|
# Auxiliary space: O(n) -> always creating array with the same size as input array 'pref' => O(n).
# ---------------------
# Pref == [5,2,0,3,1]
# Array == [5,7,2,3,2].
# - pref[0] = 5.
# - pref[1] = 5 ^ 7 = 2.
# - pref[2] = 5 ^ 7 ^ 2 = 0.
# - pref[3] = 5 ^ 7 ^ 2 ^ 3 = 3.
# - pref[4] = 5 ^ 7 ^ 2 ^ 3 ^ 2 = 1
# We're just annulling all '1' with 5 ^ 7 and getting => 2.
# And if we want to restore this '1' we can just 5 ^ 2 => 7.
# Because everything what was annulled by 7 in 5 will stay at place, and '1' which was placed in 2,
#  by relation '1' -> '0' will be annulled => we will get 7.
# 7 == 111 , 5 == 101 , 2 == 010
# 5 ^ 7 => 010
# 5 ^ 2 => 111
# And because we're already given example:
# - pref[1] = | 5 ^ 7 = 2 |
# - pref[2] = | 5 ^ 7 | ^ ?? = 0 -> ?? = 2 ^^ 0
# We can reuse prefixes => like: ! pref[x] ^ pref[x - 1] !
# Except [0] this one is always array[0] == pref[0].
# Should be correct.


test: list[int] = [5, 2, 0, 3, 1]
test_out: list[int] = [5, 7, 2, 3, 2]
assert test_out == find_array(test)

test = [13]
test_out = [13]
assert test_out == find_array(test)

test = [randint(0, 10 ** 6) for _ in range(10 ** 4)]
print(test)
