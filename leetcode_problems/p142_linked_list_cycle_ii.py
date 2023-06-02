# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
#
# There is a cycle in a linked list if there is some node in the list that can be reached again
#   by continuously following the next pointer. Internally, pos is used to denote the index of the node
#   that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle.
# Note that pos is not passed as a parameter.
# Do not modify the linked list.
# ---------------------
# The number of the nodes in the list is in the range [0, 104].
# -105 <= Node.val <= 105
# pos is -1 or a valid index in the linked-list.
# ---------------------
# Follow up: Can you solve it using O(1) (i.e. constant) memory?


class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: ListNode = next

    def __str__(self):
        return f"{self.val} -> {self.next}"


def create_linked_with_cycle(to_link: list[int], pos: int) -> tuple[ListNode, ListNode]:
    tempo = link = ListNode()
    step: int = 0
    pos_node: ListNode | None = None
    for index in range(len(to_link)):
        tempo.val = to_link[index]
        if 0 <= pos == step:
            pos_node = tempo
        if index != (len(to_link) - 1):
            tempo.next = ListNode()
            step += 1
            tempo = tempo.next
            continue
        tempo.next = pos_node
    return link, pos_node


def detect_cycle(head: ListNode) -> ListNode | None:
    # working_sol (39.7%, 10.86%) -> (65ms, 20.7mb)  time: O(n) | space: O(n)
    if not head:
        return head
    all_nodes: dict[ListNode] = {}
    temp: ListNode = head
    while temp:
        all_nodes[temp] = True
        temp = temp.next
        if temp in all_nodes:
            return temp
    return None


# Time complexity: O(n) -> traversing whole linked list once to create dictionary
# n - len of input_list^^| and extra 1 Node to check if there's cycle, and to get node where's it starting => O(n)
# Space complexity: O(n) -> storing links for all nodes of the linked_list => O(n)
#
# ---------------------
# ! Your returned value is not a ListNode type. !
# Ok. ! If there is no cycle, return null. ! Found.
# ---------------------
# Seems working, but there's no info about what we return if there's NO cycle.
# ! Output: no cycle ! What this? By default, we're returning ListNode, so it's None or False like in p141.
# I will stick to a False like p141, but this descriptions...
# ---------------------
# !
# Do not modify the linked list. !
# Ok. Now it's time to use dictionary. Last one I know how to solve it without extra info.
# So if I hit time_limit or commit correctly I will check what O(1) space here,
# because there's some big_math again, and without extra_theory practically impossible to solve.


test1_pos = 1
test1 = create_linked_with_cycle([3, 2, 0, -4], test1_pos)
test1_out = test1[1]
assert test1_out == detect_cycle(test1[1])

test2_pos = 0
test2 = create_linked_with_cycle([1, 2], test2_pos)
test2_out = test2[1]
assert test2_out == detect_cycle(test2[0])

test3_pos = -1
test3 = create_linked_with_cycle([1], test3_pos)
test3_out = False
assert test3_out == detect_cycle(test3[0])
