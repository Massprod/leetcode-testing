# You are given an integer array nums of length n.
# The score of an index i is defined as the number of indices j such that:
#  - i < j < n, and
#  - nums[i] and nums[j] have different parity (one is even and the other is odd).
# Return an integer array answer of length n, where answer[i] is the score of index i.
# --- --- --- ---
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100


def count_opposite_parity(nums: list[int]) -> list[int]:
    # working_solution: (71.73%, 96.21%) -> (3ms, 19.14mb)  Time: O(n) Space: O(1)
    counts: dict[str, int] = {
        'odd': 0,
        'even': 0
    }
    for num in nums:
        if num % 2:
            counts['odd'] += 1
        else:
            counts['even'] += 1
    out: list[int] = []
    for num in nums:
        if num % 2:
            counts['odd'] -= 1
            out.append(
                counts['even']
            )
        else:
            counts['even'] -= 1
            out.append(
                counts['odd']
            )

    return out


# Time complexity: O(n)
# n - length of the input array `nums`
# --- --- --- ---
# Space complexity: O(1)


test: list[int] = [1, 2, 3, 4]
test_out: list[int] = [2, 1, 1, 0]
assert test_out == count_opposite_parity(test)

test = [1]
test_out = [0]
assert test_out == count_opposite_parity(test)
