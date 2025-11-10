# You are given an array nums of size n, consisting of non-negative integers.
# Your task is to apply some (possibly zero) operations on the array
#  so that all elements become 0.
# In one operation, you can select a subarray [i, j] (where 0 <= i <= j < n)
#  and set all occurrences of the minimum non-negative integer in that subarray to 0.
# Return the minimum number of operations required to make all elements in the array 0.
# --- --- --- ---
# 1 <= n == nums.length <= 10 ** 5
# 0 <= nums[i] <= 10 ** 5


def min_operations(nums: list[int]) -> int:
    # working_solution: (54.38%, 95.00%) -> (222ms, 29.55mb)  Time: O(n) Space: O(n)
    # ! minimum non-negative integer in that subarray to 0 !
    # 0 <- minimum non-negative integer
    # So, we can't just take whole array and convert minimum values.
    # We always need to have some break value, between two equals.
    stack: list[int] = []
    out: int = 0
    for num in nums:
        while stack and stack[-1] > num:
            stack.pop()
        if 0 == num:
            continue
        if not stack or stack[-1] < num:
            out += 1
            stack.append(num)

    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing the whole input array `nums`, once => O(n).
# --- --- --- ---
# Space complexity: O(n)
# In the worst case, whole input array `nums` is in decreasing state.
# `stack` <- allocates space for each value from `nums` => O(n).


test: list[int] = [0, 2]
test_out: int = 1
assert test_out == min_operations(test)

test =[3, 1, 2, 1]
test_out = 3
assert test_out == min_operations(test)

test = [1, 2, 1, 2, 1, 2]
test_out = 4
assert test_out == min_operations(test)
