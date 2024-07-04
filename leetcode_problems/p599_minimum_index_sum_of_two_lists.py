# Given two arrays of strings list1 and list2,
#  find the common strings with the least index sum.
# A common string is a string that appeared in both list1 and list2.
# A common string with the least index sum is a common string such that
#  if it appeared at list1[i] and list2[j] then i + j should be the minimum value
#  among all the other common strings.
# Return all the common strings with the least index sum.
# Return the answer in any order.
# ------------------------
# 1 <= list1.length, list2.length <= 1000
# 1 <= list1[i].length, list2[i].length <= 30
# list1[i] and list2[i] consist of spaces ' ' and English letters.
# All the strings of list1 are unique.
# All the strings of list2 are unique.
# There is at least a common string between list1 and list2.
from collections import defaultdict


def find_restaurant(list1: list[str], list2: list[str]) -> list[str]:
    # working_sol (68.03%, 88.99%) -> (144ms, 16.98mb)  time: O(n + k) | space: O(min(n, k))
    min_list: list[str]
    max_list: list[str]
    cur_min: int = 10000 + 1
    out: list[str] = []
    all_strings: dict[str, int] = defaultdict(int)
    if len(list1) < len(list2):
        min_list = list1
        max_list = list2
    else:
        min_list = list2
        max_list = list1
    for index, string in enumerate(min_list):
        all_strings[string] += index
    for index, string in enumerate(max_list):
        if string not in all_strings:
            continue
        all_strings[string] += index
        if all_strings[string] < cur_min:
            out = []
            cur_min = all_strings[string]
            out.append(string)
        elif all_strings[string] == cur_min:
            out.append(string)
    return out


# Time complexity: O(n + k) <- n - length of the input array `list1`, k - length of the input array `list2`.
# We're always traversing both input arrays `list1` and `list2`, once => O(n + k).
# ------------------------
# Auxiliary space: O(min(n, k))
# We're always storing all strings from a minimum list of the input lists inside `all_strings` => O(n).
# And in the worst case, every string from `list1` will be present in `list2` in style like:
# ['a', 'b', 'c'] == list1 ; ['c', 'b', 'a'] == list2
# So, we're going to have all of them having the same indexes sum and every1 added in `out` => O(2n).


test_1: list[str] = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
test_2: list[str] = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
test_out: list[str] = ["Shogun"]
assert test_out == find_restaurant(test_1, test_2)

test_1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
test_2 = ["KFC", "Shogun", "Burger King"]
test_out = ["Shogun"]
assert test_out == find_restaurant(test_1, test_2)

test_1 = ["happy", "sad", "good"]
test_2 = ["sad", "happy", "good"]
test_out = ["happy", "sad"]
assert test_out == find_restaurant(test_1, test_2)
