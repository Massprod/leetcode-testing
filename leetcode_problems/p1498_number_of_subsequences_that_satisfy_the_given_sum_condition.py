# You are given an array of integers nums and an integer target.
#  Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it
#  is less or equal to target. Since the answer may be too large, return it modulo 109 + 7.
# --------------------
# 1 <= nums.length <= 105  ,  1 <= nums[i] <= 106  ,  1 <= target <= 106


def num_subseq(nums: list[int], target: int) -> int:
    # working_sol (91.82%, 33.87%) -> (777ms, 29.1mb)  time: O(n * (log n) + n) | space: O(1)
    nums.sort()
    subs: int = 0
    min_point: int = 0
    max_point: int = len(nums) - 1
    while min_point < max_point:
        if nums[min_point] + nums[max_point] <= target:
            options: int = max_point - min_point
            subs += 1 << options
            min_point += 1
            continue
        max_point -= 1
    if nums[min_point] << 1 <= target:
        subs += 1
    return subs % (10 ** 9 + 7)


# Time complexity: O(n * (log n) + n) -> sorting input_list with built_in => O(n * (log n)) ->
# n - len of input_list^^| -> traversing through whole input_list, checking every index as min or max points => O(n) ->
#                          -> O(n * (log n) + n)
# Space complexity: O(1) -> python built_in sort() => O(1) -> 4 extra constants, doesn't depend on input => O(1)
# --------------------
# Total subs for len == n ->  nC0 + nC1 + nC2 + … nCn = 2 ** n.
# For a future use -> always remember that bit_shift is faster than using ** or *,
#                     in this case is faster to do left_shift for 1 to option times,
#                     2 ** n => 1 << n, because left_shit is equal to (any * (2 ** n)) but it's faster.
#                     ^^took a peak on 780ms after mine 7900 ms.


test1 = [3, 5, 6, 7]
test1_target = 9
test1_out = 4
print(num_subseq(test1, test1_target))
assert test1_out == num_subseq(test1, test1_target)

test2 = [3, 3, 6, 8]
test2_target = 10
test2_out = 6
print(num_subseq(test2, test2_target))
assert test2_out == num_subseq(test2, test2_target)

test3 = [2, 3, 3, 4, 6, 7]
test3_target = 12
test3_out = 61
print(num_subseq(test3, test3_target))
assert test3_out == num_subseq(test3, test3_target)
