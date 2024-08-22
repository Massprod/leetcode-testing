# You are given a string word that consists of digits and lowercase English letters.
# You will replace every non-digit character with a space.
# For example, "a123bc34d8ef34" will become " 123  34 8  34".
# Notice that you are left with some integers that are separated by at least one space: "123", "34", "8", and "34".
# Return the number of different integers after performing the replacement operations on word.
# Two integers are considered different if their decimal representations
#  without any leading zeros are different.
# -------------------------
# 1 <= word.length <= 1000
# word consists of digits and lowercase English letters.


def new_different_integers(word: str) -> int:
    # working_sol (54.61%, 72.87%) -> (36ms, 16.46mb)  time: O(n) | space: O(n)
    digits: list[str] = []
    for char in word:
        if char.isdigit():
            digits.append(char)
        else:
            digits.append(' ')
    uniques: set[int] = set(
        [int(digit) for digit in ''.join(digits).split(' ') if digit]
    )
    return len(uniques)


# Time complexity: O(n) <- n - length of the input string `word`.
# In the worst case, there's only digits in `word`.
# Essentially, we will triple traverse all `word` chars => O(n).
# -------------------------
# Auxiliary space: O(n)
# `digits` <- allocates space for each char in `word` => O(n).
# In the worst case there' sequence like: '1 2 3 4 5'.
# We will store (n / 2) chars as uniques.
# `uniques` <- allocates space for each unique integer in `word` => O(n + n / 2)


test: str = "a123bc34d8ef34"
test_out: int = 3
assert test_out == new_different_integers(test)

test = "leet1234code234"
test_out = 2
assert test_out == new_different_integers(test)

test = "a1b01c001"
test_out = 1
assert test_out == new_different_integers(test)
