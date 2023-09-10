# Given an integer array nums, return the most frequent even element.
# If there is a tie, return the smallest one. If there is no such element, return -1.
# ------------------
# 1 <= nums.length <= 2000
# 0 <= nums[i] <= 10 ** 5


def most_frequent_even(nums: list[int]) -> int:
    # working_sol (93.81%, 88.13%) -> (236ms, 16.66mb)  time: O(n) | space: O(n)
    all_nums: dict[int, int] = {}
    for num in nums:
        if num in all_nums:
            all_nums[num] += 1
        elif num % 2 == 0:
            all_nums[num] = 1
    # num and its occurrences can be equal,
    #  so it better to use extra dict.
    correct: dict[int, int] = {}
    for key, value in all_nums.items():
        if value in correct:
            if correct[value] > key:
                correct[value] = key
            continue
        correct[value] = key
    if correct:
        return correct[max(correct.keys())]
    return -1


# Time complexity: O(n) -> traversing input_array once to count all occurrences => O(n) ->
# n - len of input_array^^| -> worst case == all values are unique, traversing dictionary with size == n, to switch
#                           values and occurrences => O(n) -> extra traverse of keys for max, with same case => O(n).
# Auxiliary space: O(n) -> 2 extra dictionaries of size == n => O(2n).


test: list[int] = [0, 1, 2, 2, 4, 4, 1]
test_out: int = 2
assert test_out == most_frequent_even(test)

test = [4, 4, 4, 9, 2, 4]
test_out = 4
assert test_out == most_frequent_even(test)

test = [29, 47, 21, 41, 13, 37, 25, 7]
test_out = -1
assert test_out == most_frequent_even(test)

test = [0, 0, 0, 0]
test_out = 0
assert test_out == most_frequent_even(test)
