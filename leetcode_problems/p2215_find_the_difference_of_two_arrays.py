# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
#   answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
#   answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.
# -----------------------
# 1 <= nums1.length, nums2.length <= 1000
# -1000 <= nums1[i], nums2[i] <= 1000


def find_difference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    # working_sol (16.33%, 40.61%) -> (750ms, 16.8mb)  time: O(max(n, m)) | space: O(2*(n + m))
    answer: list[list[int]] = [[], []]
    used: set[int] = set()
    for x in range(max(len(nums1), len(nums2))):
        if (x < len(nums1)) and (nums1[x] not in used) and (nums1[x] not in nums2):
            answer[0].append(nums1[x])
            used.add(nums1[x])
        if (x < len(nums2)) and (nums2[x] not in used) and (nums2[x] not in nums1):
            answer[1].append(nums2[x])
            used.add(nums2[x])
    return answer


# Time complexity: O(max(n, m)) -> checking every index in nums1 and nums2 once, but looping for max_len of 2 inputs =>
# n - len of nums1^^| => O(max(n, m)) or O(n) - where's n is len of longest input_list.
# m - len of nums2^^|
# Space complexity: O((n + m) + (n + m)) -> in the worst case, creating lists with all values from both inputs,
#                                           because there's no values presents in counterpart => O(n + m) ->
#                                        -> and there's duplicate for every value in input_lists,
#                                           creating set of size (n + m) => O(n + m) ->
#                                        -> leading us to => O((n + m) + (n + m)) => O(2(n + m))
# -----------------------
# Or I could just use set() to remove duplicates and scroll created sets after it.
# Should be faster, because otherwise, we're checking every duplicate being in used every time,
# and if we're creating sets without duplicates we're going to skip this check.
# -----------------------
# Yep. I was correct they're not equal length.
# -----------------------
# If we knew that len(nums1) == len(nums2), than I could do this with 1 loop.
# !
# 1 <= nums1.length, nums2.length <= 1000 ! <- Is that equal length or just range for one of them?
# Well, it's looking like len(nums1) == len(nums2), first one is correct let's fail with this assumption than.
# -----------------------
# How to do this with slicing? Duplicates can't be checked before we create a list.
# Slicing could be faster, but I don't see how we can check for duplicates.
# Slicing doesn't allow us to check if it's already added into created list, at least I don't know how.


test1_nums1 = [1, 2, 3]
test1_nums2 = [2, 4, 6]
test1_out = [[1, 3], [4, 6]]
print(find_difference(test1_nums1, test1_nums2))
assert test1_out == find_difference(test1_nums1, test1_nums2)

test2_nums1 = [1, 2, 3, 3]
test2_nums2 = [1, 1, 2, 2]
test2_out = [[3], []]
print(find_difference(test2_nums1, test2_nums2))
assert test2_out == find_difference(test2_nums1, test2_nums2)
