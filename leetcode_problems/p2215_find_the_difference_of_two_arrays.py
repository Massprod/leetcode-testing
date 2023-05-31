# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
#   answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
#   answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.
# -----------------------
# 1 <= nums1.length, nums2.length <= 1000
# -1000 <= nums1[i], nums2[i] <= 1000


def find_difference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    answer: list[list[int]] = [[], []]
    used: set[int] = set()
    for _ in nums1:
        if (_ not in used) and (_ not in nums2):
            answer[0].append(_)
            used.add(_)
    for _ in nums2:
        if (_ not in used) and (_ not in nums1):
            answer[1].append(_)
            used.add(_)
    return answer

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
