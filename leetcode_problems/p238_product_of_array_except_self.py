# Given an integer array nums, return an array answer such that answer[i] is equal
#   to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.
# ------------------
# 2 <= nums.length <= 10 ** 5
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# ------------------
# Follow up: Can you solve the problem in O(1) extra space complexity?
# (The output array does not count as extra space for space complexity analysis.)


def product_except_self(nums: list[int]) -> list[int]:
    # working_sol (40.17%, 22.78%) -> (248ms, 25.3mb)  time: O(n) | space: O(n)
    prefix: list[int] = []
    suffix: list[int] = []
    # Calculate prefixes
    prefix.append(nums[0])
    for x in range(1, len(nums) - 1):
        prefix.append(nums[x] * prefix[-1])
    # Calculate suffixes
    suffix.append(nums[-1])
    for y in range(len(nums) - 2, 0, -1):
        suffix.append(nums[y] * suffix[-1])
    # [0] is always last suffix itself, cuz there's no prefix for it.
    products: list[int] = [suffix.pop()]
    # Last prefix is also products[-1] itself, cuz there's no suffix for it.
    prefix_point: int = 0
    suffix_point: int = -1
    # prefix + suffix of any index is product except self.
    # Populated with just append() so we need to reverse suffixes.
    while prefix_point != len(prefix) - 1:
        products.append(prefix[prefix_point] * suffix[suffix_point])
        prefix_point += 1
        suffix_point -= 1
    # Last prefix:
    products.append(prefix.pop())
    return products


# Time complexity: O(n) -> traversing (n - 1) indexes of input_array, twice -> for all prefixes and suffixes ->
# n - len of input_array^^| -> extra taking products of (n - 2) elements of created suffix/prefix arrays, cuz
#                           suffix/prefix array is size of (n - 1) and their last elements didn't used =>
#                           => O(n - 1) + O(n - 1) + O(n - 2) => O(n).
# Auxiliary space: o(n) -> creating 3 extra arrays with sizes: (n - 1) + (n - 1) + (n) => O(n).
# ------------------
# Any multiplies like => 1 * 2 * 3 * 4 * 5, can be broken in prefix/suffix parts.
# 1 * 2 == suffix -> 3 <- prefix == 4 * 5.
# So we can just calculate every prefix part for every index and store it.
# Extra calculate suffix part and use it to get product without this index.
# Extra edges is SUFFIX/PREFIX itself, cuz there's no suffix part for [-1], and no prefix for [0].


test1 = [1, 2, 3, 4]
test1_out = [24, 12, 8, 6]
assert test1_out == product_except_self(test1)

test2 = [-1, 1, 0, -3, 3]
test2_out = [0, 0, 9, 0, 0]
assert test2_out == product_except_self(test2)

test3 = [0, 0]
test3_out = [0, 0]
assert test3_out == product_except_self(test3)

test4 = [100, -100]
test4_out = [-100, 100]
assert test4_out == product_except_self(test4)
