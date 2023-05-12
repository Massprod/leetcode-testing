# Given a string s consisting of words and spaces, return the length of the last word in the string.
#
# A word is a maximal substring consisting of non-space characters only.
# 1 <= s.length <= 104 and There will be at least one word in S

def length_of_last_word(s: str) -> int:
    # working_sol (6.2%, 17.44%) -> (51ms, 16.2mb)  time: O(n)  | space: O(1)
    length: int = 0
    for x in range(len(s) - 1, -1, -1):
        if s[x] == " " and length > 0:
            break
        if s[x] != " ":
            length += 1
    return length

# Time complexity: O(n) -> By the task description there's always will be word and spaces (at least 1 of each)
#                          Worst case is we're going to loop through whole input -> case like this "word   "
#                  Θ(log n) -> best of all cases -> "word   word" (only part of input will be searched)
#                  Ω(n) -> best case like this -> "word" (always at least one word, no info about spaces)
# Space complexity: O(1) -> one constant for counting length.

# Most simple way to solve it is STRIP(), but I guess it's not a correct way to use build_in methods.
# So let's try to loop and count every symbol from the end.


test1 = "Hello World"
test1_out = 5
assert test1_out == length_of_last_word(test1)
print(length_of_last_word(test1))

test2 = "   fly me   to   the moon  "
test2_out = 4
assert test2_out == length_of_last_word(test2)
print(length_of_last_word(test2))

test3 = "luffy is still joyboy"
test3_out = 6
assert test3_out == length_of_last_word(test3)
print(length_of_last_word(test3))
