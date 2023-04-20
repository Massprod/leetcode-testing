# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
#
# countAndSay(1) = "1"
# countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1),
# which is then converted into a different digit string.
# To determine how you "say" a digit string, split it into the minimal number of substrings
# such that each substring contains exactly one unique digit. Then for each substring,
# say the number of digits, then say the digit. Finally, concatenate every said digit.

# Input: n = 4
# Output: "1211"
# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = say "1" = one 1 = "11"
# countAndSay(3) = say "11" = two 1's = "21"
# countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

# always count from 1
# answer for n is say for n-1
# recursion???

def count_say(n: int) -> str:
    # working_sol (64.44%, 98.25%) time: O(n**2) | space: O(1)
    def say(word: str) -> str:
        occurs = 0
        num = word[0]
        new_say = ""
        length = len(word)
        for x in range(length):
            if num == word[x]:
                occurs += 1
                if x == length - 1:
                    new_say += str(occurs) + str(num)
                continue
            if word[x] != word[x - 1]:  # could be using ELIF instead of continue, but w.e
                new_say += str(occurs) + str(num)
                occurs = 1
                num = word[x]
                if x == length - 1:
                    num = word[x]
                    occurs = 1
                    new_say += str(occurs) + str(num)
        return new_say

    say_string = "1"
    for _ in range(n - 1):
        say_string = say(say_string)
    return say_string

# Time complexity: O(n**2) -> there's 2 loops, one executes N time and another inside executes N times.
# --------------------------
# Space complexity: O(1) -> creating one new string and repeating it in a new call. Number of strings fixed.


test1 = 1
test1_out = 1
print(count_say(1))

test2 = 4
test2_out = 1211
print(count_say(test2))

test3 = 5
test3_out = 111221
print(count_say(test3))
