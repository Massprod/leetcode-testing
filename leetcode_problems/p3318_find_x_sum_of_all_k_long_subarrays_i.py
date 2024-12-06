# You are given an array nums of n integers and two integers k and x.
# The x-sum of an array is calculated by the following procedure:
#  - Count the occurrences of all elements in the array.
#  - Keep only the occurrences of the top x most frequent elements.
#     If two elements have the same number of occurrences,
#      the element with the bigger value is considered more frequent.
#  - Calculate the sum of the resulting array.
# Note that if an array has less than x distinct elements, its x-sum is the sum of the array.
# Return an integer array answer of length n - k + 1 where answer[i] is the x-sum of the subarray nums[i..i + k - 1].
# ----------------------------------
# 1 <= n == nums.length <= 50
# 1 <= nums[i] <= 50
# 1 <= x <= k <= nums.length
from collections import Counter, deque


def find_x_sum(nums: list[int], k: int, x: int) -> list[int]:
    # working_sol (60.22%, 5.13%) -> (24ms, 17.40mb)  time: O(n * (k + k * log k)) | space: O(n + k)
    out: list[int] = []

    def get_values(w_slice: deque[int], uniques: int) -> int:
        counted: dict[int, int] = Counter(w_slice)
        sorted_slice: list[tuple[int, int]] = sorted(
            counted.items(), key=lambda val_freq: (val_freq[1], val_freq[0]), reverse=True
        )
        cur_sum: int = 0
        for val, occur in sorted_slice[:uniques]:
            cur_sum += val * occur
        return cur_sum

    start: int = 0
    end: int = k
    cur_window: deque[int] = deque(nums[:end])
    while end <= len(nums):
        out.append(
            get_values(cur_window, x)
        )
        if end == len(nums):
            break
        cur_window.popleft()
        cur_window.append(nums[end])
        start += 1
        end += 1

    return out


# Time complexity: O(n * (k + k * log k)) <- n - length of the input array `nums`.
# Always creating windows for all subarrays of the `num`.
# Count + sort all of them => O(n * (k + k * log k).
# ----------------------------------
# Auxiliary space: O(n + k)
# `out` <- allocates space for each index, if we got `k` == 1 => O(n).
# `counted` <- allocates space for all values in window of size `k` => O(n + k).
# `sorted_slice` <- allocates space for double tuples of every value from `counted` => O(n + k + k).


test: list[int] = [1, 1, 2, 2, 3, 4, 2, 3]
test_k: int = 6
test_x: int = 2
test_out: list[int] = [6, 10, 12]
assert test_out == find_x_sum(test, test_k, test_x)

test = [3, 8, 7, 8, 7, 5]
test_k = 2
test_x = 2
test_out = [11, 15, 15, 15, 12]
assert test_out == find_x_sum(test, test_k, test_x)
