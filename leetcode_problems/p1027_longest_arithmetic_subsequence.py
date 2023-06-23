# Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.
# Note that:
#   A subsequence is an array that can be derived from another array by deleting some or no elements
#       without changing the order of the remaining elements.
#   A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).
# ----------------------------
# 2 <= nums.length <= 1000
# 0 <= nums[i] <= 500


def longest_arith_seq_length(nums: list[int]) -> int:
    all_options: dict[tuple[int, int], list[int]] = {}
    record_options: dict[int, list[int]] = {}
    for x in range(1, len(nums)):
        for y in range(0, x):
            option: int = nums[x] - nums[y]
            if option not in record_options:
                all_options[option, nums[x]] = [nums[y], nums[x]]
                record_options[option] = [nums[x]]
                continue
            for g in range(len(record_options[option])):
                last_seq_val: int = record_options[option][g]
                if nums[x] - last_seq_val == option:
                    record_options[option][g] = nums[x]
                    all_options[option, nums[x]] = all_options[option, last_seq_val].copy() + [nums[x]]
                    del all_options[option, last_seq_val]
                else:
                    if nums[x] not in record_options[option]:
                        record_options[option].append(nums[x])
                    if (option, last_seq_val) not in all_options:
                        all_options[(option, nums[x])] = [nums[y], nums[x]]
                    else:
                        all_options[(option, last_seq_val)].append(nums[x])
    max_length: int = 0
    for value in all_options.values():
        max_length = max(max_length, len(value))
    return max_length


# Ok.
# ----------------------------
# Only question is, do I need to take absolute? Because absolute will be a distance, and we need this rule ->
# -> A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).
# Well what about cases like: 20 - 3 = 17 and 3 - 20 = -17, different sequences and with absolute values
# they will be the same. Yeah, no need to use absolute values here.
# ----------------------------
# No idea how to make this fast, but I know how to make this in O(n * n) ->
# -> just store every possible diff in dict and append them one by one.
# No hints given and I have no idea about TimeLimit. Let's try to fail commit.


test1 = [3, 6, 9, 12]
test1_out = 4
# print(longest_arith_seq_length(test1))

test2 = [9, 4, 7, 2, 10]
test2_out = 3
# print(longest_arith_seq_length(test2))

test3 = [20, 1, 15, 3, 10, 5, 8]
test3_out = 4
# print(longest_arith_seq_length(test3))

test4 = [1, 2]
test4_out = 2
# print(longest_arith_seq_length(test4))

# test5 - failed -> I was calculating all possible options, no matter what last value added,
#                   when we need to add value only if it's correct diff with last added value.
test5 = [83, 20, 17, 43, 52, 78, 68, 45]
test5_out = 2
# print(longest_arith_seq_length(test5))


test6 = [83, 20, 17, 43, 52, 78, 68, 104, 69, 94, 130, 45]
test6_out = 4
print(longest_arith_seq_length(test6))

test7 = [12,28,13,6,34,36,53,24,29,2,23,0,22,25,53,34,23,50,35,43,53,11,48,56,44,53,31,6,31,57,46,6,17,42,48,28,5,24,0,14,43,12,21,6,30,37,16,56,19,45,51,10,22,38,39,23,8,29,60,18]
test7_out = 4
# print(longest_arith_seq_length(test7))
