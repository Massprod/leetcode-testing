# You are given an integer array nums.
# The binary reflection of a positive integer is defined as the number obtained
#  by reversing the order of its binary digits (ignoring any leading zeros)
#  and interpreting the resulting binary number as a decimal.
# Sort the array in ascending order based on the binary reflection of each element.
# If two different numbers have the same binary reflection,
#  the smaller original number should appear first.
# Return the resulting sorted array.
# --- --- --- ---
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 10 ** 9
from random import randint
from pyperclip import copy


def sort_by_reflection(nums: list[int]) -> list[int]:
    # working_solution: (82.76%, 100%) -> (7ms, 17.32mb)  Time: O(n * log n) Space: O(n)

    def bin_value(num: int) -> tuple[int, int]:
        bin_str: str = bin(num)[2:]
        index: int = 0
        while index < len(bin_str) and '0' == bin_str[index]:
            index += 1
        no_leadings: str = bin_str[index:]
        if not no_leadings:
            no_leadings = '0'
        no_leads_reverse: str = no_leadings[::-1]
        decimal: int = int(no_leads_reverse)

        # If decimal is going to be equal, check the original
        return (decimal, num)

    nums.sort(key=lambda num: bin_value(num))
    return nums


# Time complexity: O(n * log n)
# n - length of the input array `nums`.
# --- --- --- ---
# Space complexity: O(n)


test: list[int] = [4, 5, 4]
test_out: list[int] = [4, 4, 5]
assert test_out == sort_by_reflection(test)

test = [3, 6, 5, 8]
test_out = [8, 3, 6, 5]
assert test_out == sort_by_reflection(test)

test = [randint(1, 10 ** 9) for _ in range(100)]
copy(test)  # type: ignore
