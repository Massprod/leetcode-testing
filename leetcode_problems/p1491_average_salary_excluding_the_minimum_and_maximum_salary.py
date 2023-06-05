# You are given an array of unique integers salary where salary[i] is the salary of the ith employee.
# Return the average salary of employees excluding the minimum and maximum salary.
# Answers within 10 ** -5 of the actual answer will be accepted.
# -----------------------------
# 3 <= salary.length <= 100  ,  1000 <= salary[i] <= 10 ** 6
# All the integers of salary are unique.


def average(salary: list[int]) -> float:
    # working_sol (91.96%, 91.73%) -> (37ms, 16.2mb)  time: O(n) | space: O(1)
    min_sal: int = salary[0]
    max_sal: int = salary[0]
    summ_sal: int = 0
    for sal in salary:
        summ_sal += sal
        if sal > max_sal:
            max_sal = sal
            continue
        if sal < min_sal:
            min_sal = sal
            continue
    return (summ_sal - min_sal - max_sal) / (len(salary) - 2)


# Time complexity: O(n) -> traversing whole input_list once => O(n)
# n - len of input_list^^|
# Auxiliary space: O(1) -> 3 extra constants, all INTs -> O(1)


test1 = [4000, 3000, 1000, 2000]
test1_out = 2500.00000
print(average(test1))
assert test1_out == average(test1)

test2 = [1000, 2000, 3000]
test2_out = 2000.00000
print(average(test2))
assert test2_out == average(test2)
