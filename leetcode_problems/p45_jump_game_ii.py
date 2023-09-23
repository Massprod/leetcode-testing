# You are given a 0-indexed array of integers nums of length n.
# You are initially positioned at nums[0].
# Each element nums[i] represents the maximum length of a forward jump from index i.
# In other words, if you are at nums[i], you can jump to any nums[i + j] where:
#   0 <= j <= nums[i] and
#   i + j < n
# Return the minimum number of jumps to reach nums[n - 1].
# The test cases are generated such that you can reach nums[n - 1].
# -------------------
# 1 <= nums.length <= 10 ** 4
# 0 <= nums[i] <= 1000
# It's guaranteed that you can reach nums[n - 1].


def jump(nums: list[int]) -> int:
    # working_sol (85.66%, 7.57%) -> (113ms, 22.9mb)  time: O(n * log n) | space: O(n)
    end = len(nums) - 1
    if end == 0:
        return 0
    if nums[0] >= end:
        return 1

    def best_jump(pool: list[int], start_ind: int = 0, jumps: int = 1) -> int:
        best_land_index: int = -1
        best_start: int = -1
        # Check every landing point.
        for x in range(start_ind + 1, start_ind + pool[start_ind] + 1):
            land_index: int = pool[x] + x
            # We can reach end.
            if land_index >= end:
                return jumps + 1
            # Choose point from what we can jump furthest.
            elif land_index >= best_land_index:
                best_land_index = land_index
                best_start = x
        return best_jump(pool, best_start, jumps + 1)

    return best_jump(nums)


# Time complexity: O(n * log n) -> because we're choosing best point to jump from, we will recheck some indexes
# n - len of input array^^|  not all of them, but some might be used twice => O(n * log n).
# Space complexity: O(n) -> worst case == [1, 1, 1, ... 1] -> recursion stack with call for every index => O(n).
# -------------------
# Pff. Literally solved most hard part within a 40m and failed to count jumps, cuz tried to jump twice.
# Right now we're using best_start, which I add to count step by step not double jumps.
# Mistake:
#   pos1 -> pos2 == adding jumps + 1 and after calculating best way to jump from pos2 -> pos3
#   adding jumps + 1 and calling recursion from pos3 not pos2 ^like it's doing now^. ! jumps + 2 in One sequence!
#   I was expecting to count like this is not going to be a problem.
#   But in reality it is. Because there's a chance that we can get such pos2 that equal to our end.
#   In this case we can't jump from this position, and I was already expecting this position as jump_pad. Extra +1.
#   Either I need more experience, or better just do tasks like that with 1 step in a future.


test: list[int] = [2, 3, 1, 1, 4]
test_out: int = 2
assert test_out == jump(test)

test = [2, 3, 0, 1, 4]
test_out = 2
assert test_out == jump(test)

test = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
test_out = 11
assert test_out == jump(test)

test = [1, 3, 2, 2, 2, 9]
test_out = 3
assert test_out == jump(test)

test = [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
test_out = 3
assert test_out == jump(test)

test = [5, 1, 1, 1, 1, 1, 1]
test_out = 2
assert test_out == jump(test)

# test -> Failed - I was thinking about this 0 situation at the start, and forgot to add....
#                  There's always a correct solution, and we can jump on PLACE.
test = [0]
test_out = 0
assert test_out == jump(test)

# test -> Failed - Ok. Dumb enough to not consider jump on place with any value :)
#                  len(nums) == 1 -> allways 0 jumps
test8 = [1]
test8_out = 0
assert test_out == jump(test)

test = [1, 1, 1, 1, 1]
test_out = 4
assert test_out == jump(test)

test = [1, 6, 1, 1]
test_out = 2
assert test_out == jump(test)

test = [1, 1, 1, 1]
test_out = 3
assert test_out == jump(test)

test = [1, 1, 2, 1, 1]
test_out = 3
assert test_out == jump(test)

test = [1, 2, 4, 2, 2, 2, 2, 1]
test_out = 4
assert test_out == jump(test)
