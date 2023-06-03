# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.
# --------------------------
# 1 <= nums.length <= 10 ** 5  ,  -10 ** 4 <= nums[i] <= 10 ** 4
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
# --------------------------
# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    # working_sol (5.2%, 64.58%) -> (264ms, 21.1mb)  time: O(n) | space: O(n + k)
    doubles: dict[int] = {}
    for num in nums:
        if num not in doubles:
            doubles[num] = 1
            continue
        doubles[num] += 1
    top_values: list[int] = []
    max_key: int | None = None
    step: int = 0
    while step != k:
        for key in doubles:
            if max_key is None:
                max_key = key
                continue
            if doubles[max_key] < doubles[key]:
                max_key = key
        top_values.append(max_key)
        del doubles[max_key]
        max_key = None
        step += 1
    return top_values


# Time complexity: O(n) -> traversing input_list once to recreate dict_counter for every value => O(n) ->
# n - len of input_list^^| -> checking every value in dictionary for K times to get K_max_values => O(1 * k) ->
#                          -> appending this values into top_values => O(1) -> O(n)
# ^^It's correct if we assume that all HASH operations with dictionaries is O(1).
# But I think it's O(n * k + n), because I'm still not convicted that dict operations even if there's N of them is O(1).
# --------------------------
# Auxiliary space: O(n + k) -> creating dict with all unique values from nums, worst case - no duplicates => O(n) ->
#                               -> creating top_values list with K number of values in it => O(k) -> O(n + k)
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
print(top_k_frequent(test1, test1_k))
assert test1_out == top_k_frequent(test1, test1_k)

test2 = [1]
test2_k = 1
test2_out = [1]
print(top_k_frequent(test2, test2_k))
assert test2_out == top_k_frequent(test2, test2_k)

test3 = [1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 5, 5, 5, 5, 5, 5]
test3_k = 3
test3_out = [5, 2, 1]
print(top_k_frequent(test3, test3_k))
assert test3_out == top_k_frequent(test3, test3_k)

# test4 - failed -> gosh, again im getting 0 at IF check and failing it because 0 is FALSE...
#                   Always explicitly check for None!
test4 = [3, 0, 1, 0]
test4_k = 1
test4_out = [0]
print(top_k_frequent(test4, test4_k))
assert test4_out == top_k_frequent(test4, test4_k)
