# A valid number can be split up into these components (in order):
#   A decimal number or an integer.
#       (Optional) An 'e' or 'E', followed by an integer.
#   A decimal number can be split up into these components (in order):
#       (Optional) A sign character (either '+' or '-').
#       One of the following formats:
#       One or more digits, followed by a dot '.'.
#       One or more digits, followed by a dot '.', followed by one or more digits.
#       A dot '.', followed by one or more digits.
#   An integer can be split up into these components (in order):
#       (Optional) A sign character (either '+' or '-').
#       One or more digits.
# For example, all the following are valid numbers:
# ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"],
# while the following are not valid numbers:
# ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].
#
# 1 <= s.length <= 20
# s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.
# ----------------------
# Given a string s, return true if s is a valid number.


def is_number(s: str) -> bool:
    # working_sol (22.14%, 21.72%) -> (48ms, 16.2mb)  time: O(n) | O(1)
    digits: set[str] = set()
    for _ in range(10):
        digits.add(str(_))
    pn_signs: set[str] = set()
    pn_signs.add("-"), pn_signs.add("+")
    e_sign: set[str] = set()
    e_sign.add("e"), e_sign.add("E")
    dot_sign: str = "."
    pn_sign_allowed: bool = True
    dot_allowed: bool = True
    e_sign_allowed: bool = True
    digits_used: bool = False
    digits_after: bool = False
    digits_after_used: bool = False
    for symbol in s:
        if symbol in e_sign and e_sign_allowed:
            pn_sign_allowed = True
            e_sign_allowed = False
            dot_allowed = False
            digits_after = True
            continue
        if symbol in e_sign and not e_sign_allowed:
            return False
        if symbol in pn_signs and pn_sign_allowed:
            pn_sign_allowed = False
            continue
        if symbol in pn_signs and not pn_sign_allowed:
            return False
        if symbol == dot_sign and dot_allowed:
            dot_allowed = False
            pn_sign_allowed = False
            continue
        if symbol == dot_sign and not dot_allowed:
            return False
        if symbol in digits and e_sign_allowed:
            digits_used = True
            pn_sign_allowed = False
            continue
        if symbol in digits and not e_sign_allowed and not digits_used:
            return False
        if symbol in digits and not e_sign_allowed and not digits_after_used:
            digits_after_used = True
            pn_sign_allowed = False
            continue
        if (symbol not in digits) and (symbol not in pn_signs) and (symbol not in e_sign) and (symbol != dot_sign):
            return False
    if not digits_used:
        return False
    if digits_after and not digits_after_used:
        return False
    return True

# Time complexity: O(n) -> looping once through whole input_string(list) => O(n)
# Space complexity: O(1) -> we're not creating anything that depends on input_string,
#                           but we're creating a lot of constants no matter what input is => O(1)
#                           ! maybe it's wrong, but as I understand BigO =>
#                             shows what will be extra space depending on input,
#                             and we're not creating anything that depends on input, except constants !

# One walk solution, but very hard on if statements, maybe there's more pretty solution.
# But I need to test_commit this one first.
# --------------------------------
# right_to_left walk with stopping on invalid value?
# Don't recall and can't find for now, is we allowed to have 1+ of  E sign?
# It's just the exponent of int * (10 ** num), maybe we can use two of them -> int * (10 ** num) * 10 ( ** num)
# But I don't remember using it like this anytime, assuming we can only use it once.


test1 = "0"
test1_out = True
assert test1_out == is_number(test1)

test2 = "e"
test2_out = False
assert test2_out == is_number(test2)

test3 = "."
test3_out = False
assert test3_out == is_number(test3)

# test4 - failed -> because I made very hard_to_read solution,
#                   and forgot about pn_sign need's to be blocked after first digit
#                   and unblocked after e/E sign, and blocked again after first digit
test4 = "6+1"
test4_out = False
assert test4_out == is_number(test4)

test5 = "61e12+1"
test5_out = False
assert test5_out == is_number(test5)

# test6 - failed -> bruh...
#                   Literally made this mistake in test4, but forgot about dot sign blocking pn_sign as well.
#                   ! well at least it's in last 10 cases, from 1500 cases !
test6 = ".-4"
test6_out = False
assert test6_out == is_number(test6)

valid_numbers = [
    "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10",
    "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789",
]
for _ in valid_numbers:
    assert is_number(_) is True

invalid_numbers = [
    "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53",
]
for _ in invalid_numbers:
    assert is_number(_) is False
