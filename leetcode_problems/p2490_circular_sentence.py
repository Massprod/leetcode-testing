# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
#  - For example, "Hello World", "HELLO", "hello world hello world" are all sentences.
# Words consist of only uppercase and lowercase English letters.
# Uppercase and lowercase English letters are considered different.
# A sentence is circular if:
#  - The last character of a word is equal to the first character of the next word.
#  - The last character of the last word is equal to the first character of the first word.
# For example, "leetcode exercises sound delightful", "eetcode", "leetcode eats soul"
#  are all circular sentences. However, "Leetcode is cool", "happy Leetcode", "Leetcode"
#  and "I like Leetcode" are not circular sentences.
# Given a string sentence, return true if it is circular.
# Otherwise, return false.
# -----------------------
# 1 <= sentence.length <= 500
# sentence consist of only lowercase and uppercase English letters and spaces.
# The words in sentence are separated by a single space.
# There are no leading or trailing spaces.


def is_circular_sentence(sentence: str) -> bool:
    # working_sol (77.23%, 95.88%) -> (33ms, 16.34mb)  time: O(n + k) | space: O(n)
    words: list[str] = sentence.split(' ')
    for index in range(len(words) - 1, -1, -1):
        if words[index - 1][-1] != words[index][0]:
            return False
    return True


# Time complexity: O(n + k) <- n - length of the input string `sentence`, k - words in `sentence`.
# We always splitting `sentence` => O(n).
# Extra traversing every word from `sentence` => O(n + k).
# -----------------------
# Auxiliary space: O(n)
# In the worst case there's only one word.
# `words` <- allocates space for each word from `sentence` => O(n).


test: str = "leetcode exercises sound delightful"
test_out: bool = True
assert test_out == is_circular_sentence(test)

test = "eetcode"
test_out = True
assert test_out == is_circular_sentence(test)

test = "Leetcode is cool"
test_out = False
assert test_out == is_circular_sentence(test)
