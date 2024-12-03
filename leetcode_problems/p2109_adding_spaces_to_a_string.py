# You are given a 0-indexed string s and a 0-indexed integer array spaces that describes the indices
#  in the original string where spaces will be added.
# Each space should be inserted before the character at the given index.
# For example, given s = "EnjoyYourCoffee" and spaces = [5, 9],
#  we place spaces before 'Y' and 'C', which are at indices 5 and 9 respectively.
# Thus, we obtain "Enjoy Your Coffee".
# Return the modified string after the spaces have been added.
# -------------------------
# 1 <= s.length <= 3 * 10 ** 5
# s consists only of lowercase and uppercase English letters.
# 1 <= spaces.length <= 3 * 1 ** 05
# 0 <= spaces[i] <= s.length - 1
# All the values of spaces are strictly increasing.


def add_spaces(s: str, spaces: list[int]) -> str:
    # working_sol (45.77%, 44.10%) -> (111ms, 48.89mb)  time: O(s) | space: O(s)
    out: list[str] = []
    spaces_ind: int = 0
    for index, value in enumerate(s):
        if (spaces_ind < len(spaces)
                and index == spaces[spaces_ind]):
            out.append(' ')
            spaces_ind += 1
        out.append(value)
    return ''.join(out)


# Time complexity: O(s)
# Traversing whole input string `s`, once to get all chars in correct order => O(s).
# Extra joining it together with extra spaces, and in the worst case, every char will get its own space => O(s + 2 * s).
# -------------------------
# Auxiliary space: O(s)
# `out` <- allocates space for each char of `s` and extra space for each of them => O(2 * s).


test: str = "LeetcodeHelpsMeLearn"
test_spaces: list[int] = [8, 13, 15]
test_out: str = "Leetcode Helps Me Learn"
assert test_out == add_spaces(test, test_spaces)

test = "icodeinpython"
test_spaces = [1, 5, 7, 9]
test_out = "i code in py thon"
assert test_out == add_spaces(test, test_spaces)

test = "spacing"
test_spaces = [0, 1, 2, 3, 4, 5, 6]
test_out = " s p a c i n g"
assert test_out == add_spaces(test, test_spaces)
