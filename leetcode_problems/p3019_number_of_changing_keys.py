# You are given a 0-indexed string s typed by a user.
# Changing a key is defined as using a key different from the last used key.
# For example, s = "ab" has a change of a key while s = "bBBb" does not have any.
# Return the number of times the user had to change the key.
# Note: Modifiers like shift or caps lock won't be counted in changing the key that is
#  if a user typed the letter 'a' and then the letter 'A'
#  then it will not be considered as a changing of key.
# -------------------------
# 1 <= s.length <= 100
# s consists of only upper case and lower case English letters.


def count_key_changes(s: str) -> int:
    # working_sol (94.02%, 64.06%) -> (29ms, 16.47mb)  time: O(s) | space: O(1)
    out: int = 0
    for index in range(1, len(s)):
        if s[index].lower() != s[index - 1].lower():
            out += 1
    return out


# Time complexity: O(s).
# Always traversing `s` once => O(s).
# -------------------------
# Auxiliary space: O(1)


test: str = "aAbBcC"
test_out: int = 2
assert test_out == count_key_changes(test)

test = "AaAaAaaA"
test_out = 0
assert test_out == count_key_changes(test)
