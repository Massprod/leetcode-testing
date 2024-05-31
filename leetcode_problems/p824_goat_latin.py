# You are given a string sentence that consist of words separated by spaces.
# Each word consists of lowercase and uppercase letters only.
# We would like to convert the sentence to "Goat Latin"
#  (a made-up language similar to Pig Latin.)
# The rules of Goat Latin are as follows:
#  - If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'),
#    append "ma" to the end of the word.
#    - For example, the word "apple" becomes "applema".
#  - If a word begins with a consonant (i.e., not a vowel),
#    remove the first letter and append it to the end, then add "ma".
#    - For example, the word "goat" becomes "oatgma".
#  - Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
#    - For example, the first word gets "a" added to the end,
#      the second word gets "aa" added to the end, and so on.
# Return the final sentence representing the conversion from sentence to Goat Latin.
# ------------------------
# 1 <= sentence.length <= 150
# sentence consists of English letters and spaces.
# sentence has no leading or trailing spaces.
# All the words in sentence are separated by a single space.
from string import ascii_letters
from random import choice, randint


def to_goat_latin(sentence: str) -> str:
    # working_sol (55.36%, 87.18%) -> (35ms, 16.42mb)  time: O(n) | space: O(n + k)
    out: list[str] = []
    add_a: str = 'a'
    add_ma: str = 'ma'
    vowels: set[str] = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    for index, word in enumerate(sentence.split(' ')):
        if word[0] in vowels:
            word += add_ma
        else:
            word = word[1:] + word[0] + add_ma
        word += add_a * (index + 1)  # starts from 1 and increment by 1
        out.append(word)
    return ' '.join(out)


# Time complexity: O(n) <- length of the input string `sentence`.
# Always traversing `sentence` once, to get all the word separated by `split` => O(n).
# In the worst case, all the words are going to be started with not_vowel.
# So, we're going to traverse all the words and take their slices `word[1:]` => O(n)
# Because words is essentially the `sentence` itself, but without `space`'s,
#  we're just doing extra traverse of the `sentence` (in the worst case there's only 1 word, then it's len(word) == n).
# ------------------------
# Auxiliary space: O(n + k) <- k - average length of the words in `sentence`.
# Worst case: there's only 1 word.
# `split` create another array with all the words in it => O(n)
# Extra space for every slice, => O(n + k).
# We always add (`a` * index + 1) to every word in `sentence`.
# So, for every index we're going to have an extra symbol added into our `out` string => O(2n)


test: str = "I speak Goat Latin"
test_out: str = "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
assert test_out == to_goat_latin(test)

test = "The quick brown fox jumped over the lazy dog"
test_out = ("heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa"
            " overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa")
assert test_out == to_goat_latin(test)

test = ' '.join([''.join([choice(ascii_letters) for _ in range(randint(1, 25))]) for _ in range(5)])
print(test)
