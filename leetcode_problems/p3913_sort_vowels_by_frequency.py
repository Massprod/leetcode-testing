# You are given a string s consisting of lowercase English characters.
# Rearrange only the vowels in the string so that they appear in non-increasing order of their frequency.
# If multiple vowels have the same frequency, order them by the position of their first occurrence in s.
# Return the modified string.
# Vowels are 'a', 'e', 'i', 'o', and 'u'.
# The frequency of a letter is the number of times it occurs in the string.
# --- --- --- ---
# 1 <= s.length <= 10 ** 5
# s consists of lowercase English letters


def sort_vowels(s: str) -> str:
    # working_solution: (40.39%, 82.94%) -> (123ms, 21.20mb)  Time: O(s * log s) Space: O(s)
    vowels: set[str] = {'a', 'e', 'i', 'o', 'u'}
    data: dict[str, dict[str, int]] = {}
    out: list[str] = list(s)
    for index, char in enumerate(out):
        if char not in vowels:
            continue
        if char not in data:
            data[char] = {
                'frequency': 1,
                'f_index': index,
            }
            continue
        data[char]['frequency'] += 1
    # ( frequency, first_index, char )
    # ! If multiple vowels have the same frequency, order them by the position of their first occurrence in s. !
    # There's no mentio about increasing or decreasing.
    # But, test case with the same frequency uses them in the `increasing` manner.
    # So, we just do the same => -1 to reverse the order to increasing.
    list_vowels: list[tuple[int, int, str]] = []
    for char in data:
        record: tuple[int, int, str] = (
            data[char]['frequency'], -1 * data[char]['f_index'] ,char
        )
        list_vowels.append(record)
    list_vowels.sort()
    for index, char in enumerate(out):
        if not list_vowels:
            break
        if char not in vowels:
            continue
        _, _, new_char = list_vowels[-1]
        data[new_char]['frequency'] -= 1
        if 0 == data[new_char]['frequency']:
            list_vowels.pop()
        out[index] = new_char
    
    return ''.join(out)


# Time complexity: O(s * log s)
# --- --- --- ---
# Space complexity: O(s)


test: str = "leetcode"
test_out: str = "leetcedo"
assert test_out == sort_vowels(test)

test = "aeiaaioooa"
test_out = "aaaaoooiie"
assert test_out == sort_vowels(test)

test = "baeiou"
test_out = "baeiou"
assert test_out == sort_vowels(test)
