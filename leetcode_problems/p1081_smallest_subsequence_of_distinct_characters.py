# Given a string s, return the lexicographically smallest subsequence of s
#  that contains all the distinct characters of s exactly once.
# -------------------
# 1 <= s.length <= 1000
# s consists of lowercase English letters.


def remove_duplicate(s: str) -> str:
    # working_sol (56.29%, 98.2%) -> (41ms, 16.1mb)  time: O(n) | space: O(n)
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
# -------------------
# Same as p316_remove_duplicate_letters.


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
