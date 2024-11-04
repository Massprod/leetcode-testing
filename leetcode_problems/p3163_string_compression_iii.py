# Given a string word, compress it using the following algorithm:
#  - Begin with an empty string comp. While word is not empty, use the following operation:
#     - Remove a maximum length prefix of word made of a single character c repeating at most 9 times.
#     - Append the length of the prefix followed by c to comp.
# Return the string comp.
# ---------------------------
# 1 <= word.length <= 2 * 10 ** 5
# word consists only of lowercase English letters.
from random import choice
from collections import deque
from string import ascii_lowercase


def compressed_string(word: str) -> str:
    # working_sol (80.85%, 15.10%) -> (177ms, 27.68mb)  time: O(n) | space: O(n)
    que: deque[str] = deque(word)
    out: list[str] = []
    cur_streak: int = 1
    cur_char: str = que.popleft()
    limit: int = 9
    while que:
        new_char = que.popleft()
        if cur_char == new_char and cur_streak < limit:
            cur_streak += 1
        elif cur_char != new_char:
            if cur_streak:
                out.append(
                    f'{cur_streak}{cur_char}'
                )
            cur_char = new_char
            cur_streak = 1
        elif cur_streak < limit and cur_char == que[0]:
            continue
        if limit == cur_streak:
            out.append(f'{cur_streak}{cur_char}')
            cur_streak = 0
    if cur_streak:
        out.append(
            f'{cur_streak}{cur_char}'
        )
    return ''.join(out)


# Time complexity: O(n) <- n - length of the input string `word`.
# Traversing `word` to get all the chars in `que` => O(n).
# Extra traversing all the chars from `word` to get their prefix streaks => O(2 * n).
# ---------------------------
# Auxiliary space: O(n)
# `que` <- allocates space for each char from `word` => O(n).
# In the worst case there's always sequence of non-equal chars.
# So it's going to be like: 1a1b1c1d...1a1b1c1d...etc
# `out` <- allocates space for each char from `word` + counter => O(2 * n + n).


test: str = "abcde"
test_out: str = "1a1b1c1d1e"
assert test_out == compressed_string(test)

test = "aaaaaaaaaaaaaabb"
test_out = "9a5a2b"
assert test_out == compressed_string(test)

test = "aaaaaaaaay"
test_out = "9a1y"
assert test_out == compressed_string(test)

test = ''.join([choice(ascii_lowercase) for _ in range(2 * 10 ** 5)])
print(test)
