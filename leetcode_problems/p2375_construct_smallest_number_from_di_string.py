# You are given a 0-indexed string pattern of length n consisting of the characters
#   'I' meaning increasing and 'D' meaning decreasing.
# A 0-indexed string num of length n + 1 is created using the following conditions:
#   num consists of the digits '1' to '9', where each digit is used at most once.
#   If pattern[i] == 'I', then num[i] < num[i + 1].
#   If pattern[i] == 'D', then num[i] > num[i + 1].
# Return the lexicographically smallest possible string num that meets the conditions.
# --------------------
# 1 <= pattern.length <= 8
# pattern consists of only the letters 'I' and 'D'.


def smallest_number(pattern: str) -> str:
    # working_sol (55.90%, 76.74%) -> (45ms, 16.3mb)  time: O(n) | space: O(n + 1)
    # Using stack to store all values.
    list_que: list[str] = []
    # Lexicographically smallest ->
    # -> always using the smallest option allowed, on left side.
    correct_string: str = ''
    for x in range(0, len(pattern) + 1):
        # Stack is populated from 1 -> (len(pattern) + 1),
        # always using the smallest option possible.
        list_que.append(str(x + 1))
        # So if we ever meet 'I', we can add everything stored so far.
        # It's going to be in asc_order and lexicographically_smallest.
        # Every 'D' allows us to add HIGHER value in a stack, and
        # correctly add them in DESC order after.
        if x == len(pattern) or pattern[x] == 'I':
            while len(list_que) != 0:
                correct_string += list_que.pop()
    return correct_string


# Time complexity: O(n) -> in the worst case with pattern == 'DDDDDDDD', we're going to traverse once all values for
# n - len of pattern^^| len(pat) times and extra traversing whole stack with this value to add them => O(2n).
# Auxiliary space: O(n + 1) -> same, we need to save all values == n + 1 into a stack and build string from it =>
#                             => O(n + 1) <- because we're rebuilding, stack size is decreasing and string increasing,
#                             so it's always same size of (n + 1) taken by them together.
# --------------------
# Ok. It's all good, but TLE and I just need to know about new method with using stack.
# Tried to use HINT, guess and failed. But with new method it's easy.
# We're just saving everything in a stack and because we're adding from 1 -> len(pat),
# everytime we meet 'I' -> we can just add everything from a stack because it's holding all in asc order.
# So if we need 'D' descending then we're skipping values and their just stacking one by one in ascending order,
# at the moment of 'I' again we're going to add all of them from HIGHEST on [-1] to lowest at [0].
# And number of added values in a stack is always equal to the range in a pattern.
# ! lexicographically smallest possible string ! -> String with the lowest possible option used on left side.
# Because we're adding 1 -> len(pat), we're always having the lowest possible value we can add on the left side already.
# --------------------
# Hmm. Interesting, ! lexicographically smallest possible string ! <- that's new.
# All I found is that standard check of all symbols one by one, and if first diff is higher than it's higher string.
# If it's lower, then it's lower string.


test: str = "IIIDIDDD"
test_out: str = "123549876"
assert test_out == smallest_number(test)

test = "DDD"
test_out = "4321"
assert test_out == smallest_number(test)
