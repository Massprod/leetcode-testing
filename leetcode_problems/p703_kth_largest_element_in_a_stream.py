# Design a class to find the Kth largest element in a stream.
# Note that it is the Kth largest element in the sorted order, not the Kth distinct element.
#
# Implement KthLargest class:
#   KthLargest(int k, int[] nums) -> Initializes the object with the integer k and the stream of integers nums.
#   int add(int val) -> appends the integer val to the stream
#                       and returns the element representing the Kth largest element in the stream.
# ----------------------------
# 1 <= k <= 104  ,  0 <= nums.length <= 104  ,  -104 <= nums[i] <= 104  ,  -104 <= val <= 104
# At most 104 calls will be made to add.
# It is guaranteed that there will be at least k elements in the array when you search for the kth element.
import heapq


class KthLargest:
    # working_sol (57.66%, 68.66%) -> (108ms, 20.4mb)  time: O((n * log(n)) + (m * log(k))) | space: O(n)
    def __init__(self, k: int, nums: list[int]):
        self.heap = nums
        self.heap_size = k
        heapq.heapify(self.heap)
        while len(self.heap) > self.heap_size:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.heap_size:
            heapq.heappop(self.heap)
        return self.heap[0]


# Time complexity: O((n * log(n)) + (m * log(k))) -> creating heap from an input_list(nums) ->
# n - len of input_list^^ | ! heapify(x) # transforms list into a heap, in-place, in linear time! => O(n) ->
# k - size of a heapq^^   |  -> removing elements from a heap until it reaches Kth size,
# m - num of add() calls^^|     remove element and change indexes of others  => O(n * log(n)) ->
#                            -> adding element into a head, if it's lower than the smallest element does nothing,
#                               otherwise adding element and changing indexes of a heap => O(m * log(k)) ->
#                            -> O((n * log(n)) + (m * log(k)))
# Space complexity: O(n) -> original heap created will be of input_list size, after we cull it to a k size => O(n)
# -----------------------
# For a future use -> If we need to take Kth largest or smallest element and keep track of it, no reasons to
#                     create list and sort_change it, it's always better to use HEAP which will keep track of
#                     largest and smallest values, as well as anything between them for a Kth size.
#                     Allowing us to get largest, smallest values in O(1).
# -----------------------
# Ok it was unsolvable in my case, because I didn't know about a HEAP ques.
# -----------------------
# !
# I am not sure if I can't understand English or the author of the description doesn't speak English !
# True^^ - relatable comment, description is total garbage.


test1 = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
test1_out = [None, 4, 5, 5, 8, 8]
test = KthLargest(test1[0][0], test1[0][1])
for g in range(1, len(test1)):
    print(test.heap)
    assert test1_out[g] == test.add(test1[g][0])
del test

# test2 - failed -> I didn't consider input with empty list, but this description with Kth_largest still working,
#                   let's fail again.
test2 = [[1, []], [-3], [-2], [-4], [0], [4]]
test2_out = [None, -3, -2, -2, 0, 4]
test = KthLargest(test2[0][0], test2[0][1])
for g in range(1, len(test2)):
    print(test.heap)
    assert test2_out[g] == test.add(test2[g][0])
del test
