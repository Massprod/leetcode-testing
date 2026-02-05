# You are given a string s consisting of lowercase English letters
#  and special characters.
# Your task is to perform these in order:
#  - Reverse the lowercase letters and place them back 
#    into the positions originally occupied by letters.
#  - Reverse the special characters and place them back
#    into the positions originally occupied by special characters.
# Return the resulting string after performing the reversals.
# --- --- --- ---
# 1 <= s.length <= 100
# s consists only of lowercase English letters and the special characters in "!@#$%^&*()".
from string import ascii_lowercase


def reverse_by_type(s: str) -> str:
    # working_solution: (71.61%, 77,86%) -> (2ms, 19.37mb)  Time: O(s) Space: O(s)
    index: int
    char: str
    fast_chars: set[str] = set(ascii_lowercase)
    # [ (char, index) ]
    lower_case: list[str] = []
    specials: list[str] = []
    for char in s:
        if char in fast_chars:
            lower_case.append(char)
        else:
            specials.append(char)

    _reversed: list[str] = [_char for _char in s]
    for index,  char in enumerate(_reversed):
        if char in fast_chars:
            _reversed[index] = lower_case.pop()
        else:
            _reversed[index] = specials.pop()

    out: str = ''.join(_reversed)
    return out
    

# Time complexity: O(s)
# --- --- --- ---
# Space complexity: O(s)


test: str = ")ebc#da@f("
test_out = "(fad@cb#e)"
assert test_out == reverse_by_type(test)

test: str = "z"
test_out = "z"
assert test_out == reverse_by_type(test)

test: str = "!@#$%^&*()"
test_out: str = ")(*&^%$#@!"
assert test_out == reverse_by_type(test)
