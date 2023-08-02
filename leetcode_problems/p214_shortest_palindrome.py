# You are given a string s. You can convert s to a palindrome by adding characters in front of it.
# Return the shortest palindrome you can find by performing this transformation.
# --------------------
# 0 <= s.length <= 5 * 10 ** 4
# s consists of lowercase English letters only.
from string import ascii_lowercase
from random import choice


def shortest_palindrome(s: str) -> str:
    # working_sol(39.72%, 34.86%) -> (223ms, 16.9mb)  time: O(n * log n) | space: O(n)
    if not s:
        return ""
    # We allowed to place symbols only on the left side,
    # so if there's anything on the left side unused we can't counterbalance.
    # Basically we need longest_palindrome from original string which only starts on [0].
    left_l: int = 0
    # Right-limit on the other hand is [-1], cuz we need LONGEST.
    # And first palindrome we meet, is going to be longest if we start from the end.
    right_l: int = len(s) - 1
    while left_l <= right_l:
        # If [0] != [right_l], last symbols aren't equal
        # it can't be palindrome at all.
        if s[left_l] == s[right_l]:
            # Cutting by left/right parts.
            middle: int = right_l // 2
            l_point: int = middle
            # If it's EVEN -> there's no middle element.
            # And middle itself is 2 elements.
            if (right_l + 1) % 2 == 0:
                r_point: int = l_point + 1
                # Naming is a bit off, cuz it's not 100% palindrome but w.e
                # Left slice.
                pali_left: str = s[:l_point + 1]
                # Right slice -> reversed.
                pali_right: str = s[right_l: r_point - 1:-1]
                # If both parts are equal -> it's 100% palindrome, and we can use it.
                if pali_left == pali_right:
                    # Only last element not in palindrome, need to rebuild it later.
                    if (right_l + 1) == (len(s) - 1):
                        new_string: str = s[-1] + s
                        return new_string
                    # More than last element not in palindrome.
                    # Right_limit => index where palindrome ENDs.
                    new_string = s[:right_l:-1] + pali_left + pali_right[::-1] + s[right_l + 1:]
                    return new_string
            # If it's ODD -> there's middle element.
            # And we can slice from it, ignoring the middle.
            else:
                # Same approach, but we need to include middle ->
                l_point = middle - 1
                r_point = middle + 1
                pali_left = s[:l_point + 1]
                pali_right = s[right_l: r_point - 1:-1]
                if pali_left == pali_right:
                    if (right_l + 1) == (len(s) - 1):
                        new_string: str = s[-1] + s
                        return new_string
                    # -> we're ignoring middle element while checking for correct palindrome,
                    # but it still needs to be included in the end.
                    new_string = s[:right_l:-1] + pali_left + s[middle] + pali_right[::-1] + s[right_l + 1:]
                    return new_string
        right_l -= 1


# Time complexity: O(n * log n) -> in the worst case, we're traversing whole input_string and for each index passed
# n - len of input_string^^| we could be checking for palindrome s[0] == s[right_l], like ->
#                       -> "aaaabaaaaa", in this case we're going to check part of the 's' at least 5 times =>
#                       => and only 6 time is lucky one to get palindrome => O(n * log n).
# Auxiliary space: O(n) -> in the worst case whole input_string is palindrome ->
#                       -> so pali_left + pali_right == n => O(n) ->
#                       -> actually what if we only have 1 element correct and everything else will be reversed,
#                       we're saving all slices in new_string -> in this case it should be O(2n) ->
#                       -> cuz we're going to make new_string with size of == ((n - 1) * 2 + 1) => O(2n) => O(n).
#                       Still linear scaling from n tho.
# --------------------
# Ok. Slicing is faster, guess I was lucky to at least get confirmation it's correct idea with 8800ms :)
# How can I cull slicing even more? Like save original state and take only right_most if it's incorrect?
# Then I wouldn't be slicing original s everytime.
# --------------------
# Ok. Idea is correct, but first why do I even start from middle?
# I wasn't sure it's working idea and tested, but it's actually can be at least done with window,
# and not checking everything but only [0] == [right_l] -> Rebuild.
# Hmm. Window is even slower.
# --------------------
# Ok. Empty is always correct, 1 symbol is also always correct.
# And after testing with: "aaaacecaaa" => "aaacecaaaacecaaa" -> I can say that we need to find LONGEST palindrome
# inside of given string, but it always should start from LEFT|[0] -> cuz otherwise we need to put something in
# counterbalance on other side, and we're not allowed to place anything on RIGHT side.
# So basically -> find the longest palindrome inside -> put everything from right side which isn't part of palindrome
# on left side -> if there's NO palindrome with start at [0], just put everything in counter.
# Should be correct. Let's try.


test: str = "aacecaaa"
test_out: str = "aaacecaaa"
assert test_out == shortest_palindrome(test)

test = "abcd"
test_out = "dcbabcd"
assert test_out == shortest_palindrome(test)

test = ""
test_out = ""
assert test_out == shortest_palindrome(test)

test = "aaaacecaaa"
test_out = "aaacecaaaacecaaa"
assert test_out == shortest_palindrome(test)

test = "baaaaabcdef"
test_out = "fedcbaaaaabcdef"
assert test_out == shortest_palindrome(test)

test = ""
for _ in range(5 * 10 ** 4):
    test += choice(ascii_lowercase)
# print(test)
