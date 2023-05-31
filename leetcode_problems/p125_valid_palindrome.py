# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
# and removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.
# -------------------
# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.


def is_palindrome(s: str) -> bool:
    pass


# -------------------
# !
# Alphanumeric characters are made up of the 26 letters of the alphabet (A through Z)
# and the digits 0 through 9. So, 1, 2, q, f, m, p, and 10 are all examples of letters and numbers.
# Alphanumeric characters also include characters like *, &, and @. !
# !
# s consists only of printable ASCII characters -> 20 - 127numbers. !
# Hmm. How we should consider *, &, @ and others into reading of a palindrome?
# !
# Alphanumeric characters include letters and numbers. !
# I will stick to this for now, if I fail because there's some other signs. Not my fault, because this description...
# ASCII for nums and lowercase_letters in this case: 30 - 39, 97 - 122 (inclusive)


test1 = "A man, a plan, a canal: Panama"
test1_out = True

test2 = "race a car"
test2_out = False

test3 = " "
test3_out = True
