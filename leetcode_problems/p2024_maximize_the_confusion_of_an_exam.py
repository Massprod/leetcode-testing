# A teacher is writing a test with n true/false questions,
#  with 'T' denoting true and 'F' denoting false.
# He wants to confuse the students by maximizing the number of consecutive questions
#  with the same answer (multiple trues or multiple falses in a row).
# You are given a string answerKey, where answerKey[i] is the original answer to the ith question.
# In addition, you are given an integer k, the maximum number of times you may perform the following operation:
#   Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').
# Return the maximum number of consecutive 'T's or 'F's in the answer key
#  after performing the operation at most k times.
# --------------------------
# n == answerKey.length
# answerKey[i] is either 'T' or 'F'
# 1 <= n <= 5 * 10 ** 4  ,  1 <= k <= n


def max_consecutive_answers(answerKey: str, k: int) -> int:
    # working_sol (66.16%, 55.49%) -> (413ms, 16.8mb)  time: O(n) | space: O(1)
    length: int = len(answerKey)
    if length == 1:
        return 1
    left: int = 0
    right: int = 0
    max_sub: int = 0
    f_count: int = 0
    t_count: int = 0
    while right != length:
        if answerKey[right] == "T":
            t_count += 1
        elif answerKey[right] == "F":
            f_count += 1
        while min(f_count, t_count) > k:
            if answerKey[left] == "T":
                t_count -= 1
            elif answerKey[left] == "F":
                f_count -= 1
            left += 1
        max_sub = max(max_sub, (right - left) + 1)
        right += 1
    return max_sub


# Time complexity: O(n) -> standard sliding windows with traversing whole input_array once with right limit => O(n) ->
# n - len of answerKey^^| -> and closing left_limit in the worst case like TTFTTFF and k = 1,
#                            then we will visit n - (k * 2) indexes => O(n - (k * 2)) -> O(n) + O(n - (k * 2)) => O(n).
# Auxiliary space: O(1) -> only constants used, none of them depends on input => O(1).
# --------------------------
# Window problem again.
# Only problem I can't see how we can manage both options together?
# Like we can do one traverse to get max_sub with all T, and another to get F.
# What we can maintain together? Minimum appearances?
# Like if we know that there's only 2 options T or F, then we can maintain MIN(t, f).
# Because if one option exceeds limit of k, then another is either in k limit, and we can flip it.
# Or it will exceed as well, but they should never exceed together,
#  and we can shrink window until at least one is in limit.
# If it's in limit than it can be flipped, and we will get correct sub_array.


test1 = "TTFF"
test1_k = 2
test1_out = 4
print(max_consecutive_answers(test1, test1_k))
assert test1_out == max_consecutive_answers(test1, test1_k)

test2 = "TFFT"
test2_k = 1
test2_out = 3
print(max_consecutive_answers(test2, test2_k))
assert test2_out == max_consecutive_answers(test2, test2_k)

test3 = "TTFTTFTT"
test3_k = 1
test3_out = 5
print(max_consecutive_answers(test3, test3_k))
assert test3_out == max_consecutive_answers(test3, test3_k)

test4 = "T"
test4_k = 100
test4_out = 1
print(max_consecutive_answers(test4, test4_k))
assert test4_out == max_consecutive_answers(test4, test4_k)
