# You are given an integer array nums.
# A subarray is called balanced if the number of distinct even numbers in the subarray
#  is equal to the number of distinct odd numbers.
# Return the length of the longest balanced subarray.
# --- --- --- ---
# 1 <= nums.length <= 1500
# 1 <= nums[i] <= 10 ** 5


def longest_balanced(nums: list[int]) -> int:
    # working_solution: (97.45%, 57.02%) -> (297ms, 19.56mb)  Time: O(n ** 2) Space: O(n)
    out: int = 0
    even: set[int] = set()
    odd: set[int] = set()
    for start in range(len(nums)):
        max_option: int = len(nums) - start
        if out >= max_option:
            break
        for end in range(start, len(nums)):
            if nums[end] % 2:
                odd.add(nums[end])
            else:
                even.add(nums[end])
            if len(even) != len(odd):
                continue
            out = max(out, (end - start) + 1)
        even.clear()
        odd.clear()
    
    return out


# Time complexity: O(n ** 2)
# n - length of the input array `nums`.
# --- --- --- ---
# Space complexity: O(n)


test: list[int] = [2, 5, 4, 3]
test_out: int = 4
assert test_out == longest_balanced(test)

test = [3, 2, 2, 5, 4]
test_out = 5
assert test_out == longest_balanced(test)

test = [1, 2, 3, 2]
test_out = 3
assert test_out == longest_balanced(test)
