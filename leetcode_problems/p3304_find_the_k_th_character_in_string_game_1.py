# Alice and Bob are playing a game.
# Initially, Alice has a string word = "a".
# You are given a positive integer k.
# Now Bob will ask Alice to perform the following operation forever:
#  - Generate a new string by changing each character in word to its next character in the English alphabet,
#     and append it to the original word.
# For example, performing the operation on "c" generates "cd"
#  and performing the operation on "zb" generates "zbac".
# Return the value of the kth character in word,
#  after enough operations have been done for word to have at least k characters.
# Note that the character 'z' can be changed to 'a' in the operation.
# -------------------------
# 1 <= k <= 500


def kth_character(k: int) -> str:
    # working_sol (54.99%, 21.46%) -> (11ms, 16.66mb)  time: O(k) | space: O(k)
    string: str = 'a'
    while k > len(string):
        new_string: str = ''.join(
            [chr(ord(char) + 1 if ord(char) < 123 else 97) for char in string]
        )
        string += new_string
    return string[k - 1]


# Time complexity: O(k)
# Always building string of size at least `k` => O(k).
# -------------------------
# Auxiliary space: O(k)
# `string` <- allocates space for at least `k` chars => O(k).


test: int = 5
test_out: str = "b"
assert test_out == kth_character(test)

test = 10
test_out = "c"
assert test_out == kth_character(test)
