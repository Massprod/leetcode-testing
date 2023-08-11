# You are given a binary string s consisting only of zeroes and ones.
# A substring of s is considered balanced if all zeroes are before ones and the number
#   of zeroes is equal to the number of ones inside the substring.
# Notice that the empty substring is considered a balanced substring.
# Return the length of the longest balanced substring of s.
# A substring is a contiguous sequence of characters within a string.
# --------------------
# 1 <= s.length <= 50
# '0' <= s[i] <= '1'


def find_the_longest(s: str) -> int:
    # working_sol (85.05%, 95.36%) -> (47ms, 16.19mb)  time: O(n) | space: O(1)
    # All pairs.
    all_count: int = 0
    # Zeroes to build pair with.
    count_zeroes: int = 0
    # Current index of input_s.
    index: int = 0
    while index != len(s):
        # Count '0' and move on.
        if s[index] == '0':
            count_zeroes += 1
            index += 1
            continue
        # We can start counting pairs.
        if s[index] == '1':
            # There's no '0' pair to build with.
            if count_zeroes == 0:
                index += 1
                continue
            # Current substring size.
            current_count: int = 0
            # If there's '0' left, we can try to build a pair.
            while count_zeroes != 0:
                current_count += 1
                index += 1
                # All array is used or reset of zeroes_count.
                if index == len(s) or s[index] != '1':
                    count_zeroes = 0
                    break
                count_zeroes -= 1
            # We need maximum correct substring.
            all_count = max(current_count, all_count)
    return all_count * 2


# Time complexity: O(n) -> traversing input_array, once => O(n).
# Auxiliary space: O(1) -> only 4 constant INTs used, none of them depends on input => O(1).
# --------------------
# Should be just counter with start from 0 and breaking when more than count(0) one's(1) met.


test: str = "01000111"
test_out: int = 6
assert test_out == find_the_longest(test)

test = "00111"
test_out = 4
assert test_out == find_the_longest(test)

test = "111"
test_out = 0
assert test_out == find_the_longest(test)

test = "001"
test_out = 1
assert test_out == find_the_longest(test)
