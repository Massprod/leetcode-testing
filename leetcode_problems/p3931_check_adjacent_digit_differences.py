# You are given a string s consisting of digits.
# Return true if the absolute difference between every pair of adjacent digits
#  is at most 2, otherwise return false.
# The absolute difference between a and b is defined as abs(a - b).
# --- --- --- ---
# 2 <= s.length <= 100
# s consists only of digits.


def is_adjacent_diff_at_most_two(s: str) -> bool:
    # working_solution: (100%, 100%) -> (0ms, 0mb)  Time: O(s) Space: O(1)
    for index in range(1, len(s)):
        if 2 < abs(int(s[index]) - int(s[index - 1])):
            return False
    return True


# Time complexity: O(s)
# --- --- --- ---
# Space complexity: O(1)


test: str = "132"
test_out: bool = True
assert test_out == is_adjacent_diff_at_most_two(test)

test = "129"
test_out = False
assert test_out == is_adjacent_diff_at_most_two(test)
