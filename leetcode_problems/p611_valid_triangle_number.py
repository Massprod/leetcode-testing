# Given an integer array nums, return the number of triplets chosen from the array
#  that can make triangles if we take them as side lengths of a triangle.
# --- --- --- ---
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000


def triangle_number(nums: list[int]) -> int:
    # working_solution: (97.53%, 82.54%) -> (395ms, 17.77mb)  Time: O(n ** 2) Space: O(n)
    # side + side > main_side => correct triangle
    # Take highest, find 2 others => good.
    nums.sort()
    out: int = 0

    for index in range(len(nums) - 1, -1, -1):
        side_main: int = nums[index]
        left: int = 0            # lowest
        right: int = index - 1   # highest we could use
        while left < right:
            # If we can get correct pairs with the currently highest.
            # Then we already included all the options with it.
            # So, we need to take the next highest option.
            if (nums[left] + nums[right]) > side_main:
                out += right - left
                right -= 1
            # If we can't get correct pair at all, try to use something bigger.
            else:
                left += 1
    
    return out


# Time complexity: O(n ** 2) <- n - length of the input array `nums`.
# Sorting the input array takes => O(n * log n).
# And we extra traverse the whole array with nested (n - 1) loop => O(n * n + n * log n)
# --- --- --- ---
# Space complexity: O(n)
# `sort` <- takes O(n).


test: list[int] = [2, 2, 3, 4]
test_out: int = 3
assert test_out == triangle_number(test)

test = [4, 2, 3, 4]
test_out = 4
assert test_out == triangle_number(test)
