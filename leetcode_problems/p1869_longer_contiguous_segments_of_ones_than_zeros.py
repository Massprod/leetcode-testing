# Given a binary string s, return true if the longest contiguous segment of 1's
#  is strictly longer than the longest contiguous segment of 0's in s, or return false otherwise.
# For example, in s = "110100010" the longest continuous segment of 1s has length 2,
#  and the longest continuous segment of 0s has length 3.
# Note that if there are no 0's, then the longest continuous segment of 0's is considered to have a length 0.
# The same applies if there is no 1's.
# -------------------------
# 1 <= s.length <= 100
# s[i] is either '0' or '1'.


def check_zero_ones(s: str) -> bool:
    # working_sol (83.65%, 65.18%) -> (31ms, 16.42mb)  time: O(s) | space: O(1)
    zero_seq: int = 0
    ones_seq: int = 0
    cur_seq: int = 0
    cur_sym: str = s[0]
    for char in s:
        if char == cur_sym:
            cur_seq += 1
        else:
            if '1' == cur_sym:
                ones_seq = max(ones_seq, cur_seq)
            else:
                zero_seq = max(zero_seq, cur_seq)
            cur_seq = 1
            cur_sym = char
    if '1' == cur_sym:
        ones_seq = max(ones_seq, cur_seq)
    else:
        zero_seq = max(zero_seq, cur_seq)
    return ones_seq > zero_seq


# Time complexity: O(s)
# Always traversing whole input string `s`, once => O(s).
# -------------------------
# Auxiliary space: O(1).


test: str = "1101"
test_out: bool = True
assert test_out == check_zero_ones(test)

test = "111000"
test_out = False
assert test_out == check_zero_ones(test)

test = "110100010"
test_out = False
assert test_out == check_zero_ones(test)
