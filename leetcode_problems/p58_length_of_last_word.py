# Given a string s consisting of words and spaces, return the length of the last word in the string.
#
# A word is a maximal substring consisting of non-space characters only.
# 1 <= s.length <= 104 and There will be at least one word in S

def length_of_last_word(s: str) -> int:
    count: int = 0
    for x in range(len(s) - 1, -1, -1):
        if s[x] == " " and count > 0:
            break
        if s[x] != " ":
            count += 1
    return count

# Most simple way to solve it is STRIP(), but I guess it's not a correct way to use build_in methods.
# So let's try to loop and count every symbol from the end.


test1 = "Hello World"
test1_out = 5
print(length_of_last_word(test1))

test2 = "   fly me   to   the moon  "
test2_out = 4
print(length_of_last_word(test2))

test3 = "luffy is still joyboy"
test3_out = 6
print(length_of_last_word(test3))
