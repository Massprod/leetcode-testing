# A sentence is a list of tokens separated by a single space with no leading or trailing spaces.
# Every token is either a positive number consisting of digits 0-9 with no leading zeros,
#  or a word consisting of lowercase English letters.
#  - For example, "a puppy has 2 eyes 4 legs" is a sentence with seven tokens:
#    "2" and "4" are numbers and the other tokens such as "puppy" are words.
# Given a string s representing a sentence, you need to check if all the numbers in s
#  are strictly increasing from left to right
#  (i.e., other than the last number, each number is strictly smaller than the number on its right in s).
# Return true if so, or false otherwise.
# ------------------------
# 3 <= s.length <= 200
# s consists of lowercase English letters, spaces, and digits from 0 to 9, inclusive.
# The number of tokens in s is between 2 and 100, inclusive.
# The tokens in s are separated by a single space.
# There are at least two numbers in s.
# Each number in s is a positive number less than 100, with no leading zeros.
# s contains no leading or trailing spaces.


def are_numbers_ascending(s: str) -> bool:
    # working_sol (55.72%, 62.29%) -> (35ms, 16.45mb)  time: O(s) | space: O(s)
    words: list[str] = s.split(' ')
    prev_num: int = -1
    for word in words:
        if word.isnumeric():
            cur_num: int = int(word)
            if -1 != prev_num and cur_num <= prev_num:
                return False
            prev_num = cur_num
    return True


# Time complexity: O(s)
# Always splitting `s` into words => O(s).
# In the worst case every token is 1 symbol.
# Extra traversing all the words to check => O(s + (s / 2)).
# ------------------------
# Auxiliary space: O(s)
# Every token is symbol, and we delete half of `s` symbols == ' '.
# `words` <- allocates space for `s / 2` chars => O(s).


test: str = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
test_out: bool = True
assert test_out == are_numbers_ascending(test)

test = "hello world 5 x 5"
test_out = False
assert test_out == are_numbers_ascending(test)

test = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"
test_out = False
assert test_out == are_numbers_ascending(test)
