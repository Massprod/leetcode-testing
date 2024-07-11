# You are given a string s that consists of lower case English letters and brackets.
# Reverse the strings in each pair of matching parentheses,
#  starting from the innermost one.
# Your result should not contain any brackets.
# -------------------
# 1 <= s.length <= 2000
# s only contains lower case English characters and parentheses.
# It is guaranteed that all parentheses are balanced.


def reverse_parentheses(s: str) -> str:
    # working_sol (91.13%, 81.94%) -> (30ms, 16.44mb)  time: O(s) | space: O(s)
    opened: str = '('
    closed: str = ')'
    # [index of the opener]
    openers: list[int] = []
    # [index of the counterpart]
    pairs: list[int] = [0 for _ in s]
    for index in range(len(s)):
        if opened == s[index]:
            openers.append(index)
        elif closed == s[index]:
            counter_ind: int = openers.pop()
            pairs[index] = counter_ind
            pairs[counter_ind] = index
    out: list[str] = []
    index: int = 0
    direction: int = 1
    # Start to move: left -> right.
    while index < len(s):
        # Change direction and starting position depending on what we encounter.
        if opened == s[index] or closed == s[index]:
            index = pairs[index]
            direction *= -1
        # Record every char on the path, we always maintain a correct direction => just use it.
        else:
            out.append(s[index])
        index += direction
    return ''.join(out)


# Time complexity: O(s)
# Always traversing `s`, once to get all parentheses pairs => O(s).
# Extra traversing every index, once to get them in the correct order => O(2s).
# -------------------
# Auxiliary space: O(s)
# In the worst case, we're not going to have any parentheses.
# So, out `openers` is empty, but it doesn't matter. Because `pairs` and `out` is both of size `s` => O(2s).


test: str = "(abcd)"
test_out: str = "dcba"
assert test_out == reverse_parentheses(test)

test = "(u(love)i)"
test_out = "iloveu"
assert test_out == reverse_parentheses(test)

test = "(ed(et(oc))el)"
test_out = "leetcode"
assert test_out == reverse_parentheses(test)
