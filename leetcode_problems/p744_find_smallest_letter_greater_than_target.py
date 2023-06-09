# You are given an array of characters letters that is sorted in non-decreasing order, and a character target.
# There are at least two different characters in letters.
#
# Return the smallest character in letters that is lexicographically greater than target.
# If such a character does not exist, return the first character in letters.
# ---------------------
# 2 <= letters.length <= 10 ** 4
# letters[i] is a lowercase English letter.
# letters is sorted in non-decreasing order.
# letters contains at least two different characters.
# target is a lowercase English letter.


def next_greatest_letter(letters: list[str], target: str) -> str:
    pass


test1 = ["c", "f", "j"]
test1_target = "a"
test1_out = "c"

test2 = ["c", "f", "j"]
test2_target = "c"
test2_out = "f"

test3 = ["x", "x", "y", "y"]
test3_target = "z"
test3_out = "x"
