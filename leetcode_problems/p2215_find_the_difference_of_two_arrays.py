# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
#   answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
#   answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.
# -----------------------
# 1 <= nums1.length, nums2.length <= 1000
# -1000 <= nums1[i], nums2[i] <= 1000


def find_difference_sets(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    # working_sol (94.98%, 82.94%) -> (176ms, 16.7mb)  time: O(2 * (n + m)) | space: O(2 * ((log g) + (log h))
    set1: set[int] = set(nums1)
    set2: set[int] = set(nums2)
    answer: list[list[int]] = [
        [num for num in set1 if num not in set2],
        [num for num in set2 if num not in set1],
    ]
    return answer


# Time complexity: O(2 * (n + m)) -> worst case, there's no duplicates, creating sets for nums1, nums2 => O(n + m) ->
# n - len of set1^^|   -> traversing whole set1 to create first list of answer => O(n) ->
# m - len of set2^^|   -> traversing whole set2 to create second list of answer => O(m) -> O(2*(n + m))
# Space complexity: O(2 * ((log g) + (log h)) -> creating set1 of (nums1 - number of duplicates) => O(log g) ->
# g - len of nums1^^| -> creating set2 of (nums2 - number of duplicates) => O(log h) ->
# h - len os nums2^^| -> in the worst case there's no counterparts, creating list(answer) with size of (set1 + set2) =>
#                     => O((log g) + (log h)) -> O(2 * ((log g) + (log h))
# -----------------------
# Yep. Faster. But I'm 99% sure it's only faster if we're having a lot of duplicates,
# because if there's no duplicates we're wasting extra step to create set.
# But if we don't have duplicates I could implement slicing from the start, which is always faster(slicing_fastest).
# For a future use -> if I have a lot of duplicates, always delete them with set, instead of checking every one by one.
# -----------------------
# Or I could just use set() to remove duplicates and scroll created sets after it.
# Should be faster, because otherwise, we're checking every duplicate being in used every time,
# and if we're creating sets without duplicates we're going to skip this check.
# Extra to this we could use slicing because there's no duplicates.


def find_difference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    # working_sol (16.33%, 40.61%) -> (750ms, 16.8mb)  time: O(max(n, m)) | space: O(2 * (n + m))
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
# n - len of nums1^^| => O(max(n, m)) or O(j) - where's j is len of longest input_list.
# m - len of nums2^^|
# Space complexity: O((n + m) + (n + m)) -> in the worst case, creating lists with all values from both inputs,
#                                           because there's no values presents in counterpart => O(n + m) ->
#                                        -> and there's duplicate for every value in input_lists,
#                                           creating set of size (n + m) => O(n + m) ->
#                                        -> leading us to => O((n + m) + (n + m)) => O(2 * (n + m))
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
assert test1_out == find_difference_sets(test1_nums1, test1_nums2)

test2_nums1 = [1, 2, 3, 3]
test2_nums2 = [1, 1, 2, 2]
test2_out = [[3], []]
print(find_difference(test2_nums1, test2_nums2))
assert test2_out == find_difference(test2_nums1, test2_nums2)
assert test2_out == find_difference_sets(test2_nums1, test2_nums2)
