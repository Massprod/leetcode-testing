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
    # to_check = [str(_) for _ in range(0, 10)]
    # sign = 1
    # digits = ""
    # for char in s:
    #     if char == "-":
    #         sign *= -1
    #     elif char not in to_check and len(digits) != 0:
    #         break
    #     elif char not in to_check:
    #         continue
    #     elif char in to_check:
    #         digits += char
    # if len(digits) == 0:
    #     return 0
    # num = int(digits) * sign
    # min_num = -2 ** 31
    # max_num = 2 ** 31 - 1
    # if min_num < num < max_num:
    #     return num
    # elif num <= min_num:
    #     return min_num
    # elif num >= max_num:
    #     return max_num
    # rebuild whole
    to_check = [str(_) for _ in range(0, 10)]
    sign = 1
    digits = ""
    start = " "
    string_dict = {}
    for key, value in enumerate(s):
        string_dict[key] = value
    lenght = len(string_dict)
    for x in range(lenght):
        if x == lenght - 1 and string_dict[x] not in to_check:
            break
        elif x == lenght - 1 and string_dict[x] in to_check:
            digits += string_dict[x]
        elif string_dict[x] == start and string_dict[x + 1] != start:
            for y in range(x + 1, lenght):
                if string_dict[y] == "-":
                    sign *= -1
                elif string_dict[y] == "+":
                    sign *= 1
                elif string_dict[y] in to_check:
                    digits += string_dict[y]
                elif string_dict[y] not in to_check:
                    break
            break
        elif string_dict[x] in to_check:
            digits += string_dict[x]
            for z in range(x + 1, lenght):
                if string_dict[z] == "-":
                    sign *= -1
                elif string_dict[z] == "+":
                    sign *= 1
                elif string_dict[z] in to_check:
                    digits += string_dict[z]
                elif string_dict[z] not in to_check:
                    break
            break
        elif string_dict[x] == "-":
            sign *= -1
        elif string_dict[x] == ".":
            break
        elif string_dict[x] not in to_check:
            continue

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
test9 = "sdfgsdf000-123000wer1230--"
test10 = "words and 987"
# test10 - failed because we START reading after WHITESPACE and if it's not digits we ignore it
# (don't even thought about ignoring string with digits...)
test11 = "   -42"
test12 = "-91283472332"
# test 12 - failed because I counted option with digits at start and digits after whitespace,
# in THEM I count "-" or "+" but if sign before this part it was ignored. Was counting before changes
test13 = ".1"
# test 13 - failed???
# print(my_atoi(test1))
# print(my_atoi(test2))
# print(my_atoi(test3))
# print(my_atoi(test4))
# print(my_atoi(test5))
# print(my_atoi(test6))
# print(my_atoi(test7))
# print(my_atoi(test8))
# print(my_atoi(test9))
# print(my_atoi(test10))
# print(my_atoi(test11))
# print(my_atoi(test12))
print(my_atoi(test13))