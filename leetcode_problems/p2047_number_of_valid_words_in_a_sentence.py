# A sentence consists of lowercase letters ('a' to 'z'),
#  digits ('0' to '9'),
#  hyphens ('-'),
#  punctuation marks ('!', '.', and ','),
#  and spaces (' ') only.
# Each sentence can be broken down into one or more tokens separated by one or more spaces ' '.
# A token is a valid word if all three of the following are true:
#  - It only contains lowercase letters, hyphens, and/or punctuation (no digits).
#  - There is at most one hyphen '-'. If present, it must be surrounded by lowercase characters
#    ("a-b" is valid, but "-ab" and "ab-" are not valid).
#  - There is at most one punctuation mark. If present, it must be at the end of the token
#    ("ab,", "cd!", and "." are valid, but "a!b" and "c.," are not valid).
# Examples of valid words include "a-b.", "afad", "ba-c", "a!", and "!".
# Given a string sentence, return the number of valid words in sentence.
# ----------------------
# 1 <= sentence.length <= 1000
# sentence only contains lowercase English letters, digits, ' ', '-', '!', '.', and ','.
# There will be at least 1 token.


def count_valid_words(sentence: str) -> int:
    # working_sol (48.93%, 86.63%) -> (47ms, 16.58mb)  time: O(n) | space: O(n)
    out: int = 0
    tokens: list[str] = sentence.split(' ')
    punctuation_marks: set[str] = {'!', '.', ','}

    def check(token: str) -> bool:
        nonlocal punctuation_marks
        hyphen: bool = False
        punctuation: bool = False
        for index, char in enumerate(token):
            if char.isdigit():
                return False
            elif '-' == char:
                if hyphen:
                    return False
                left: int = index - 1
                right: int = index + 1
                if not (0 <= left < len(token) and 0 <= right < len(token)):
                    return False
                if not (token[left].islower() and token[right].islower()):
                    return False
                hyphen = True
            elif char in punctuation_marks:
                if punctuation:
                    return False
                if index != len(token) - 1:
                    return False
                punctuation = True
        return True

    for _token in tokens:
        if _token and check(_token):
            out += 1
    return out


# Time complexity: O(n) <- n - length of the input string `sentence`.
# Always using every char of `sentence`, twice => O(2 * n).
# ----------------------
# Auxiliary space: O(n)
# In the worst case there's no ' ' in `sentence`.
# `tokens` <- will allocate space for each char in `sentence` => O(n).


test: str = "cat and  dog"
test_out: int = 3
assert test_out == count_valid_words(test)

test = "!this  1-s b8d!"
test_out = 0
assert test_out == count_valid_words(test)

test = "alice and  bob are playing stone-game10"
test_out = 5
assert test_out == count_valid_words(test)

test = (" -a ,a .a !a -a, -a. -a! -a- ,a- ,a, ,a. ,a!"
        " .a, .a. .a- ,a- .a! !a- !a, !a. !a! a-, a-- a-. a-! a-a a--a a!, a-vb-c,")
test_out = 1
assert test_out == count_valid_words(test)
