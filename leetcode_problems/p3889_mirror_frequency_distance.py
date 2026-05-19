# You are given a string s consisting of lowercase English letters and digits.
# For each character, its mirror character is defined
#  by reversing the order of its character set:
#  - For letters, the mirror of a character is the letter at the same position from the end of the alphabet.
#   - For example, the mirror of 'a' is 'z', and the mirror of 'b' is 'y', and so on.
#  - For digits, the mirror of a character is the digit at the same position from the end of the range '0' to '9'.
#   - For example, the mirror of '0' is '9', and the mirror of '1' is '8', and so on.
# For each unique character c in the string:
#  - Let m be its mirror character.
#  - Let freq(x) denote the number of times character x appears in the string.
#  - Compute the absolute difference between their frequencies, defined as: |freq(c) - freq(m)|
# The mirror pairs (c, m) and (m, c) are the same and must be counted only once.
# Return an integer denoting the total sum of these values over all such distinct mirror pairs.
# --- --- --- ---
# 1 <= s.length <= 5 * 10 ** 5
# s consists only of lowercase English letters and digits.
from string import ascii_lowercase, digits
from collections import Counter


def mirror_frequency(s: str) -> int:
    # working_solution: (9.56%, 70.89%) -> (1497ms, 23.69mb)  Time: O(s) Space: O(s)
    mirrors: dict[str, str] = {}
    for index, value in enumerate(ascii_lowercase):
        rev_index: int = -1 - index
        mirrors[value] = ascii_lowercase[rev_index]
        mirrors[ascii_lowercase[rev_index]] = value
    for index, value in enumerate(digits):
        rev_index: int = -1 - index
        mirrors[value] = digits[rev_index]
        mirrors[digits[rev_index]] = value
    counter: dict[str, int] = Counter(s)
    used: set[tuple[str, str]] = set()
    out: int = 0
    for char in s:
        pair_used: bool = False
        mirror: str = mirrors[char]
        pairs: list[tuple[str, str]] = [
            (char, mirror), (mirror, char)
        ]
        for pair in pairs:
            if pair not in used:
                used.add(pair)
                continue
            pair_used = True
            break
        if pair_used:
            continue
        c_mirror: int = counter.get(mirror, 0)
        c_char: int = counter.get(char, 0)
        out += abs(c_mirror - c_char)

    return out


# Time complexity: O(s)
# --- --- --- ---
# Space complexity: O(s)


test: str = "ab1z9"
test_out: int = 3
# assert test_out == mirror_frequency(test)

test = "4m7n"
test_out = 2
# assert test_out == mirror_frequency(test)

test = "byby"
test_out = 0
# assert test_out == mirror_frequency(test)

test = "zzzzz"
test_out = 5
assert test_out == mirror_frequency(test)
