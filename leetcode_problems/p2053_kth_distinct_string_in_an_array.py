# A distinct string is a string that is present only once in an array.
# Given an array of strings arr, and an integer k,
#  return the kth distinct string present in arr.
# If there are fewer than k distinct strings, return an empty string "".
# Note that the strings are considered in the order in which they appear in the array.
# -----------------------------
# 1 <= k <= arr.length <= 1000
# 1 <= arr[i].length <= 5
# arr[i] consists of lowercase English letters.
from random import choice, randint
from string import ascii_lowercase


def kth_distinct(arr: list[str], k: int) -> str:
    # working_sol (98.18%, 75.33%) -> (56ms, 16.77mb)  time: O(n * log n) | space: O(n)
    # { string: first_index }
    occurs: dict[str, int] = {}
    # { string: first_and_last_index}
    singles: dict[str, int] = {}
    for index, string in enumerate(arr):
        if string in occurs:
            if string in singles:
                singles.pop(string)
        else:
            occurs[string] = index
            singles[string] = index
    if len(singles) < k:
        return ""
    order: list[str] = sorted(singles.keys(), key=lambda x: singles[x])
    return order[k - 1]


# Time complexity: O(n * log n) <- n - length of the input array `arr`.
# Always traversing whole input array `arr`, once to get all the strings and their occurrences => O(n).
# In the worst case, every string is unique, so we will sort whole `arr` => O(n * log n + n).
# -----------------------------
# Auxiliary space: O(n)
# `occurs` <- always stores every string from `arr` => O(n).
# `singles` <- in the worst case with every string being unique, every string will be stored => O(2 * n).
# `order` <- extra array of size `n` to store every unique value => O(3 * n).


test: list[str] = ["d", "b", "c", "b", "c", "a"]
test_k: int = 2
test_out: str = "a"
assert test_out == kth_distinct(test, test_k)

test = ["aaa", "aa", "a"]
test_k = 1
test_out = "aaa"
assert test_out == kth_distinct(test, test_k)

test = ["a", "b", "a"]
test_k = 3
test_out = ""
assert test_out == kth_distinct(test, test_k)

test = [''.join([choice(ascii_lowercase) for _ in range(randint(1, 5))]) for _ in range(1000)]
print(test)
