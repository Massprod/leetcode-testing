# Given a non-empty array of non-negative integers nums,
#  the degree of this array is defined as the maximum frequency of any one of its elements.
# Your task is to find the smallest possible length of a (contiguous) subarray of nums,
#  that has the same degree as nums.
# --------------------
# nums.length will be between 1 and 50,000.
# nums[i] will be an integer between 0 and 49,999.
from random import randint


def find_shortest_sub_array(nums: list[int]) -> int:
    # working_sol (66.99%, 21.30%) -> (176ms, 18.8mb)  time: O(n) | space: O(n)
    # {value:
    #   {
    #     left: most left index when this value occurred,
    #     right: most right index when this value occurred,
    #     occurs: number of times this value occurred,
    #   }
    # }
    all_vals: dict[int, dict[str, int]] = {}
    for index, num in enumerate(nums):
        if num not in all_vals:
            all_vals[num] = {
                'left': index,
                'right': index,
                'occurs': 1,
            }
            continue
        all_vals[num]['right'] = index
        all_vals[num]['occurs'] += 1
    # {occurrences: {all values with this number of occurrences} }
    occurs: dict[int, set[int]] = {}
    for num, data in all_vals.items():
        if data['occurs'] not in occurs:
            occurs[data['occurs']] = {num}
        occurs[data['occurs']].add(num)
    out: int = len(nums)
    # `nums` edge == `subarray` edge <- we're always going to have subarray with the same
    #  max number of occurrences for value.
    # But we can have different values, and we need to check all of them.
    # And because we only care about `max` occurrences == edge,
    #  we can find distance between their first and last occurrences == left, right indexes.
    for option in occurs[max(occurs.keys())]:
        out = min(
            out,
            (all_vals[option]['right'] - all_vals[option]['left']) + 1  # +1 - zero indexed
        )
    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# Worst case: every value is unique, and essentially we're just going to traverse whole array
#  3 times.
# First: get all occurrences and indexes => O(n).
# Second: get all values set with their occurrences, and in our case occurrences == # of values => O(2n).
# Third: check every option, which again in our case is equal to `n` => O(3n).
# --------------------
# Auxiliary space: O(n)
# `all_vals` will hold `n` keys and for each constant values => O(n).
# `occurs` will hold `n` keys and for each only 1 option => O(2n).


test: list[int] = [1, 2, 2, 3, 1]
test_out: int = 2
assert test_out == find_shortest_sub_array(test)

test = [1, 2, 2, 3, 1, 4, 2]
test_out = 6
assert test_out == find_shortest_sub_array(test)

test = [randint(0, 49_999) for _ in range(50_000)]
print(test)
