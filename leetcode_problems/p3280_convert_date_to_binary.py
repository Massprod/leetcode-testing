# You are given a string date representing a Gregorian calendar date in the yyyy-mm-dd format.
# date can be written in its binary representation obtained by converting year, month,
#  and day to their binary representations without any leading zeroes
#  and writing them down in year-month-day format.
# Return the binary representation of date.
# ------------------------
# date.length == 10
# date[4] == date[7] == '-', and all other date[i]'s are digits.
# The input is generated such that date represents a valid Gregorian calendar date between Jan 1st, 1900
#  and Dec 31st, 2100 (both inclusive).


def convert_date_to_binary(date: str) -> str:
    # working_sol (75.46%, 23.95%) -> (32ms, 16.57mb)  time: O(n) | space: O(n)
    return '-'.join([str(bin(int(value)))[2:] for value in date.split('-')])


# Time complexity: O(n) <- n - length of the input string `date`.
# Always traversing `date` once to split it => O(n).
# Extra converting every value from it to INT and STR again with joining them after => O(2 * n).
# ------------------------
# Auxiliary space: O(n)
# `split` <- creates an array with the sum sized strings as `date` => O(n).


test: str = "2080-02-29"
test_out: str = "100000100000-10-11101"
assert test_out == convert_date_to_binary(test)

test = "1900-01-01"
test_out = "11101101100-1-1"
assert test_out == convert_date_to_binary(test)
