# Given a string of English letters s, return the greatest English letter which occurs
#  as both a lowercase and uppercase letter in s.
# The returned letter should be in uppercase. If no such letter exists, return an empty string.
# An English letter b is greater than another letter a if b appears after a in the English alphabet.
# ----------------------
# 1 <= s.length <= 1000
# s consists of lowercase and uppercase English letters.


def greatest_letter(s: str) -> str:
    # working_sol (76.25%, 88.94%) -> (37ms, 16.44mb)  time: O(s) | space: O(1)
    chars: list[list[int]] = [[0, 0] for _ in range(27)]
    for char in s:
        place: int = 0
        if char.isupper():
            place = 1
        char_index: str = char.lower()
        chars[ord(char_index) - 97][place] = 1
    for index in range(len(chars) - 1, -1, -1):
        if all(chars[index]):
            return chr(index + 97).upper()
    return ''


# Time complexity: O(s)
# Always traversing whole input string `s`, once => O(s).
# ----------------------
# Auxiliary space: O(1)
# `chars` <- always of the same size => O(1).


test: str = "lEeTcOdE"
test_out: str = "E"
assert test_out == greatest_letter(test)

test = "arRAzFif"
test_out = "R"
assert test_out == greatest_letter(test)

test = "AbCdEfGhIjK"
test_out = ""
assert test_out == greatest_letter(test)
