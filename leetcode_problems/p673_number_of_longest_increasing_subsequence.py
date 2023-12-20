# Given an integer array nums, return the number of longest increasing subsequences.
# Notice that the sequence has to be strictly increasing.
# ------------------
# 1 <= nums.length <= 2000
# -10 ** 6 <= nums[i] <= 10 ** 6
from random import randint


def find_numbers_of_lis(nums: list[int]) -> int:
    # working_sol (95.24%, 7.9%) -> (303ms, 17.6mb)  time: O(n * n) | space: O(n)
    if len(nums) == 1:
        return 1
    # All values can be counted as SUBSEQ by themselves, and PATHS to them is 1.
    # [maximum size of sequences ending on this index, number of sequences with this size ending on this index]
    subseq_lens: list[list[int, int]] = [[1, 1] for _ in nums]
    # Starting from 1 index, because first value is always SUBSEQ by itself and there's only 1 PATH to it.
    for x in range(1, len(nums)):
        # Starting from 0, because we counted every value as subseq of 1 by themselves.
        max_seq: int = 0
        # All correct PATHS leading to this index, always at least 1 path.
        paths: int = 1
        # All equal values on continuous streak will have same paths:
        # 1, 2, 3, 3 -> 1, 2, 3 | 1, 2, 3
        if nums[x] == nums[x - 1]:
            subseq_lens[x][0] = subseq_lens[x - 1][0]
            subseq_lens[x][1] = subseq_lens[x - 1][1]
        # Otherwise, try to continue previous or build a new one.
        else:
            y: int = x - 1
            while y > -1:
                # Ignore everything that's higher or equal.
                # Higher can't correctly lead us to `x`.
                # Equal can't either, because there's something incorrect between.
                # Only care about subsequences we can continue with nums[x].
                if nums[x] > nums[y]:
                    # Same maximum subsequence size => just continue these paths.
                    if max_seq == subseq_lens[y][0]:
                        paths += subseq_lens[y][1]
                    # Bigger subsequence size => new maximum size + new paths to continue.
                    elif max_seq < subseq_lens[y][0]:
                        max_seq = subseq_lens[y][0]
                        paths = subseq_lens[y][1]
                y -= 1
            # (1 + max_seq) <- 1 our `x` element + maximum subsequence size on the left side.
            subseq_lens[x][0] += max_seq
            # All subsequences with length == `max_seq`, we have on the left side.
            subseq_lens[x][1] = paths
    max_len: int = 0
    max_paths: int = 0
    for sub_length, paths in subseq_lens:
        # Same maximum length => continuation of previous subsequences with this size.
        # [1, 1, 1, 2, 2, 2, 3, 3, 3] -> there's 9 PATHS leading to every '3'.
        if max_len == sub_length:
            max_paths += paths
        # New maximum size + paths.
        elif sub_length > max_len:
            max_len, max_paths = sub_length, paths
    return max_paths


# Time complexity: O(n * n) <- n - length of input array `nums`.
# Creating `subseq_lens` with same size as `nums` => O(n).
# Traversing all indexes of `nums` | `subseq_lens` and from each of them we're doing left side traverse from x -> 0.
# Extra traverse of `subseq_lens` to get maximum paths => O(n).
# ------------------
# Auxiliary space: O(n).
# Extra array `subseq_lens` with size of `n` => O(n).
# ------------------
# Failing tests with 2k constraints, no idea how to debug it correctly.
# Ok case with 100 values failed, at least can work with it.
# Sheesh. 5 minutes to lose streak, and as always made a mistake when tried to fix something faster.
# In this case -> duplicates. Placed somewhat placeholder to ignore values with len == 1,
# and because of that it was just annulling all correct paths. Fixed it in the first part, but forgot about second.
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


test: list[int] = [1, 3, 5, 4, 7]
test_out: int = 2
assert test_out == find_numbers_of_lis(test)

test = [2, 2, 2, 2, 2]
test_out = 5
assert test_out == find_numbers_of_lis(test)

test = [1, 3, 5, 4, 3, 2, 1, 7, 8, 5, 4, 3, 9, 9, 10]
test_out = 4
assert test_out == find_numbers_of_lis(test)

test = [1, 3, 5, 4, 3, 2, 1, 7, 8, 5, 4, 3, 9, 9, 10, 1, 3, 5, 4, 3, 2, 1, 7, 8, 5, 4, 3, 9, 9, 10]
test_out = 18
assert test_out == find_numbers_of_lis(test)

test = [10, 9, 8, 7, 6, 5, 4, 5, 6, 7, 8, 9, 10]
test_out = 1
assert test_out == find_numbers_of_lis(test)

test = [10, 9, 8, 7, 6, 5, 4]
test_out = 7
assert test_out == find_numbers_of_lis(test)

test = [10, 9, 8, 7, 6, 5, 4, 10, 4, 4, 4, 4, 5, 6, 7, 8, 9, 10]
test_out = 5
assert test_out == find_numbers_of_lis(test)

# test8 -> failed -> WTF? We can REVERSE array? Mistake! We can count reverse same way as duplicates.
#                    We need to treat them like they're just SEQ with length == 1.
test = [2, 1]
test_out = 2
assert test_out == find_numbers_of_lis(test)

test = [1, 1, 1, 2, 2, 2, 3, 3, 3]
test_out = 27
assert test_out == find_numbers_of_lis(test)

test = [
    -738843, 786410, -536728, -539386, 379285, -148869, -782271, 819633, 229891, 560168, 274806, -248057, 148771,
    93575, 128686, -605868, -156544, -690633, -972451, 193027, 386215, 181721, -558354, 832974, -38899, -645533,
    -975041, 125219, -955662, -714755, -211848, 419771, 309818, -926434, 234075, -126078, 22014, -513193, -162515,
    -36927, -182778, -139872, -677258, -867353, -893257, -854597, 14023, -682726, 482107, -116374, 170771, 932865,
    -466288, -768738, 298367, 100223, -371681, 544741, -779074, -339769, -118173, 118014, -979322, -146293,
    -457279, 652766, 528204, 447490, 838440, -884975, 37314, 119231, -425741, 430601, -371584, 503548, -932225,
    -422538, -473232, 722683, -858865, -986787, -980122, -168536, -34327, -347536, 107889, 884541, 632349,
    -500448, 924701, -742585, 152177, -744001, 350988, 581215, -758164, 927561, 712003
]
test_out = 12
assert test_out == find_numbers_of_lis(test)

test = [randint(-10 ** 6, 10 ** 6) for _ in range(2000)]
print(test)
