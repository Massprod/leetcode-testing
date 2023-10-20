# Given two strings s and t, return true if they are equal
#  when both are typed into empty text editors. '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.
# ---------------------
# 1 <= s.length, t.length <= 200
# s and t only contain lowercase letters and '#' characters.
# ---------------------
# Follow up: Can you solve it in O(n) time and O(1) space?
from string import ascii_lowercase
from random import choice


def backspace_compare(s: str, t: str) -> bool:
    # working_sol (62.46%, 83.41%) -> (38ms, 16.11mb)  time: O(s + t) | space: O(1)
    back1_count: int = 0
    index1: int = len(s) - 1
    back2_count: int = 0
    index2: int = len(t) - 1
    sym1: bool = False
    sym2: bool = False
    # Go backwards and calc every '#' to delete symbols.
    # We can use 's' or 't' to find first symbol 'sym1',
    #  it doesn't matter because they need to be equal anyway.
    while True:
        if sym1:
            # Same as symbol search in 's'.
            while index2 != -1:
                if t[index2] == '#':
                    back2_count += 1
                    index2 -= 1
                elif t[index2] != '#':
                    if back2_count == 0:
                        sym2 = True
                        break
                    back2_count -= 1
                    index2 -= 1
            # Equal strings == equal symbols.
            if sym1 and sym2:
                if s[index1] == t[index2]:
                    index1 -= 1
                    index2 -= 1
                    sym1 = False
                    sym2 = False
                else:
                    return False
            else:
                return False
        # We checked every symbol in 's'.
        # But 't' is still not done,
        #  we need to check if there's symbols left in 't'.
        elif index1 == -1:
            while index2 != -1:
                if t[index2] == '#':
                    index2 -= 1
                    back2_count += 1
                else:
                    if back2_count == 0:
                        return False
                    back2_count -= 1
                    index2 -= 1
            break
        # Find how many symbols we need to delete.
        elif s[index1] == '#':
            back1_count += 1
            index1 -= 1
        elif s[index1] != '#':
            # If we don't need to delete.
            # Then we need to find equal symbol in 't'.
            if back1_count == 0:
                sym1 = True
            # Or delete this symbol.
            else:
                back1_count -= 1
                index1 -= 1
    return True


# Time complexity: O(s + t) -> traversing both input strings 's' and 't' once => O(s + t).
# Auxiliary space: O(1) -> only constant INTs and two bools used, none of them depends on input => O(1).
# ---------------------
# Working with stack, but it's too easy.
# Constant space, huh. We definitely can't go left -> right, cuz we have no idea how many symbols we will delete.
# And because of that w.e we do it can all be failed by 10+ deletions later. Go backwards?
# Like, count every '#' symbol we meet and then delete all symbols until we meet something with '#' == 0?
# Should work, let's try.


test_s: str = "ab#c"
test_t: str = "ad#c"
test_out: bool = True
assert test_out == backspace_compare(test_s, test_t)

test_s = "ab##"
test_t = "c#d#"
test_out = True
assert test_out == backspace_compare(test_s, test_t)

test_s = "a#c"
test_t = "b"
test_out = False
assert test_out == backspace_compare(test_s, test_t)

test_s = "bxj##tw"
test_t = "bxj###tw"
test_out = False
assert test_out == backspace_compare(test_s, test_t)

test_s = "bbbextm"
test_t = "bbb#extm"
test_out = False
assert test_out == backspace_compare(test_s, test_t)

test_s = ''.join([choice(f'{ascii_lowercase}#') for _ in range(200)])
test_t = ''.join([choice(f'{ascii_lowercase}#') for _ in range(200)])
print(test_s)
print('=============!')
print(test_t)
