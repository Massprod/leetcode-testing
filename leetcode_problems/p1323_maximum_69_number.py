# You are given a positive integer num consisting only of digits 6 and 9.
# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
# ----------------------
# 1 <= num <= 10 ** 4
# num consists of only 6 and 9 digits.


def maximum_69_number(num: int) -> int:
    # working_sol (96.75%, 52.08%) -> (25ms, 16.47mb)  time: O(n) | space: O(n)
    str_num: list[str] = list(str(num))
    for index, char in enumerate(str_num):
        if '6' == char:
            str_num[index] = '9'
            break
    return int(''.join(str_num))


# Time complexity: O(n) <- n - number of digits in input value `num`
# Always traversing every digit to create `str_num` => O(n).
# In the worst case there's no `6` in `num`, so we traverse it again => O(2 * n).
# Extra traverse to join and convert => O(3 * n).
# ----------------------
# Auxiliary space: O(n).
# We store every digit in `str_num` => O(n).
# Extra creating and array with `join` => O(2 * n).


test: int = 9669
test_out: int = 9969
assert test_out == maximum_69_number(test)

test = 9996
test_out = 9999
assert test_out == maximum_69_number(test)

test = 9999
test_out = 9999
assert test_out == maximum_69_number(test)
