# You are given a string word and a non-negative integer k.
# Return the total number of substrings of word that contain every vowel
#  ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.
# ----------------------
# 5 <= word.length <= 2 * 10 ** 5
# word consists only of lowercase English letters.
# 0 <= k <= word.length - 5
from random import choice

from string import ascii_lowercase

from pyperclip import copy

from collections import defaultdict, deque


def count_of_substrings(word: str, k: int) -> int:
    # working_sol (15.61%, 20.81%) -> (3320ms, 24.58mb)  time: O(n) | space: O(n)
    cur_char: str
    # consonants => everything else
    vowels: set[str] = ['a', 'e', 'i', 'o', 'u']
    # If last index value is not consonant => we can build extra sub from it.
    # If it's consonant we will ignore it in the window build.
    last_con_ind: int = len(word)
    consonant_suffixes: deque[int] = deque([])
    # We don't want to recalc all the options to expand the window.
    # So, we can just calc them from a `suffix`.
    # From index == 1 -> index 3, we can build 2 subs without changing `left_l`.
    # And because we need to shrink and we could use shrinked window as a sub as well.
    # We will extra reuse it for this as well.
    for index in range(len(word) - 1, -1, -1):
        consonant_suffixes.appendleft(last_con_ind)
        if word[index] in vowels:
            continue
        last_con_ind = index
    # { char: # of appereances in the current window }
    vowels_count: dict[str, int] = defaultdict(int)
    out: int = 0
    left_l: int = 0
    right_l: int = 0
    w_consonants: int = 0
    while right_l < len(word):
        # Expand and count while we can.
        char: str = word[right_l]
        if char in vowels:
            vowels_count[char] += 1
        else:
            w_consonants += 1
        # We can use this.
        # And we have 2 options to build.
        # Expand and recalc, but we already have suffixes => we use them.
        # Shring and recalc, same => we can reuse suffixes.
        # Just check both options and count substrings we can use.
        if k == w_consonants and len(vowels_count) == len(vowels):
            expand_limit: int = consonant_suffixes[right_l]
            subs: int = expand_limit - right_l
            while k == w_consonants and len(vowels_count) == len(vowels):
                out += subs
                cur_char = word[left_l]
                if cur_char not in vowels:
                    w_consonants -= 1
                elif cur_char in vowels_count:
                    vowels_count[cur_char] -= 1
                    if 0 == vowels_count[word[left_l]]:
                        vowels_count.pop(word[left_l])
                left_l += 1
        # No matter the case, consonants > k => we shrink the window.
        while k < w_consonants:
            cur_char = word[left_l]
            if cur_char not in vowels:
                w_consonants -= 1
            elif cur_char in vowels_count:
                vowels_count[cur_char] -= 1
                if 0 == vowels_count[word[left_l]]:
                    vowels_count.pop(word[left_l])
            left_l += 1
        right_l += 1
    
    return out


# Time complexity: O(n) <- n - length of the input string `word`
# Traversing whole input string `word` to get suffixes => O(n).
# Exttra traversing it with sliding window, while using every index of the string
#  at most twice => O(n + 2 * n).
# ----------------------
# Auxiliary space: O(n)
# `consonant_suffixes` <- allocates space for each index of the `word`.


test: str = 'aeioqq'
test_k: int = 1
test_out: int = 0
assert test_out == count_of_substrings(test, test_k)

test = 'aeiou'
test_k = 0
test_out = 1
assert test_out == count_of_substrings(test, test_k)

test = 'ieaouqqieaouqq'
test_k = 1
test_out = 3
assert test_out == count_of_substrings(test, test_k)

test = ''.join([choice(ascii_lowercase) for _ in range(2 * 10 ** 5)])
copy(test)
