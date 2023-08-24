# Given an array of strings words and a width maxWidth,
#  format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
# You should pack your words in a greedy approach; that is,
#  pack as many words as you can in each line.
# Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
# Extra spaces between words should be distributed as evenly as possible.
# If the number of spaces on a line does not divide evenly between words,
#  the empty slots on the left will be assigned more spaces than the slots on the right.
# For the last line of text, it should be left-justified, and no extra space is inserted between words.
# Note:
#   - A word is defined as a character sequence consisting of non-space characters only.
#   - Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
#   - The input array words contains at least one word.
# -----------------
# 1 <= words.length <= 300
# 1 <= words[i].length <= 20
# words[i] consists of only English letters and symbols.
# 1 <= maxWidth <= 100
# words[i].length <= maxWidth
from random import choice, randint
from string import ascii_lowercase


def full_justify(words: list[str], maxWidth: int) -> list[str]:
    # working_sol (98.82%, 69.23%) -> (29ms, 16.4mb)  time: O(n) | space: O(n * M)
    all_lines: list[str] = []
    # Iterative approach.
    cur_word: int = 0
    while cur_word != len(words):
        # Creating line by line.
        cur_line: list[str] = []
        # cur len != len(cur_line)
        # But equal to words already placed +1
        #  for every space before the words.
        cur_len: int = 0
        # First shouldn't have +1 space, extra check.
        first: bool = True
        while cur_word != len(words):
            # First is just word, and it's len() by itself.
            # ! words[i].length <= maxWidth !
            # Extra we always can use at least 1 word per line.
            if first:
                cur_line.append(words[cur_word])
                first = False
                cur_len += len(words[cur_word])
                cur_word += 1
                continue
            # Any other word is always having space before it.
            # If adding new word exceeds the limit, break.
            if len(words[cur_word]) + 1 + cur_len <= maxWidth:
                cur_line.append(' ' + words[cur_word])
                cur_len += 1 + len(words[cur_word])
                cur_word += 1
                continue
            break
        # Last line is unique, and all we need is ->
        # -> join this line and fill right the side with spaces.
        if cur_word == len(words):
            all_lines.append(''.join(cur_line) + ' ' * (maxWidth - cur_len))
        else:
            # All empty space we can use.
            empty_space: int = maxWidth - cur_len
            if empty_space != 0:
                # One|Two words on the line, is essentially the same,
                #  we're filling only the Gap.
                if len(cur_line) <= 2:
                    cur_line[0] = cur_line[0] + ' ' * empty_space
                else:
                    # even_spaces -> every word will have same amount before it, except [0].
                    even_spaces: int = empty_space // (len(cur_line) - 1)
                    # extra_spaces -> spaces we should place on Left side in prior.
                    # ! empty slots on the left will be assigned more spaces !
                    extra_spaces: int = empty_space % (len(cur_line) - 1)
                    # Placing spaces AFTER the word, so we don't need last_word of the line.
                    for x in range(len(cur_line) - 1):
                        cur_line[x] = cur_line[x] + ' ' * even_spaces
                    space_index: int = 0
                    # Placing them as evenly as possible, until we can.
                    # one by one == most even.
                    while extra_spaces:
                        if space_index == len(cur_line) - 1:
                            space_index = 0
                        cur_line[space_index] = cur_line[space_index] + ' '
                        extra_spaces -= 1
                        space_index += 1
            # Saving correctly build lines, one by one.
            all_lines.append(''.join(cur_line))
    return all_lines


# Time complexity: O(n) -> essentially it's Linear == O(n), because we always do the same thing ->
# n - len of input_array^^| -> always filling the line with spaces, which can differ by number of operations,
#                           but they never exceed max_width and in some cases insta saving lines ->
#                           -> dunno how to calc correctly number of iterations for ALL words if we're
#                           filling spaces, like it's always different from 0 to even max_width - 1.
#                           In some cases we're not filling the gaps at all, something like:
#                           O(n * ((K - 1) + (M - G) % (K - 1))) <- where K is len(cur_line) and M is maxWidth.
#                            (M - G) - gap we need to fill, and G is len(''.join(cur_line)).
#                           This should be more correct.
# Auxiliary space: O(n * M) -> worst case should be something -> every Word is size of maxWidth, so we will
# M - input maxWidth^^|  get Lines == Words => O(n * M).
# -----------------
# Ok working will max_constraints, but I need tricky parts to test. Time to fail commit.
# Or not, completed correctly.


test: list[str] = ["This", "is", "an", "example", "of", "text", "justification."]
test_w: int = 16
test_out: list[str] = [
    "This    is    an",
    "example  of text",
    "justification.  "
]
assert test_out == full_justify(test, test_w)

test = ["What", "must", "be", "acknowledgment", "shall", "be"]
test_w = 16
test_out = [
    "What   must   be",
    "acknowledgment  ",
    "shall be        "
]
assert test_out == full_justify(test, test_w)

test = [
    "Science", "is", "what", "we", "understand", "well", "enough",
    "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"
]
test_w = 20
test_out = [
    "Science  is  what we",
    "understand      well",
    "enough to explain to",
    "a  computer.  Art is",
    "everything  else  we",
    "do                  "
]
assert test_out == full_justify(test, test_w)

test = []
for _ in range(300):
    test_word: str = ''
    for _ in range(randint(1, 20)):
        test_word += choice(ascii_lowercase)
    test.append(test_word)
# print(test)
