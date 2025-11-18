# You are given an integer array nums.
# In one move, you may increase the value of any single element nums[i] by 1.
# Return the minimum total number of moves required
#  so that all elements in nums become equal.
# --- --- --- ---
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100


def min_moves(nums: list[int]) -> int:
    # working_solution: (100%, 41.41%) -> (0ms, 17.84mb)  Time: O(n) Space: O(1)
    out: int = 0
    # We either need to increase some value to the max
    # Or we would need to reduce it to the min.
    # W.e the case, we will make the same # of moves.
    max_val: int = max(nums)
    for num in nums:
        out += abs(max_val - num)
    
    return out


# Time complexity: O(n)
# n - length of the input array `nums`.
# --- --- --- ---
# Space complexity: O(1)


test: list[int] = [2, 1, 3]
test_out: int = 3
assert test_out == min_moves(test)

test = [4, 4, 5]
test_out = 2
assert test_out == min_moves(test)
