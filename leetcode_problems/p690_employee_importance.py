# You have a data structure of employee information,
#  including the employee's unique ID, importance value, and direct subordinates' IDs.
# You are given an array of employees employees where:
#  - employees[i].id is the ID of the ith employee.
#  - employees[i].importance is the importance value of the ith employee.
#  - employees[i].subordinates is a list of the IDs
#    of the direct subordinates of the ith employee.
# Given an integer id that represents an employee's ID,
#  return the total importance value of this employee
#  and all their direct and indirect subordinates.
# --------------------
# 1 <= employees.length <= 2000
# 1 <= employees[i].id <= 2000
# All employees[i].id are unique.
# -100 <= employees[i].importance <= 100
# One employee has at most one direct leader and may have several subordinates.
# The IDs in employees[i].subordinates are valid IDs.
from functools import cache


class Employee:
    def __init__(self, id: int, importance: int, subordinates: list[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


def get_importance(employees: list[Employee], id: int) -> int:
    # working_sol (46.75%, 12.33%) -> (119ms, 19.10mb)  time: O(n) | space: O(n)
    # { id: employee }
    fast_emps: dict[int, Employee] = {
        emp.id: emp for emp in employees
    }
    # Standard backtrack.
    @cache
    def dfs(id: int) -> int:
        nonlocal fast_emps

        employee: Employee = fast_emps[id]
        if not employee.subordinates:
            return employee.importance
        
        importance_sum: int = employee.importance
        for sub_id in employee.subordinates:
            importance_sum += dfs(sub_id)
        
        return importance_sum

    out: int = dfs(id)
    return out


# Time complexity: O(n) <- number of all Workers
# In the worst case, we're given `id` of a main worker which have every1 else as 
#  an employee => we will use every1 of them, once => O(n).
# --------------------
# Auxiliary space: O(n).
# `fast_emps` <- allocates space for each unique employee from `employees` => O(n).
# `@cache` <- allocates space for each unique call, and in the worst case `n`=> O(2 * n).


test: list[Employee] = [
    Employee(1, 5, [2, 3]),
    Employee(2, 3, []),
    Employee(3, 3, [])
]
test_id: int = 1
test_out: int = 11
assert test_out == get_importance(test, test_id)

test = [
    Employee(1, 5, [5]),
    Employee(5, -3, [])
]
test_id = 5
test_out = -3
assert test_out == get_importance(test, test_id)
