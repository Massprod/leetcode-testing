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
        self.nums = list(sorted(nums))
        self.kth = -k

    def add(self, val: int) -> int:
        for x in range(len(self.nums)):
            if self.nums[x - 1] < val <= self.nums[x]:
                self.nums.insert(x, val)
                break
            if x == len(self.nums) - 1 and val > self.nums[x]:
                self.nums.append(val)
        return self.nums[self.kth]


# There's no way it's just a returning of -kth index, so I can only fail to see what this description is.
# ----------------------
# !
# returns the element representing the Kth largest element in the stream.!
# What? Kth_largest_element? Is that index from 0 to largest, or from -1 to largest?
# Because in a first test it's looking like we need to return nums[-Kth],
# after adding new element and sorting.
# [4, 5, 8, 2] -> first add 3 -> [2, 3, 4, 5, 8] -> Kth == 3, but we return 4, and it's index == 2, or index == -3 ->
# [2, 3, 4, 5, 8] -> add 5 -> [2, 3, 4, 5, 5, 8] -> now we return 5 and it's index == 3 , or index == -3 ->
# [2, 3, 4, 5, 5, 8] -> add 10 -> [2, 3, 4, 5, 5, 8, 10] -> return 5, still goes for index == 3, or index == -3 ->
# [2, 3, 4, 5, 5, 8, 10] -> add 9 -> [2, 3, 4, 5, 5, 8, 9, 10] -> return 8, and now it's only index == -3,
# So we're taking some LARGEST nums, and choosing Kth of them, searching backwards, at least it's look like this.
# And we're allowed to return duplicates, so it's not like we choose from 3 largest NUMS, but only index.
# Because if we needed to choose 3 largest UNIQUE num than after adding 5 we should return 4 not 5,
# there's 3, 4, 5, 5, 8 -> 8 is first largest, 5 is second largest, 4 is third largest, and we should return Kth == 3,
# but in test1 we're returning 5, which is possible only if we're returning something on INDEX == -3.
# Maybe it's wrong but there's 1 case with 5 which points to it, other's is correct for returning third_largest.
# Not intuitive description, so I will need to fail to see this.
# !
# Note that it is the Kth largest element in the sorted order, not the Kth distinct element. !
# This one implies, that it's actually should be one of the LARGEST nums to choose from, than why we're returning 5?
# It's second largest, or we should count duplicates as well? Dumbest description I have ever seen.


test1 = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
test1_out = [None, 4, 5, 5, 8, 8]
test = KthLargest(test1[0][0], test1[0][1])
for g in range(1, len(test1)):
    print(test.nums)
    assert test1_out[g] == test.add(test1[g][0])
