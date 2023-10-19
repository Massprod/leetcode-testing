# Given two strings s and t, return true if they are equal
#  when both are typed into empty text editors. '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.
# ---------------------
# 1 <= s.length, t.length <= 200
# s and t only contain lowercase letters and '#' characters.
# ---------------------
# Follow up: Can you solve it in O(n) time and O(1) space?


def backspace_compare(s: str, t: str) -> bool:
    # working_sol (53.62%, 83.77%) -> (39ms, 16.1mb)  time: O(s + t) | space: O(s + t)
    word1: list[str] = []
    word2: list[str] = []
    for sym in s:
        if sym == '#':
            if word1:
                word1.pop()
        else:
            word1.append(sym)
    for sym in t:
        if sym == '#':
            if word2:
                word2.pop()
        else:
            word2.append(sym)
    return word1 == word2


# Time complexity: O(s + t) -> traversing both input strings 's' and 't' to get result => O(s + t) ->
#                              -> extra traverse to compare => O(2 * (s + t))
# Auxiliary space: O(s + t) -> worst case == no backspaces -> every symbol of both strings will be stored => O(s + t)


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
