# Given two non-negative integers, num1 and num2 represented as string,
#  return the sum of num1 and num2 as a string.
# You must solve the problem without using any built-in library for handling
#  large integers (such as BigInteger).
# You must also not convert the inputs to integers directly.
# ------------------------
# 1 <= num1.length, num2.length <= 10 ** 4
# num1 and num2 consist of only digits.
# num1 and num2 don't have any leading zeros except for the zero itself.


def add_strings(num1: str, num2: str) -> str:
    # working_sol (97.28%, 77.43%) -> (32ms, 16.67mb)  time: O(n) | space: O(n)
    # Assume we can't use int() at all.
    # But we know that ascii for 0 -> 9 is 48 -> 57.
    # So, we can get any digit with: ord('digit') - ord('0').
    remainder: int = 0
    if len(num1) < len(num2):
        lower_limit: int = len(num1)
        higher_limit: int = len(num2)
    else:
        lower_limit, higher_limit = len(num2), len(num1)
    out: str = ''
    # We need always to summarise lower sized string first, and use remainder with higher one.
    # Using all digits from lower string first.
    for index in range(-1, lower_limit * -1 - 1, -1):
        digit1: int = ord(num1[index]) - ord('0')
        digit2: int = ord(num2[index]) - ord('0')
        cur_sum: int = digit1 + digit2 + remainder
        if 9 < cur_sum:
            remainder = 1
            cur_sum -= 10
        else:
            remainder = 0
        # Assume we can't use str() either.
        out += chr(48 + cur_sum)
    highest: str = num1 if len(num1) > len(num2) else num2
    # For higher one, we need to include remainder + all digits in this string.
    # Higher string is always starting from (len(lower) - 1) index, if they're equal we ignore loop.
    for index in range(lower_limit * -1 - 1, higher_limit * -1 - 1, -1):
        digit1 = ord(highest[index]) - ord('0')
        cur_sum = digit1 + remainder
        if 9 < cur_sum:
            remainder = 1
            cur_sum -= 10
        else:
            remainder = 0
        out += chr(48 + cur_sum)
    if remainder:
        out += chr(48 + remainder)
    # We summarized from right -> left, so we need to reverse it.
    return out[::-1]


# Time complexity: O(max(num1, num2)).
# We always traversing both input strings, but we care about max() sized
# Extra, we're reversing sum, which can be max(num1, num2) + 1 size, if we have remainder to add.
# O(max(num1, num2) + 1)
# ------------------------
# Auxiliary space: O(O(max(num1, num2)).
# Same, we can get string `out` of size max(num1, num2) + 1 if we have remainder => O(max(num1, num2) + 1).


test_1: str = "11"
test_2: str = "123"
test_out: str = "134"
assert test_out == add_strings(test_1, test_2)

test_1 = "456"
test_2 = "77"
test_out = "533"
assert test_out == add_strings(test_1, test_2)

test_1 = "0"
test_2 = "0"
test_out = "0"
assert test_out == add_strings(test_1, test_2)

test_1 = "9"
test_2 = "99"
test_out = "108"
assert test_out == add_strings(test_1, test_2)
