# Given an input string s, reverse the order of the words.
#  A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.
#  Note that s may contain leading or trailing spaces or multiple spaces between two words.
#  The returned string should only have a single space separating the words. Do not include any extra spaces.
# -------------------
# 1 <= s.length <= 104
# s contains English letters (upper-case and lower-case), digits, and spaces ' '.
# There is at least one word in s.
# -------------------
# Follow-up: If the string data type is mutable in your language,
# can you solve it in-place with O(1) extra space?


def reverse_words_rebuild(s: str) -> str:
    new_words: str = ""
    new_word: str = ""
    for x in range(len(s) - 1, -1, -1):
        if (x != (len(s) - 1) and s[x] == " " and s[x + 1] != " ") or x == 0:
            if x == 0 and s[0] != " ":
                new_word += s[0]
            if len(new_words) >= 1 and new_word != "":
                new_words += " "
            for y in range(len(new_word) - 1, -1, -1):
                new_words += new_word[y]
            new_word = ""
            continue
        elif x != 0 and s[x] != " " and s[x - 1] == " ":
            new_word += f"{s[x]}"
        elif s[x] != " ":
            new_word += s[x]
    return new_words


# -------------------
# Basic rebuilding with O(n) space is easy, so it's better to try O(1).
# But, even better is to do both.


test1 = "the sky is blue"
test1_out = "blue is sky the"
print(reverse_words_rebuild(test1))

test2 = "  hello world  "
test2_out = "world hello"
print(reverse_words_rebuild(test2))

test3 = "a good   example"
test3_out = "example good a"
print(reverse_words_rebuild(test3))
