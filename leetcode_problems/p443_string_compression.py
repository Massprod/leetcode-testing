# Given an array of characters chars, compress it using the following algorithm:
#  Begin with an empty string s. For each group of consecutive repeating characters in chars:
#    - If the group's length is 1, append the character to s.
#    - Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead,
#   be stored in the input character array chars.
# Note that group lengths that are 10 or longer will be split into multiple characters in chars.
# After you are done modifying the input array, return the new length of the array.
# You must write an algorithm that uses only constant extra space.
# ----------------------
# 1 <= chars.length <= 2000
# chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.


def compress(chars: list[str]) -> int:
    # working_sol (84.03%, 97.79%) -> (65ms 16.29mb)  time: O(n) | space: O(1)
    # index -> current index we start searching.
    # start_index -> index from who we're starting.
    index: int = 0
    start_index: int = 0
    while index != len(chars):
        count: int = 0
        # Count every consecutive symbol.
        while index != len(chars) and chars[index] == chars[start_index]:
            count += 1
            index += 1
        # If there's only 1 we don't need to add count.
        if count == 1:
            chars[start_index:index] = [chars[start_index]]
            # Skip 1 index, replaced.
            index = start_index + 1
            # Starting next search from this index.
            start_index = index
            continue
        # Replace indexes we counted, with symbol and it's counter.
        chars[start_index:index] = [chars[start_index]] + [_ for _ in str(count)]
        # Every symbol in str(count) will take 1 index ->
        index = start_index
        # -> so we need to skip indexes after our starting point,
        #    equal to its length.
        for _ in str(count):
            index += 1
        # -> and extra index for placed symbol before it.
        index += 1
        start_index = index
    # ! return the new length of the array !
    return len(chars)


# Time complexity: O(n) -> traversing and using every index for counting, once => O(n) ->
# n - len of input_array^^| -> but slicing, we changing one index for count == 1, so it's constant ->
#                           -> but if we have more than 1 symbol, then it's removing of some indexes and placing
#                           new ones, extra change of indexing for others, no idea how to calc it correctly.
#                           It's like 10-15% slower than string solution, but string is extra space.
#                           And only can be ignored if they allow it. But this one is real in_place.
#                           Extra for string i can correctly calc O(n) :) No slicing, so it's replacing of orig list.
# Auxiliary space: O(1) -> only 3 constant INTs used => O(1).
# ----------------------
# Ok. We actually need to change input_array.
# Rebind => chars[:] = list(str_count),
# or it's better to build real in_place solution without string.
# It should be slower, because slicing will take more time for changes.
# ----------------------
# ! You must write an algorithm that uses only constant extra space. ! ->
# -> ! Begin with an empty string s ! <- What? So we allowed to use string to store and then
# just replace original list with list(string)?
# Otherwise, I can save it all in original_list, but then I would need to slice it and change
# which is a lot of moves for no reason. If we allowed to use string to store it.
# And they're literally saying => ! If the group's length is 1, append the character to s. !
# So I will stick to using string.


test: list[str] = ["a", "a", "b", "b", "c", "c", "c"]
test_out: int = 6
assert test_out == compress(test)

test = ["a"]
test_out = 1
assert test_out == compress(test)

test = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
test_out = 4
assert test_out == compress(test)
