# You are given an integer array nums, where nums[i] represents
#  the points scored in the ith game.
# There are exactly two players. Initially, the first player is active
#  and the second player is inactive.
# The following rules apply sequentially for each game i:
# If nums[i] is odd, the active and inactive players swap roles.
# In every 6th game (that is, game indices 5, 11, 17, ...),
#  the active and inactive players swap roles.
# The active player plays the ith game and gains nums[i] points.
# Return the score difference, defined as the first player's total score
#  minus the second player's total score.
# --- --- --- ---
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 1000


def score_difference(nums: list[int]) -> int:
    # working_solution: (99.24%, 21.02%) -> (1ms, 19.52mb)  Time: O(n) Space: O(1)
    p1_score: int = 0
    p1_active: bool = True
    p2_score: int = 0
    p2_active: bool = False
    for index in range(len(nums)):
        if nums[index] % 2:
            p1_active, p2_active = p2_active, p1_active
        if 0 == (index + 1) % 6:
            p1_active, p2_active = p2_active, p1_active
        if p1_active:
            p1_score += nums[index]
        else:
            p2_score += nums[index]
    
    return p1_score - p2_score


# Time complexity: O(n)
# n - length of the input array `nums`
# --- --- --- ---
# Space complexity: O(1)


test: list[int] = [1, 2, 3]
test_out: int = 0
assert test_out == score_difference(test)

test = [2, 4, 2, 1, 2, 1]
test_out = 4
assert test_out == score_difference(test)

test = [1]
test_out = -1
assert test_out == score_difference(test)
