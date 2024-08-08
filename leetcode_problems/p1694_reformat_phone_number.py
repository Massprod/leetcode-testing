# You are given a phone number as a string number.
# number consists of digits, spaces ' ', and/or dashes '-'.
# You would like to reformat the phone number in a certain manner.
# Firstly, remove all spaces and dashes.
# Then, group the digits from left to right into blocks of length 3 until there are 4 or fewer digits.
# The final digits are then grouped as follows:
#  - 2 digits: A single block of length 2.
#  - 3 digits: A single block of length 3.
#  - 4 digits: Two blocks of length 2 each.
# The blocks are then joined by dashes.
# Notice that the reformatting process should never produce any blocks of length 1
#  and produce at most two blocks of length 2.
# Return the phone number after formatting.
# ----------------------
# 2 <= number.length <= 100
# number consists of digits and the characters '-' and ' '.
# There are at least two digits in number.
from collections import deque
from random import choice, randint


def reformat_number(number: str) -> str:
    # working_sol (77.52%, 16.48mb) -> (32ms, 16.48mb)  time: O(n) | space: O(n)
    seq: str
    cor_numbers: deque[str] = deque([])
    for char in number:
        if char.isdigit():
            cor_numbers.append(char)
    out: list[str] = []
    while 2 <= (len(cor_numbers) - 3):
        seq: str = ''
        for _ in range(3):
            seq += cor_numbers.popleft()
        out.append(seq)
    if 4 != len(cor_numbers):
        out.append(''.join(cor_numbers))
    else:
        for _ in range(2):
            seq = ''
            for _ in range(2):
                seq += cor_numbers.popleft()
            out.append(seq)
    return '-'.join(out)


# Time complexity: O(n) <- n - length of the input string `number`
# Always traversing `number` once to get all the allowed chars => O(n).
# In the worst case, every char is allowed, so we extra traverse every char once again => O(2 * n).
# ----------------------
# Auxiliary space: O(n)
# `cor_numbers` <- will hold every char from `number` => O(n)
# `out` <- will hold every char from `number` and extra `n // 3 - 1` dashes => O(n + n + n // 3 - 1).


test: str = "1-23-45 6"
test_out: str = "123-456"
assert test_out == reformat_number(test)

test = "123 4-567"
test_out = "123-45-67"
assert test_out == reformat_number(test)

test = "123 4-5678"
test_out = "123-456-78"
assert test_out == reformat_number(test)

test = ''.join([choice([str(randint(1, 10)), ' ', '-']) for _ in range(50)])
print(test)
