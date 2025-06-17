# The following actions must be performed in order to generate
# You are given a string caption representing the caption for a video.
#  a valid tag for the video:
# 1. Combine all words in the string into a single camelCase string
#    prefixed with '#'.
#   A camelCase string is one where the first letter of all words
#    except the first one is capitalized.
#   All characters after the first character in each word must be lowercase.
# 2. Remove all characters that are not an English letter, except the first '#'.
# 3. Truncate the result to a maximum of 100 characters.
# Return the tag after performing the actions on caption.
# ----------------------------
# 1 <= caption.length <= 150
# caption consists only of English letters and ' '.
from string import ascii_letters


def generate_tag(caption: str) -> str:
    # working_sol (100.00%, 97.78%) -> (0ms, 17.56mb)  time: O(n) | space: O(n)
    caption = caption.strip()
    fast_chars: set[str] = set(ascii_letters)
    words: list[str] = caption.split(' ')
    out: list[str] = []

    for word in words:
        check_word: list[str] = []
        for char in word:
            if char not in fast_chars:
                continue
            check_word.append(char)
        new_word: str = ''.join(check_word).lower()
        if out:
            out.append(new_word.capitalize())
        else:
            out.append(new_word)
    
    return '#' + ''.join(out)[:99]


# Time complexity: O(n) <- n - length of the input string `caption`.
# Always traversing each char of the input string `caption`, twice.
# To check them for english letters + lowercase convertion => O(2 * n).
# ----------------------------
# Auxiliary space: O(n)
# `out` <- allocates space for each char of the input string `caption` => O(n).
# In the  worst case `caption` contains only 1 word.
# `check_word` <- allocates space for each char of the input string `caption` => O(2 * n).77


test: str = 'Leetcode daily streak achieved'
test_out: str = '#leetcodeDailyStreakAchieved'
assert test_out == generate_tag(test)

test = 'can I Go There'
test_out = '#canIGoThere'
assert test_out == generate_tag(test)

test = 'hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh' \
       'hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh'
test_out = '#hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh' \
           'hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh'
assert test_out == generate_tag(test)
