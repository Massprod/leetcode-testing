# Implement the myAtoi(string s) function, which converts a string
# to a 32-bit signed integer (similar to C/C++'s atoi function).
#
# The algorithm for myAtoi(string s) is as follows:
#
# Read in and ignore any leading whitespace.
# Check if the next character (if not already at the end of the string) is '-' or '+'.
# Read this character in if it is either. This determines if the final result is negative or positive respectively.
# Assume the result is positive if neither is present.
# Read in next the characters until the next non-digit character or the end of the input is reached.
# The rest of the string is ignored.
# Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0.
# Change the sign as necessary (from step 2).
# If the integer is out of the 32-bit signed integer range [-231, 231 - 1],
# then clamp the integer so that it remains in the range.
# Specifically, integers less than -231 should be clamped to -231,
# and integers greater than 231 - 1 should be clamped to 231 - 1.
# Return the integer as the final result.
# Note:
#
# Only the space character ' ' is considered a whitespace character.
# Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

def my_atoi(s: str) -> int:
    # working_sol (76.50%, 16.30%)  time: O(n) | space: O(n)
    to_check = [str(_) for _ in range(0, 10)]
    digits = ""
    whitespace = " "
    sign = 1
    string_dict = {}
    for key, value in enumerate(s):
        string_dict[key] = value
    lenght = len(string_dict)
    for x in range(lenght):
        if string_dict[x] == whitespace:
            continue
        elif string_dict[x] == "-":
            sign *= -1
            for y in range(x + 1, lenght):
                if string_dict[y] in to_check:
                    digits += string_dict[y]
                else:
                    break
            break
        elif string_dict[x] == "+":
            for y in range(x + 1, lenght):
                if string_dict[y] in to_check:
                    digits += string_dict[y]
                else:
                    break
            break
        elif string_dict[x] in to_check:
            digits += string_dict[x]
            for y in range(x + 1, lenght):
                if string_dict[y] in to_check:
                    digits += string_dict[y]
                else:
                    break
            break
        elif string_dict[x] not in to_check:
            break
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


# Time complexity: O(n) -> in worst case we are going through whole LIST.
# Space complexity: O(n) -> creating new dictionary of input len.

# Overall it's really easy Task, but I was not careful with rules and expected this to READ ANY STRING
# and return ANY number in it. Even if we had more than 1 sign to change and no matter what was before DIGIT
# But for the task we needed to READ string only with certain START and continue if next symbol is DIGIT


test1 = "   -42  sdfa"
test2 = str(-2 ** 31)
test3 = str(2 ** 31 - 1)
test4 = ""
test5 = "  "
test6 = "--++11"
test7 = " -+ 11"
test8 = "  sadfasdfqwerqwerqw--_11wertwqerqwer"
test9 = "sdfgsdf000-123000wer1230--"
test10 = "words and 987"
# test10 - failed because we START reading after WHITESPACE and if it's not digits we ignore it
# (don't even thought about ignoring string with digits...)
test11 = "   -42"
test12 = "-91283472332"
# test 12 - failed because I counted option with digits at start and digits after whitespace,
# in THEM I count "-" or "+" but if sign before this part it was ignored. Was counting before changes
test13 = ".1"
# test 13 - failed because I was not correct with reading rules and if cursor not on Digit, Whitespace, Sign
# we should ignore this string because There's NO leading_whitespaces, sign or digit at [0]
# Means I should rebuild WHOLE because I was incorrect from the beginning :)
# Solution is much simpler than I was thinking. I was thinking about reading whole STRING with some conditions, but
# if I was reading more carefully
# I would get that we BREAK everything if string doesn't start with WHITESPACE, SIGN, DIGIT
test14 = "+-12"
print(my_atoi(test1))
print(my_atoi(test2))
print(my_atoi(test3))
print(my_atoi(test4))
print(my_atoi(test5))
print(my_atoi(test6))
print(my_atoi(test7))
print(my_atoi(test8))
print(my_atoi(test9))
print(my_atoi(test10))
print(my_atoi(test11))
print(my_atoi(test12))
print(my_atoi(test13))
print(my_atoi(test14))
