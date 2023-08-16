# Given the head of a singly linked list, reverse the list, and return the reversed list.
# ---------------------
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
# ---------------------
# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?


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


def reverse_list(head: ListNode) -> ListNode:
    # working_sol (79.93%, 10.72%) -> (43ms, 22.8mb)  time: O(n) | space: O(1)
    if not head:
        return head

    def reverse(last_node: ListNode) -> tuple[ListNode, ListNode]:
        """
        :param last_node: node from who we're doing recursion call.
        :return: tuple, with last_node called and NEW starting node after reversing.
        """
        # If end is reached == set as new START and assign everything to it.
        if not last_node.next:
            start: ListNode = last_node
            return last_node, start
        if node := reverse(last_node.next):
            # Reassign, to escape inf_loop.
            last_node.next = None
            # Assign this call node to the lastly assigned node.
            node[0].next = last_node
            return node[0].next, node[1]

    return reverse(head)[1]


# Time complexity: O(n) -> traversing whole input_list once to get last_node => O(n) ->
# n - len of input_list^^| -> reassigning every node from input_list as a next_nodes for last_node we found => O(n).
# Auxiliary space: O(1) -> not creating anything, using only links to already existed nodes => O(1)
# !
# ignoring recursion stack, because there's p148 and official solution to that ignores it, calling 3 recursions O(1) !
# ---------------------
# Ok. It was harder than I expected and I can't find a way how to save, new_start after reaching END.
# Not in tuple or extra place to save, but we need to store this last node, so I guess there's no way around it.
# Tried some ways to make it link to head, or prev nodes, but it's either recursion or I get some nodes deleted.
# So either there's no way to skip this, or I don't know how, for now.
# Won't google for it, there's a lot of tasks on this matter anyway, if I stuck at one of them than google is a way.
# ---------------------
# Always solving linked_list iteratively, time to check recursion.


test: ListNode = create_linked([1, 2, 3, 4, 5])
test_out: list[int] = [5, 4, 3, 2, 1]
t_one_linked(reverse_list(test), test_out)

test = create_linked([1, 2])
test_out = [2, 1]
t_one_linked(reverse_list(test), test_out)
