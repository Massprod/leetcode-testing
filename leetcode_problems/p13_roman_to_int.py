# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral,
#  just two ones added together. 12 is written as XII,
#  which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is written as IV.
# Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX.
# There are six instances where subtraction is used:
#   I can be placed before V (5) and X (10) to make 4 and 9.
#   X can be placed before L (50) and C (100) to make 40 and 90.
#   C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.
# ----------------------
# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].


def roman_to_int(s: str) -> int:
    # working_sol (93.80%, 39.89%) -> (42ms, 16.3mb)  time: O(n) | space: O(1)
    symbols: dict[str, int] = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    # Last value either by itself or will be subtracted.
    # But we can use it instantly.
    roman: int = symbols[s[-1]]
    for x in range(len(s) - 2, -1, -1):
        # Only case of subtraction is when lower placed before higher value.
        if symbols[s[x]] < symbols[s[x + 1]]:
            roman -= symbols[s[x]]
            continue
        roman += symbols[s[x]]
    return roman


# Time complexity: O(n) -> creating of dictionary with roman values, always constant => O(1) ->
# n - len of input string^^| ->  traverse of whole input string, once => O(n).
# Auxiliary space: O(1) -> dictionary is always constant and extra INT, which doesn't depend on input as well => O(1).


test: str = "III"
test_out: int = 3
assert test_out == roman_to_int(test)

test = "LVIII"
test_out = 58
assert test_out == roman_to_int(test)

test = "MCMXCIV"
test_out = 1994
assert test_out == roman_to_int(test)
