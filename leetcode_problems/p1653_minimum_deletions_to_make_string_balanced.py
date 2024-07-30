# You are given a string s consisting only of characters 'a' and 'b'.
# You can delete any number of characters in s to make s balanced.
# s is balanced if there is no pair of indices (i,j)
#  such that i < j and s[i] = 'b' and s[j]= 'a'.
# Return the minimum number of deletions needed to make s balanced.
# -------------------------
# 1 <= s.length <= 10 ** 5
# s[i] is 'a' or 'b'.
from random import choice


def minimum_deletions(s: str) -> int:
    # working_sol (88.33%, 52.00%) -> (207ms, 17.86mb)  time: O(s) | space: O(s)
    # a -> b is fine.
    # b -> a not fine.
    # So, all we care is to delete every 'b' before 'a'.
    # But what about cases, when there's more 'b' than 'a'.
    # Like: 'aaabbbbbaaa' <- we can delete either 5 'b's or 3 'a's.
    # We can just use stack, and delete everything one by one.
    # If there's more 'b's then we delete less number of 'a's after it.
    # And if there's less 'b's we're just going to delete less number of 'b' and leave extra 'a's.
    out: int = 0
    stack: list[str] = []
    for char in s:
        if 'a' == char:
            if stack and 'b' == stack[-1]:
                stack.pop()
                out += 1
        else:
            stack.append(char)
    return out


# Time complexity: O(s)
# In the worst case: all chars are in pairs 'ba'.
# We're going to traverse every char in `s` and extra delete (s // 2) chars from stack => O(s + s // 2).
# -------------------------
# Auxiliary space: O(s)
# In the worst case there's no incorrect pairs, every char will be added into `stack`.
# `stack` <- will allocate space for every char from `s` => O(s).


test: str = "aababbab"
test_out: int = 2
assert test_out == minimum_deletions(test)

test = "bbaaaaabb"
test_out = 2
assert test_out == minimum_deletions(test)

test = ''.join(choice(['a', 'b']) for _ in range(10 ** 5))
print(test)
