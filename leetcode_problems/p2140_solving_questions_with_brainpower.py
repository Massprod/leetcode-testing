# You are given a 0-indexed 2D integer array questions where questions[i] = [pointsi, brainpoweri].
# The array describes the questions of an exam, where you have to process the questions in order
#   (i.e., starting from question 0) and make a decision whether to solve or skip each question.
# Solving question i will earn you pointsi points, but you will be unable
#   to solve each of the next brainpoweri questions. If you skip question i,
#   you get to make the decision on the next question.
# Return the maximum points you can earn for the exam.
# ------------------------
# 1 <= questions.length <= 105  ,  questions[i].length == 2  ,  1 <= pointsi, brainpoweri <= 105


def most_points(questions: list[list[int]]) -> int:
    pass


test1 = [[3, 2], [4, 3], [4, 4], [2, 5]]
test1_out = 5

test2 = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
test2_out = 7
