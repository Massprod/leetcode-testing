# You are given a 0-indexed string s and a dictionary of words dictionary.
# You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary.
# There may be some extra characters in s which are not present in any of the substrings.
# Return the minimum number of extra characters left over if you break up s optimally.
# ----------------------
# 1 <= s.length <= 50
# 1 <= dictionary.length <= 50
# 1 <= dictionary[i].length <= 50
# dictionary[i] and s consists of only lowercase English letters
# dictionary contains distinct words


def min_extra_char(s: str, dictionary: list[str]) -> int:
    # working_sol (90.21%, 41.01%) -> (204ms, 16.90mb)  time: O(n * n + m) | space: O(n + m)
    # Standard memo.
    recur_cache: dict[int, int] = {}
    fast_dict: set[str] = set(dictionary)

    def check(index: int) -> int:
        # Last index, we can't build anything from it.
        if index == len(s):
            return 0
        # Reuse.
        if index in recur_cache:
            return recur_cache[index]
        # We always have 2 options, skip symbol and don't use it.
        # Then it's left_over == +1.
        min_used: int = 1 + check(index + 1)
        # Or try to build correct word from it.
        for x in range(index + 1, len(s) + 1):
            # If we can build word presented in dictionary from it, then it's not left_overs.
            if s[index: x] in fast_dict:
                # ! minimum number of extra characters left over if you break up s optimally !
                # And we need min(left_overs) == using maximum words from dict.
                min_used = min(min_used, check(x))
        recur_cache[index] = min_used
        return min_used

    return check(0)


# Time complexity: O(n * n + m) -> for every call we're recalling with next index, and looping indexes: len(s) - index ->
# m - len of input_dictionary^^|  -> again memorization, which easy to implement but hell to count ->
# n - len of input_string^^|  -> assume case is like S = 'sssssssss', and dictionary is ['s', 's' ... 's'],
#                             then we're just traversing once with every index and reuse them => O(n) ->
#                             -> if we add ['ss', 'sss', 'ssss', etc 's * len(s)'] still we're making the call
#                             and insta return cached result, but it's still loop for (len(s) - index) times.
#                             For 0 index it's always n - 1 indexes checked times, so it's at least O(n * n).
#                             Sticking to O(n * n + m) <- where m is set(dictionary).
# Auxiliary space: O(n + m) -> saving every index_result into a dict_cache, at max there's n indexes checked => O(n) ->
#                           -> extra recreating input_dictionary into a set() => O(m) -> and recursion will have at max
#                           depth == n, cuz we're checking only indexes of input_string => O(n) -> O(2n + m).
# ----------------------
# ! if you break up s optimally ! <- Assuming that we need to use MAXIMUM of words we can take from dictionary.
# Then it's just try to build correct word from any index, and if we can't then try from next.
# Constraints are low, so it should be correct to build from anything. But can we cull some checks?
# Like we can save count for every symbol in dictionary and just ignore if there's 0 left.
# But then it could be a little bit faster for cases with unrepresented symbols in dictionary,
#  and much slower for cases when S is like 5 symbols, while dictionary is 50 words with 50 lengths.
# Cuz we could just try and build this 5 symbols for every index, but with saving it's extra traverse for every
#  word in dictionary and extra counting + we need to maintain it. Nah. Let's try just building subs from indexes.


test: str = "leetscode"
test_d: list[str] = ["leet", "code", "leetcode"]
test_out: int = 1
assert test_out == min_extra_char(test, test_d)

test = "sayhelloworld"
test_d = ["hello", "world"]
test_out = 3
assert test_out == min_extra_char(test, test_d)
