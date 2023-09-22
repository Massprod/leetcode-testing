# Given two strings ransomNote and magazine,
#  return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.
# ----------------
# 1 <= ransomNote.length, magazine.length <= 10 ** 5
# ransomNote and magazine consist of lowercase English letters.
from collections import Counter


def can_construct(ransomNote: str, magazine: str) -> bool:
    # working_sol (87.59%, 87.50%) -> (49ms, 16.5mb)  time: O(n + m) | space: O(n)
    # Count all symbols.
    all_symbols: dict[str, int] = Counter(magazine)
    # Use them once if we can.
    for symbol in ransomNote:
        if symbol in all_symbols:
            if not all_symbols[symbol]:
                return False
            all_symbols[symbol] -= 1
        else:
            return False
    return True


# Time complexity: O(n + m) -> traversing both input_strings once => O(n + m).
# n - len of input_string: magazine^^|
# m - len of input_string: ransomNote^^|
# Auxiliary space: O(n) -> extra Counter() with all symbols from magazine => O(n).


test_note: str = "a"
test_mag: str = "b"
test_out: bool = False
assert test_out == can_construct(test_note, test_mag)

test_note = "aa"
test_mag = "ab"
test_out = False
assert test_out == can_construct(test_note, test_mag)

test_note = "aa"
test_mag = "aab"
test_out = True
assert test_out == can_construct(test_note, test_mag)
