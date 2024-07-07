# You are given a string s of lowercase English letters
#  and an array widths denoting how many pixels wide each lowercase English letter is.
# Specifically, widths[0] is the width of 'a', widths[1] is the width of 'b', and so on.
# You are trying to write s across several lines, where each line is no longer than 100 pixels.
# Starting at the beginning of s, write as many letters on the first line
#  such that the total width does not exceed 100 pixels.
# Then, from where you stopped in s,
#  continue writing as many letters as you can on the second line.
# Continue this process until you have written all of s.
# Return an array result of length 2 where:
#  - result[0] is the total number of lines.
#  - result[1] is the width of the last line in pixels.
# --------------------------
# widths.length == 26
# 2 <= widths[i] <= 10
# 1 <= s.length <= 1000
# s contains only lowercase English letters.
from string import ascii_lowercase
from random import choice, randint


def number_of_lines(widths: list[int], s: str) -> list[int]:
    # working_sol (74,47%, 94.15%) -> (33ms, 16.39mb)  time: O(s) | space: O(1)
    all_lines: int = 1
    cur_line: int = 0
    for char in s:
        char_index: int = ord(char) - 97
        next_size: int = cur_line + widths[char_index]
        if 100 < next_size:
            all_lines += 1
            cur_line = widths[char_index]
        else:
            cur_line = next_size
    return [all_lines, cur_line]


# Time complexity: O(s)
# Always traversing whole `s`, once => O(s)
# --------------------------
# Auxiliary space: O(1)
# Only constant INT's used, none of them depends on input => O(1).


test_width: list[int] = [
    10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10
]
test_s: str = "abcdefghijklmnopqrstuvwxyz"
test_out: list[int] = [3, 60]
assert test_out == number_of_lines(test_width, test_s)

test_width = [4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
test_s = "bbbcccdddaaa"
test_out = [2, 4]
assert test_out == number_of_lines(test_width, test_s)

test_width = [randint(2, 10) for _ in range(26)]
test_s = ''.join([choice(ascii_lowercase) for _ in range(1000)])
print(test_width, '\n\n', test_s)
