# You are given a binary string s and an integer k.
# A binary string satisfies the k-constraint if either of the following conditions holds:
#  - The number of 0's in the string is at most k.
#  - The number of 1's in the string is at most k.
# Return an integer denoting the number of substrings
#  of s that satisfy the k-constraint.
# ---------------------
# 1 <= s.length <= 50 
# 1 <= k <= s.length
# s[i] is either '0' or '1'.


def count_k_contstraint_substrings(s: str, k: int) -> int:
    # working_sol (100.00%, 88.42%) -> (0ms, 17.66mb)  time: O(n) | space: O(1)
    # Standard sliding window.
    w_zeroes: int = 0
    w_ones: int = 0
    left_l: int = 0
    right_l: int = 0
    out: int = 0
    while right_l < len(s):
        if '0' == s[right_l]:
            w_zeroes +=1
        else:
            w_ones += 1
        # We care only about one of the conditions satisfied.
        # So, if one overflow we don't care, only both.
        while k < w_zeroes and k < w_ones:
            if '0' == s[left_l]:
                w_zeroes -= 1
            else:
                w_ones -= 1
            left_l += 1
        out += (right_l - left_l) + 1  # +1 for 0-indexes
        right_l += 1

    return out


test: str = "10101"
test_k: int = 1
test_out: int = 12
assert test_out == count_k_contstraint_substrings(test, test_k)

test = "1010101"
test_k = 2
test_out = 25
assert test_out == count_k_contstraint_substrings(test, test_k)

test = "11111"
test_k = 1
test_out = 15
assert test_out == count_k_contstraint_substrings(test, test_k)
