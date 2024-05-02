# We define the usage of capitals in a word to be
#  right when one of the following cases holds:
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.
# --------------------------
# 1 <= word.length <= 100
# word consists of lowercase and uppercase English letters.
from random import choice
from string import ascii_uppercase, ascii_lowercase, ascii_letters


def detect_capital_use(word: str) -> bool:
    # working_sol (58.41%, 37.63%) -> (35ms, 16.58mb)  time: O(n) | space: O(1)
    first_cap: bool = True if word[0].isupper() else False
    lower_exist: bool = True if not first_cap else False
    cap_exist: bool = False
    for index in range(1, len(word)):
        if word[index].isupper():
            cap_exist = True
        elif word[index].islower():
            lower_exist = True
        elif first_cap and lower_exist and cap_exist:
            break
    # First capital and there's another capital with lower chars.
    if first_cap and lower_exist and cap_exist:
        return False
    # First capital and everything else is capital.
    elif first_cap and not lower_exist:
        return True
    # First isn't capital and there's lower + capital.
    elif not first_cap and lower_exist and cap_exist:
        return False
    # No capitals
    return True


# Time complexity: O(n) <- n - length of input string `word`
# Always using all indexes of the input string `word` once => O(n).
# --------------------------
# Auxiliary space: O(1)
# Only 3 constant `bool`'s used => O(1).


test: str = "USA"
test_out: bool = True
assert test_out == detect_capital_use(test)

test = "FlaG"
test_out = False
assert test_out == detect_capital_use(test)

test = "mL"
test_out = False
assert test_out == detect_capital_use(test)

test = ''.join([choice(ascii_letters) for _ in range(100)])
print(test)
