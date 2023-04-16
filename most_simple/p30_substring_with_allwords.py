# You are given a string s and an array of strings words. All the strings of words are of the same length.
#
# A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.
#
# For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab"
# are all concatenated strings. "acdbef" is not a concatenated substring because
# it is not the concatenation of any permutation of words.
# Return the starting indices of all the concatenated substrings in s.
# You can return the answer in any order.


def sub_indexes(s: str, words: list[str]) -> list[int]:
    # working_sol (70.7%, 13.70%)
    num_words = len(words)
    len_word = len(words[0])
    sub_size = len_word * num_words
    check_words = {}
    for _ in words:
        try:
            if check_words[_]:
                check_words[_] += 1
        except KeyError:
            check_words[_] = 1

    def exist(index):
        used_words = check_words.copy()
        checked = 0
        for y in range(index,  index + sub_size, len_word):
            sliced = s[y: y + len_word]
            try:
                if used_words[sliced] > 0:
                    used_words[sliced] -= 1
                    checked += 1
                else:
                    break
            except KeyError:
                return False
        if checked == num_words:
            return True
        return False
    hay_length = len(s)
    last_possible_index = hay_length - sub_size + 1
    indexes = []
    for x in range(last_possible_index):
        if exist(x):
            indexes.append(x)
    return indexes


test1 = "barfoothefoobarman"
test1_words = ["foo", "bar"]
test1_out = [0, 9]
print(sub_indexes(test1, test1_words))
assert sub_indexes(test1, test1_words) == test1_out

test2 = "wordgoodgoodgoodbestword"
test2_words = ["word", "good", "best", "good"]
test2_out = [8]
# test2 - fail. Didn't take into account that words can be repeated.
print(sub_indexes(test2, test2_words))
assert sub_indexes(test2, test2_words) == test2_out
