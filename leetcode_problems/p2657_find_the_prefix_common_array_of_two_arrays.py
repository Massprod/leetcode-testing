# You are given two 0-indexed integer permutations A and B of length n.
# A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers
#  that are present at or before the index i in both A and B.
# Return the prefix common array of A and B.
# A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.
# -------------------------
# 1 <= A.length == B.length == n <= 50
# 1 <= A[i], B[i] <= n
# It is guaranteed that A and B are both a permutation of n integers.
from random import shuffle
from collections import defaultdict


def find_the_prefix_common_array(A: list[int], B: list[int]) -> list[int]:
    # working_sol (60.99%, 88.89%) -> (113ms, 16.50mb)  time: O(n) | space: O(n)
    out: list[int] = []
    prefix: int = 0
    # { value: occurrences }
    counter: dict[int, int] = defaultdict(int)
    for index in range(len(A)):
        counter[A[index]] += 1
        counter[B[index]] += 1
        if 1 < counter[A[index]]:
            prefix += 1
            # Only 1 occurrence of value in `A` and `B`
            # We can annul it after we get a pair.
            counter[A[index]] = 0
        if 1 < counter[B[index]]:
            prefix += 1
            counter[B[index]] = 0
        out.append(prefix)
    return out


# Time complexity: O(n) <- n - length of the input array `A` | `B`.
# Always traversing every index of `A` => O(n).
# -------------------------
# Auxiliary space: O(n)
# We always have sequence with unique values in inclusive range 1 -> n.
# All these values going to be stored in `counter` => O(n).


test_A: list[int] = [1, 3, 2, 4]
test_B: list[int] = [3, 1, 2, 4]
test_out: list[int] = [0, 2, 3, 4]
assert test_out == find_the_prefix_common_array(test_A, test_B)

test_A = [2, 3, 1]
test_B = [3, 1, 2]
test_out = [0, 1, 3]
assert test_out == find_the_prefix_common_array(test_A, test_B)

test_A = [val for val in range(1, 51)]
shuffle(test_A)
print(test_A)
