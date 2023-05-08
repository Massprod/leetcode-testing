# You are given an integer array nums. You are initially positioned at the array's first index,
# and each element in the array represents your maximum jump length at that position.
#
# Return true if you can reach the last index, or false otherwise.

def can_jump(nums: list[int]) -> bool:
    end = len(nums) - 1
    if len(nums) == 1:
        return True
    if nums[0] >= end:
        return True

    def can_reach(pool: list[int], start_ind: int = 0) -> bool:
        if pool[start_ind] == 0:
            return False
        for x in range(start_ind + 1, start_ind + pool[start_ind] + 1):
            land_index = pool[x] + x
            if land_index >= end:
                return True
            recur = can_reach(pool, land_index)
            if recur:
                return True
            if not recur and (x == start_ind + pool[start_ind]):
                return False
    return can_reach(nums)


# ---------------------------
# p45 <- already solved similar but counting JUMPS.
#        How we can't reach the end??
#        Only with 0 at the way?? <- cuz if there's not 0 on a way we just jump further and further,
#                                    and only if there's 0 we stop. Correct logic??
#                                    Don't see any way we could stop jumping from START to END
#                                    if there's no 0 on the way.


test1 = [2, 3, 1, 1, 4]
test1_out = True
assert can_jump(test1) == test1_out
print(can_jump(test1))

test2 = [3, 2, 1, 0, 4]
test2_out = False
assert can_jump(test2) == test2_out
print(can_jump(test2))

test3 = [1, 1, 1, 1, 1, 1, 2, 11]
test3_out = True
assert can_jump(test3) == test3_out
print(can_jump(test3))

test4 = [1, 0, 1]
test4_out = False
assert can_jump(test4) == test4_out
print(can_jump(test4))

# test5 - failed <- I wanted to strip p45 and make it one_way, which is mistaken.
#                   Because we need to check every possible way to jump from, like I already did...
test5 = [3, 0, 8, 2, 0, 0, 1]
test5_out = True
assert can_jump(test5) == test5_out
print(can_jump(test5))

test6 = [3, 0, 2, 2, 0, 1, 0, 1]
test6_out = False
assert can_jump(test6) == test6_out
print(can_jump(test6))
