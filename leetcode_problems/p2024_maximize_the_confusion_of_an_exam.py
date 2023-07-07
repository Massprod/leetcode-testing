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
    pass


test1 = "TTFF"
test1_k = 2
test1_out = 4

test2 = "TFFT"
test2_k = 1
test2_out = 3

test3 = "TTFTTFTT"
test3_k = 1
test3_out = 5
