# You are given an array of unique integers salary where salary[i] is the salary of the ith employee.
# Return the average salary of employees excluding the minimum and maximum salary.
# Answers within 10 ** -5 of the actual answer will be accepted.
# -----------------------------
# 3 <= salary.length <= 100  ,  1000 <= salary[i] <= 10 ** 6
# All the integers of salary are unique.


def average(salary: list[int]) -> float:
    min_sal: int = salary[0]
    max_sal: int = salary[0]
    summ_sal: int | float = 0
    for sal in salary:
        summ_sal += sal
        if sal > max_sal:
            max_sal = sal
            continue
        if sal < min_sal:
            min_sal = sal
            continue
    return (summ_sal - min_sal - max_sal) / (len(salary) - 2)


test1 = [4000, 3000, 1000, 2000]
test1_out = 2500.00000
print(average(test1))
assert test1_out == average(test1)

test2 = [1000, 2000, 3000]
test2_out = 2000.00000
print(average(test2))
assert test2_out == average(test2)
