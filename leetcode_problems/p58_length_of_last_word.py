# Given a string s consisting of words and spaces,
#  return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.
# ----------------------
# 1 <= s.length <= 10 ** 4
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.


def length_of_last_word(s: str) -> int:
    # working_sol (75.23%, 96.32%) -> (35ms, 16.1mb)  time: O(n)  | space: O(1)
    length: int = 0
    # We need last -> start from end.
    for x in range(len(s) - 1, -1, -1):
        # Skip leading spaces.
        if s[x] != " ":
            length += 1
        # Space after word == word checked.
        elif length > 0:
            break
    return length


# Time complexity: O(n) -> By the task description there's always will be word and spaces (at least 1 of each)
#                          Worst case is we're going to loop through whole input -> case like this "word   "
#                  Θ(log n) -> best of all cases -> "word   word" (only part of input will be searched)
#                  Ω(n) -> best case like this -> "word" (always at least one word, no info about spaces)
# Space complexity: O(1) -> one constant INT for counting length => O(1).
# ----------------------
# Most simple way to solve it is STRIP(), but I guess it's not a correct way to use build_in methods.
# So let's try to loop and count every symbol from the end.


test: str = "Hello World"
test_out: int = 5
assert test_out == length_of_last_word(test)

test = "   fly me   to   the moon  "
test_out = 4
assert test_out == length_of_last_word(test)

test = "luffy is still joyboy"
test_out = 6
assert test_out == length_of_last_word(test)
