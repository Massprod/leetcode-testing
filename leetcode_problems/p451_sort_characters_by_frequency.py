# Given a string s, sort it in decreasing order based on the frequency of the characters.
# The frequency of a character is the number of times it appears in the string.
# Return the sorted string. If there are multiple answers, return any of them.
# --------------------
# 1 <= s.length <= 5 * 10 ** 5
# s consists of uppercase and lowercase English letters and digits.
from string import ascii_lowercase, ascii_uppercase
from random import choice


def frequency_sort(s: str) -> str:
    # working_sol (84.24%, 89.64%) -> (46ms, 17.58mb)  time: O(n * log n) | space: O(n)
    # Count all symbols occurrences.
    all_symbs: dict[str, int] = {}
    for sym in s:
        if sym in all_symbs:
            all_symbs[sym] += 1
            continue
        all_symbs[sym] = 1
    # Sort them in decreasing order.
    decreasing: list[int] = sorted(all_symbs.values(), reverse=True)
    # Reverse to get fast access for maximum occurrences.
    all_decreasing: dict[int, list[str]] = {}
    for sym, occur in all_symbs.items():
        if occur in all_decreasing:
            all_decreasing[occur].append(sym)
            continue
        all_decreasing[occur] = [sym]
    # Create new string with symbols in decreasing occurrences.
    out: str = ''
    for _ in decreasing:
        out += _ * all_decreasing[_].pop()
    return out


# Time complexity: O(n * log n) -> traversing once to get all occurrences => O(n) -> worst case == all symbols unique,
# n - len of input_string^^| -> sorting all values, and # of values are equal to n -> O(n * log n) ->
#                            -> traversing dictionary with all unique symbols stored, reversing sym -> occur => O(n) ->
#                            -> creating new string in descending order of symbols => O(n).
# Auxiliary space: O(n) -> 2 dictionaries with same worst case, unique values => O(2n) ->
#                       -> extra list with the same size == n => O(n).


test: str = "tree"
test_out: str = "eert"
assert test_out == frequency_sort(test)

test = "cccaaa"
test_out = "aaaccc"
assert test_out == frequency_sort(test)

test = "Aabb"
test_out = "bbaA"
assert test_out == frequency_sort(test)

test = ''
for _ in range(10 ** 3):
    if choice([1, 3]) == 1:
        test += choice(ascii_uppercase)
        continue
    test += choice(ascii_lowercase)
print(test)
