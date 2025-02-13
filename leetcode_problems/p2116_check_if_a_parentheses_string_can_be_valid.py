# A parentheses string is a non-empty string consisting only of '(' and ')'.
# It is valid if any of the following conditions is true:
#  - It is ().
#  - It can be written as AB (A concatenated with B),
#    where A and B are valid parentheses strings.
#  - It can be written as (A), where A is a valid parentheses string.
# You are given a parentheses string s and a string locked, both of length n.
# locked is a binary string consisting only of '0's and '1's.
# For each index i of locked,
#  - If locked[i] is '1', you cannot change s[i].
#  - But if locked[i] is '0', you can change s[i] to either '(' or ')'.
# Return true if you can make s a valid parentheses string.
# Otherwise, return false.
# ----------------------
# n == s.length == locked.length
# 1 <= n <= 10 ** 5
# s[i] is either '(' or ')'.
# locked[i] is either '0' or '1'.


def can_be_valid(s: str, locked: str) -> bool:
    # working_sol (80.28%, 5.41%) -> (63ms, 22.03mb)  time: O(s) | space: O(s)
    # We can't balance `odd` string.
    if len(s) % 2:
        return False

    open: str = '('
    close: str = ')'
    # [ index of opened bracket ]
    opened: list[int] = []
    # [ index of wildcard == we can get w.e we want from it ]
    wildcards: list[int] = []
    for index, bracket in enumerate(s):
        # wildcard
        if '0' == locked[index]:
            wildcards.append(index)
        elif open == bracket:
            opened.append(index)
        elif close == bracket:
            # We can close some open bracket
            if opened:
                opened.pop()
            # We can convert to open bracket and close it
            elif wildcards:
                wildcards.pop()
            # We can't use this close bracket => False
            else:
                return False
    
    # If there's still opened brackets we need to close them.
    # Only way to do this, is wildcards placed on the right side of them.
    # Check in reverse, because we still need to close all of them,
    #  but that way we can do this in O(1).
    while (opened and wildcards
           and opened[-1] < wildcards[-1]):
        opened.pop()
        wildcards.pop()
    
    return True if not opened else False


# Time complexity: O(s)
# In the worst case there's equal amount of open brackets and wildcards.
# Alligned in the way => all open brackets can be closed.
# We will traverse whole `s` to store them.
# And extra traverse n // 2 indexes again to pop them one by one => O(s).
# ----------------------
# Auxiliary space: O(s)
# `opened` and `wildcards` <- both combined, always equal to size of `s` => O(s).


test_s: str = "))()))"
test_locked: str = "010100"
test_out = True
assert test_out == can_be_valid(test_s, test_locked)

test_s = "()()"
test_locked = "0000"
test_out = True
assert test_out == can_be_valid(test_s, test_locked)

test_s = ")"
test_locked = "0"
test_out = False
assert test_out == can_be_valid(test_s, test_locked)
