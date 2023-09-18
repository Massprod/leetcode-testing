# Given an array of integers nums, sort the array in ascending order and return it.
# You must solve the problem without using any built-in functions in O(nlog(n))
#  time complexity and with the smallest space complexity possible.
# ----------------------
# 1 <= nums.length <= 5 * 10 ** 4
# -5 * 10 ** 4 <= nums[i] <= 5 * 10 ** 4
from random import randint


def sort_array(nums: list[int]) -> list[int]:
    # working_sol (59.63%, 75.55%) -> (1538ms, 24mb)  time: O(n * log n) | space: O(n)

    def merge_sort(array: list[int]) -> None:
        if len(array) > 1:
            middle: int = len(array) // 2
            left_half: list[int] = array[:middle]
            right_half: list[int] = array[middle:]
            merge_sort(left_half)
            merge_sort(right_half)
            left: int = 0
            right: int = 0
            orig: int = 0
            # Exhaust one half.
            while left != len(left_half) and right != len(right_half):
                if left_half[left] <= right_half[right]:
                    array[orig] = left_half[left]
                    left += 1
                else:
                    array[orig] = right_half[right]
                    right += 1
                orig += 1
            # Add what's left in one of the half's.
            while left != len(left_half):
                array[orig] = left_half[left]
                left += 1
                orig += 1
            while right != len(right_half):
                array[orig] = right_half[right]
                right += 1
                orig += 1

    merge_sort(nums)
    return nums


# Time complexity: O(n * log n) -> The time complexity of Merge Sort isθ(Nlog(N)) in all 3 cases
# n - len of input_array^^|        (worst, average, and best) as merge sort always divides the array
#                                  into two halves and takes linear time to merge two halves.
# Auxiliary space: O(n) -> we're always taking two halves from every input and using extra space to save them
#                          in left|right -> at max it will store same size as original array => O(n).
# ----------------------
# Done only 1 sorting task so far, and it's actually more Memory task.
# Previously used merge_sort which is O(n * log n).
# So, it should be correct to use it here even with O(n) extra space it's still OK on Time.
# Doubt someone expects from us creating of a new sorting method.
# Topic on that: https://www.geeksforgeeks.org/merge-sort/


test: list[int] = [5, 2, 3, 1]
test_out: list[int] = [1, 2, 3, 5]
assert test_out == sort_array(test)

test = [5, 1, 1, 2, 0, 0]
test_out = [0, 0, 1, 1, 2, 5]
assert test_out == sort_array(test)

test = [randint(-5 * 10 ** 4, 5 * 10 ** 4) for _ in range(10 ** 3)]
assert sorted(test) == sort_array(test)
print(test)
