# You are given an array of characters letters that is sorted in non-decreasing order, and a character target.
# There are at least two different characters in letters.
#
# Return the smallest character in letters that is lexicographically greater than target.
# If such a character does not exist, return the first character in letters.
# ---------------------
# 2 <= letters.length <= 10 ** 4
# letters[i] is a lowercase English letter.
# letters is sorted in non-decreasing order.
# letters contains at least two different characters.
# target is a lowercase English letter.


def next_greatest_letter(letters: list[str], target: str) -> str:
    # working_sol (48.3%, 67.25%) -> (135ms, 67.25%)  time: O(n) | space: O(1)
    if target > letters[-1] or target < letters[0]:
        return letters[0]
    for x in range(len(letters)):
        if x == (len(letters) - 1):
            if target < letters[x]:
                return letters[x]
        if target < letters[x] < letters[x + 1]:
            return letters[x]
    return letters[0]


# Time complexity: O(n) -> in the worst case, traversing whole input_list => O(n).
# n - len of input_list^^|
#                  Θ(n) -> only part of the input_listr will be checked => O(n)
#                  Ω(1) -> best case with [0] or [-1] indexes being correct => O(1)
# Auxiliary space: O(1) -> nothing extra.
# ---------------------


test1 = ["c", "f", "j"]
test1_target = "a"
test1_out = "c"
print(next_greatest_letter(test1, test1_target))
assert test1_out == next_greatest_letter(test1, test1_target)

test2 = ["c", "f", "j"]
test2_target = "c"
test2_out = "f"
print(next_greatest_letter(test2, test2_target))
assert test2_out == next_greatest_letter(test2, test2_target)

test3 = ["x", "x", "y", "y"]
test3_target = "z"
test3_out = "x"
print(next_greatest_letter(test3, test3_target))
assert test3_out == next_greatest_letter(test3, test3_target)
