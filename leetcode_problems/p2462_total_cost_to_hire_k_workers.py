# You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the ith worker.
# You are also given two integers k and candidates.
# We want to hire exactly k workers according to the following rules:
#   You will run k sessions and hire exactly one worker in each session.
#   In each hiring session, choose the worker with the lowest cost from either the first candidates workers
#       or the last candidates workers. Break the tie by the smallest index.
#   For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first hiring session,
#       we will choose the 4th worker because they have the lowest cost [3,2,7,7,1,2].
#   In the second hiring session, we will choose 1st worker because they have the same lowest cost as 4th worker,
#       but they have the smallest index [3,2,7,7,2]. Please note that the indexing may be changed in the process.
#   If there are fewer than candidates workers remaining, choose the worker with the lowest cost among them.
#       Break the tie by the smallest index.
#   A worker can only be chosen once.
# Return the total cost to hire exactly k workers.
# ------------------------
# 1 <= costs.length <= 10 ** 5
# 1 <= costs[i] <= 10 ** 5
# 1 <= k, candidates <= costs.length
import heapq


def total_cost(costs: list[int], k: int, candidates: int) -> int:
    # working_sol (60.27%, 81.88%) -> (860ms, 26.9mb)  time: O(n) | space: O(n)
    left_index: int = 0
    right_index: int = len(costs) - 1
    left_list: heapq = []
    heapq.heapify(left_list)
    right_list: heapq = []
    heapq.heapify(right_list)
    cost_to_hire: int = 0
    # if we have 2 * candidates, then there's a reason to store them
    # as left or right to compare indexes.
    # otherwise we can just make 1 heapq and take min_values from it.
    if len(costs) // 2 >= candidates:
        while len(left_list) != candidates:
            heapq.heappush(left_list, costs[left_index])
            heapq.heappush(right_list, costs[right_index])
            left_index += 1
            right_index -= 1
    else:
        # in case of 1 side heap, we just take every min_value
        # indexes isn't a problem
        while len(left_list) != len(costs):
            heapq.heappush(left_list, costs[left_index])
            left_index += 1
        while k:
            cost_to_hire += heapq.heappop(left_list)
            k -= 1
        return cost_to_hire
    # same rule if we can sustain left and right parts as whole,
    # we should use them to see indexes.
    # otherwise we need a 1 heap to get all min_values no matter indexing.
    while k and left_index <= right_index:
        left_candi: int | None = left_list[0]
        right_candi: int | None = right_list[0]
        if left_candi < right_candi:
            cost: int = heapq.heappop(left_list)
            cost_to_hire += cost
            k -= 1
        elif right_candi < left_candi:
            cost: int = heapq.heappop(right_list)
            cost_to_hire += cost
            k -= 1
        elif left_candi == right_candi:
            cost: int = heapq.heappop(left_list)
            cost_to_hire += cost
            k -= 1
        if len(left_list) != candidates and left_index <= right_index:
            heapq.heappush(left_list, costs[left_index])
            left_index += 1
        if len(right_list) != candidates and left_index <= right_index:
            heapq.heappush(right_list, costs[right_index])
            right_index -= 1
    # extra checking for k == 0,
    # because we could still don't exhaust hiring potential
    if k == 0:
        return cost_to_hire
    # sorting to correct merge, because we're getting iterator
    # with just 2 heaps merged together, if they're not sorted
    # it will lead to 2 unsorted lists, which is incorrect.
    left_list.sort()
    right_list.sort()
    merged: iter = iter(heapq.merge(left_list, right_list))
    # exhaust hiring potential
    while k:
        cost_to_hire += next(merged)
        k -= 1
    return cost_to_hire


# Time complexity: O(n) -> overall we're just traversing whole input_list once to add values into a heapq and
# n - len of input_list^^| compare them between left_right part, or just taking min_values from one heapq => O(n)
#                          ^^There's sorting part, but we're sorting only left and right lists, which is
#                            O(log n * log n) -> size of (log n) and sort() <- (size * log size).
#                            Ignoring that, because it's lower than O(n), and in the case when our candidates
#                            will be higher than len(counts) // 2, we're not sorting at all,
#                            and just using 1 heapq of size n. All operations in heapq -> pop(), push() => O(1).
# Auxiliary space: O(n) -> in the worst case, there's candidates > len(count) // 2, then
#                          we're creating one heapq of size n => O(n).
#                          In most cases we're creating 2 heapq's, but combined they will never be more
#                          than size of candidates * 2 and always lower than n.
# ------------------------
# Used hints to use HEAPQ, that's it on extra info.
# Failed first commit because -> low on experience with heaps and didn't know I need to sort() them explicitly before
#                                merging, otherwise I was taking unsorted values from default_list.
# Rebuild this without merging, and it worked, and fixed this part to work with merging.


test1 = [17, 12, 10, 2, 7, 2, 11, 20, 8]
test1_k = 3
test1_candidates = 4
test1_out = 11
print(total_cost(test1, test1_k, test1_candidates))
assert test1_out == total_cost(test1, test1_k, test1_candidates)

test2 = [1, 2, 4, 1]
test2_k = 3
test2_candidates = 3
test2_out = 4
print(total_cost(test2, test2_k, test2_candidates))
assert test2_out == total_cost(test2, test2_k, test2_candidates)

test3 = [7, 7, 7, 7, 7, 7, 7]
test3_k = 7
test3_candidates = 7
test3_out = 49
print(total_cost(test3, test3_k, test3_candidates))
assert test3_out == total_cost(test3, test3_k, test3_candidates)

test4 = [1, 2, 2, 1]
test4_k = 2
test4_candidates = 2
test4_out = 2
print(total_cost(test4, test4_k, test4_candidates))
assert test4_out == total_cost(test4, test4_k, test4_candidates)

# test5 - failed -> I was thinking merge will autosort_heaps, and we can just take next() until we want it.
#                   Well it doesn't :)
#                   The actual mistake here is that I'm not having much experience with HEAPS, and I was thinking,
#                   that if I heapify() any list it's going to be sorted by default, and we can merge them together.
#                   But I was wrong, and we need to use heap.sort() explicitly.
test5 = [28, 35, 21, 13, 21, 72, 35, 52, 74, 92, 25, 65, 77, 1, 73, 32, 43, 68, 8, 100, 84, 80, 14, 88, 42, 53, 98, 69,
         64, 40, 60, 23, 99, 83, 5, 21, 76, 34]
test5_k = 32
test5_candidates = 12
test5_out = 1407
print(total_cost(test5, test5_k, test5_candidates))
assert test5_out == total_cost(test5, test5_k, test5_candidates)
