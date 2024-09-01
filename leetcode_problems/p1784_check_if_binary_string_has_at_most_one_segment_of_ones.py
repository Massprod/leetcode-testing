# Given a binary string s without leading zeros,
#  return true if s contains at most one contiguous segment of ones.
# Otherwise, return false.
# -----------------
# 1 <= s.length <= 100
# s[i] is either '0' or '1'.
# s[0] is '1'.


def check_ones_segment(s: str) -> bool:
    # working_sol (60.68%, 89.60%) -> (34ms, 16.34mb)  time: O(s) | space: O(1)
    # ! string s without leading zeros !
    # So, the only way there's going to be two sequences.
    # It's when `0 -> 1`, and it can happen only after index == 0.
    for index in range(1, len(s)):
        if '1' == s[index] and '0' == s[index - 1]:
            return False
    return True


# Time complexity: O(s)
# Always using every index of `s`, once => O(s).
# -----------------
# auxiliary space: O(1).


test: str = "1001"
test_out: bool = False
assert test_out == check_ones_segment(test)

test = "110"
test_out = True
assert test_out == check_ones_segment(test)
