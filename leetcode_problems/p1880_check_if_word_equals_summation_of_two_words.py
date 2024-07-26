# The letter value of a letter is its position
#  in the alphabet starting from 0 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, etc.).
# The numerical value of some string of lowercase English letters s is the concatenation
#  of the letter values of each letter in s, which is then converted into an integer.
# For example, if s = "acb", we concatenate each letter's letter value, resulting in "021".
# After converting it, we get 21.
# You are given three strings firstWord, secondWord, and targetWord,
#  each consisting of lowercase English letters 'a' through 'j' inclusive.
# Return true if the summation of the numerical values of firstWord
#  and secondWord equals the numerical value of targetWord, or false otherwise.
# -----------------------
# 1 <= firstWord.length, secondWord.length, targetWord.length <= 8
# firstWord, secondWord, and targetWord consist of lowercase English letters from 'a' to 'j' inclusive.


def is_sum_equal(first_word: str, second_word: str, target_word: str) -> bool:
    # working_sol (94.12%, 57.75%) -> (28ms, 16.48mb)  time: O(a + b + c) | space: O(a + b + c)
    first_sum: list[str] = []
    for char in first_word:
        first_sum.append(str(ord(char) - 97))
    first: int = int(''.join(first_sum))
    second_sum: list[str] = []
    for char in second_word:
        second_sum.append(str(ord(char) - 97))
    second: int = int(''.join(second_sum))
    target_sum: list[str] = []
    for char in target_word:
        target_sum.append(str(ord(char) - 97))
    target: int = int(''.join(target_sum))
    return (first + second) == target


# Time complexity: O(a + b + c) <- a - length of the input string `first_word`,
#                                  b - length of the input string `second_word`,
#                                  c - length of the input string `target_word`.
# Always traversing all 3 strings, once to get their char values => O(a + b + c).
# Extra traversing all the char values to get their sums => O(2 * (a + b + c).
# -----------------------
# Auxiliary space: O(a + b + c)
# All 3 arrays to store chars with corresponding string sizes => O(a + b + c).


test_first: str = "acb"
test_second: str = "cba"
test_target: str = "cdb"
test_out: bool = True
assert test_out == is_sum_equal(test_first, test_second, test_target)

test_first = "aaa"
test_second = "a"
test_target = "aab"
test_out = False
assert test_out == is_sum_equal(test_first, test_second, test_target)

test_first = "aaa"
test_second = "a"
test_target = "aaa"
test_out = True
assert test_out == is_sum_equal(test_first, test_second, test_target)
