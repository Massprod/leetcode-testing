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
    end = len(nums) - 1
    if len(nums) == 1:
        return 0
    if nums[0] >= end:
        return 1

    def best_jump(pool: list[int], start_ind: int = 0, jumps: int = 0):
        jumps += 1
        best_land_index = -1
        for x in range(start_ind + 1, start_ind + pool[start_ind] + 1):
            land_index = pool[x] + x
            if land_index >= end:
                if jumps == 1:
                    return jumps + 1
                return jumps
            if land_index >= best_land_index:
                best_land_index = land_index
                continue
            while pool[land_index] == 0:
                land_index -= 1
        jumps += 1
        return best_jump(pool, best_land_index, jumps)
    return best_jump(nums)


test1 = [2, 3, 1, 1, 4]
test1_out = 2
print(jump(test1))

test2 = [2, 3, 0, 1, 4]
test2_out = 2
print(jump(test2))

test3 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
test3_out = 11
print(jump(test3))

test4 = [1, 3, 2, 2, 2, 9]
test4_out = 3
print(jump(test4))

test5 = [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
test5_out = 3
print(jump(test5))

test6 = [5, 1, 1, 1, 1, 1, 1]
test6_out = 2
print(jump(test6))

# test7 - failed - I was thinking about this 0 situation at the start, and forgot to add....
#                  There's always a correct solution, and we can jump on PLACE.
test7 = [0]
test7_out = 0
print(jump(test7))

# test8 - failed - Ok. Dumb enough to not consider jump on place with any value :)
#                  len(nums) == 1 -> allways 0 jumps
test8 = [1]
test8_out = 0
print(jump(test8))

test9 = [1, 1, 1, 1, 1]
test9_out = 4
print(jump(test9))
