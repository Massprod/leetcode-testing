# You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the ith worker.
# You are also given two integers k and candidates.
# We want to hire exactly k workers according to the following rules:
#   You will run k sessions and hire exactly one worker in each session.
#   In each hiring session, choose the worker with the lowest cost from either the first candidates workers
#      or the last candidates workers. Break the tie by the smallest index.
#   For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first hiring session,
#      we will choose the 4th worker because they have the lowest cost [3,2,7,7,1,2].
#   In the second hiring session, we will choose 1st worker because they have the same lowest cost as 4th worker,
#      but they have the smallest index [3,2,7,7,2]. Please note that the indexing may be changed in the process.
#   If there are fewer than candidates workers remaining, choose the worker with the lowest cost among them.
#      Break the tie by the smallest index.
#   A worker can only be chosen once.
# Return the total cost to hire exactly k workers.
# ------------------------
# 1 <= costs.length <= 10 ** 5
# 1 <= costs[i] <= 10 ** 5
# 1 <= k, candidates <= costs.length
import heapq


def total_cost(costs: list[int], k: int, candidates: int) -> int:
    # working_sol (97.06%, 81.88%) -> (707ms, 26.9mb)  time: O(n) | space: O(n)
    left_index: int = 0
    right_index: int = len(costs) - 1
    left_list: heapq = []
    heapq.heapify(left_list)
    right_list: heapq = []
    heapq.heapify(right_list)
    cost_to_hire: int = 0
    # If we have costs >= (2 * candidates), then there's a reason
    #  to store them as left or right to compare indexes.
    # Otherwise, we can just make 1 heap and take min_values from it.
    # Because candidates will cover whole array, indexes doesn't matter.
    if len(costs) // 2 >= candidates:
        while len(left_list) != candidates:
            heapq.heappush(left_list, costs[left_index])
            heapq.heappush(right_list, costs[right_index])
            left_index += 1
            right_index -= 1
    else:
        # Candidates cover whole array, we can take w.e we want.
        while len(left_list) != len(costs):
            heapq.heappush(left_list, costs[left_index])
            left_index += 1
        while k:
            cost_to_hire += heapq.heappop(left_list)
            k -= 1
        return cost_to_hire
    # Same approach, we only care about candidates being separated.
    # If they can cover whole array(after deleting hired).
    # We can take whoever we want, indexes doesn't matter.
    # And they're separated while left_index != right index.
    while k and left_index <= right_index:
        left_candi: int = left_list[0]
        right_candi: int = right_list[0]
        if left_candi < right_candi:
            cost: int = heapq.heappop(left_list)
            cost_to_hire += cost
            k -= 1
        elif right_candi < left_candi:
            cost = heapq.heappop(right_list)
            cost_to_hire += cost
            k -= 1
        # left_list -> candidates with Lower indexes.
        # right_list -> candidates with Higher indexes.
        elif left_candi == right_candi:
            cost = heapq.heappop(left_list)
            cost_to_hire += cost
            k -= 1
        if len(left_list) != candidates:
            heapq.heappush(left_list, costs[left_index])
            left_index += 1
        if len(right_list) != candidates:
            heapq.heappush(right_list, costs[right_index])
            right_index -= 1
    # Extra check for k == 0,
    #  because we still can have hiring potential
    if k == 0:
        return cost_to_hire
    # Sorting for correct merging -> heapq.merge()
    # -> ! Merge multiple sorted inputs into a single sorted output !
    left_list.sort()
    right_list.sort()
    merged: iter = iter(heapq.merge(left_list, right_list))
    # Exhaust hiring potential.
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
#                            and just using 1 heapq of size n. All operations in heapq -> pop(), push() => O(log n).
# Auxiliary space: O(n) -> in the worst case, there's candidates > len(count) // 2, then
#                          we're creating one heapq of size n => O(n).
#                          In most cases we're creating 2 heapq's, but combined they will never be more
#                          than size of candidates * 2 and always lower than n.
# ------------------------
# Used hints to use HEAPQ, that's it on extra info.
# Failed first commit because -> low on experience with heaps and didn't know I need to sort() them explicitly before
#                                merging, otherwise I was taking unsorted values from default_list.
# Rebuild this without merging, and it worked, and fixed this part to work with merging.


test: list[int] = [17, 12, 10, 2, 7, 2, 11, 20, 8]
test_k: int = 3
test_candidates: int = 4
test_out: int = 11
assert test_out == total_cost(test, test_k, test_candidates)

test = [1, 2, 4, 1]
test_k = 3
test_candidates = 3
test_out = 4
assert test_out == total_cost(test, test_k, test_candidates)

test = [7, 7, 7, 7, 7, 7, 7]
test_k = 7
test_candidates = 7
test_out = 49
assert test_out == total_cost(test, test_k, test_candidates)

test = [1, 2, 2, 1]
test_k = 2
test_candidates = 2
test_out = 2
assert test_out == total_cost(test, test_k, test_candidates)

# test5 - failed -> I was thinking merge will autosort_heaps, and we can just take next() until we want it.
#                   Well it doesn't :)
#                   The actual mistake here is that I'm not having much experience with HEAPS, and I was thinking,
#                   that if I heapify() any list it's going to be sorted by default, and we can merge them together.
#                   But I was wrong, and we need to use heap.sort() explicitly.
test = [
    28, 35, 21, 13, 21, 72, 35, 52, 74, 92, 25, 65, 77, 1, 73, 32, 43, 68, 8,
    100, 84, 80, 14, 88, 42, 53, 98, 69, 64, 40, 60, 23, 99, 83, 5, 21, 76, 34
]
test_k = 32
test_candidates = 12
test_out = 1407
assert test_out == total_cost(test, test_k, test_candidates)
