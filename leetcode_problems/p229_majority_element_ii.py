# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
# ------------------------
# 1 <= nums.length <= 5 * 10 ** 4
# -10 ** 9 <= nums[i] <= 10 ** 9
# ------------------------
# Follow up: Could you solve the problem in linear time and in O(1) space?


def majority_element(nums: list[int]) -> list[int]:
    # working_sol (69.11%, 20.85%) -> (111ms, 17.9mb)  time: O(n) | space: O(1)
    elements: list[int] = [0, 0]
    first_c: int = 0
    second_c: int = 0
    # Standard Boyer-Moore for major.
    for num in nums:
        if elements[0] == num:
            first_c += 1
        elif elements[1] == num:
            second_c += 1
        elif first_c == 0:
            elements[0] = num
            first_c += 1
        elif second_c == 0:
            elements[1] = num
            second_c += 1
        else:
            first_c -= 1
            second_c -= 1
    # We only need elements which occur > len(nums) // 3
    out: list[int] = []
    limit: int = len(nums) // 3
    first_c, second_c = 0, 0
    # Count.
    for num in nums:
        if num == elements[0]:
            first_c += 1
        elif num == elements[1]:
            second_c += 1
    # Append if correct.
    if first_c > limit:
        out.append(elements[0])
    if second_c > limit:
        out.append(elements[1])
    return out


# Time complexity: O(n) -> traversing once to get 2 major elements => O(n) ->
# n - len of input_array^^| -> traversing again to count their occurrences, we only care about > n // 3 => O(n).
# Auxiliary space: O(1) -> 2 lists which doesn't depend on input, and 3 extra constant INTs => O(1).
# ------------------------
# https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_string-search_algorithm
# Same as p169, but with 2 elements.


test: list[int] = [3, 2, 3]
test_out: list[int] = [3]
assert test_out == majority_element(test)

test = [1]
test_out = [1]
assert test_out == majority_element(test)

test = [1, 2]
test_out = [1, 2]
assert test_out == majority_element(test)

test = [2, 1, 1, 3, 1, 4, 5, 6]
test_out = [1]
assert test_out == majority_element(test)
