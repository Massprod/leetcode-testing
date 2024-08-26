# Given a string s and a character letter,
#  return the percentage of characters in s that equal letter rounded down to the nearest whole percent.
# -----------------------------
# 1 <= s.length <= 100
# s consists of lowercase English letters.
# letter is a lowercase English letter.


def percentage_letter(s: str, letter: str) -> int:
    # working_sol (74.88%, 97.91%) -> (32ms, 16.39mb)  time: O(s) | space: O(1)
    return int(
        (s.count(letter) / len(s)) * 100
    )


# Time complexity: O(s)
# Always traversing whole input string `s` to get all `letter` occurrences => O(s).
# -----------------------------
# Auxiliary space: O(1).


test: str = "foobar"
test_letter: str = "o"
test_out: int = 33
assert test_out == percentage_letter(test, test_letter)

test = "jjjj"
test_letter = "k"
test_out = 0
assert test_out == percentage_letter(test, test_letter)

test = "sgawtb"
test_letter = "s"
test_out = 16
assert test_out == percentage_letter(test, test_letter)
