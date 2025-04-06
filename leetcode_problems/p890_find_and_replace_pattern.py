# Given a list of strings words and a string pattern,
#  return a list of words[i] that match pattern.
# You may return the answer in any order.
# A word matches the pattern if there exists a permutation of letters p
#  so that after replacing every letter x in the pattern with p(x),
#  we get the desired word.
# Recall that a permutation of letters is a bijection from letters to letters:
#  every letter maps to another letter, and no two letters map to the same letter.
# -----------------------
# 1 <= pattern.length <= 20
# 1 <= words.length <= 50
# words[i].length == pattern.length
# pattern and words[i] are lowercase English letters.


def find_and_replace_pattern(words: list[str], pattern: str) -> list[str]:
    # working_sol (100.00%,  90.15%) -> (0ms, 17.61mb)  time: O(n * g) | space: O(n * g + g)
    out: list[str] = []
    for word in words:
        # { pattern_char: word_char }
        chars_map: dict[str, str] = {}
        # { assigned chars }
        used_chars: set[str] = set()
        correct: bool = True
        for index in range(len(word)):
            word_char: str = word[index]
            pattern_char: str = pattern[index]
            # Cringe checks, but Im too tired to rebuild it :)
            # We either get a correct mapping of the char.
            if (chars_map.get(pattern_char)
                and chars_map[pattern_char] == word_char):
                continue
            # Or it's incorrect, and a `char` we need to map is already mapped
            #  to something else.
            if (
                (chars_map.get(pattern_char) and chars_map[pattern_char] != word_char)
                or
                word_char in used_chars
                ):
                correct = not correct
                break
            chars_map[pattern_char] = word_char
            used_chars.add(word_char)
        
        if correct:
            out.append(word)
    
    return out


# Time complexity: O(n * g) <- n - length of the input array `words`,
#                              g - avg length of the word in `words`.
# Always traversing whole input array `words`, and check every char in it's words.
# In the worst case, every word is correct for the pattern => O(n * g).
# -----------------------
# Auxiliary space: O(n * g + g)
# `out` <- allocates space for each word from `words` => O(n * g).
# `chars_map` and `used_chars` <- both allocates space for each unique char from `word`.
# And as we know, worst case == everything can be used, so it's avg => O(n * g + 2 * g).


test: list[str] = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
test_pattern: str = "abb"
test_out: list[str] = ["mee", "aqq"]
assert test_out == find_and_replace_pattern(test, test_pattern)

test = ["a","b","c"]
test_pattern = "a"
test_out = ["a", "b", "c"]
assert test_out == find_and_replace_pattern(test, test_pattern)
