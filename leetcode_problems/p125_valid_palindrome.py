# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
# and removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.
# -------------------
# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.


def is_palindrome(s: str) -> bool:
    # working_sol (13.96%, 55.25%) -> (78ms, 16.8mb)  time: O(n) | space: O(1)
    empty: bool = True
    correct_pali: bool = False
    left: int = 0
    right: int = len(s) - 1
    while left <= right:
        if 48 <= ord(s[left].lower()) <= 57 or 97 <= ord(s[left].lower()) <= 122:
            empty = False
            left_check: str = s[left].lower()
        else:
            left_check = ""
            left += 1
        if 48 <= ord(s[right].lower()) <= 57 or 97 <= ord(s[right].lower()) <= 122:
            empty = False
            right_check: str = s[right].lower()
        else:
            right_check = ""
            right -= 1
        if left_check and right_check:
            if left_check == right_check:
                correct_pali = True
                left += 1
                right -= 1
            else:
                correct_pali = False
                break
    if not empty:
        return correct_pali
    if empty:
        return True


# Time complexity: O(n) -> traversing whole input string and checking for allowed ASCII symbols, for every index =>
#                           => O(n)
#                  Θ(log n) -> only part of the input string will be checked and break at incorrect pair => O(log n)
#                  Ω(1) -> empty string, correct palindrome => Ω(1)
# n - len of input string^^|
# Space complexity: O(1) -> constant space no matter what input string is, left_right_checks always len(1) => O(1)
# -------------------
# Question is, do I need to check middle symbol explicitly?
# Because if we don't meet counterpart on right or left side it's always return False,
# and if there's incorrect sign in a middle when left == right it doesn't matter.
# If there's correct sign in a middle, it still doesn't matter because 1 sign is read as palindrome anyway.
# Dunno about numbers, cuz what numbers in a WORD? But they made a description mentioning on that.
# ^^Incorrect, we need to check middle in case of a single correct sign in a string. <- test4
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
# ASCII for nums and lowercase_letters in this case: 48 - 57, 97 - 122 (inclusive)
# No idea why numbers included in a palindrome WORD but w.e. Description declares it.


test1 = "A man, a plan, a canal: Panama"
test1_out = True
print(is_palindrome(test1))
assert test1_out == is_palindrome(test1)

test2 = "race a car"
test2_out = False
print(is_palindrome(test2))
assert test2_out == is_palindrome(test2)

test3 = " "
test3_out = True
print(is_palindrome(test3))
assert test3_out == is_palindrome(test3)

# test4 - failed -> Made this without rebuilding and counter. Failed to see such cases...
#                   Can be fixed by checking middle sign, what I was thinking, but ignored.
#                   Because this middle sign doesn't matter in case if there was at least 1 counterpart.
test4 = "a."
test4_out = True
print(is_palindrome(test4))
assert test4_out == is_palindrome(test4)

test5 = "a.b   b a.ba"
test5_out = False
print(is_palindrome(test5))
assert test5_out == is_palindrome(test5)
