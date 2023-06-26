# You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the ith worker.
# You are also given two integers k and candidates.
# We want to hire exactly k workers according to the following rules:
#   You will run k sessions and hire exactly one worker in each session.
#   In each hiring session, choose the worker with the lowest cost from either the first candidates workers
#       or the last candidates workers. Break the tie by the smallest index.
#   For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first hiring session,
#       we will choose the 4th worker because they have the lowest cost [3,2,7,7,1,2].
#   In the second hiring session, we will choose 1st worker because they have the same lowest cost as 4th worker
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
    left_index: int = 0
    right_index: int = len(costs) - 1
    left_list: heapq = []
    heapq.heapify(left_list)
    right_list: heapq = []
    heapq.heapify(right_list)
    cost_to_hire: int = 0
    if len(costs) // 2 >= candidates:
        while len(left_list) != candidates:
            heapq.heappush(left_list, costs[left_index])
            heapq.heappush(right_list, costs[right_index])
            left_index += 1
            right_index -= 1
    else:
        while len(left_list) != len(costs):
            heapq.heappush(left_list, costs[left_index])
            left_index += 1
        while k:
            cost_to_hire += heapq.heappop(left_list)
            k -= 1
        return cost_to_hire
    left_list.sort()
    right_list.sort()
    print(left_list)
    print(right_list)
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
    if k == 0:
        return cost_to_hire
    while k:
        if len(left_list) > 0:
            left_candi = left_list[0]
        else:
            left_candi = None
        if len(right_list) > 0:
            right_candi = right_list[0]
        else:
            right_candi = None
        if left_candi and right_candi:
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
        elif left_candi:
            cost_to_hire += heapq.heappop(left_list)
            k -= 1
        elif right_candi:
            cost_to_hire += heapq.heappop(right_list)
            k -= 1
    return cost_to_hire


test1 = [17, 12, 10, 2, 7, 2, 11, 20, 8]
test1_k = 3
test1_candidates = 4
test1_out = 11
print(total_cost(test1, test1_k, test1_candidates))

test2 = [1, 2, 4, 1]
test2_k = 3
test2_candidates = 3
test2_out = 4
print(total_cost(test2, test2_k, test2_candidates))

test3 = [7, 7, 7, 7, 7, 7, 7]
test3_k = 7
test3_candidates = 7
test3_out = 49
print(total_cost(test3, test3_k, test3_candidates))

test4 = [1, 2, 2, 1]
test4_k = 2
test4_candidates = 2
test4_out = 10
print(total_cost(test4, test4_k, test4_candidates))

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
