# Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.
# Note that:
#   A subsequence is an array that can be derived from another array by deleting some or no elements
#       without changing the order of the remaining elements.
#   A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).
# ----------------------------
# 2 <= nums.length <= 1000
# 0 <= nums[i] <= 500


def longest_arith_seq_length(nums: list[int]) -> int:
    all_options: dict[int, list[int]] = {}
    for x in range(1, len(nums)):
        for y in range(0, x):
            option: int = nums[x] - nums[y]
            if option not in all_options:
                all_options[option] = [nums[y], nums[x]]
            else:
                all_options[option].append(nums[x])
    max_length: int = 0
    for value in all_options.values():
        max_length = max(max_length, len(value))
    return max_length


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
