# Given an encoded string, return its decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets
#   is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
# You may assume that the input string is always valid; there are no extra white spaces,
#   square brackets are well-formed, etc.
# Furthermore, you may assume that the original data does not contain any digits
#   and that digits are only for those repeat numbers, k.
# For example, there will not be input like 3a or 2[4].
# The test cases are generated so that the length of the output will never exceed 105.
# --------------------
# 1 <= s.length <= 30
# s consists of lowercase English letters, digits, and square brackets '[]'.
# s is guaranteed to be a valid input.
# All the integers in s are in the range [1, 300].


def decode_string(s: str) -> str:
    # working_sol (81.55%, 73.71%) -> (37ms, 16.3mb)  time: O(n) | space: O(∑(k * m))
    list_stack: list[str | int] = []
    index: int = 0
    # String to repeat.
    repeat: str = ''
    # Number of repeats.
    repeats: str = ''
    while index != len(s):
        # Every digit is actually a start of '[',
        # and creating of a new string.
        if s[index].isdigit():
            # So we can store currently build string ->
            list_stack.append(repeat)
            # -> and reset it.
            repeat = ''
            # Keep record of the repeats number.
            repeats += s[index]
            index += 1
            continue
        # End of repeats number ->
        if s[index] == '[':
            # -> store and reset it.
            list_stack.append(int(repeats))
            repeats = ''
            index += 1
            continue
        # We need to build and store string build inside
        # '[' and ']' to the first correspond opening bracket.
        if s[index] == ']':
            # Empty string, doesn't matter.
            if repeat:
                list_stack.append(repeat)
                repeat = ''
            # We always store in order Number of repeats at [-2]
            # and string we need to repeat at [-1].
            # So if we stored multiple strings like: 5[2[a]2[b]2[c]3[d]]
            # we need to combine everything until we can repeat it for '5' times.
            while type(list_stack[-2]) != int:
                list_stack[-1] = list_stack[-2] + list_stack.pop()
            # Currently build string to repeat ->
            cur_repeat: str = list_stack.pop()
            # -> Number of repeats for it.
            cur_repeats: int = list_stack.pop()
            # Expand previously stored string with new one,
            # and we store empty string if it was before digits.
            # So it's never index_error.
            list_stack[-1] += cur_repeat * cur_repeats
            index += 1
            continue
        # Build string without any repeats and store it later.
        # Or store empty if there's nothing to build from.
        repeat += s[index]
        index += 1
    # Everything stored in a list_stack, so we need to concat.
    # Extra to this last repeat which didn't hit any of ']'
    # needs to be explicitly added as well.
    # Otherwise, it's just empty string added, which doesn't matter.
    return ''.join(list_stack) + repeat


# Time complexity: O(n) -> traversing whole input array once to create stack => O(n) ->
# n - len of input_array^^| -> in the worst case ']' will be at last index, so we will traverse whole stack once again
#                           and use every index twice => O(2n).
# Auxiliary space: O(∑(k * m)) -> this one is hard, cuz we're storing all created strings inside a stack ->
#                           -> so we need to store every string * of it repeats, how to do this? ->
#                           -> no idea, sticking to O(k * m) <- k == number of repeats for current_string,
#                                                               m == len of this string
#                           We need to calc this for every unique string we can take from original_input.
#                           Out of my lvl, for now. Might be O(∑(k * m)) if string is not repeated then k == 1.
# --------------------
# Actually monster created, failed to even load submit request, and it's correct in submissions :)
# Ok. Second time is fine. Who is their editor? Cuz some Medium tasks is literally counting index + values,
# and this is Medium when it's overhead in compare to most of them.
# Well at least I made it correctly, and I will search more elegant way later.
# --------------------
# Add everything stop at '[' and start building new string, go back in stack when ']' until '['?
# Ok. Some monster looking solution, but it's actually the hardest STACK I met so far, dunno why it's Medium, or
# I'm missing something. Working for basic cases and some of mine with tricky parts, but I need more. Time to fail.


test: str = "3[a]2[bc]"
test_out: str = "aaabcbc"
assert test_out == decode_string(test)

test = "3[a2[c]]"
test_out = "accaccacc"
assert test_out == decode_string(test)

test = "2[abc]3[cd]ef"
test_out = "abcabccdcdcdef"
assert test_out == decode_string(test)

test = "abc1[abc5[ss]4[bb]6[sdf]]"
test_out = "abcabcssssssssssbbbbbbbbsdfsdfsdfsdfsdfsdf"
assert test_out == decode_string(test)
