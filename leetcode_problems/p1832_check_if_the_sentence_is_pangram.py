# A pangram is a sentence where every letter of the English alphabet appears at least once.
# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram,
#  or false otherwise.
# -------------------------
# 1 <= sentence.length <= 1000
# sentence consists of lowercase English letters.


def check_if_pangram(sentence: str) -> bool:
    # working_sol (59.00%, 69.33%) -> (35ms, 16.40mb)  time: O(n) | space: O(n)
    return len(set(sentence)) == 26


# Time complexity: O(n) <- n - length of the input string `sentence`
# Always traversing `sentence`, once => O(n).
# -------------------------
# Auxiliary space: O(n)
# In the worst case, every char in `sentence` is unique.
# `set(sentence)` <- allocates space for each unique char in `sentence` => O(n).


test: str = "thequickbrownfoxjumpsoverthelazydog"
test_out: bool = True
assert test_out == check_if_pangram(test)

test = "leetcode"
test_out = False
assert test_out == check_if_pangram(test)
