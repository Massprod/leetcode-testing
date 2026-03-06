# You are given a string s that consists of lowercase English letters.
# Return the string obtained by removing all trailing vowels from s.
# The vowels consist of the characters 'a', 'e', 'i', 'o', and 'u'.
# --- --- --- ---
# 1 <= s.length <= 100
# s consists of only lowercase English letters.


def trim_trailing_vowels(s: str) -> str:
    # working_solution: (100%, 63.59%) -> (0ms, 19.21mb)  Time: O(s) Space: O(s)
    vowels: set[str] = {'a', 'e', 'i', 'o', 'u'}
    index: int = len(s) - 1
    while -1 < index and s[index] in vowels:
        index -= 1

    out: str = s[:index + 1]

    return out


# Time complexity: O(s)
# --- --- --- ---
# Space complexity: O(1)


test: str = "idea"
test_out: str = "id"
assert test_out == trim_trailing_vowels(test)

test = "day"
test_out = "day"
assert test_out == trim_trailing_vowels(test)

test = "aeiou"
test_out = ""
assert test_out == trim_trailing_vowels(test)
