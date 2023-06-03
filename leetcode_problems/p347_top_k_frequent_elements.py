# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.
# --------------------------
# 1 <= nums.length <= 10 ** 5  ,  -10 ** 4 <= nums[i] <= 10 ** 4
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
# --------------------------
# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


def top_k_frequent(nums: list[int], k: int) -> list[int]:
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
            if not max_key:
                max_key = key
                continue
            if doubles[max_key] < doubles[key]:
                max_key = key
        top_values.append(max_key)
        del doubles[max_key]
        max_key = None
        step += 1
    return top_values


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

test2 = [1]
test2_k = 1
test2_out = [1]
print(top_k_frequent(test2, test2_k))

test3 = [1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 5, 5, 5, 5, 5, 5]
test3_k = 3
test3_out = [1, 3, 5]
print(top_k_frequent(test3, test3_k))
