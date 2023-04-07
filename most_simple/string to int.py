# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
#
# The algorithm for myAtoi(string s) is as follows:
#
# Read in and ignore any leading whitespace.
# Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
# Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
# Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
# If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
# Return the integer as the final result.
# Note:
#
# Only the space character ' ' is considered a whitespace character.
# Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

def my_atoi(s: str) -> int:
    to_check = [str(_) for _ in range(0, 10)]
    sign = 1
    digits = ""
    for char in s:
        if char == "-":
            sign *= -1
        elif char not in to_check and len(digits) != 0:
            break
        elif char not in to_check:
            continue
        elif char in to_check:
            digits += char
    if len(digits) == 0:
        return 0
    num = int(digits) * sign
    min_num = -2 ** 31
    max_num = 2 ** 31 - 1
    if min_num < num < max_num:
        return num
    elif num <= min_num:
        return min_num
    elif num >= max_num:
        return max_num




test1 = "   -42  sdfa"
test2 = str(-2 ** 31)
test3 = str(2 ** 31 - 1)
test4 = ""
test5 = "  "
test6 = "--++11"
test7 = " -+ 11"
test8 = "  sadfasdfqwerqwerqw--_11wertwqerqwer"
test9 = " sdfgsdf000-123000wer1230--"
print(my_atoi(test1))
print(my_atoi(test2))
print(my_atoi(test3))
print(my_atoi(test4))
print(my_atoi(test5))
print(my_atoi(test6))
print(my_atoi(test7))
print(my_atoi(test8))
print(my_atoi(test9))