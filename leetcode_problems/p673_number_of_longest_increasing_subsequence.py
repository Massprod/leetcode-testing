# Given an integer array nums, return the number of longest increasing subsequences.
# Notice that the sequence has to be strictly increasing.
# ------------------
# 1 <= nums.length <= 2000
# -10 ** 6 <= nums[i] <= 10 ** 6
from random import randint


def find_numbers_of_lis(nums: list[int]) -> int:
    # working_sol (93.71%, 52.88%) -> (642ms, 16.7mb)  time: O(n * log n) | space: O(n)
    # unique case, no reasons to bother
    if len(nums) == 1:
        return 1
    # All values can be counted as SUBSEQ by themselves, and PATHS to them is 1.
    # seq_lens, stores => LEN of SUBSEQ to some index, and correct PATHS to get into this index.
    # Correct_path == any correct SUBSEQ leading to it, but with different last value ->
    # -> like 1, 3, 5, 4, 7 => 1, 3, 5, 7 | 1, 3, 4, 7 <- same length diff PATH.
    seq_lens: list[list[int, int]] = [[1, 1]] + [[1, 1] for _ in nums[1:]]
    # Starting from 1, cuz first value is always SUBSEQ by itself and there's only 1 PATH to it.
    for x in range(1, len(nums)):
        # Setting defaults.
        # max_seq will always be updated in a loops,
        # if it's not then there's no correct SUBSEQ leading to this index.
        max_seq: int = 0
        # All correct PATHS leading to this index.
        # There's always at least 1, and I'm not incrementing them,
        # so it's should be 1 by default to set it correctly if there's None leading.
        paths: int = 1
        # If values are equal, then every PATH leading to it
        # can be used to lead for the same value.
        # Same goes for a SUBSEQ 1, 2, 3, 3 -> 1, 2, 3 | 1, 2, 3
        # So it can be copied.
        if nums[x] == nums[x - 1]:
            seq_lens[x][0] = seq_lens[x - 1][0]
            seq_lens[x][1] = seq_lens[x - 1][1]
        # If value is higher than previous, then we need to find
        # every SUBSEQ with the same LENGTH in previous part of the array.
        # Which already stored, with their PATHs.
        # Most important is that we need MAX_LENGTH not just any equals.
        if nums[x] > nums[x - 1]:
            # Starting from previous element, cuz it's first index
            # from who we can build correct SUBSEQ.
            y: int = x - 1
            while y > -1:
                # Ignore everything that's higher or equal.
                # Higher can't correctly lead us to X.
                # Equal can't either.
                if nums[x] > nums[y]:
                    # Count every PATHs leading to the indexes,
                    # from what we can build correct SUBSEQ with maximized size.
                    if max_seq == seq_lens[y][0]:
                        paths += seq_lens[y][1]
                    # Everytime we found SUBSEQ with bigger size, update.
                    if max_seq < seq_lens[y][0]:
                        max_seq = seq_lens[y][0]
                        paths = seq_lens[y][1]
                y -= 1
            # Increment by maximum size SUBSEQ.
            seq_lens[x][0] += max_seq
            # Set every possible correct path leading to this index.
            seq_lens[x][1] = paths
        # Actual repeat of previous part, but with start from
        # x - 2, cuz we already now that's nums[x - 1] > nums[x].
        # So we can't start any correct SUBSEQ from it.
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
    # Default by 0, cuz there's no way correct SUBSEQ
    # will have 0 PATHS and LENGTH.
    max_len: int = 0
    max_paths: int = 0
    # Traversing whole SUBSEQ lengths and their PATHS
    for g in range(len(seq_lens)):
        # If SUBSEQ is having same length as previous,
        # we can just increment correct PATHS.
        # Example:
        # [1, 1, 1, 2, 2, 2, 3, 3, 3] ->
        # -> there's 9 PATHS leading to every '3'.
        if max_len == seq_lens[g][0]:
            max_paths += seq_lens[g][1]
        # If there's SUBSEQ with higher length,
        # updating it with his values.
        if seq_lens[g][0] > max_len:
            max_len = seq_lens[g][0]
            max_paths = seq_lens[g][1]
    return max_paths


