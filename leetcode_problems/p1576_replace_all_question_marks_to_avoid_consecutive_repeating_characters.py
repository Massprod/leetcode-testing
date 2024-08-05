# Given a string s containing only lowercase English letters and the '?' character,
#  convert all the '?' characters into lowercase letters such that the final string
#  does not contain any consecutive repeating characters.
# You cannot modify the non '?' characters.
# It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.
# Return the final string after all the conversions (possibly zero) have been made.
# If there is more than one solution, return any of them.
# It can be shown that an answer is always possible with the given constraints.
# ------------------
# 1 <= s.length <= 100
# s consist of lowercase English letters and '?'.
from random import choice
from string import ascii_lowercase


def modify_string(s: str) -> str:
    # working_sol (42.70%, 29.20%) -> (39ms, 16.54mb)  time: O(s) | space: O(s)
    out: list[str] = []
    left_limit: str = ''
    if '?' == s[0]:
        left_limit = 'a'
    right_limit: str = 'z'
    questions: int = 0
    right: int = 0
    var1: str = choice(ascii_lowercase)
    var2: str = choice(ascii_lowercase)
    while var1 == var2:
        var2 = choice(ascii_lowercase)
    while right < len(s):
        # Use any char before `?` as a `left_limit`.
        if '?' != s[right]:
            left_limit = s[right]
            right_limit = ''
            out.append(s[right])
            right += 1
            continue
        # Count all `?` we need to replace.
        while right < len(s) and '?' == s[right]:
            questions += 1
            right += 1
        # If string doesnt ends with `?` we should consider `right_limit`.
        if right != len(s):
            right_limit = s[right]
        # Garbage choose of a symbols to use :)
        while var1 == left_limit or var1 == right_limit:
            var1 = choice(ascii_lowercase)
        while var1 == var2 or var2 == left_limit or var2 == right_limit:
            var2 = choice(ascii_lowercase)
        # We don't care about anything except, our string shouldn't have consecutive chars.
        # So, we can take 2 w.e chars and repeat them.
        # They only should differ with `left_limit` and `right_limit`.
        while questions:
            if questions % 2:
                out.append(var2)
            else:
                out.append(var1)
            questions -= 1
    return ''.join(out)


# Time complexity: O(s)
# Because im using `choice` - for no actual reason, we could just take `ord` of the limiters.
# But in both cases, it's a single traverse of the `s` to get all the question marks and extra `s` traverse
#  to replace it with some sequence of 2 chars => O(2 * s).
# ------------------
# Auxiliary space: O(s)
# `out` <- in the end, it's always going to store every char from `s`, but `?` changed to some chars => O(s).
