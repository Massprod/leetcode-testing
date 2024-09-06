# An integer n is strictly palindromic if, for every base b between 2 and n - 2 (inclusive),
#  the string representation of the integer n in base b is palindromic.
# Given an integer n, return true if n is strictly palindromic and false otherwise.
# A string is palindromic if it reads the same forward and backward.
# -----------------------
# 4 <= n <= 10 ** 5


def is_strictly_palindromic(n: int) -> bool:
    # working_sol (83.93%, 89.13%) -> (30ms, 16.38mb)  time: O(n) | space: O(n)
    def convert_to_base(number: int, base: int) -> str:
        if number == 0:
            return '0'

        digits = []
        while number:
            remainder = number % base
            if remainder >= 10:
                # Convert remainder to corresponding letter for base > 10
                digits.append(chr(55 + remainder))  # 'A' is chr(65), so 10 -> 'A', 11 -> 'B', etc.
            else:
                digits.append(str(remainder))
            number //= base

        # Join and reverse the digits to form the correct representation
        return ''.join(digits[::-1])

    def is_palindrome(string: str) -> bool:
        return string[:len(string) // 2 + 1] == string[len(string) // 2:]

    for _base in range(2, n - 1):
        if not is_palindrome(convert_to_base(n, _base)):
            return False
    return True


# Time complexity: O(n)
# Always calculating bases in range(2, n - 1) => O(n).
# -----------------------
# Auxiliary space: O(n)
# `digits` <- always stored all the digits from `n` => O(n).


test: int = 9
test_out: bool = False
assert test_out == is_strictly_palindromic(test)

test = 4
test_out = False
assert test_out == is_strictly_palindromic(test)