# Time complexity: O(n * log n) -> creating array with the same size as input_array to store LENGTH and
# n - len of input_array^^| correct SUBSEQ paths to some index => O(n) -> traversing whole input_array once ->
#                           -> but for every index in the array we're doing backwards path(walk/traverse)
#                           from this index to the start([0]) -> so it should be O(n * log n) =>
#                           => where (log n) is always changing from 1 to (n - 1) ->
#                           -> extra to this, we're traversing completed seq_lens with all LENGTH and PATHS stored =>
#                           => it's having same length as input_array => O(n).
# Auxiliary space: O(n) -> we're creating extra list with lists inside which holds 2 values(LENGTH, PATHS)
#                          for every value(index) in input_array -> so we're basically doubling input_array values =>
#                          => O(2n) -> extra to this 5 constant INTs used, none of them depends on input.
# ------------------
# Failing tests with 2k constraints, no idea how to debug it correctly.
# Ok case with 100 values failed, at least can work with it.
# Sheesh. 5 minutes to lose streak, and as always made a mistake when tried to fix something faster.
# In this case -> duplicates. Placed somewhat placeholder to ignore values with len == 1,
# and because of that it was just annulling all correct paths. Fixed it in first part, but forgot about second.
# DP problems is hardest, so far.
# ------------------
# Ok. Working in one way correctly, but there's nothing in description about REVERSing this arrays.
# But in tests, there's [2, 1] and we should consider reverse paths...
# And most twisted thing is why this is [10, 9, 8, 7, 6, 5, 4, 5, 6, 7, 8, 9, 10] correct 1 path and
# [10, 9, 8, 7, 6, 5, 4] <- can be read in reverse. Wtf?
# Ok. I was mistaken we're just getting 7 paths with 1 length, this need to be treated as duplicates when counted
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
assert test1_out == find_numbers_of_lis(test1)

test2 = [2, 2, 2, 2, 2]
test2_out = 5
assert test2_out == find_numbers_of_lis(test2)

test3 = [1, 3, 5, 4, 3, 2, 1, 7, 8, 5, 4, 3, 9, 9, 10]
test3_out = 4
assert test3_out == find_numbers_of_lis(test3)

test4 = [1, 3, 5, 4, 3, 2, 1, 7, 8, 5, 4, 3, 9, 9, 10, 1, 3, 5, 4, 3, 2, 1, 7, 8, 5, 4, 3, 9, 9, 10]
test4_out = 18
assert test4_out == find_numbers_of_lis(test4)

test5 = [10, 9, 8, 7, 6, 5, 4, 5, 6, 7, 8, 9, 10]
test5_out = 1
assert test5_out == find_numbers_of_lis(test5)

test6 = [10, 9, 8, 7, 6, 5, 4]
test6_out = 7
assert test6_out == find_numbers_of_lis(test6)

test7 = [10, 9, 8, 7, 6, 5, 4, 10, 4, 4, 4, 4, 5, 6, 7, 8, 9, 10]
test7_out = 5
assert test7_out == find_numbers_of_lis(test7)

# test8 -> failed -> WTF? We can REVERSE array? Mistake! We can count reverse same way as duplicates.
#                    We need to treat them like they're just SEQ with length == 1.
test8 = [2, 1]
test8_out = 2
assert test8_out == find_numbers_of_lis(test8)

# test9 -> failed -> Same problem as test10, but it was in first_part(nums[x] > nums[x - 1]).
test9 = [1, 1, 1, 2, 2, 2, 3, 3, 3]
test9_out = 27
assert test9_out == find_numbers_of_lis(test9)

# test10 -> failed -> Forgot to delete incorrect annulling of duplicates in second_part(nums[x] < nums[x - 1]) ->
#                     -> it was annulling correct path we needed to count,
#                        this is why I was getting x2, x3 lower results.
test10 = [
    -738843, 786410, -536728, -539386, 379285, -148869, -782271, 819633, 229891, 560168, 274806, -248057, 148771,
    93575, 128686, -605868, -156544, -690633, -972451, 193027, 386215, 181721, -558354, 832974, -38899, -645533,
    -975041, 125219, -955662, -714755, -211848, 419771, 309818, -926434, 234075, -126078, 22014, -513193, -162515,
    -36927, -182778, -139872, -677258, -867353, -893257, -854597, 14023, -682726, 482107, -116374, 170771, 932865,
    -466288, -768738, 298367, 100223, -371681, 544741, -779074, -339769, -118173, 118014, -979322, -146293,
    -457279, 652766, 528204, 447490, 838440, -884975, 37314, 119231, -425741, 430601, -371584, 503548, -932225,
    -422538, -473232, 722683, -858865, -986787, -980122, -168536, -34327, -347536, 107889, 884541, 632349,
    -500448, 924701, -742585, 152177, -744001, 350988, 581215, -758164, 927561, 712003
]
test10_out = 12
assert test10_out == find_numbers_of_lis(test10)

test: list[int] = []
for _ in range(1, 100):
    test.append(randint(-10 ** 6, 10 ** 6))
print(test)
print(find_numbers_of_lis(test))
