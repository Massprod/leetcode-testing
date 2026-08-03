# You are given an integer array nums.
# Choose exactly one pair of distinct indices i and j.
# The strength of the pair is defined as
#  (nums[i] * nums[j]) / gcd(nums[i], nums[j]) ** 2.
# Return the maximum strength over all possible pairs.
# --- --- --- ---
# 2 <= nums.length <= 2000
# 1 <= nums[i] <= 10 ** 5


def max_pair_strength(nums: list[int]) -> int:
    # working_solution: (40%, 100%) -> (2164ms, 19.98mb)  Time: O(n ** 2) Space: O(n)
    out: int = 0
    
    def gcd(higher: int, lower: int) -> int:
        if 0 == lower:
            return higher
        
        return gcd(lower, higher % lower)

    sorted_nums: list[int] = sorted(nums, reverse=True)
    for index, val_1 in enumerate(sorted_nums):
        # If we already have answer higher than `maximum` * current.
        # We can't get anything higher.
        if out > val_1 * sorted_nums[0]:
            break
        for val_2 in sorted_nums[index + 1:]:
            cur_prod: int = val_1 * val_2
            # Everything else is going to be lower.
            if out >= cur_prod:
                break
            cur_gcd: int = gcd(val_1, val_2)
            cur: int = cur_prod // cur_gcd // cur_gcd
            out = max(out, cur)
    
    return out


# Time complexity: O(n ** 2)
# n - length of the input array `nums`
# --- --- --- ---
# Space complexity: O(n)


test: list[int] = [2, 3, 5]
test_out: int = 15
assert test_out == max_pair_strength(test)

test = [4, 6, 8]
test_out = 12
assert test_out == max_pair_strength(test)

test = [3, 3]
test_out = 1
assert test_out == max_pair_strength(test)
