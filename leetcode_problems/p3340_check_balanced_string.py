# You are given a string num consisting of only digits.
# A string of digits is called balanced if the sum of the digits
#  at even indices is equal to the sum of digits at odd indices.
# Return true if num is balanced, otherwise return false.
# ---------------------
# 2 <= num.length <= 100
# num consists of digits only


def is_balanced(num: str) -> bool:
    # working_sol (100%, 98.11%) -> (0ms, 16.50mb)  time: O(n) | space: O(1)
    odd_sum: int = 0
    even_sum: int = 0
    for index in range(len(num)):
        if index % 2:
            odd_sum += int(num[index])
        else:
            even_sum += int(num[index])
    return odd_sum == even_sum


# Time complexity: O(n) <- n - length of the input string `num`.
# Always traversing whole input string `num`, once => O(n).
# ---------------------
# Auxiliary space: O(1)
# Only 2 constant INTs used, none of them depends on input => O(1).


test: str = "1234"
test_out: bool = False
assert test_out == is_balanced(test)

test = "24123"
test_out = True
assert test_out == is_balanced(test)
