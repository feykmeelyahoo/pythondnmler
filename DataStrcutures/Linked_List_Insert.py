"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as
"""


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def printmetoend(self):
        print(self.data)
        if self.next is not None:
            self.next.printmetoend()


                # return back the head of the linked list in the below method.


node6 = Node(6, None)
node5 = Node(5, node6)
node4 = Node(4, node5)
node3 = Node(3, node4)
node2 = Node(2, node3)
node1 = Node(1, node2)
node0 = Node(0, node1)


# This is a "method-only" submission.
# You only need to complete this method.
def InsertNth(head, data, position):
    newHead = head
    if head is None:
        return Node(data, None)
    elif position == 0:
        return Node(data, head)
    else:
        for _ in range(position - 1):
            newHead = newHead.next

        newHead.next = Node(data, newHead.next)

    return head

myHead=InsertNth(node0, 55, 3)

myHead.printmetoend()