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
    if nums[0] >= end:
        return 1

    def best_jump(pool: list[int], start_ind: int = 0, steps: int = 1):
        steps += 1
        best_land_index = -1
        for x in range(start_ind + 1, pool[start_ind] + 1):
            land_index = pool[x] + x
            print(pool[start_ind])
            if land_index >= end:
                return steps
            if land_index >= best_land_index:
                best_land_index = land_index
                continue
            while pool[land_index] == 0:
                land_index -= 1
        best_jump(pool, best_land_index, steps)
    return best_jump(nums)


test1 = [2, 3, 1, 1, 4]
test1_out = 2
print(jump(test1))

test2 = [2, 3, 0, 1, 4]
test2_out = 2
print(jump(test2))

