# You are given an integer array nums of even length n.
# You have to merge the elements of nums in pairs by merging nums[0]
#  with nums[1], nums[2] with nums[3], and so on, until nums[n - 2] with nums[n - 1].
# Return the minimum value among all the resulting merged integers.
# To merge two integers, concatenate all the decimal digits of the first integer
#  followed by all the decimal digits of the second integer.
# --- --- --- ---
# 2 <= n == nums.length <= 100
# n is even
# 1 <= nums[i] <= 1000

def min_merged_integer(nums: list[int]) -> int:
    # working_solution: (48.50%, 57.09%) -> (3ms, 19.17mb)  Time: O(n) Space: O(1)
    out: int = 4_000_000_000
    for index in range(1, len(nums), 2):
        pair: int = int(
            str(nums[index - 1]) + str(nums[index])
        )
        out = min(out, pair)
    
    return out


# Time complexity: O(n)
# n - length of the input array `nums`
# --- --- --- ---
# Space complexity: O(1)


test: list[int] = [23, 55, 42, 21]
test_out: int = 2355
assert test_out == min_merged_integer(test)

test = [34, 7, 11, 11]
test_out = 347
assert test_out == min_merged_integer(test)

test = [9, 20]
test_out = 920
assert test_out == min_merged_integer(test)
