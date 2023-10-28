# Given an integer n, your task is to count how many strings of length n
#  can be formed under the following rules:
#   Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
#   Each vowel 'a' may only be followed by an 'e'.
#   Each vowel 'e' may only be followed by an 'a' or an 'i'.
#   Each vowel 'i' may not be followed by another 'i'.
#   Each vowel 'o' may only be followed by an 'i' or a 'u'.
#   Each vowel 'u' may only be followed by an 'a'.
# Since the answer may be too large, return it modulo 10 ** 9 + 7.
# ------------------------
# 1 <= n <= 2 * 10 ** 4


def count_vowel_perm(n: int) -> int:
    # working_sol (52.64%, 68.47%) -> (278ms, 16.5mb)  time: O(n) | space: O(1)
    vowel_strings: dict[str, int] = {
        'a': 1,
        'e': 1,
        'i': 1,
        'o': 1,
        'u': 1,
    }
    # We can reuse previously built strings, by description rules.
    for x in range(n - 1):
        a_end: int = vowel_strings['e']
        e_end: int = vowel_strings['a'] + vowel_strings['i']
        i_end: int = 0
        for key in vowel_strings:
            if key != 'i':
                i_end += vowel_strings[key]
        o_end: int = vowel_strings['i'] + vowel_strings['u']
        u_end: int = vowel_strings['a']
        vowel_strings['a'] = a_end
        vowel_strings['e'] = e_end
        vowel_strings['i'] = i_end
        vowel_strings['o'] = o_end
        vowel_strings['u'] = u_end
    return sum(vowel_strings.values()) % (10 ** 9 + 7)


# Time complexity: O(n) -> one loop for 'n' iterations => O(n) -> always sum() of 5 elements => O(1).
# n - input value 'n'^^|
# Auxiliary space: O(1) -> constant dictionary + 5 constant INTs nothing depends on input => O(1).
# ------------------------
# Hints:
# !
# Use dynamic programming.
# Let dp[i][j] be the number of strings of length i that ends with the j-th vowel.
# Deduce the recurrence from the given relations between vowels.
# !
# Ok. What we essentially care is that how we ended the string.
# n == 1, everything is only 1 symbol.
# n == 2, we can continue by the rules: e => ea, ei
# n == 3, we can continue this two: ea, ei -> eae, ei(any except i)
# So, it's like we have # of strings equal to # of recursion calls?
# Because if we can continue building we will call a recursion with correct symbol to use.
# And it's extra string?
# Then why do we need a recursion? If we can just store # of already built strings.


test: int = 1
test_out: int = 5
assert test_out == count_vowel_perm(test)

test = 2
test_out = 10
assert test_out == count_vowel_perm(test)

test = 5
test_out = 68
assert test_out == count_vowel_perm(test)

test = 1111
test_out = 262650274
assert test_out == count_vowel_perm(test)
