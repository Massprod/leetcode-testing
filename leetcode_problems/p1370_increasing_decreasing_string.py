# You are given a string s.
# Reorder the string using the following algorithm:
#  1. Pick the smallest character from s and append it to the result.
#  2. Pick the smallest character from s which is greater than the last appended character to the result and append it.
#  3. Repeat step 2 until you cannot pick more characters.
#  4. Pick the largest character from s and append it to the result.
#  5. Pick the largest character from s which is smaller than the last appended character to the result and append it.
#  6. Repeat step 5 until you cannot pick more characters.
#  7. Repeat the steps from 1 to 6 until you pick all characters from s.
# In each step, If the smallest or the largest character appears more than once
#  you can choose any occurrence and append it to the result.
# Return the result string after sorting s with this algorithm.
# -----------------------
# 1 <= s.length <= 500
# s consists of only lowercase English letters.
from random import choice
from collections import Counter
from string import ascii_lowercase


def sort_string(s: str) -> str:
    # working_sol (40.90%, 91.70%) -> (65ms, 16.43mb)  time: O(s) | space: O(s)

    def use_char(char: str) -> None:
        if char in chars:
            out.append(char)
            chars[char] -= 1
            if not chars[char]:
                chars.pop(char)

    chars: dict[str, int] = Counter(s)
    char_ascii: int = 97
    out: list[str] = []
    shift: int = 1
    while chars:
        cur_char: str = chr(char_ascii)
        use_char(cur_char)
        # When we reach highest `char`, we're making a turn and choosing the LARGEST again.
        if 122 == char_ascii and 1 == shift:
            shift = -1
            use_char(cur_char)
        # Same for the smallest, we use it and start a new sequence from it.
        elif 97 == char_ascii and -1 == shift:
            shift = 1
            use_char(cur_char)
        char_ascii += shift
    return ''.join(out)


# Time complexity: O(s).
# We're always have the same sequence check, 97 -> 122 | 122 -> 97, until we use all chars from `s` => O(s).
# -----------------------
# Auxiliary space: O(s)
# In the worst case, every char in `s` is unique and all of them stored in `chars` => O(s).
# We can even, call it constant because there's only ascii english_lowercase options in `s`.


test: str = "aaaabbbbcccc"
test_out: str = "abccbaabccba"
assert test_out == sort_string(test)

test = "rat"
test_out = "art"
assert test_out == sort_string(test)

test = ''.join([choice(ascii_lowercase) for _ in range(500)])
print(test)
