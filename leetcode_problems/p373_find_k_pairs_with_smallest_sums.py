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
    all_sums_heap: list[tuple[int, int, int]] = []
    all_sums: list[list[int, int]] = []
    heapq.heapify(all_sums_heap)
    default_sum: tuple[int, int, int] = (nums1[0] + nums2[0], 0, 0)
    heapq.heappush(all_sums_heap, default_sum)
    duplicates: set[tuple[int, int]] = {(0, 0)}
    while k and all_sums_heap:
        current_sum: tuple[int, int, int] = heapq.heappop(all_sums_heap)
        index_nums1: int = current_sum[1]
        index_nums2: int = current_sum[2]
        pair_1: tuple[int, int] = (index_nums1 + 1, index_nums2)
        pair_2: tuple[int, int] = (index_nums1, index_nums2 + 1)
        all_sums.append([nums1[index_nums1], nums2[index_nums2]])
        if (index_nums1 + 1) < len(nums1) and pair_1 not in duplicates:
            sum_pair: tuple[int, int, int] = (
                nums1[index_nums1 + 1] + nums2[index_nums2],
                index_nums1 + 1,
                index_nums2
            )
            heapq.heappush(all_sums_heap, sum_pair)
            duplicates.add(pair_1)
        if (index_nums2 + 1) < len(nums2) and pair_2 not in duplicates:
            sum_pair = (
                nums1[index_nums1] + nums2[index_nums2 + 1],
                index_nums1,
                index_nums2 + 1
            )
            heapq.heappush(all_sums_heap, sum_pair)
            duplicates.add(pair_2)
        k -= 1
    return all_sums


test1_1 = [1, 7, 11]
test1_2 = [2, 4, 6]
test1_k = 3
test1_out = [[1, 2], [1, 4], [1, 6]]
print(k_smallest_pairs(test1_1, test1_2, test1_k))

test2_1 = [1, 1, 2]
test2_2 = [1, 2, 3]
test2_k = 2
test2_out = [[1, 1], [1, 1]]
print(k_smallest_pairs(test2_1, test2_2, test2_k))

test3_1 = [1, 2]
test3_2 = [3]
test3_k = 3
test3_out = [[1, 3], [2, 3]]
print(k_smallest_pairs(test3_1, test3_2, test3_k))

test4_1 = [1]
test4_2 = [2]
test4_k = 100
test4_out = [1, 2]
print(k_smallest_pairs(test4_1, test4_2, test4_k))
