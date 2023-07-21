# Given an integer array nums, return the number of longest increasing subsequences.
# Notice that the sequence has to be strictly increasing.
# ------------------
# 1 <= nums.length <= 2000
# -10 ** 6 <= nums[i] <= 10 ** 6
from random import randint


def find_numbers_of_lis(nums: list[int]) -> int:
    if len(nums) == 1:
        return 1
    seq_lens: list[list[int, int]] = [[1, 1]] + [[1, 1] for _ in nums[1:]]
    for x in range(1, len(nums)):
        max_seq: int = 0
        paths: int = 1
        if nums[x] == nums[x - 1]:
            seq_lens[x][0] = seq_lens[x - 1][0]
            seq_lens[x][1] = seq_lens[x - 1][1]
        if nums[x] > nums[x - 1]:
            y: int = x - 1
            while y > -1:
                if nums[x] > nums[y]:
                    if max_seq == seq_lens[y][0]:
                        paths += seq_lens[y][1]
                    if max_seq < seq_lens[y][0]:
                        max_seq = seq_lens[y][0]
                        paths = seq_lens[y][1]
                y -= 1
            seq_lens[x][0] += max_seq
            seq_lens[x][1] = paths
        if nums[x] < nums[x - 1]:
            y = x - 2
            while y > -1:
                if nums[x] > nums[y]:
                    if max_seq == seq_lens[y][0]:
                        paths += seq_lens[y][1]
                    if max_seq < seq_lens[y][0]:
                        max_seq = seq_lens[y][0]
                        paths = seq_lens[y][1]
                y -= 1
            seq_lens[x][0] += max_seq
            seq_lens[x][1] = paths
            if max_seq == 1:
                seq_lens[x][1] = 1
    # print(seq_lens)
    max_len: int = 0
    max_paths: int = 0
    cur_val: int | None = None
    for g in range(len(seq_lens)):
        if cur_val is None:
            cur_val = nums[g]
        if cur_val == nums[g]:
            max_paths += 1
        if seq_lens[g][0] > max_len:
            max_len = seq_lens[g][0]
            max_paths = seq_lens[g][1]
    return max_paths

# Ok. Working in one way correctly, but there's nothing in description about REVERSing this arrays.
# But in tests, there's [2, 1] and we should consider reverse paths...
# ------------------
# Ok. Made correct counting of seq_len for all sequence to some index, but I don't count number of ways to get here.
# And this is actually what we need to return. How to store/count it?
# I was counting just sequence from some value which is lower than nums[y],
# but I need highest seq_len from ALL of these values. Rebuild.
# ------------------
# Pretty sure it's DP problem, cuz it's too slow to check everything with recursion, and we need to cull it.
# Normal recursion flow is 1 -> 3 -> 5 skip 4 -> 7, but it's either we go deeper one by one indexes,
# which is actually can be stored in some array like default DP approach, or we just check everything from diff starts.
# Then DP[x] should store every SEQ possible for this [x], only part is how we deal with breakpoints.
# Like in test1 -> 5, 4 -> we need to continue from 3 and there can be 5,4,4,4,4,4,4,3,3 etc. we can't just use some
# constant. Only way I see is traverse everything before that 4 and find element which lower and most right placed.
# So WHILE Y - 1 < Y  and Y == some element which was [X - 1] from breakpoint, then we can continue counting from this.
# ! STRICTLY INCREASING ! -> if values are equal we can just ignore them. 4,4,4,4,4,3 all ignore until 3.
# But for the length of SEQ it should be counted as 1.
# In the end -> 1, 3, 5, 4, 4, 4, 7 =>
# X == 0 SEQ = 1 -> 1
# X == 1 SEQ = 2 -> 1, 3
# X == 2 SEQ = 3 -> 1, 3, 5
# X == 3 SEQ = 3 -> 1, 3, 4
# X == 4 SEQ = 3 -> 1, 3, 4
# same for all 4
# X == 6 SEQ = 4 -> 1, 3, 5, 7 | 1, 3, 4, 7
# After everything just count MAX values in DP. Should be correct.
# Extra, any value is SEQ of itself == len = 1.


test1 = [1, 3, 5, 4, 7]
test1_out = 2
print(find_numbers_of_lis(test1))

test2 = [2, 2, 2, 2, 2]
test2_out = 5
print(find_numbers_of_lis(test2))

test3 = [1, 3, 5, 4, 3, 2, 1, 7, 8, 5, 4, 3, 9, 9, 10]
test3_out = 4
print(find_numbers_of_lis(test3))

test4 = [1, 3, 5, 4, 3, 2, 1, 7, 8, 5, 4, 3, 9, 9, 10, 1, 3, 5, 4, 3, 2, 1, 7, 8, 5, 4, 3, 9, 9, 10]
print(find_numbers_of_lis(test4))

test5 = [10, 9, 8, 7, 6, 5, 4, 5, 6, 7, 8, 9, 10]
print(find_numbers_of_lis(test5))

test6 = [10, 9, 8, 7, 6, 5, 4]
print(find_numbers_of_lis(test6))

test7 = [10, 9, 8, 7, 6, 5, 4, 10, 4, 4, 4, 4, 5, 6, 7, 8, 9, 10]
print(find_numbers_of_lis(test7))

# test8 -> failed -> WTF? We can REVERSE array?
test8 = [2, 1]
print(find_numbers_of_lis(test8))

# test: list[int] = []
# for _ in range(1, 2000):
#     test.append(randint(-10 ** 6, 10 ** 6))
# print(test)
# print(find_numbers_of_lis(test))
