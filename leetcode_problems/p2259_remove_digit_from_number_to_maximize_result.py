# You are given a string number representing a positive integer and a character digit.
# Return the resulting string after removing exactly one occurrence of digit from number
#  such that the value of the resulting string in decimal form is maximized.
# The test cases are generated such that digit occurs at least once in number.
# ----------------------
# 2 <= number.length <= 100
# number consists of digits from '1' to '9'.
# digit is a digit from '1' to '9'.
# digit occurs at least once in number.
from string import digits
from random import choice


def remove_digit(number: str, digit: str) -> str:
    # working_sol (70.92%, 92.80%) -> (34ms, 16.38mb)  time: O(n) | space: O(n)
    out: str
    remove_ind: int
    occurrences: list[int] = []
    remove_last: bool = True
    for index, dig in enumerate(number):
        if digit == dig:
            occurrences.append(index)
    # If only 1 occurrence or last digit.
    # The Best option is to delete the last occurrence,
    #  but ONLY if we don't have some pair when (occurrence < occurrence + 1).
    if 1 == len(occurrences):
        remove_ind = occurrences.pop()
        out = number[:remove_ind] + number[remove_ind + 1:]
        return out
    if occurrences[-1] == len(number) - 1:
        last_index: int = occurrences.pop()
    else:
        last_index = occurrences[-1]
    while occurrences:
        cur_ind: int = occurrences.pop()
        if int(number[cur_ind]) < int(number[cur_ind + 1]):
            remove_last = False
            remove_ind = cur_ind
    if remove_last:
        out = number[:last_index] + number[last_index + 1:]
        return out
    out = number[:remove_ind] + number[remove_ind + 1:]
    return out


# Time complexity: O(n) <- n - length of the input string `number`.
# Always traversing `number`, once => O(n).
# In the worst case there's only `digit` in `number`.
# So, we're going to traverse it as whole, again => O(2 * n).
# And always slicing it => O(3 * n).
# ----------------------
# Auxiliary space: O(n)
# `occurrences` <- will allocate space for every num in `number` => O(n).


test: str = "123"
test_digit: str = "3"
test_out: str = "12"
assert test_out == remove_digit(test, test_digit)

test = "1231"
test_digit = "1"
test_out = "231"
assert test_out == remove_digit(test, test_digit)

test = "551"
test_digit = "5"
test_out = "51"
assert test_out == remove_digit(test, test_digit)

digits = digits[1:]
test = ''.join([choice(digits) for _ in range(100)])
print(test)
