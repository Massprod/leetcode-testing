# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
# ------------------
# 1 <= columnNumber <= 2 ** 31 - 1


def convert_to_title(columnNumber: int) -> str:
    # working_sol (43.38%, 23.11%) -> (44ms, 16.4mb)  time: O(log n) | space: O(n)
    # N = (B + 1) * 26 ** 2 + (X + 1) * 26 ** 1 + (Z + 1) * 26 ** 0
    title: str = ''
    while columnNumber:
        columnNumber -= 1
        title += chr(97 + columnNumber % 26)
        columnNumber //= 26
    return title[::-1]


# Time complexity: O(log n) -> log_26(n), but we can ignore constants anyway => O(log n).
# n - input value^^|
# Auxiliary space: O(n) -> size of a string depends on input_value, higher == longer => O(n).
# ------------------
# Unsolvable without knowing how it's done in Excel.
# Ok. Convert to 26 base -> N = (B + 1) * 26 ** 2 + (X + 1) * 26 ** 1 + (Z + 1) * 26 ** 0
# Extra take -1 from every option to get correct symbol, alphabet in our task is from 1 not 0.


test: int = 1
test_out: str = 'a'
assert test_out == convert_to_title(test)

test = 28
test_out = 'ab'
assert test_out == convert_to_title(test)

test = 701
test_out = 'zy'
assert test_out == convert_to_title(test)
