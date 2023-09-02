# Given a string array words, return an array of all characters that show up
#  in all strings within the words (including duplicates).
# You may return the answer in any order.
# ------------------
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of lowercase English letters.


def common_chars(words: list[str]) -> list[str]:
    # working_sol (28.46%, 76.49%) -> (68ms, 16.3mb)  time: O(k * n) | space: O(n * k)
    # We need word with minimum length, faster check.
    min_word: int = 0
    min_length: int = len(words[0])
    for y in range(len(words)):
        if min_length > len(words[y]):
            min_length = len(words[y])
            min_word = y
    # We need symbols which present in ALL strings and duplicates as well.
    # So we need to know how many symbols presented.
    # Otherwise, we can't count # of duplicates correctly.
    chars_per_word: dict[str, dict[str, int]] = {}
    for x in range(len(words)):
        # Ignore check word.
        if x == min_word:
            continue
        # Add new word.
        if words[x] not in chars_per_word:
            chars_per_word[words[x]] = {}
        # Count every word symbols.
        for sym in words[x]:
            if sym not in chars_per_word[words[x]]:
                chars_per_word[words[x]][sym] = 1
                continue
            chars_per_word[words[x]][sym] += 1
    common_list: list[str] = []
    # Check if symbol from minimum length word is present in all.
    for sym in words[min_word]:
        common: bool = True
        for word in chars_per_word:
            # Not present.
            if sym not in chars_per_word[word]:
                common = False
            # Present but all duplicates already used.
            elif chars_per_word[word][sym] == 0:
                common = False
        # Present correctly.
        if common:
            # Mark usage.
            for word in chars_per_word:
                chars_per_word[word][sym] -= 1
            common_list.append(sym)
    return common_list


# Time complexity: O(k * n) -> traversing input_array once, to get min_word => O(n) -> traverse all words except min,
# k - len of words inside^^| and count symbol occurrences => O(n * k) -> worst case, every word is same length,
# n - len of input_array^^|  check every symbol from min_word => traverse only stored words twice O(k * (n + n)).
# Auxiliary space: O(n * k + n) -> dictionary with all words as keys, and dictionaries with their symbols as values =>
#                              => O(n * k) -> extra list with all symbols from min_word, worst case len(min_word) == n
#                              => O(n * k + n).


test: list[str] = ["bella", "label", "roller"]
test_out: list[str] = ["e", "l", "l"]
assert test_out == common_chars(test)

test = ["cool", "lock", "cook"]
test_out = ["c", "o"]
assert test_out == common_chars(test)
