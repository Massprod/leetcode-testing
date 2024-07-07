# International Morse Code defines a standard encoding
#  where each letter is mapped to a series of dots and dashes, as follows:
#   'a' maps to ".-",
#   'b' maps to "-...",
#   'c' maps to "-.-.", and so on.
# For convenience, the full table for the 26 letters of the English alphabet is given below:
#  [".-","-...","-.-.","-..",".","..-.","--.","....","..",
#   ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
#   "...","-","..-","...-",".--","-..-","-.--","--.."]
# Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.
# For example, "cab" can be written as "-.-..--...", which is the concatenation
#  of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word.
# Return the number of different transformations among all words we have.
# ----------------------
# 1 <= words.length <= 100
# 1 <= words[i].length <= 12
# words[i] consists of lowercase English letters.
from string import ascii_lowercase


def unique_morse_repres(words: list[str]) -> int:
    # working_sol (89.73%, 27.19%) -> (33ms, 16.52mb)  time: O(n * k) | space: O(n + k)
    uniques: set[str] = set()
    morse: list[str] = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
                        ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
                        "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    fast_morse: dict[str, str] = {ascii_lowercase[index]: value for index, value in enumerate(morse)}
    for word in words:
        word_morse: list[str] = []
        for char in word:
            word_morse.append(fast_morse[char])
        uniques.add(''.join(word_morse))
    return len(uniques)


# Time complexity: O(n * k) <- n - length of the input array `words`, k - average length of word in `words`.
# Always traversing whole input array `words` and every char of the words in it => O(n * k).
# ----------------------
# Auxiliary space: O(n + k)
# In the worst case, every word in `words` is going to give us a unique Morse version of itself => O(n).
# And every Morse version is going to be stored in `uniques`, and their sizes depend on the word => O(n + k).


test: list[str] = ["gin", "zen", "gig", "msg"]
test_out: int = 2
assert test_out == unique_morse_repres(test)

test = ["a"]
test_out = 1
assert test_out == unique_morse_repres(test)
