# Given two non-negative integers low and high.
# Return the count of odd numbers between low and high (inclusive).
# ---------------------
# 0 <= low <= high <= 10 ** 9


def count_odds(low: int, high: int) -> int:
    # working_sol (56.69%, 75.85%) -> (34ms, 16.43mb)  time: O(1) | space: O(1)
    range_vals: int = high - low + 1
    if range_vals % 2:
        if low % 2 or high % 2:
            return range_vals // 2 + 1
        return range_vals // 2
    return range_vals // 2


# Time complexity: O(1)
# ---------------------
# Auxiliary space: O(1)


test_low: int = 3
test_high: int = 7
test_out: int = 3
assert test_out == count_odds(test_low, test_high)

test_low = 8
test_high = 10
test_out = 1
assert test_out == count_odds(test_low, test_high)
