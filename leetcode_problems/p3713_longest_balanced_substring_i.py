# You are given a string s consisting of lowercase English letters.
# A substring of s is called balanced if all distinct characters in the substring
#  appear the same number of times.
# Return the length of the longest balanced substring of s.
# --- --- --- ---
# 1 <= s.length <= 1000
# s consists of lowercase English letters.


def longest_balanced(s: str) -> int:
    # working_solution: (94.16%, 62.89%) -> (1049ms, 19.29mb)  Time: O(s ** 2) Space: O(s)
    out: int = 0
    for start in range(len(s)):
        uniques: dict[str, int] = {}
        # We don't want to loop for each iteration => count how many unique values we meet.
        count_uniques: int = 0
        # Current maximum occurrences.
        current_max: int = 0
        # Current subs with the `current_max` occurrences of each distinct.
        count_max: int = 0
        for index in range(start, len(s)):
            cur_char: str = s[index]
            uniques[cur_char] = uniques.get(cur_char, 0) + 1
            char_occurs: int = uniques[cur_char]
            if 1 == char_occurs:
                count_uniques += 1
            # Break of the balanced sub.
            if char_occurs > current_max:
                current_max, count_max = char_occurs, 1
            elif char_occurs == current_max:
                count_max += 1
            # We need same number of unique values and subs.
            if count_uniques == count_max:
                sub_length: int = index - start + 1  # +1 - 0 indexed
                out = max(out, sub_length)

    return out


# Time complexity: O(s ** 2)
# --- --- --- ---
# Space complexity: O(s)
# `uniques` <- allocates space for each unique value from `s`.


test: str = "abbac"
test_out: int = 4
assert test_out == longest_balanced(test)

test = "zzabccy"
test_out = 4
assert test_out == longest_balanced(test)

test = "aba"
test_out = 2
assert test_out == longest_balanced(test)
