# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character
#   while preserving the order of characters.
# No two characters may map to the same character, but a character may map to itself.
# ---------------------
# 1 <= s.length <= 5 * 10 ** 4
# t.length == s.length
# s and t consist of any valid ascii character.


def is_isomorphic(s: str, t: str) -> bool:
    # working_sol (93.88%, 80.77%) -> (45ms, 16.5mb)  time: O(n) | space: O(n)
    # Symbol assigned from s -> t and t -> s.
    s_pairs: dict[str, str] = {}
    t_pairs: dict[str, str] = {}
    # ! t.length == s.length ! <- constraint.
    for x in range(len(s)):
        # If both symbols not assigned, we can assign them to each other.
        if t[x] not in t_pairs and s[x] not in s_pairs:
            s_pairs[s[x]] = t[x]
            t_pairs[t[x]] = s[x]
            continue
        # If t[x] already assigned, and s[x] not assigned,
        # means we can't assign s[x] to t[x] and we can't skip symbols.
        elif t[x] in t_pairs and s[x] not in s_pairs:
            return False
        # Opposite, s[x] assigned and t[x] is empty,
        # we can't use t[x] to replace s[x] and we can't skip symbols.
        elif s[x] in s_pairs and t[x] not in t_pairs:
            return False
        # If t[x] already assigned, but for a different symbol in s,
        # we can't use t[x] to replace not assigned symbol.
        elif t[x] in t_pairs and t_pairs[t[x]] != s[x]:
            return False
    # If every t -> s pairs correctly used.
    return True


# Time complexity: O(n) -> using every index of s and t, once => O(2n) => O(n) <- input_arrays always same_length.
# n - len of input_arrays^^|
# Auxiliary space: O(n) -> in the worst case there's only unique symbols in t -> every symbol will be assigned
#                          with correct pair in s and stored => O(2n) => O(n).
# ---------------------
# Ok. Made some tests -> we can use any symbol from t to place in s, no matter how many times.
# But every symbol from t is assigned to replaced symbol in s, and we can't use it to replace anything else.
# "papert" "titlet" -> False, cuz we can't use t[-1] == t  to place on s[-1] == t, cuz "t" already in pair with "p".


test_s: str = "egg"
test_t: str = "add"
test_out: bool = True
assert test_out == is_isomorphic(test_s, test_t)

test_s = "foo"
test_t = "bar"
test_out = False
assert test_out == is_isomorphic(test_s, test_t)

test_s = "paper"
test_t = "title"
test_out = True
assert test_out == is_isomorphic(test_s, test_t)

test_s = "aaab"
test_t = "dddd"
test_out = False
assert test_out == is_isomorphic(test_s, test_t)

test_s = "abcdefa"
test_t = "abcdeff"
test_out = False
assert test_out == is_isomorphic(test_s, test_t)
