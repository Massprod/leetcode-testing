# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.
# ---------------------
# k == lists.length
# 0 <= k <= 10 ** 4
# 0 <= lists[i].length <= 500
# -10 ** 4 <= lists[i][j] <= 10 ** 4
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 10 ** 4.
from random import randint


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


def t_one_linked(to_test: ListNode, testout: list[int]) -> None:
    tempo: ListNode = to_test
    count: int = 0
    for _ in range(len(testout)):
        assert testout[_] == tempo.val
        tempo = tempo.next
        count += 1
    assert count == len(testout)


def merge_k_lists(lists: list[ListNode]) -> ListNode | None:
    # working_sol (73.66%, 77.66%) -> (92ms, 19.9mb)  time: O((n * k) * log n) | space: O(n)
    if not lists:
        return None

    def merge_sort(roots: list[ListNode]) -> ListNode:
        # Standard Merge Sort.
        if len(roots) == 1:
            return roots[0]
        middle: int = len(roots) // 2
        left: ListNode = merge_sort(roots[:middle])
        right: ListNode = merge_sort(roots[middle:])
        new_root: ListNode = ListNode(0)
        cursor: ListNode = new_root
        while left and right:
            if left.val < right.val:
                cursor.next = left
                cursor = cursor.next
                left = left.next
            else:
                cursor.next = right
                cursor = cursor.next
                right = right.next
        if left:
            cursor.next = left
        elif right:
            cursor.next = right
        return new_root.next

    return merge_sort(lists)


# Time complexity: O((n * k) * log n) <- n - length of input array 'lists',
#                                        k - average length of LinkedLists inside 'lists'.
# We divide original 'lists' into a max of (log n) parts, and the merging of all
# sublists(LinkedLists) into a single LL will take (n * k) times.
# O((n * k) * log n)
# Auxiliary space: O(n)
# Slices will be essentially with ~2n summarized size from every call.


test_pre: list[list[int]] = [[1, 4, 5], [1, 3, 4], [2, 6]]
test: list[ListNode] = [create_linked(prep) for prep in test_pre]
test_out: list[int] = [1, 1, 2, 3, 4, 4, 5, 6]
t_one_linked(merge_k_lists(test), test_out)

test_pre = []
test = [create_linked(prep) for prep in test_pre]
test_out = []
t_one_linked(merge_k_lists(test), test_out)

test_pre = [[]]
test_out = []
test = [create_linked(prep) for prep in test_pre]
t_one_linked(merge_k_lists(test), test_out)

test_pre = [sorted([randint(-10 ** 4, 10 ** 4) for _ in range(500)]) for _ in range(19)]
# print(test_pre)
test = [create_linked(prep) for prep in test_pre]
test_out = sorted([val for x in range(len(test_pre)) for val in test_pre[x]])
t_one_linked(merge_k_lists(test), test_out)
