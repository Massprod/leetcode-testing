# Given a string s, return the longest palindromic substring in s.
# ----------------------
# 1 <= s.length <= 1000
# s consist of only digits and English letters
from random import choice
from string import ascii_letters, digits


def longest_subpal(s: str) -> str:
    # working_sol (99.18%, 24.61%) -> (80ms, 16.7mb)  time: O(n) | space: O(n)
    if not s:
        return ''
    if len(s) == 1:
        return s
    # Any 1 symbol can be a palindrome.
    longest: str = s[0]
    pal_start_points: list[list[int]] = []
    # Starting points include ODD|EVEN options.
    # [0] and [1] can't include ODD, so it's unique check.
    if s[0] == s[1]:
        longest = s[0] + s[1]
    for x in range(2, len(s)):
        # Even starts from 2 points.
        if s[x] == s[x - 1]:
            # Starts are 0-indexed, +1 for correct length.
            # We can't build more than left|right side.
            # So, maximum size of palindrome is (left|right side * 2).
            max_len: int = min(
                (x - 1 + 1) * 2,  # if left side is lower
                (len(s) - x + 1) * 2,  # if right side is lower
            )
            pal_start_points.append([max_len, x])
        # Odd start, needs to include middle from the beginning.
        if s[x] == s[x - 2]:
            # Same left|right sides, but with +1 for middle element.
            max_len = min((x - 2 + 1) * 2, (len(s) - x + 1) * 2) + 1
            pal_start_points.append([max_len, x - 2, x])
    # Because we're skipping palindrome checks if already visited longer palindrome.
    # It's good to just sort them in descending and try to use Longest options first.
    # They might be not palindromes, but at least we can assume it.
    # And skip lower size checks after.
    pal_start_points.sort(key=lambda y: y[0], reverse=True)
    for start in pal_start_points:
        # Already visited same size or higher.
        # Everything else is going to be lower or equal.
        max_len = start[0]
        if max_len <= len(longest):
            break
        cur_pal: str = ''
        # Even.
        if len(start) == 2:
            left_l: int = start[1] - 1
            right_l: int = start[1]
        # Odd.
        else:
            left_l = start[1]
            right_l = start[2]
            # Middle element.
            cur_pal += s[left_l + 1]
        # Trying to expand on both sides, while we can.
        while 0 <= left_l and right_l < len(s) and s[left_l] == s[right_l]:
            cur_pal = s[left_l] + cur_pal + s[right_l]
            left_l -= 1
            right_l += 1
        # Update longest.
        if len(cur_pal) > len(longest):
            longest = cur_pal
    return longest


# Time complexity: O(n) -> traverse of whole input string to get starting points, once => O(n) ->
# n - len of input string^^| -> worst case? == 'a' * 1000 -> we can start palindrome from any index ->
#                            -> we will start from  middle [499] and start building from it ->
#                            -> visit every index, and then we will check every other start point and skip it ->
#                            -> so it should be close to linear, because it's not really the worst case,
#                            after I changed sorting and now using the longest size option, we will skip other checks.
#                            Dunno, but it's improved from 300ms to 80ms. Sticking to a linear O(n).
#                            We start from longest and then skip any lower options we find.
#                            In case with 'a' * 1000, it's just 2 traverses:
#                             1 find start_points,
#                             2 find longest from middle.
# Auxiliary space: O(n) -> worst case == 'a' * 1000 -> we will add every index as starting point and
#                          most of them will be added twice for ODD option, extra max_len for everyone => O(2n).


test: str = "babad"
test_out: str = 'aba'
assert test_out == longest_subpal(test)

test = "cbbd"
test_out = 'bb'
assert test_out == longest_subpal(test)

test = "bb"
test_out = 'bb'
assert test_out == longest_subpal(test)

test = ''
for _ in range(1000):
    test += choice([choice(ascii_letters), choice(digits)])
print(test)
