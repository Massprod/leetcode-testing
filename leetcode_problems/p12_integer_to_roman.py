# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together.
# 12 is written as XII, which is simply X + II.
# The number 27 is written as XXVII, which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is written as IV.
# Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX.
# There are six instances where subtraction is used:
#   I can be placed before V (5) and X (10) to make 4 and 9.
#   X can be placed before L (50) and C (100) to make 40 and 90.
#   C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral.
# ----------------
# 1 <= num <= 3999


def int_to_roman(num: int) -> str:
    # working_sol (94.21%, 96.73%) -> (42ms, 16.1mb)  time: O(n) | space: O(n)
    # All romans with subtraction options.
    values: dict[int, str] = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }
    roman: str = ""
    # ! Roman numerals are usually written
    #   largest to smallest from left to right. !
    # So, we can just use highest -> lowest values.
    for key, value in values.items():
        while num >= key:
            num -= key
            roman += value
    return roman


# Time complexity: O(n) -> creating dictionary with all roman_options, always constant => O(1) ->
# n - input value^^| -> decreasing input value until it's equal to 0 => O(n).
# Auxiliary space: O(n) -> dictionary is always constant => O(1) -> output string with roman version of input value
#                          depend on input => O(n).
#                          Maybe we can call worst_case: n == 3999, then it's size == 9, but it's still linear O(n).


test: int = 3
test_out: str = "III"
assert test_out == int_to_roman(test)

test = 58
test_out = "LVIII"
assert test_out == int_to_roman(test)

test = 1994
test_out = "MCMXCIV"
assert test_out == int_to_roman(test)
