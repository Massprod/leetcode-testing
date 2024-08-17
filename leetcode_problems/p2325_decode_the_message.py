# You are given the strings key and message,
#  which represent a cipher key and a secret message, respectively.
# The steps to decode message are as follows:
#  1. Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
#  2. Align the substitution table with the regular English alphabet.
#  3. Each letter in message is then substituted using the table.
#  4. Spaces ' ' are transformed to themselves.
#  - For example, given key = "happy boy" (actual key would have at least one instance
#    of each letter in the alphabet), we have the partial substitution table of
#    ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').
# Return the decoded message.
# ---------------------
# 26 <= key.length <= 2000
# key consists of lowercase English letters and ' '.
# key contains every letter in the English alphabet ('a' to 'z') at least once.
# 1 <= message.length <= 2000
# message consists of lowercase English letters and ' '.
from string import ascii_lowercase


def decode_message(key: str, message: str) -> str:
    # working_sol (94.79%, 60.77%) -> (30ms, 16.57mb)  time: O(n + m) | space: O(m)
    alph_index: int = 0
    alphabet: str = ascii_lowercase
    to_use: set[str] = set(ascii_lowercase)
    # { key_char: alph_char }
    dec_pairs: dict[str, str] = {
        ' ': ' ',
    }
    for char in key:
        if char in to_use:
            dec_pairs[char] = alphabet[alph_index]
            alph_index += 1
            to_use.remove(char)
    out: list[str] = []
    for char in message:
        out.append(dec_pairs[char])
    return ''.join(out)


# Time complexity: O(n + m) <- n - length of the input string `key`, m - length of the input string `message`.
# Always traversing both input strings, once => O(n + m).
# Extra traversing whole `message` to join it => O(n + 2 * m).
# ---------------------
# Auxiliary space: O(m)
# By the constraints, we're always going to have all the alphabet present.
# `dec_pairs` <- always of the same size == 27.
# `out` <- always allocate space for every char in `message` => O(m).


test_key: str = "the quick brown fox jumps over the lazy dog"
test_message: str = "vkbs bs t suepuv"
test_out: str = "this is a secret"
assert test_out == decode_message(test_key, test_message)

test_key = "eljuxhpwnyrdgtqkviszcfmabo"
test_message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
test_out = "the five boxing wizards jump quickly"
assert test_out == decode_message(test_key, test_message)
