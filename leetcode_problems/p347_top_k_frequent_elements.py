# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.
# --------------------------
# 1 <= nums.length <= 10 ** 5  ,  -10 ** 4 <= nums[i] <= 10 ** 4
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
# --------------------------
# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    # working_sol (94.23%, 46.12%) -> (101ms, 21.2mb)  time: O(n + (log n)) | space: O(2n)
    doubles: dict[int] = {}
    for num in nums:
        if num not in doubles:
            doubles[num] = 1
            continue
        doubles[num] += 1
    reverse_doubles: list[tuple[int, int]] = list(sorted([(value, key) for (key, value) in doubles.items()]))
    reverse_doubles: list[int] = [tup[1] for tup in reverse_doubles]
    return reverse_doubles[-k:]


# Time complexity: O(n + (log n)) -> traversing through whole input_list to create dictionary with all unique_values =>
# n - len of input_list^^| => O(n) -> creating reversed + sorted version of (key, value) pairs from created dictionary
# m - num of unique values^^|  in form of a list with these pairs as tuples => O(m) ->
#                             -> taking sorted keys out of these pairs, and returning K number of keys => O(log m) ->
#                             -> O(n + m + (log m)) -> in the worst case there's no duplicates, so we can call it ->
#                             -> O(n + n + (log n)) => O(2n + (log n)) => O(n + (log n))
# --------------------------
# Auxiliary space: O(2n) -> creating dict with all unique values from nums, worst case - no duplicates => O(n) ->
#                           -> creating copy of that dictionary as a list but sorted and reversed pairs => O(n) ->
#                           -> changing tuples in this list to INTs holding keys, and returning K number of keys ->
#                           -> O(n + n) => O(2n)
# --------------------------
# Ok. Now it's faster, changed K * n scrolling through dictionary.
# Now we're rebuilding this dictionary with sorted values for keys, and after this taking key_values we need.
# [-k:] -> all keys we need.
# --------------------------
# Hmm. What about same number of duplicates?
# !
# It is guaranteed that the answer is unique. ! -> Ok. But duplicates is not the same value.
# What if there's 1 * 4,  and 8 * 4, what I should return?
# !
# return the k most frequent elements. ! -> No info about duplicates and what to do with them.
# Guess I will just fail to see what they want me to do with that.
# --------------------------
# Ok. Same approach as p217, but now we're storing count of num appearances and choosing max from dict.
# O(n) -> for create this dict -> O(n) to traverse this dict and get K frequent elements.


test1 = [1, 1, 1, 2, 2, 3]
test1_k = 2
test1_out = [1, 2]
test = top_k_frequent(test1, test1_k)
assert len(test1_out) == len(test)
for _ in test:
    assert _ in test1_out
del test

test2 = [1]
test2_k = 1
test2_out = [1]
test = top_k_frequent(test2, test2_k)
assert len(test2_out) == len(test)
for _ in test:
    assert _ in test2_out
del test

test3 = [1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 5, 5, 5, 5, 5, 5]
test3_k = 3
test3_out = [5, 2, 1]
test = top_k_frequent(test3, test3_k)
assert len(test3_out) == len(test)
for _ in test:
    assert _ in test3_out
del test

# test4 - failed -> gosh, again im getting 0 at IF check and failing it because 0 is FALSE...
#                   Always explicitly check for None!
test4 = [3, 0, 1, 0]
test4_k = 1
test4_out = [0]
test = top_k_frequent(test4, test4_k)
assert len(test4_out) == len(test)
for _ in test:
    assert _ in test4_out
del test
