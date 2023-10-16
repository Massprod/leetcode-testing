# Given an integer rowIndex, return the rowIndex (0-indexed) row of the Pascal's triangle.
# -----------------
# Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
# -----------------
# 0 <= rowIndex <= 33


def get_row(rowIndex: int) -> list[int]:
    # working_sol (68.36%, 82.18%) -> (37ms, 16.2mb)  time: O(n * k) | space: O(n + 1)
    if rowIndex == 0:
        return [1]
    if rowIndex == 1:
        return [1, 1]
    row: list[int] = [1, 2, 1]
    cur_row: int = 2
    while cur_row != rowIndex:
        # Last element is always '1'.
        for x in range(len(row) - 1):
            row[x] = row[x] + row[x + 1]
        # First element is always '1'.
        row = [1] + row
        cur_row += 1
    return row


# Time complexity: O(n * k) -> always creating a 'row' with (k + 1) elements with loop, where k == cur_row ->
# n - input value 'rowIndex'^^| -> every row elements in pascal_triangle == (row_index + 1) => O(n * k).
# k - currently existing row we increment^^|
# Auxiliary space: O(n + 1) -> using only 1 array to calculate all rows for follow up and maximum elements on the row
#                              is always equal to (row_index + 1) => O(n + 1).


test: int = 3
test_out: list[int] = [1, 3, 3, 1]
assert test_out == get_row(test)

test = 0
test_out = [1]
assert test_out == get_row(test)

test = 1
test_out = [1, 1]
assert test_out == get_row(test)

test = 33
test_out = [
    1, 33, 528, 5456, 40920, 237336, 1107568, 4272048, 13884156, 38567100, 92561040, 193536720, 354817320, 573166440,
    818809200, 1037158320, 1166803110, 1166803110, 1037158320, 818809200, 573166440, 354817320, 193536720, 92561040,
    38567100, 13884156, 4272048, 1107568, 237336, 40920, 5456, 528, 33, 1
]
assert test_out == get_row(test)
