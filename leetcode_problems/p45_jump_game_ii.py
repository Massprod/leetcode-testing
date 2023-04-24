# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
#
# Each element nums[i] represents the maximum length of a forward jump from index i.
# In other words, if you are at nums[i], you can jump to any nums[i + j] where:
#
# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1].
# The test cases are generated such that you can reach nums[n - 1].

# Brute forcing again?

def jump(nums: list[int]) -> int:
    # working_sol (93.75%, 7.77%) -> (121ms, 20.5mb)  time: O(n * log n) -> space: O(n)
    end = len(nums) - 1
    if len(nums) == 1:
        return 0
    if nums[0] >= end:
        return 1

    def best_jump(pool: list[int], start_ind: int = 0, jumps: int = 1):
        best_land_index = -1
        best_start = -1
        for x in range(start_ind + 1, start_ind + pool[start_ind] + 1):
            land_index = pool[x] + x
            if land_index >= end:
                return jumps + 1
            if land_index >= best_land_index:
                best_land_index = land_index
                best_start = x
                continue
            while pool[land_index] == 0:
                land_index -= 1
        return best_jump(pool, best_start, jumps + 1)
    return best_jump(nums)

# Time complexity: O(n * log n) -> we're looping through whole input array and checking available
#                                  jump indexes for every index, worst case checking 3/4 extra.
#                                  (not sure about log n, maybe it's actually n * n)
# Space complexity: O(n) -> only constants and input array for recursion stack.

# Pff. Literally solved most hard part within a 40m and failed to count jumps, cuz tried to jump twice.


test1 = [2, 3, 1, 1, 4]
test1_out = 2
print(jump(test1))
assert test1_out == jump(test1)

test2 = [2, 3, 0, 1, 4]
test2_out = 2
print(jump(test2))
assert test2_out == jump(test2)

test3 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
test3_out = 11
print(jump(test3))
assert test3_out == jump(test3)

test4 = [1, 3, 2, 2, 2, 9]
test4_out = 3
print(jump(test4))
assert test4_out == jump(test4)

test5 = [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
test5_out = 3
print(jump(test5))
assert test5_out == jump(test5)

test6 = [5, 1, 1, 1, 1, 1, 1]
test6_out = 2
print(jump(test6))
assert test6_out == jump(test6)

# test7 - failed - I was thinking about this 0 situation at the start, and forgot to add....
#                  There's always a correct solution, and we can jump on PLACE.
test7 = [0]
test7_out = 0
print(jump(test7))
assert test7_out == jump(test7)

# test8 - failed - Ok. Dumb enough to not consider jump on place with any value :)
#                  len(nums) == 1 -> allways 0 jumps
test8 = [1]
test8_out = 0
print(jump(test8))
assert test8_out == jump(test8)

test9 = [1, 1, 1, 1, 1]
test9_out = 4
print(jump(test9))
assert test9_out == jump(test9)

test10 = [1, 6, 1, 1]
test10_out = 2
print(jump(test10))
assert test10_out == jump(test10)

test11 = [1, 1, 1, 1]
test11_out = 3
print(jump(test11))
assert test11_out == jump(test11)

test12 = [1, 1, 2, 1, 1]
test12_out = 3
print(jump(test12))
assert test12_out == jump(test12)

test13 = [1, 2, 4, 2, 2, 2, 2, 1]
test13_out = 4
print(jump(test13))
assert test13_out == jump(test13)
