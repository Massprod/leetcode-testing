# You are given an integer num.
# You will apply the following steps to num two separate times:
#  - Pick a digit x (0 <= x <= 9).
#  - Pick another digit y (0 <= y <= 9). Note y can be equal to x.
#  - Replace all the occurrences of x in the decimal representation of num by y.
# Let a and b be the two results from applying the operation to num independently.
# Return the max difference between a and b.
# Note that neither a nor b may have any leading zeros, and must not be 0.
# ----------------------------
# 1 <= num <= 10 ** 8


def max_diff(num: int) -> int:
    # working_sol (100.00%, 89.32%) -> (0ms, 17.69mb)  time: O(n) | space: O(n)
    # Lowest can't be `0`, so the lowest digit we should use is `1`.
    # Highest digit we should use is `9`.
    # Best option to get the highest value:
    #  take first digit if it's not equal `9` and convert it to `9`,
    #  or find another lower digit option.
    str_num: str = str(num)
    target_digit: str = ''
    for dig in str_num:
        if '9' != dig:
            target_digit = dig
            break
    highest: str = str_num.replace(target_digit, '9') if target_digit else str_num
    # Best option to get the lowest value:
    #  take first digit if it's not equal to `1` and convert it to `0`,
    #  of find another higher digit option.
    target_digit = ''
    for dig in str_num:
        if '1' != dig and '0' != dig:
            target_digit = dig
            break
    lowest = str_num
    if target_digit:
        # We can't have leading zeroes => we can't zero first value => make it `1`.
        if target_digit == str_num[0]:
            lowest = str_num.replace(target_digit, '1')
        # Otherwise, skip it and use zero.
        else:
            lowest = str_num.replace(target_digit, '0')
    
    return int(highest) - int(lowest)


# Time complexity: O(n) <- n - number of digits in the input value `num`.
# Always converting `num` into string => O(n).
# Extra traversing all the characters, once for 4 times => O(5 * n).
# -------------------------
# Auxiliary space: O(n)
# `str_num` & `highest` & `lowest` <- allocates space for each digit => O(n).


test: int = 555
test_out: int = 888
assert test_out == max_diff(test)

test = 9
test_out = 8
assert test_out == max_diff(test)
