# You are given two 0-indexed strings s and target.
# You can take some letters from s and rearrange them to form new strings.
# Return the maximum number of copies of target that can be formed by taking letters
#  from s and rearranging them.
# ----------------------------
# 1 <= s.length <= 100
# 1 <= target.length <= 10
# s and target consist of lowercase English letters.
from collections import Counter


def rearrange_characters(s: str, target: str) -> int:
    # working_sol (95.77%, 48.59%) -> (26ms, 16.54mb)  time: O(s + target) | space: O(s + target)
    # { char: occurrences }
    all_chars: dict[str, int] = Counter(s)
    target_chars: dict[str, int] = Counter(target)
    if len(target_chars) > len(all_chars):
        return 0
    out: int = len(s)
    for char in target_chars:
        if char in all_chars:
            # We might need more than 1 char to use == floor div to get number of uses.
            out = min(out, all_chars[char] // target_chars[char])
        else:
            out = 0
            break
    return out


# Time complexity: O(s + target)
# Always traversing both input arrays to get all occurrences => O(s + target).
# Extra traversing all unique chars from `target`, once => O(s + target + target).
# ----------------------------
# Auxiliary space: O(s + target)
# In the worst case, there's all unique chars in `s` and `target`.
# `all_chars` <- allocates space for each unique char from `s` => O(s)
# `target_chars` <- allocates space for each unique char from `target` => O(target).


test: str = "ilovecodingonleetcode"
test_target: str = "code"
test_out: int = 2
assert test_out == rearrange_characters(test, test_target)

test = "abcba"
test_target = "abc"
test_out = 1
assert test_out == rearrange_characters(test, test_target)

test = "abbaccaddaeea"
test_target = "aaaaa"
test_out = 1
assert test_out == rearrange_characters(test, test_target)
