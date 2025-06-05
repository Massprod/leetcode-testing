# You are given a 0-indexed integer array nums of even length.
# As long as nums is not empty, you must repetitively:
#  - Find the minimum number in nums and remove it.
#  - Find the maximum number in nums and remove it.
#  - Calculate the average of the two removed numbers.
# The average of two numbers a and b is (a + b) / 2.
#  - For example, the average of 2 and 3 is (2 + 3) / 2 = 2.5.
# Return the number of distinct averages calculated using the above process.
# Note that when there is a tie for a minimum or maximum number, any can be removed.
# -----------------------------
# 2 <= nums.length <= 100
# nums.length is even.
# 0 <= nums[i] <= 100


def distinct_averages(nums: list[int]) -> int:
    # working_sol (100.00%, 67.72%) -> (0ms, 17.74mb)  time: O(n) | space: O(n)
    out: int = 0
    avgs: set[float] = set()
    nums.sort()
    left: int = 0
    right: int = len(nums) - 1
    while left < right:
        avg: float = (nums[left] + nums[right]) / 2
        if avg not in avgs:
            out += 1
            avgs.add(avg)
        left += 1
        right -= 1

    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing every value of the `nums` => O(n).
# -----------------------------
# Auxiliary space: O(n)
# In the worst case every pair will give unique `avg` => O(n).


test: list[int] = [4, 1, 4, 0, 3, 5]
test_out: int = 2
assert test_out == distinct_averages(test)

test = [1, 100]
test_out = 1
assert test_out == distinct_averages(test)
