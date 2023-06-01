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


class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        pass

    def add(self, val: int) -> int:
        pass


test1 = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
test1_out = [None, 4, 5, 5, 8, 8]
