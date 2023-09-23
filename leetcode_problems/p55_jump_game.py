# You are given an integer array nums. You are initially positioned at the array's first index,
#  and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.
# ----------------
# 1 <= nums.length <= 10 ** 4
# 0 <= nums[i] <= 10 ** 5


def can_jump(nums: list[int]) -> bool:
    # working_sol (38.80%, 5.61%) -> (429ms, 27.7mb)  time: O(n * log n) | space: O(n)
    end: int = len(nums) - 1
    if end == 0:
        return True
    if nums[0] >= end:
        return True

    def best_jump(pool: list[int], start_ind: int = 0) -> bool:
        # Only case we stop is 0 options to jump: pool[index] == 0.
        if start_ind != end and pool[start_ind] == 0:
            return False
        best_land_index: int = -1
        best_start: int = -1
        # Check every landing point.
        for x in range(start_ind + 1, start_ind + pool[start_ind] + 1):
            land_index: int = x + pool[x]
            # We can reach end.
            if land_index >= end:
                return True
            # Choose point from what we can jump furthest.
            elif land_index >= best_land_index:
                best_land_index = land_index
                best_start = x
        return best_jump(pool, best_start)

    return best_jump(nums)


# Time complexity: O(n * log n) -> because we're choosing best point to jump from, we will recheck some indexes
# n - len of input array^^|  not all of them, but some might be used twice => O(n * log n).
# Space complexity: O(n) -> worst case == [1, 1, 1, 1, 1, 1, 1] -> recursion stack with call for every index => O(n).
# ---------------------------
# Failed by trying to STRIP my p45 version and make it work faster, without checking every jump, which isn't correct.
# Could have avoided fails and just use it from the start, or just rebuild.
# ---------------------------
# p45 <- already solved similar but counting JUMPS.
#        How we can't reach the end??
#        Only with 0 at the way?? <- cuz if there's not 0 on a way we just jump further and further,
#                                    and only if there's 0 we stop. Correct logic??
#                                    Don't see any way we could stop jumping from START to END
#                                    if there's no 0 on the way.
#                                    ^^correct logic but I tricked myself to thinking about ONE_JUMP_ROUTE
#                                      not considering any other jump_positions :) failed test5 cuz of this...


test: list[int] = [2, 3, 1, 1, 4]
test_out: bool = True
assert test_out == can_jump(test)

test = [3, 2, 1, 0, 4]
test_out = False
assert test_out == can_jump(test)

test = [1, 1, 1, 1, 1, 1, 2, 11]
test_out = True
assert test_out == can_jump(test)

test = [1, 0, 1]
test_out = False
assert test_out == can_jump(test)

test = [3, 0, 8, 2, 0, 0, 1]
test_out = True
assert test_out == can_jump(test)

test = [3, 0, 2, 2, 0, 1, 0, 1]
test_out = False
assert test_out == can_jump(test)

test = [5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]
test_out = True
assert test_out == can_jump(test)
