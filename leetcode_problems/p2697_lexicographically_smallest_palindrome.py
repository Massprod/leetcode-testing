# You are given a string s consisting of lowercase English letters,
#  and you are allowed to perform operations on it.
# In one operation, you can replace a character in s with another lowercase English letter.
# Your task is to make s a palindrome with the minimum number of operations possible.
# If there are multiple palindromes that can be made using the minimum number of operations,
#  make the lexicographically smallest one.
# A string a is lexicographically smaller than a string b (of the same length)
#  if in the first position where a and b differ, string a has a letter that appears
#  earlier in the alphabet than the corresponding letter in b.
# Return the resulting palindrome string.
# --------------------------
# 1 <= s.length <= 1000
# s consists of only lowercase English letters.


def make_smallest_palindrome(s: str) -> str:
    # working_sol (68.07%, 89.21%) -> (105ms, 16.59mb)  time: O(s) | space: O(s)
    left: int = 0
    right: int = len(s) - 1
    out: list[str] = []
    while left < right:
        min_sym: str = min(s[left], s[right])
        out.append(min_sym)
        left += 1
        right -= 1
    if left == right:
        out.append(s[left])
        return ''.join(out + out[:left][::-1])
    return ''.join(out + out[::-1])


# Time complexity: O(s)
# Traversing `s`, once to get all the minimum chars => O(s)
# Extra traversing `len(s) // 2` chars to reverse => O(s + s // 2)
# --------------------------
# Auxiliary space: O(s)
# `out` <- only contains half of the chars from `s` + 1 for middle if odd => O(s // 2 + 1).
# `output` <- output string is always of the same size as `s` => O(s + s // 2 + 1)


test: str = "egcfe"
test_out: str = "efcfe"
assert test_out == make_smallest_palindrome(test)

test = "abcd"
test_out = "abba"
assert test_out == make_smallest_palindrome(test)

test = "seven"
test_out = "neven"
assert test_out == make_smallest_palindrome(test)
