# You are given the head of a linked list, and an integer k.
# Return the head of the linked list after swapping the values of the kth node from the beginning
#   and the kth node from the end (the list is 1-indexed).
# ----------------------
# The number of nodes in the list is n.
# 1 <= k <= n <= 10 ** 5  ,  0 <= Node.val <= 100


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


def swap_nodes(head: ListNode, k: int) -> ListNode:
    # working_sol (75.95%, 34.80%) -> (952ms, 50.9mb)  time: O(n) | space: O(n)
    if not head:
        return head
    all_nodes: list[ListNode] = [0]  # for 1 indexed
    tempo: ListNode = head
    while tempo:
        all_nodes.append(tempo)
        tempo = tempo.next
    all_nodes[k].val, all_nodes[-k].val = all_nodes[-k].val, all_nodes[k].val
    return head


# Time complexity: O(n) -> traversing input_list once, and creating list with links to every node => O(n)
# n - number of nodes in input_list^^|
# Auxiliary space: O(n) -> extra list with all links to a nodes of input_list => O(n)
# ----------------------
# No info about correct input, guess this is why it's medium.
# Because what if k == 3, and list is having 1 node?
# !
# The number of nodes in the list is n.  1 <= k <= n <= 10 ** 5 !
# Ok. It's fine.
# ----------------------
# No limitations, jus save whole list and swap k nodes in a list, append is O(1) get index is O(1),
# should be enough.


test1 = [1, 2, 3, 4, 5]
test1_k = 2
test1_out = [1, 4, 3, 2, 5]
test1_linked = create_linked(test1)
test = swap_nodes(test1_linked, test1_k)
t_one_linked(test, test1_out)
del test

test2 = [7, 9, 6, 6, 7, 8, 3, 0, 9, 5]
test2_k = 5
test2_out = [7, 9, 6, 6, 8, 7, 3, 0, 9, 5]
test2_linked = create_linked(test2)
test = swap_nodes(test2_linked, test2_k)
t_one_linked(test, test2_out)
del test
