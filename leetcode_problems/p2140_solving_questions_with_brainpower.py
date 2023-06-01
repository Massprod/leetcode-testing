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
    # googled_sol (73.48%, 87.2%) -> (1625ms, 62.5mb)  time: O(n) | space: O(n)
    if len(questions) == 1:
        return questions[0][0]
    dynamic: list[int] = [0 for _ in range(len(questions))]
    dynamic[-1] = questions[-1][0]
    for x in range(len(questions) - 2, -1, -1):
        dynamic[x] = questions[x][0]
        skip: int = questions[x][1]
        if x + skip + 1 < len(questions):
            dynamic[x] += dynamic[x + skip + 1]
        dynamic[x] = max(dynamic[x], dynamic[x + 1])
    return dynamic[0]


# Time complexity: O(n) -> traversing input list once => O(n)
# n - len of input list^^|
# Space complexity: O(n) -> extra list of input_list size => O(n)
# --------------------
# Ok. Time to stop jumping on next_solution_key, and return to normal flow like before,
# otherwise I will be wasting time and forced to google.
# And there's no reason to learn it if I can't do this myself.
# full description => https://leetcode.com/problems/solving-questions-with-brainpower/editorial/


test1 = [[3, 2], [4, 3], [4, 4], [2, 5]]
test1_out = 5
print(most_points(test1))
assert test1_out == most_points(test1)

test2 = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
test2_out = 7
print(most_points(test2))
assert test2_out == most_points(test2)

test3 = [[1, 1], [3, 2], [1, 3], [5, 2], [6, 4], [4, 1], [2, 1], [1, 1]]
test3_out = 9
print(most_points(test3))
assert test3_out == most_points(test3)

test4 = [
    [21, 2], [1, 2], [12, 5], [7, 2], [35, 3], [32, 2], [80, 2], [91, 5], [92, 3], [27, 3], [19, 1], [37, 3], [85, 2],
    [33, 4], [25, 1], [91, 4], [44, 3], [93, 3], [65, 4], [82, 3], [85, 5], [81, 3], [29, 2], [25, 1], [74, 2],
    [58, 1], [85, 1], [84, 2], [27, 2], [47, 5], [48, 4], [3, 2], [44, 3], [60, 5], [19, 2], [9, 4], [29, 5], [15, 3],
    [1, 3], [60, 2], [63, 3], [79, 3], [19, 1], [7, 1], [35, 1], [55, 4], [1, 4], [41, 1], [58, 5],
]
test4_out = 781
print(most_points(test4))
assert test4_out == most_points(test4)

test5 = [[12, 46], [78, 19], [63, 15], [79, 62], [13, 10]]
test5_out = 79
print(most_points(test5))
assert test5_out == most_points(test5)

test6 = [
    [72, 5], [36, 5], [95, 5], [50, 1], [62, 1], [14, 3], [72, 5], [86, 2], [43, 3], [51, 3], [14, 1], [91, 5],
    [47, 4], [72, 4], [63, 5], [40, 3], [68, 1], [8, 3], [84, 5], [7, 5], [40, 1], [35, 3], [66, 2], [39, 5], [40, 1],
    [92, 3], [67, 5], [34, 3], [84, 4], [75, 5], [6, 1], [71, 3], [77, 3], [25, 3], [53, 3], [32, 3], [88, 5], [18, 2],
    [21, 3], [78, 2], [69, 5], [45, 4], [94, 2], [70, 1], [85, 2], [7, 2], [68, 4], [71, 4], [57, 2], [12, 5], [53, 5],
    [51, 3], [46, 1], [28, 3]
]
test6_out = 845
print(most_points(test6))
assert test6_out == most_points(test6)
