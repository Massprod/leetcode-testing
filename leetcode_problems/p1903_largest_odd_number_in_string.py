# You are given a string num, representing a large integer.
# Return the largest-valued odd integer (as a string) that is a non-empty substring of num,
#  or an empty string "" if no odd integer exists.
# A substring is a contiguous sequence of characters within a string.
# -----------------------
# 1 <= num.length <= 10 ** 5
# num only consists of digits and does not contain any leading zeros.


def largest_odd_number(num: str) -> str:
    # working_sol (84.33%, 79.82%) -> (49ms, 79.82%)  time: O(n) | space: O(1)
    # Last digit ODD => number is ODD.
    # Last digit EVEN => number is EVEN.
    # We go right -> left to get maximised.
    for x in range(len(num) - 1, -1, -1):
        if int(num[x]) % 2:
            return num[:x + 1]
    return ""


# Time complexity: O(n) <- n - length of input string 'num'.
# Single traverse if ODD not present.
# Auxiliary space: O(1).


test: str = "52"
test_out: str = "5"
assert test_out == largest_odd_number(test)

test = "4206"
test_out = ""
assert test_out == largest_odd_number(test)

test = "35427"
test_out = "35427"
assert test_out == largest_odd_number(test)
