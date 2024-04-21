# You are given a string title consisting of one or more words separated by a single space,
#  where each word consists of English letters.
# Capitalize the string by changing the capitalization of each word such that:
#  - If the length of the word is 1 or 2 letters, change all letters to lowercase.
#  - Otherwise, change the first letter to uppercase and the remaining letters to lowercase.
# Return the capitalized title.
# --------------------
# 1 <= title.length <= 100
# title consists of words separated by a single space without any leading or trailing spaces.
# Each word consists of uppercase and lowercase English letters and is non-empty.
from random import choice
from string import ascii_letters


def capitalize_title(title: str) -> str:
    # working_sol (60.86%, 57.88%) -> (35ms, 16.58mb)  time: O(n) | space: O(n)
    out: str = ''
    word: str = ''
    for char in title:
        if ' ' == char:
            if 1 <= len(word) <= 2:
                out += word.lower() + char
            if 3 <= len(word):
                out += word[0].title() + word[1:].lower() + char
            word = ''
            continue
        word += char
    if word:
        if 1 <= len(word) <= 2:
            out += word.lower()
        if 3 <= len(word):
            out += word[0].title() + word[1:].lower()
    return out


# Time complexity: O(n) <- n - length of input string `title`
# Always traversing whole input string `title` and using every index twice, to get to it and use it => O(2n).
# --------------------
# Auxiliary space: O(n).
# Always recreating whole input string `title` but with different Capitalization.
# And in the worst case we can have whole string without any space, so we will have `word` with size == `n` => O(2n).


test: str = "capiTalIze tHe titLe"
test_out: str = "Capitalize The Title"
assert test_out == capitalize_title(test)

test = "First leTTeR of EACH Word"
test_out = "First Letter of Each Word"
assert test_out == capitalize_title(test)

test = "i lOve leetcode"
test_out = "i Love Leetcode"
assert test_out == capitalize_title(test)

test = ''.join([''.join([choice(ascii_letters) for _ in range(choice([1, 5, 10]))]) + ' ' for _ in range(10)])
print(test)
