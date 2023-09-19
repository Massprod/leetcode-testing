# You are given two integers m and n, which represent the dimensions of a matrix.
# You are also given the head of a linked list of integers.
# Generate an m x n matrix that contains the integers in the linked list
#  presented in spiral order (clockwise), starting from the top-left of the matrix.
# If there are remaining empty spaces, fill them with -1.
# Return the generated matrix.
# -------------------
# 1 <= m, n <= 10 ** 5
# 1 <= m * n <= 10 ** 5
# The number of nodes in the list is in the range [1, m * n].
# 0 <= Node.val <= 1000


class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: ListNode = next

    def __str__(self):
        return f"{self.val} -> {self.next}"


def create_linked(to_link: list[int]) -> ListNode:
    tempo = link = ListNode()
    for index in range(len(to_link)):
        tempo.val = to_link[index]
        if index != (len(to_link) - 1):
            tempo.next = ListNode()
            tempo = tempo.next
    return link


def spiral_matrix(m: int, n: int, head: ListNode) -> list[list[int]]:
    # working_sol (19.28%, 51.67%) -> (1204ms, 68mb)  time: O(n * m) | space: O(n * m)
    matrix: list[list[int]] = [[-1 for _ in range(n)] for _ in range(m)]
    all_steps: int = m * n
    max_y: int = m - 1
    max_x: int = n - 1
    min_y: int = 0
    min_x: int = 0
    steps: int = 1
    x: int = 0
    dx: int = 1
    y: int = 0
    dy: int = 0
    # Only 1 column.
    if max_x == 0:
        dx = 0
        dy = 1
    if head:
        matrix[y][x] = head.val
        head = head.next
    else:
        matrix[y][x] = -1
    steps += 1
    turn: int = 0
    while steps <= all_steps:
        if turn == 3:
            min_y += 1
            max_y -= 1
            turn += 1
        if turn == 5:
            min_x += 1
            max_x -= 1
            turn = 0
        x += dx
        y += dy
        if head:
            matrix[y][x] = head.val
            head = head.next
        else:
            matrix[y][x] = -1
        # Up.
        if x == max_x and dy == 0 and dx == 1:
            turn += 1
            dy = 1
            dx = 0
        # Left.
        elif y == max_y and dx == 0 and dy == 1:
            turn += 1
            dy = 0
            dx = -1
        # Down.
        elif x == min_x and dy == 0 and dx == -1:
            turn += 1
            dy = -1
            dx = 0
        # Right.
        elif y == min_y and dx == 0 and dy == -1:
            turn += 1
            dy = 0
            dx = 1
        steps += 1
    return matrix


# Time complexity: O(n * m) -> using every cell and creating matrix => O(2 * (n * m))
# n - row len of matrix^^|
# m - col len of matrix^^|
# Auxiliary space: O(n * m) -> matrix with size == (n * m) => O(n * m).


test: ListNode = create_linked([3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0])
test_m: int = 3
test_n: int = 5
test_out: list[list[int]] = [[3, 0, 2, 6, 8], [5, 0, -1, -1, 1], [5, 2, 4, 9, 7]]
assert test_out == spiral_matrix(test_m, test_n, test)

test = create_linked([0, 1, 2])
test_m = 1
test_n = 4
test_out = [[0, 1, 2, -1]]
assert test_out == spiral_matrix(test_m, test_n, test)

test = create_linked([8, 24, 5, 21, 10, 11, 11, 12, 6, 17])
test_m = 10
test_n = 1
test_out = [[8], [24], [5], [21], [10], [11], [11], [12], [6], [17]]
assert test_out == spiral_matrix(test_m, test_n, test)
