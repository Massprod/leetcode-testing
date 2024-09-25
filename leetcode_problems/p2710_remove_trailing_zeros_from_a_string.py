# Given a positive integer num represented as a string,
#  return the integer num without trailing zeros as a string.
# -----------------------
# 1 <= num.length <= 1000
# num consists of only digits.
# num doesn't have any leading zeros.


def remove_trailing_zeros(num: str) -> str:
    # working_sol (64.93%, 94.24%) -> (41ms, 16.49mb)  time: O(n) | space: O(1)
    start: int = 0
    end: int = len(num) - 1
    while '0' == num[start]:
        start += 1
    while start < end and '0' == num[end]:
        end -= 1
    return num[start: end + 1]


# Time complexity: O(n) <- n - length of the input string `num`.
# In the worst case, there's only '0' in `num`.
# We will use every char of `num`, once => O(n).
# -----------------------
# Auxiliary space: O(1)
# Only two constant INTs used, none of them depends on input => O(1).


test: str = "51230100"
test_out: str = "512301"
assert test_out == remove_trailing_zeros(test)

test = "123"
test_out = "123"
assert test_out == remove_trailing_zeros(test)
