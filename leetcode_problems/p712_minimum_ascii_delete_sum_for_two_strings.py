# Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.
# --------------
# 1 <= s1.length, s2.length <= 1000
# s1 and s2 consist of lowercase English letters.
from string import ascii_lowercase
from random import choice


def minimum_delete_sum(s1: str, s2: str) -> int:
    # working_sol (36.60%, 20.68%) -> (972ms, 201.7mb)  time: O((log n) * 3 ** n) | space: O(3 ** n)
    rec_cache: dict[tuple[int, int], int] = {}

    def delete_symbol(s1_index: int, s2_index: int) -> int:
        if (s1_index, s2_index) in rec_cache:
            return rec_cache[s1_index, s2_index]
        if s1_index < 0:
            cur_sum: int = 0
            for _ in range(s2_index + 1):
                cur_sum += ord(s2[_])
            rec_cache[s1_index, s2_index] = cur_sum
            return cur_sum
        if s2_index < 0:
            cur_sum = 0
            for _ in range(s1_index + 1):
                cur_sum += ord(s1[_])
            rec_cache[s1_index, s2_index] = cur_sum
            return cur_sum
        if s1[s1_index] == s2[s2_index]:
            return delete_symbol(s1_index - 1, s2_index - 1)
        min_sum: int = min(
            ord(s1[s1_index]) + delete_symbol(s1_index - 1, s2_index),
            ord(s2[s2_index]) + delete_symbol(s1_index, s2_index - 1)
        )
        rec_cache[s1_index, s2_index] = min_sum
        return min_sum

    return delete_symbol(len(s1) - 1, len(s2) - 1)


# Time complexity: O((log n) * 3 ** n) -> recursion tree with depth of n and 3 options => O(3 ** n) ->
# n - highest length of input strings^^| -> and every call is ending with negative value of index, so we're extra
#                       traverse some part from one of the input_strings, actually in the worst case ->
#                       -> if we're only taking -1 from lowest length input_string and there's no duplicates in s2,
#                       it's going to leave us with full traverse of longest input_string => O(n * 3 ** n) ->
#                       -> but it should be only once and else is just a part of them, extra we're saving calls,
#                       so it's mostly going to be reused, dunno how to calc it correctly, maybe smth =>
#                       => O((log n) * 3 ** n).
# Auxiliary space: O(3 ** n) -> every call is stored in cache(dict) => O(3 ** n).
# --------------
# Ok. Minimum_value we can delete is always should leave MOST of the original string in place, so it should be
# problem to find maximum_substring presented in both.
# For this we can just delete elements one by one right to left, and skip same symbols.
# Every symbol deleted is counted and if 1 string is exhausted while other is still presented we can just delete
# everything from it, cuz every equal symbol is already skipped.
# Counted everything deleted from both_strings and find min() from all options.
# Cuz we either skip if equal or delete 1 symbol from one of the strings.
# One by one deleting guess is best, cuz we're not going to skip any symbols.
# And as before its DP problem even in HINTS they say it, so I will build recursion with cache.
# Cuz I will never build DP without recursion first.


test1_s1 = "sea"
test1_s2 = "eat"
test1_out = 231
assert test1_out == minimum_delete_sum(test1_s1, test1_s2)

test2_s1 = "delete"
test2_s2 = "leet"
test2_out = 403
assert test2_out == minimum_delete_sum(test2_s1, test2_s2)

test3_s1 = "tsiirurobgldgpdfthhkuelgbnzkpnpgteuxcapyewxtvscncotdzwuxsbtggyqjbipaquii" \
           "nchsqipzrjbounifofofihwxniyixkxlwhamikdvjwdkknibfepsmkypdqdzqumptmsvdtbn" \
           "ttznwyooapzrokcxufcwdjyfwydearfuabkzlqsweqfqbuxwbwmnlatbxkoctgnacfccgbru" \
           "blqpbwxwnyuimiieoufjvvegfxomqrqmqjlkwzexjwisevkhcfmsnvbfembvibqtpmsmlgep" \
           "ujrmzvbkfpiqdpmkfwvrkdlamrucnvsshtfmsnkjzdyaw"
test3_s2 = "deuxwmwghadjxpauhbkjuiiscdpiqjxevkekqilbkunxoyzpkjxojeusbzgxgslblpmbbmjn" \
           "neejobqpdqedqqlbnjjrvyjiyooouanetfscgcveerdavwabvjclosofveuvpuuujmkkipyc" \
           "mndjusimefltwhqnmnjnpujrxsdmetynsctnzueiliaaogzwwvflekjehetlxtvsjlxfxybl" \
           "mhhjepuitrozitlusrragebqdxrgaadfdgclngyaittisltwqkntxhstkhzlmfnfwjhmleot" \
           "njqywkyecvwgotodckhbqbmlkkkuxrzvkxovvfsmnwnag"
test3_out = 49848
assert test3_out == minimum_delete_sum(test3_s1, test3_s2)

# test4 -> failed -> I was checking if symbols on s1_index == s2_index, which isn't correct, cuz
#                    when index goes to negative it can trigger this again [-1] == [2] like that,
#                    and because of that it was recalling with [-2] etc. And getting wrong indexes to check.
#                    So we need to check first if indexes are Negative and this already mean we can cull
#                    other string to 0, cuz 1 of them is exhausted and no symbols left to match.
test4_s1 = "xnbteodleejrzeo"
test4_s2 = "gaouojqkkk"
test4_out = 2255
assert test4_out == minimum_delete_sum(test4_s1, test4_s2)

test: str = ""
for _ in range(999):
    test += choice(ascii_lowercase)
print(test)
