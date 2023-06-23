# Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.
# Note that:
#   A subsequence is an array that can be derived from another array by deleting some or no elements
#       without changing the order of the remaining elements.
#   A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).
# ----------------------------
# 2 <= nums.length <= 1000
# 0 <= nums[i] <= 500


def longest_arith_seq_length(nums: list[int]) -> int:
    # googled_sol (64.41%, 27.50%) -> (3085ms, 60.7mb)  time: O(n * n) | space: O(n * n)
    all_options: dict[tuple[int, int], int] = {}
    for x in range(1, len(nums)):
        for y in range(0, x):
            option: int = nums[x] - nums[y]
            if (y, option) not in all_options:
                all_options[x, option] = 2
                continue
            all_options[x, option] = all_options[y, option] + 1
    max_length: int = 0
    for value in all_options.values():
        max_length = max(max_length, value)
    return max_length


# Time complexity: O(n * n) -> for every index in input_list, we're checking every index before it => O(n * n) ->
# n - len of input_list^^| -> in the worst case, there's no arithmetic sequence in input_list, so there's no
#                          duplicated options all of them are unique, and we're going to store n * n values,
#                          to find max_length after that we need to traverse all these values once again => O(n * n) ->
#                          -> O(n * n) + O(n * n) => O(n * n).
# Auxiliary space: O(n * n) -> in the worst case, there's no arithmetic sequence in input_list, so there's no
#                          duplicated options all of them are unique, and we're going to store n * n values => O(n * n).
# ----------------------------
# Googled solution:
# Dynamic approach to store every possible options we encounter before ->
# -> we're just storing options we encounter on left_to_right path into a dictionary:
# like in test6 => [83, 20, 17, 43, 52, 78, 68, 104, 69, 94, 130, 45] ->
# -> 78 - 52 = 26 == option is stored, and for every other index after [5](78) we're checking this option(26)
# at index [7](104) option(26) for [5](78) is going to be correct => and we already stored every possible
# value we can add into a sequence in all_options[5, 26] == 2, because it's correct for a new index we can just
# add this as a +1 to length => repeating this for every index for which nums[x] - nums[y] is correct option.
# Values in this dictionary is just number of values into a sequence.
# ----------------------------
# Temper_tantrum_below.
# Failed miserably with trying to do this with searching for all possible paths.
# I was storing every possible option we can find with different last values in a path,
# and failed. There was miscalculation for cases like 53, 53, 53, 53, 0, 0, 0 ->
# -> in my solution it was counting this as option with diff == 0, so it's been stored as one path,
# and because of that 53 was duplicated and instead of 4 53 path we get 7 53 path, tried to store
# different paths and last_seq_values on them to differ in these cases. But didn't fix this part
# and got another problems which couldn't resolver.
# Ok. From this one, I'm ignoring dailies and ignoring everything except learn_ladder ->
# -> because it's stupid to jump on cases even if they look easy. Because of this skipped tasks from 90+
# I'm just failing a lost and googling too much.
# Ignore dailies, ignore recommended tasks, only learn_ladder from 90+ where I stopped before.


test1 = [3, 6, 9, 12]
test1_out = 4
print(longest_arith_seq_length(test1))

test2 = [9, 4, 7, 2, 10]
test2_out = 3
print(longest_arith_seq_length(test2))

test3 = [20, 1, 15, 3, 10, 5, 8]
test3_out = 4
print(longest_arith_seq_length(test3))

test4 = [1, 2]
test4_out = 2
print(longest_arith_seq_length(test4))

# test5 - failed -> I was calculating all possible options, no matter what last value added,
#                   when we need to add value only if it's correct diff with last added value.
test5 = [83, 20, 17, 43, 52, 78, 68, 45]
test5_out = 2
print(longest_arith_seq_length(test5))

test6 = [83, 20, 17, 43, 52, 78, 68, 104, 69, 94, 130, 45]
test6_out = 4
print(longest_arith_seq_length(test6))

test7 = [12, 28, 13, 6, 34, 36, 53, 24, 29, 2, 23, 0, 22, 25, 53, 34, 23, 50, 35, 43, 53, 11, 48, 56, 44, 53, 31, 6, 31,
         57, 46, 6, 17, 42, 48, 28, 5, 24, 0, 14, 43, 12, 21, 6, 30, 37, 16, 56, 19, 45, 51, 10, 22, 38, 39, 23, 8, 29,
         60, 18]
test7_out = 4
print(longest_arith_seq_length(test7))
