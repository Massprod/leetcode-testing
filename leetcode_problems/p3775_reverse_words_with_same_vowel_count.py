# You are given a string s consisting of lowercase English words,
#  each separated by a single space.
# Determine how many vowels appear in the first word.
# Then, reverse each following word that has the same vowel count.
# Leave all remaining words unchanged.
# Return the resulting string.
# Vowels are 'a', 'e', 'i', 'o', and 'u'.
# --- --- --- ---
# 1 <= s.length <= 10 ** 5
# s consists of lowercase English letters and spaces.
# Words in s are separated by a single space.
# s does not contain leading or trailing spaces.


def reverse_words(s: str) -> str:
    # working_solution: (80.45%, 84.76%) -> (140ms, 21.88mb)  Time: O(s) Space: O(s)
    vowels: set[str] = { 'a', 'e', 'i', 'o', 'u' }

    def count_vowels(word: str) -> int:
        nonlocal vowels
        count: int = 0
        for char in word:
            if char in vowels:
                count += 1

        return count
    
    words: list[str] = s.split(' ')
    first_count: int = count_vowels(words[0])
    
    for index in range(1, len(words)):
        if first_count == count_vowels(words[index]):
            words[index] = words[index][::-1]
    
    return ' '.join(words)


# Time complexity: O(s)
# --- --- --- ---
# Space complexity: O(s)


test: str = 'cat and mice'
test_out: str = 'cat nda mice'
assert test_out == reverse_words(test)

test = 'book is nice'
test_out = 'book is ecin'
assert test_out == reverse_words(test)

test = 'banana healthy'
test_out = 'banana healthy'
assert test_out == reverse_words(test)
