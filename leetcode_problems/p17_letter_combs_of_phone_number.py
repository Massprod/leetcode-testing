# Given a string containing digits from 2-9 inclusive,
#   return all possible letter combinations that the number could represent.
# Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons) is given below.
# Note that 1 does not map to any letters.
# ---------------------
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].


def letter_combinations(digits: str) -> list[str]:
    # working_sol (98.78%, 98.42%) -> (31ms, 16.1mb)  time: O(n ** k) | space: O(n ** k)
    # Unique case with empty.
    if len(digits) == 0:
        return []
    # All digits symbol options.
    options: dict[str, list[str]] = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }
    # Combining backwards, so we need to take Base first ->
    # -> Last digit is a Base with who everything will be combined.
    if len(digits) == 1:
        return options[digits[0]]
    # Every digit symbol can be used with every other digit symbol ->
    # -> "77" -> "pp", "pq", "pr" etc.
    # Duplicates are allowed, so we're just taking every symbol of last digit
    # and building every combination with previous digits backwards.
    already_added: list[str] = letter_combinations(digits[:-1])
    new_options: list[str] = options[digits[-1]]
    all_combs: list[str] = [alr + new for alr in already_added for new in new_options]
    return all_combs


# Time complexity: O(n ** k) -> basically in the worst case we're having 4 nested loops with 3 or 4 size ->
# n -> longest of input_digit options^^| -> so it's something like n1 * n2 * n3 * n4 where n == len(options[digit]) ->
# k -> len of input_digits^^| -> like "7777" we're just getting n ** 4, it's correct, but I don't know can we
#                             just use n as longest, cuz it can be 3 or 4 -> w.e O() is worst case anyway =>
#                             => O(n ** k).
# Auxiliary space: O(n ** k) -> we're storing every combination and all combinations of 2 arrays is X * Y,
#                               X <- elements of first array, Y <- elements of second array ->
#                               -> we're combining all digits, and their equal to k => so it's k arrays with n size =>
#                               => O(n ** k).
# ---------------------
# For the future - always go to recursion if there's 2+ for loops needed
# Made only 2 tasks with recursion and failed to see it here.....


test: str = "23"
test_out: list[str] = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
assert test_out == letter_combinations(test)

test = ""
test_out = []
assert test_out == letter_combinations(test)

test = "2"
test_out = ["a", "b", "c"]
assert test_out == letter_combinations(test)
