# Given a string s, return the longest palindromic substring in s.
# ----------------------
# 1 <= s.length <= 1000
# s consist of only digits and English letters
from random import choice
from string import ascii_letters, digits


def longest_subpal(s: str) -> str:
    # working_sol (98.85%, 20.82%) -> (76ms, 16.7mb)  time: O(n * log n) | space: O(n)
    # Any single symbol can be a palindrome.
    if len(s) == 1:
        return s
    longest: str = s[0]
    # [0] + [1] can't be ODD sized palindrome, so it's unique check.
    if s[0] == s[1]:
        longest = s[0] + s[1]
    # Find all index options from whom we can start to build palindromes.
    # (maximum possible length of palindrome, rightmost start index)
    pal_start_points: list[tuple[int, int]] = []
    for x in range(2, len(s)):
        # Even sized palindrome, starts from 2 indexes.
        if s[x] == s[x - 1]:
            # Rightmost start index 'x' 0-indexed, +1 for correct length.
            # Maximum size of palindrome is (left|right side * 2).
            # We can't build more than left|right sides, so we choose minimum.
            max_len: int = min(
                (x - 1 + 1),  # left side
                (len(s) - x + 1),  # right side
            )
            pal_start_points.append((max_len * 2, x))
        # Odd sized, starts from 3 indexes => needs to include middle.
        if s[x] == s[x - 2]:
            # Same left and right sides check, but with +1 for middle element.
            max_len = min((x - 2 + 1), (len(s) - x + 1))
            pal_start_points.append((max_len * 2 + 1, x))
    # Because we're skipping palindrome checks if already visited longer palindrome.
    # It's good to just sort them in descending order and try to use longest options first.
    # They might be not palindromes, but at least we can assume it.
    # And skip lower size checks after.
    pal_start_points.sort(key=lambda y: y[0], reverse=True)
    for start in pal_start_points:
        max_len = start[0]
        # Already visited same size or higher.
        # Everything else is going to be lower or equal.
        if max_len <= len(longest):
            break
        cur_pal: str = ''
        # Even.
        if not max_len % 2:
            left_l: int = start[1] - 1  # leftmost index to start from
            right_l: int = start[1]  # rightmost index to start from
        # Odd.
        else:
            left_l = start[1] - 2
            right_l = start[1]
            cur_pal += s[left_l + 1]  # middle element
        # Trying to expand on both sides, while we can.
        while 0 <= left_l and right_l < len(s) and s[left_l] == s[right_l]:
            cur_pal = s[left_l] + cur_pal + s[right_l]
            left_l -= 1
            right_l += 1
        # Update longest.
        if len(cur_pal) > len(longest):
            longest = cur_pal
    return longest


# Time complexity: O(n * log n) <- n - length of input string `s`.
# First we find every starting point for palindrome by checking every index of `s` => O(n).
# Worst case: we can start building palindrome from every index.
# Second we're sorting them in descending order by maximum possible length => O(n * log n).
# Third, we're always start building palindromes from LONGEST -> SHORTEST.
# And this part is questionable, because it should be O(n * n), if we can start building from every index and
#  their sizes are full string like:  'aaaaaaaa....aaaa'.
# But, because we start from LONGEST, we will just break after one full traverse => O(n).
# What if we have like elements from middle with max_len == 499, 498, etc... 2, 1.
# So, we will check 499, and it fails with len == 3 assuming its ODD.
# And everything until max_len == 2, will be checked and fail with len == 3, assuming all of them were ODD.
# Then we will check every index + some part of the string, not even HALF.
# Can we call it O(n * log n)? it's definitely not exponent (n * n).
# Dunno, but I will stick to O(n * log n).
# ----------------------
# Auxiliary space: O(n).
# Worst case: we can start building palindromes from every index.
# So, we will have `pal_start_points` with tuple (max_len, index) type for every index => O(n).
# Extra string `longest` can have maximum size of `n`, when palindrome is in the middle => O(n).
# And extra to this, standard sort() takes O(n) to sort as well.
# O(3n).


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
