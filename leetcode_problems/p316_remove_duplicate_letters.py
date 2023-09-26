# Given a string s, remove duplicate letters so that every letter appears once and only once.
# You must make sure your result is the smallest in lexicographical order among all possible results.
# ----------------------
# 1 <= s.length <= 10 ** 4
# s consists of lowercase English letters.
from random import choice
from string import ascii_lowercase


def remove_duplicate(s: str) -> str:
    # working_sol (92.26%, 97.39%) -> (35ms, 16.2mb)  time: O(n) | space: O(n)
    # (symbol)
    stack: list[str] = [s[0]]
    # (symbol, used_index)
    used: dict[str, int] = {s[0]: 0}
    # (symbol, last_index)
    # Last occurrence.
    most_right: dict[str, int] = {}
    for x in range(len(s)):
        most_right[s[x]] = x
    # Lexico smallest == use smallest symbol possible.
    for y in range(1, len(s)):
        # Already used, but to escape deleting it with using not last index.
        # We need to update its index.
        if s[y] in used and used[s[y]] != most_right[s[y]]:
            used[s[y]] = y
        elif s[y] not in used:
            # Delete everything higher, except ones that's already on most right index.
            # Which means they will never occur again, and we need everything used Once.
            while stack and s[y] < stack[-1] and used[stack[-1]] != most_right[stack[-1]]:
                used.pop(stack.pop()[0])
            stack.append(s[y])
            used[s[y]] = y
    return ''.join(stack)


# Time complexity: O(n) -> traversing whole input string to get all most_right indexes of symbols => O(n) ->
# n - len of input string^^| -> traversing it again to get the smallest lexicographic subsequence ->
#                            -> and because we're maintaining stack we can use all indexes twice => O(2n).
# Auxiliary space: O(n) -> dictionary with all symbols and their most_right indexes => O(n) ->
#                          -> dictionary with all symbols and their used indexes => O(n) ->
#                          -> worst case == everything unique -> stack with all symbols in it => O(n).
# ----------------------
# ! 1 <= s.length <= 10 ** 4 !
# 100% not DP with these constraints.
# Stack tag.
# ! smallest in lexicographical order !
# Essentially we need to use the smallest string on left side from all the options.
# How we can decide on it? Use most right? Like: 'aaaaaaaaaaa', and we only need last 'a'
# In this case we need to maintain right_most position. What about: 'acccccaaabbbbbaaaac'
# In this case we need to use first 'a', then 'b' and 'c'.
# Task tagged with Stack, so maintain a stack of everything used?
# What to delete? We delete every 'c' except last, maintain most_right and delete everything if it's lexico higher?
# Like we add 'accccc' in a stack, then 'a', we delete every 'c' because there's some 'c' on right side after this.
# Actually, we need to delete everything not just 'c', everything which higher or equal.
# Or ignore adding 'a' if last value in a stack is the same.
# Should be correct. Let's try.
# Extra, we need to maintain used indexes, otherwise we will delete something lower which was not updated == skipped.


test: str = "bcabc"
test_out: str = "abc"
assert test_out == remove_duplicate(test)

test = "cbacdcbc"
test_out = "acdb"
assert test_out == remove_duplicate(test)

test = 'egguazqdbemuzvxofwiozloipmrrozdzuflzowbkkekoezvtxgasytkshcdesvjgdewclyzhyysxersxustedljgtonlugougjpk'
test_out = 'aqbefilmcdsvgwyzhrxjtnoupk'
assert test_out == remove_duplicate(test)

test = 'bbcaac'
test_out = 'bac'
assert test_out == remove_duplicate(test)

test = 'bcbac'
test_out = 'bac'
assert test_out == remove_duplicate(test)

test = ''
for _ in range(10 ** 3):
    test += choice(ascii_lowercase) * 2
# print(test)
