# You are given an encoded string s. To decode the string to a tape,
#  the encoded string is read one character at a time and the following steps are taken:
#   - If the character read is a letter, that letter is written onto the tape.
#   - If the character read is a digit d, the entire current tape is repeatedly written d - 1 more times in total.
# Given an integer k, return the kth letter (1-indexed) in the decoded string
# -------------------
# 2 <= s.length <= 100
# s consists of lowercase English letters and digits 2 through 9.
# s starts with a letter.
# 1 <= k <= 10 ** 9
# It is guaranteed that k is less than or equal to the length of the decoded string.
# The decoded string is guaranteed to have less than 2 ** 63 letters.
from random import choice, randint
from string import ascii_lowercase


def decode_at_index(s: str, k: int) -> str:
    # working_sol (71.72%, 86.87%) -> (36ms, 16.16mb)  time: O(n) | space: O(n)
    # Start length == 0, empty string
    stack: list[int] = [0]
    index: int = 0
    # Store every length of string we could build.
    while stack[-1] < k:
        # Multiply length by digit.
        if s[index].isdigit():
            stack.append(stack[-1] * int(s[index]))
        # Otherwise, it's just increased by 1 symbol.
        else:
            stack.append(stack[-1] + 1)
        # Check every symbol, until we build string with len >= k.
        index += 1
    # len(stack) == number of changes.
    # I.e. every index of stack is index of 's' on which we made some changes.
    # Multiplied or just increased our string.
    index = len(stack) - 1
    # ! kth letter (1-indexed) !
    # So, when k == stack[-1].
    # On this action we built correct string with k == length.
    # And we need (0-indexed) => (index -= 1)
    while k:
        k %= stack.pop()
        index -= 1
    # And if we multiplied on this index == action.
    # Then we can just take last symbol added before it.
    while s[index].isdigit():
        index -= 1
    return s[index]


# Time complexity: O(n) -> worst case == k = max_len we can build ->
# n - len of input string^^| -> traversing whole input string to get max_length => O(n).
# Auxiliary space: O(n) -> for every symbol in input string, adding length into a stack => O(n).
# -------------------
# Ok we can't just use a string => Memory Limit.
# Then what do we need to store? Tags: string, stack.
# We can maintain length of string we're building in a stack, and then find index of character by k.
# Take modulus of 'k' until we find k == cur_length in stack, then we can take this length index to get correct char.


test: str = "leet2code3"
test_k: int = 10
test_out: str = "o"
assert test_out == decode_at_index(test, test_k)

test = "ha22"
test_k = 5
test_out = "h"
assert test_out == decode_at_index(test, test_k)

test = "a2345678999999999999999"
test_k = 1
test_out = "a"
assert test_out == decode_at_index(test, test_k)

test = ''
for _ in range(100):
    test += choice([choice(ascii_lowercase), str(randint(2, 9))])
