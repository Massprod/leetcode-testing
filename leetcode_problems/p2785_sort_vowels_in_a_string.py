# Given a 0-indexed string s, permute s to get a new string t such that:
#   - All consonants remain in their original places. More formally,
#     if there is an index i with 0 <= i < s.length such that s[i] is a consonant, then t[i] = s[i].
#   - The vowels must be sorted in the nondecreasing order of their ASCII values.
#     More formally, for pairs of indices i, j with 0 <= i < j < s.length such that s[i] and s[j] are vowels,
#      then t[i] must not have a higher ASCII value than t[j].
# Return the resulting string.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in lowercase or uppercase.
# Consonants comprise all letters that are not vowels.
# --------------
# 1 <= s.length <= 10 ** 5
# s consists only of letters of the English alphabet in uppercase and lowercase.


def sort_vowels(s: str) -> str:
    # working_sol (92.42%, 70.06%) -> (124ms, 19.06mb)  time: O(n * log n) | space: O(n)
    vowels: set[str] = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}
    vowel_sort: list[str] = sorted([sym for sym in s if sym in vowels])
    index: int = 0
    out: str = ''
    for sym in s:
        if sym in vowels:
            out += vowel_sort[index]
            index += 1
        else:
            out += sym
    return out


# Time complexity: O(n * log n) -> worst case == every symbol is vowel -> we will sort whole string => O(n * log n) ->
# n - len of input string 's'^^| -> and rebuild it again in sorted order => O(n).
# Auxiliary space: O(n) -> constant set with all vowels O(1) -> extra list with all vowels, same case => O(n) ->
#                          -> extra string with same size as original => O(2n).


test: str = "lEetcOde"
test_out: str = "lEOtcede"
assert test_out == sort_vowels(test)

test = "lYmpH"
test_out = "lYmpH"
assert test_out == sort_vowels(test)
