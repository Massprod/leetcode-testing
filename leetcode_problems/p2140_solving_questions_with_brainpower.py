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
    if len(questions) == 1:
        return questions[0][0]
    used: set[int] = set()
    used_values: dict = {}
    path: list[int] = []

    def count_points(start: int, cur_max_points: int = 0) -> int:
        cur_max_points += questions[start][0]
        for g in range(start + questions[start][1] + 1, len(questions)):
            path.append(count_points(g, cur_max_points))
            used.add(g)
            used_values[g] = questions[start][0]
        return cur_max_points

    for x in range(len(questions)):
        cur_points: int = questions[x][0]
        for y in range(x + questions[x][1] + 1, len(questions)):
            if y not in used or questions[x][0] > used_values[y]:
                path.append(count_points(y, cur_points))
                used.add(y)
                used_values[y] = cur_points
    if len(path) != 0:
        return max(path)
    return max(questions)[0]


# Ok. Made this with skipping second step values if we already started from them  with values higher this current step.
# But how to skip all other with including previous?
# -------------------------
# Correct solution, but time_limit what can I cull?
# -------------------------
# Recursion like with counting best steps/jumps?


test1 = [[3, 2], [4, 3], [4, 4], [2, 5]]
test1_out = 5
print(most_points(test1))

test2 = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
test2_out = 7
print(most_points(test2))

test3 = [[1, 1], [3, 2], [1, 3], [5, 2], [6, 4], [4, 1], [2, 1], [1, 1]]
print(most_points(test3))

test4 = [
    [21, 2], [1, 2], [12, 5], [7, 2], [35, 3], [32, 2], [80, 2], [91, 5], [92, 3], [27, 3], [19, 1], [37, 3], [85, 2],
    [33, 4], [25, 1], [91, 4], [44, 3], [93, 3], [65, 4], [82, 3], [85, 5], [81, 3], [29, 2], [25, 1], [74, 2],
    [58, 1], [85, 1], [84, 2], [27, 2], [47, 5], [48, 4], [3, 2], [44, 3], [60, 5], [19, 2], [9, 4], [29, 5], [15, 3],
    [1, 3], [60, 2], [63, 3], [79, 3], [19, 1], [7, 1], [35, 1], [55, 4], [1, 4], [41, 1], [58, 5],
]
print(most_points(test4))

test5 = [[12, 46], [78, 19], [63, 15], [79, 62], [13, 10]]
print(most_points(test5))
