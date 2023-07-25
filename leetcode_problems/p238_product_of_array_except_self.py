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
    # working_sol (69.64%, 97.8%) -> (237ms , 23.3mb)  time: O(n) | space: O(1)
    # For constant space storing everything in products.
    products: list[int] = [0, nums[0]]  # [0] is placeholder for last_suffix.
    # First prefixes:
    for x in range(1, len(nums) - 1):
        products.append(nums[x] * products[-1])
    # Last prefix is always last product of the last element except itself.
    suffix: int = nums[-1]
    # Last element is already set == last_prefix.
    # So we're starting from len() - 2
    products_point: int = len(products) - 2
    # We can use prefixes and multiply suffix until [1].
    # Cuz first element doesn't have prefix and last_suffix is product of [0] except_itself.
    while products_point >= 1:
        # Prefix * Suffix
        products[products_point] *= suffix
        # We're going backwards, so we can just multiply our suffix index_by_index
        suffix *= nums[products_point]
        # products_point -> points to a prefix of nums[pp] element and element itself,
        # element needs to be used to multiply suffix as well.
        products_point -= 1
    # last_suffix == product of [0] except_itself
    products[0] = suffix
    return products


# Time complexity: O(n) -> traversing n indexes of input_array, once -> for all prefixes ->
# n - len of input_array^^| -> extra traverse over created products(prefix) array to multiply it by suffix => O(n).
# Auxiliary space: O(1) -> if we ignore result_array as we asked, then only 2 extra INTs used => O(1).
# ------------------
# ! The output array does not count as extra space for space complexity analysis. !
# So we allowed to use only 1 extra array^^.
# Store every prefix as before, but skip part with suffixes?
# Like we know that first element is SUFFIX[-1] amd last is PREFIX[-1], we can use PREFIX[-1] insta.
# But for suffix we can walk backwards and multiply it for every index we pass until [0].
# At [0] we need to place SUFFIX itself. Let's try.
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

test5 = [2, 2, 3, 4]
test5_out = [24, 24, 16, 12]
assert test5_out == product_except_self(test5)
