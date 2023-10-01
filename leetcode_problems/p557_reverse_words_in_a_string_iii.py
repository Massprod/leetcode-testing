# Given a string s, reverse the order of characters in each word within
#  a sentence while still preserving whitespace and initial word order.
# ---------------
# 1 <= s.length <= 5 * 10 ** 4
# s contains printable ASCII characters.
# s does not contain any leading or trailing spaces.
# There is at least one word in s.
# All the words in s are separated by a single space.


def reverse_words(s: str) -> str:
    # working_sol (88.98%, 98.97%) -> (37ms, 16.7mb)  time: O(n) | space: O(n)
    # ! s does not contain any leading or trailing spaces.
    #   All the words in s are separated by a single space. !
    return ' '.join([word[::-1] for word in s.split()])


# Time complexity: O(n) -> traversing whole input string once to split => O(n) ->
# n - len of input string^^| -> extra every word to reverse => O(log n) <- we have spaces, so it's only a part ->
#                            -> recreating string with same size => O(n).
# Auxiliary space: O(n) -> reversed string + list with all words, linear => O(n).


test: str = "Let's take LeetCode contest"
test_out: str = "s'teL ekat edoCteeL tsetnoc"
assert test_out == reverse_words(test)

test = "God Ding"
test_out = "doG gniD"
assert test_out == reverse_words(test)
