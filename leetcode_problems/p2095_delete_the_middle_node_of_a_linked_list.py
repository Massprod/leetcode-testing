# You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.
# The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing,
#   where ⌊x⌋ denotes the largest integer less than or equal to x.
# For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
# --------------------------
# The number of nodes in the list is in the range [1, 10 ** 5].
# 1 <= Node.val <= 10 ** 5


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


def delete_middle(head: ListNode) -> ListNode:
    # working_sol (91.30%, 60.8%) -> (1669ms, 63mb)  time: O(n) | space: O(n)
    temp: ListNode = head
    nodes: list[ListNode] = []
    while temp:
        nodes.append(temp)
        temp = temp.next
    middle: int = int(len(nodes) / 2)
    if middle == 0:
        head = head.next
        return head
    if middle == 1:
        nodes[middle - 1].next = nodes[middle].next
        return head
    nodes[middle - 1].next = nodes[middle + 1]
    return head


# Time complexity: O(n) -> traversing whole input_linked_list once => O(n) ->
# n - nodes in input_list^^| -> deleting middle node => O(1) -> O(n).
# Auxiliary space: O(n) -> storing links to every node in a list of n size => O(n)
# --------------------------
# Don't actually understand why they're giving us a hint about tort_hare method, because we're
# going to travel all linked_list anyway and how it's faster to find middle with that?
# Especially if we're using this method we need to hold not only tortoise but node before it,
# and in cases of lists of 1 node, hare is insta error because it's node.next == None.
# It's cleaner and simpler just to create list of all, and find middle after.
# But it's taking O(n) space, tortoise will give us O(1), cuz we could hold only 3 links of nodes:
#   middle_node(tortoise), prev_middle_node, last_node(hare).
# So I guess for a future use I will remember that. But in this case we're not restricted to that.
# --------------------------
# Don't see how it's medium task, either it's some trick or strict TimeLimit.
# Taking a HINT, and I suppose it's TimeLimit because they're saying to use tortoise_hare method.
# Actually let's try to just use list, because there's no restriction on space, and why bother with
# extra check on lists of size 1 and other minors.


test1 = create_linked([1, 3, 4, 7, 1, 2, 6])
test1_out = [1, 3, 4, 1, 2, 6]
delete_middle(test1)
t_one_linked(test1, test1_out)

test2 = create_linked([1, 2, 3, 4])
test2_out = [1, 2, 4]
delete_middle(test2)
t_one_linked(test2, test2_out)

test3 = create_linked([2, 1])
test3_out = [2]
delete_middle(test3)
t_one_linked(test3, test3_out)

test4 = create_linked([1, 2, 3])
test4_out = [1, 3]
delete_middle(test4)
t_one_linked(test4, test4_out)
