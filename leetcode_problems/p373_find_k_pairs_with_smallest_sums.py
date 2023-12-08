# You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
# Define a pair (u, v) which consists of one element from the first array and one element from the second array.
# Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.
# ----------------
# 1 <= nums1.length, nums2.length <= 10 ** 5
# -10 ** 9 <= nums1[i], nums2[i] <= 10 ** 9
# nums1 and nums2 both are sorted in ascending order.
# 1 <= k <= 10 ** 4
import heapq


def k_smallest_pairs(nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
    # working_sol (77.30%, 33.50%) -> (935ms, 36.53mb)  time: O(m * n * log(m * n)) | space: O(m * n)
    # (sum of index values, index of nums1, index of nums2)
    all_sums_heap: list[tuple[int, int, int]] = []
    k_sums: list[list[int, int]] = []
    heapq.heapify(all_sums_heap)
    # Starting lowest possible sum.
    current_sum: tuple[int, int, int] = (nums1[0] + nums2[0], 0, 0)
    heapq.heappush(all_sums_heap, current_sum)
    # Used pairs of indexes.
    duplicates: set[tuple[int, int]] = {(0, 0)}
    while k and all_sums_heap:
        current_sum = heapq.heappop(all_sums_heap)
        index_nums1: int = current_sum[1]
        index_nums2: int = current_sum[2]
        # We're given arrays in ascending order, best option is to step +1 from lowest option so far.
        pair_1: tuple[int, int] = (index_nums1 + 1, index_nums2)
        pair_2: tuple[int, int] = (index_nums1, index_nums2 + 1)
        k_sums.append([nums1[index_nums1], nums2[index_nums2]])
        # If array still didn't exhausted and index pair is not used,
        #  adding this sum() and mark pair as used.
        if pair_1 not in duplicates and pair_1[0] < len(nums1):
            lowest_sum_pair: tuple[int, int, int] = (
                nums1[pair_1[0]] + nums2[pair_1[1]],
                pair_1[0],
                pair_1[1],
            )
            heapq.heappush(all_sums_heap, lowest_sum_pair)
            duplicates.add(pair_1)
        if pair_2 not in duplicates and pair_2[1] < len(nums2):
            lowest_sum_pair = (
                nums1[pair_2[0]] + nums2[pair_2[1]],
                pair_2[0],
                pair_2[1],
            )
            heapq.heappush(all_sums_heap, lowest_sum_pair)
            duplicates.add(pair_2)
        k -= 1
    return k_sums


# Time complexity: O(m * n * log(m * n)) <- m - length of input array 'nums1', n - length of input array 'nums2'.
# Worst case 'k' >= all possible combinations == m * n.
# We will use every combination of indexes and push them into a heapq.
# heapq() push(), pop() operations are log(len(heapq)) and in the end we can have heapq with all combinations.
# ----------------
# Auxiliary space: O(m * n).
# 'all_sums_heap', 'k_sums', 'duplicates' with all combinations allocated => O(3 * m * n)
# ----------------
# Can be done with calculating every combination and their sum, but because we're given sorted nums1, nums2.
# We can use heapq, to use sum of every possible pairs.
# Default pair is always the lowest values (0, 0) and any other option which going to be lowest and higher than (0, 0),
# is either (0, 1) or (1, 0). Because heap is always maintain the lowest value, we can just take it and it's indexes.
# No matter what we add into it, we just need to pop() K times, and add every possible pair into a heap on the way.


test_nums1: list[int] = [1, 7, 11]
test_nums2: list[int] = [2, 4, 6]
test_k: int = 3
test_out: list[list[int]] = [[1, 2], [1, 4], [1, 6]]
assert test_out == k_smallest_pairs(test_nums1, test_nums2, test_k)

test_nums1 = [1, 1, 2]
test_nums2 = [1, 2, 3]
test_k = 2
test_out = [[1, 1], [1, 1]]
assert test_out == k_smallest_pairs(test_nums1, test_nums2, test_k)

test_nums1 = [1, 2]
test_nums2 = [3]
test_k = 3
test_out = [[1, 3], [2, 3]]
assert test_out == k_smallest_pairs(test_nums1, test_nums2, test_k)

test_nums1 = [1]
test_nums2 = [2]
test_k = 100
test_out = [[1, 2]]
assert test_out == k_smallest_pairs(test_nums1, test_nums2, test_k)
