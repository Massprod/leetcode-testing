# Convert a non-negative integer num to its English words representation.
# --------------------------
# 0 <= num <= 2 ** 31 - 1


def number_to_words(num: int) -> str:
    # working_sol (54.07%, 47.47%) -> (37ms, 16.65mb)  time: O(log num) | space: O(num)
    if 0 == num:
        return 'Zero'
    ones: dict[int, str] = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
    }
    tens: dict[int, str] = {
        2: "Twenty",
        3: "Thirty",
        4: "Forty",
        5: "Fifty",
        6: "Sixty",
        7: "Seventy",
        8: "Eighty",
        9: "Ninety",
    }
    chunk_indexes: list[str] = ['', 'Thousand', 'Million', 'Billion']
    out: list[str] = []
    chunk_index: int = 0
    while num:
        if num % 1000 != 0:
            chunk_string: list[str] = []
            chunk = num % 1000
            if chunk >= 100:
                chunk_string.append(f'{ones[chunk // 100]} Hundred ')
                chunk %= 100
            if chunk >= 20:
                chunk_string.append(f'{tens[chunk // 10]} ')
                chunk %= 10
            if chunk > 0:
                chunk_string.append(f'{ones[chunk]} ')
            chunk_string.append(f'{chunk_indexes[chunk_index]} ')
            out.append(''.join(chunk_string))
        num //= 1000
        chunk_index += 1
    out.reverse()
    return ''.join(out).strip()


# Time complexity: O(log num)
# Depleting `num` chunk by chunk to get the correct string, makes its logarithmic => O(log num).
# --------------------------
# Auxiliary space: O(num)
# `chunk_string` and `out` depends on a `num`, higher -> longer, but no idea of correct description => O(num).


test: int = 123
test_out: str = "One Hundred Twenty Three"
assert test_out == number_to_words(test)

test = 12345
test_out = "Twelve Thousand Three Hundred Forty Five"
assert test_out == number_to_words(test)

test = 1234567
test_out = "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
assert test_out == number_to_words(test)
