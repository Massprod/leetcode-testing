# You are given a string num representing a large integer.
# An integer is good if it meets the following conditions:
#   - It is a substring of num with length 3.
#   - It consists of only one unique digit.
# Return the maximum good integer as a string or an empty string "" if no such integer exists.
# Note:
# A substring is a contiguous sequence of characters within a string.
# There may be leading zeroes in num or a good integer.
# -------------------
# 3 <= num.length <= 1000
# num only consists of digits.


def largest_good_integer(num: str) -> str:
    # working_sol (87.22%, 85.62%) -> (36ms, 16.20mb)  time: O(n) | space: O(1)
    out: str = '-1'
    for x in range(2, len(num)):
        if num[x] == num[x - 1] == num[x - 2]:
            out = str(max(int(out), int(num[x - 2:x + 1])))
    if out[0] == '0':
        # int() removes extra 0's.
        return '000'
    elif out == '-1':
        return ''
    return out


# Time complexity: O(n) <- n - length of input string 'num'.
# Single traverse of the whole input string 'nums' => O(n).
# Auxiliary space: O(1).


test: str = "6777133339"
test_out: str = "777"
assert test_out == largest_good_integer(test)

test = "2300019"
test_out = "000"
assert test_out == largest_good_integer(test)

test = "42352338"
test_out = ""
assert test_out == largest_good_integer(test)

test = "222"
test_out = "222"
assert test_out == largest_good_integer(test)
