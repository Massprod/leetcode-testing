# Given the binary representation of an integer as a string s,
#  return the number of steps to reduce it to 1 under the following rules:
#  - If the current number is even, you have to divide it by 2.
#  - If the current number is odd, you have to add 1 to it.
# It is guaranteed that you can always reach one for all test cases.
# ---------------------------
# 1 <= s.length <= 500
# s consists of characters '0' or '1'
# s[0] == '1'


def num_steps(s: str) -> int:
    # working_sol (75.19%, 94.14%) -> (34ms, 16.48mb)  time: O(s) | space: O(1)
    out: int = 0
    int_s: int = int(s, 2)
    while 1 != int_s:
        if not int_s % 2:
            int_s >>= 1
        else:
            int_s += 1
        out += 1
    return out


# Time complexity: O(s)
# Always depend on input value, linearly: first to convert string -> int, second to deplete => O(s).
# ---------------------------
# Auxiliary space: O(1)
# Always only 2 INT's used => O(1)


test: str = "1101"
test_out: int = 6
assert test_out == num_steps(test)

test = "10"
test_out = 1
assert test_out == num_steps(test)

test = "1"
test_out = 0
assert test_out == num_steps(test)
