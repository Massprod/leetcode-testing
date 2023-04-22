# Given an unsorted integer array nums, return the smallest missing positive integer.
#
# You must implement an algorithm that runs in O(n) time and uses constant extra space.

# Add metrics in a future % is good but numbers should be here. Maybe revisit other's will see.

def first_positive(nums: list[int]) -> int:
    # working_sol (52.42%, 46.58%) -> (372ms, 27.9mb) time: O(n * log n) | space O(n)
    min_pos = 1
    nums.sort()
    for x in range(len(nums)):
        if nums[x] <= 0:
            continue
        if nums[x] == min_pos:
            min_pos += 1
            continue
        if nums[x] > min_pos:
            return min_pos
    return min_pos

# Time complexity: O(n * log n) -> worst case we loop through whole list of nums and min_pos will be (nums[-1] + 1)
# Space complexity: O(n) -> one constant min_pos, and doesn't depend on input.
#
# Ok. Python sort() takes at lowest Ω(n), violating the rule with memory. Found the catch.
# -----------------------------
# ! "No extra space" implies some amount of space,
# usually exactly n, is available via the input, and no more should be used !
# -> Ok. That's a catch I guess, not available to use min_pos as a constant.
# -----------------------------
# ! a space complexity of O(1) means that the space required by the algorithm to process data is constant;
# it does not grow with the size of the data on which the algorithm is operating. !
# -----------------------------
# ! For an algorithm to take constant extra space,
# the extra variables used to solve it should not change with the input size !
# But all googled solution's at least uses LEN(NUMS) as constant n, which depends on input size. Hmm
# -----------------------------
# Where's the catch? Hard problem, can't be so easy...
# We allowed to sort, and minimal positive int is 1
# If there's not presented any value equal to 1 it's always return 1,
# and if there's 1, next 2 with same logic. Hmm


test1 = [1, 2, 0]
test1_out = 3
print(first_positive(test1))

test2 = [3, 4, -1, 1]
test2_out = 2
print(first_positive(test2))

test3 = [7, 8, 9, 11, 12]
test3_out = 1
print(first_positive(test3))
