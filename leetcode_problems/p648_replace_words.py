# In English, we have a concept called root, which can be followed by some other word
#  to form another longer word - let's call this word successor.
# For example, when the root "an" is followed by the successor word "other",
#  we can form a new word "another".
# Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces,
#  replace all the successors in the sentence with the root forming it.
# If a successor can be replaced by more than one root,
#  replace it with the root that has the shortest length.
# Return the sentence after the replacement.
# -----------------
# 1 <= dictionary.length <= 1000
# 1 <= dictionary[i].length <= 100
# dictionary[i] consists of only lower-case letters.
# 1 <= sentence.length <= 10 ** 6
# sentence consists of only lower-case letters and spaces.
# The number of words in sentence is in the range [1, 1000]
# The length of each word in sentence is in the range [1, 1000]
# Every two consecutive words in sentence will be separated by exactly one space.
# sentence does not have leading or trailing spaces.


def replace_words(dictionary: list[str], sentence: str) -> str:
    # working_sol (99.17%, 91.20%) -> (75ms, 24.7mb)  time: O(m) | space: O(n + m)
    # ! called root, which can be followed by some other word !
    # ^^We need only words from dictionary, which can be used to build
    #  another words when used as Prefixes.
    # So it's Essentially search for the smallest prefix.
    dictionary_: set[str] = set()
    max_length: int = 0
    # Input is list, rebuild to dict|set for O(1) get.
    for _ in dictionary:
        # And it's better to know maximum length of a prefix.
        # Cuz words can be larger than prefix,
        #  and because we're checking every word index by index.
        # We can be sure that prefix with size > max_length,
        #  can't be present in dictionary.
        max_length = max(max_length, len(_))
        dictionary_.add(_)
    # ! will be separated by exactly one space ! <- constraint
    # Instead of building words by indexes, just rebuild
    #  into list of presented words.
    new_sentence: list[str] = sentence.split(' ')
    for x in range(len(new_sentence)):
        for y in range(1, len(new_sentence[x])):
            prefix: str = new_sentence[x][0: y]
            if len(prefix) > max_length:
                break
            # Always building from left -> right, symbol by symbol.
            # So it's always smallest version used.
            if prefix in dictionary_:
                new_sentence[x] = prefix

    return ' '.join(new_sentence)


# Time complexity: O(m) -> traversing input_dictionary once to create hash_table => O(n) -> building list with
# n - len of input_dictionary^^| all words from sentence => O(m) -> worst case, every word is the same, and
# m - len of input_sentence^^|   prefix which can be used with them having the same size ->
#                                -> so for every word we will check all indexes until prefix found => O(m).
# Auxiliary space: O(n + m) -> creating set() with all values from input_dictionary, same size => O(n) ->
#                           -> creating list with all words from input_sentence => O(m).
# -----------------
# Ok. First version with indexes working correctly, but it should be faster with slicing.
# Yep 300ms -> 75ms. Same approach just with slicing.
# -----------------
# ! when the root "an" is followed by the successor word "other" !
# So we need to find prefix in dict and replace it?
# Cuz it's not like we need ANY substring, we can only use something can allow us to build word from it,
#  used as prefix.
# Tested with 'other' == root, 'another' in sentence, and its expecting 'another' as return.
# Should be correct.


test: list[str] = ["cat", "bat", "rat"]
test_sen: str = "the cattle was rattled by the battery"
test_out: str = "the cat was rat by the bat"
assert test_out == replace_words(test, test_sen)

test = ["a", "b", "c"]
test_sen = "aadsfasf absbs bbab cadsfafs"
test_out = "a a b c"
assert test_out == replace_words(test, test_sen)

test = ["cat", "bat", "rat", "other"]
test_sen = "the cattle was rattled by the battery another"
test_out = "the cat was rat by the bat another"
assert test_out == replace_words(test, test_sen)
