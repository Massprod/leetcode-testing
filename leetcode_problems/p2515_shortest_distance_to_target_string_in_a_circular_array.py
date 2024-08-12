# You are given a 0-indexed circular string array words and a string target.
# A circular array means that the array's end connects to the array's beginning.
# Formally, the next element of words[i] is words[(i + 1) % n]
#  and the previous element of words[i] is words[(i - 1 + n) % n], where n is the length of words.
# Starting from startIndex, you can move to either the next word or the previous word with 1 step at a time.
# Return the shortest distance needed to reach the string target.
# If the string target does not exist in words, return -1.
# ---------------------
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] and target consist of only lowercase English letters.
# 0 <= startIndex < words.length


def closest_target(words: list[str], target: str, start_index: int) -> int:
    # working_sol (61.54%, 89.42%) -> (56ms, 16.58mb)  time: O(n * max(k, target)) | space: O(1)
    if words[start_index] == target:
        return 0
    left: int = start_index - 1
    left_steps: int = 1
    right: int = start_index + 1
    right_steps: int = 1
    while left != start_index and right != start_index:
        if 0 > left:
            left = len(words) - 1
        if len(words) == right:
            right = 0
        if words[left] == target:
            return left_steps
        if words[right] == target:
            return right_steps
        left -= 1
        right += 1
        left_steps += 1
        right_steps += 1
    return -1


# Time complexity: O(n * max(k, target)) <- n - length of the input string `words`,
#                                           k - average length of words in `words`
# In the worst case, if there's no `target` in `words`.
# We're going to traverse `words` twice, and for each index we check all chars from `target`
#  and current_word => O(2 * (n * max(k, target))).
# ---------------------
# Auxiliary space: O(1)
# Only 4 constant INTs used, none of them depends on input => O(1).


test: list[str] = ["hello", "i", "am", "leetcode", "hello"]
test_target: str = "hello"
test_start: int = 1
test_out: int = 1
assert test_out == closest_target(test, test_target, test_start)

test = ["a", "b", "leetcode"]
test_target = "leetcode"
test_start = 0
test_out = 1
assert test_out == closest_target(test, test_target, test_start)

test = ["i", "eat", "leetcode"]
test_target = "ate"
test_start = 0
test_out = -1
assert test_out == closest_target(test, test_target, test_start)
