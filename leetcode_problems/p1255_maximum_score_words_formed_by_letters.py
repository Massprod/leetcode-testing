# Given a list of words, list of single letters (might be repeating)
#  and score of every character.
# Return the maximum score of any valid set of words formed by using the given letters
#  (words[i] cannot be used two or more times).
# It is not necessary to use all characters in letters and each letter can only be used once.
# Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.
# ---------------------------
# 1 <= words.length <= 14
# 1 <= words[i].length <= 15
# 1 <= letters.length <= 100
# letters[i].length == 1
# score.length == 26
# 0 <= score[i] <= 10
# words[i], letters[i] contains only lower case English letters.
from string import ascii_lowercase
from random import choice, randint
from collections import Counter, defaultdict


def max_score_words(words: list[str], letters: list[str], score: list[int]) -> int:
    # working_sol (44.90%, 75.28%) -> (54ms, 16.65mb)  time: O(k * 2 ** n + g) | space: O(n + g + k)
    # {char: occurrences}
    cur_letters: dict[str, int] = Counter(letters)

    def count_score(word: str) -> int:
        word_score: int = 0
        for char in word:
            word_score += score[ord(char) - 97]
        return word_score

    def check(index: int, cur_score: int) -> int:
        # We have only 2 options to check every subset.
        # Use or skip any word on the path.
        # The Only thing we care, if we want to use a word is that
        #  do we have enough letters or not?
        if index >= len(words):
            return cur_score
        skip: int = check(index + 1, cur_score)
        can_be_used: bool = True
        # {char: times used}
        used_chars: defaultdict[str, int] = defaultdict(int)
        for char in words[index]:
            if char in cur_letters and cur_letters[char]:
                cur_letters[char] -= 1
                used_chars[char] += 1
                continue
            can_be_used = False
            break
        use: int = 0
        if can_be_used:
            use = check(index + 1, cur_score + count_score(words[index]))
        # Restore used letters after we check the path.
        for char, t_used in used_chars.items():
            cur_letters[char] += t_used
        return max(skip, use)

    return check(0, 0)


# Time complexity: O(k * 2 ** n + g) <- k - maximum length of a word in `words`,
#                                       n - length of the input array `words`,
#                                       g - length of iht input array `letters`.
# We're always traversing `letters` once, to calculate number of occurrences for every letter => O(g).
# Then we're using recursion to check every possible subset we can create
#  and for every word we check, we're looping through all the chars to see if we can use that word => O(k).
# Extra looping this word again to restore `used_chars`, and we're counting score for an every word => O(2k).
# And because we're checking every possible subset, our recursion will take O(2 ** n * k + g)
# ---------------------------
# Auxiliary space: O(n + g + k)
# In the worst case, we're going to have every word in `words` which we can use with our `letters`.
# So, we always store all letters of `letters` and their occurrences => O(g).
# Recursion will have a stack of max size == `n`, if we use every word of `words` => O(n).
# Extra in every call, for every word we're trying to use we will store all the symbols of it in `used_chars` => O(k)


test: list[str] = ["dog", "cat", "dad", "good"]
test_letters: list[str] = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]
test_score: list[int] = [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
test_out: int = 23
assert test_out == max_score_words(test, test_letters, test_score)

test = ["xxxz", "ax", "bx", "cx"]
test_letters = ["z", "a", "b", "c", "x", "x", "x"]
test_score = [4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 10]
test_out = 27
assert test_out == max_score_words(test, test_letters, test_score)

test = ["leetcode"]
test_letters = ["l", "e", "t", "c", "o", "d"]
test_score = [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
test_out = 0
assert test_out == max_score_words(test, test_letters, test_score)

test = [''.join([choice(ascii_lowercase) for _ in range(15)]) for _ in range(14)]
test_letters = [choice(ascii_lowercase) for _ in range(100)]
test_score = [randint(0, 10) for _ in range(26)]
print(test, end='\n-----------\n')
print(test_letters, end='\n-----------\n')
print(test_score, end='\n-----------\n')
