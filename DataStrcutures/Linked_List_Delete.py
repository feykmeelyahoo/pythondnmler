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


node6 = Node(6)
node5 = Node(5, node6)
node4 = Node(4, node5)
node3 = Node(3, node4)
node2 = Node(2, node3)
node1 = Node(1, node2)
node0 = Node(0, node1)


# This is a "method-only" submission.
# You only need to complete this method.

def Delete(head, position):
    if position == 0:
        return head.next
    else:
        curr_node = head
        for _ in range(position):
            prev_node = curr_node
            curr_node = curr_node.next
        prev_node.next = curr_node.next
    return head

def Delete2(head, position):
    if head is None:
        return None
    elif position == 0 and head.next is not None:
        return Node(head.next.data, head.next.next)

    nodeToDel = head
    curNode = nodeToDel

    for _ in range(position):
        curNode = nodeToDel
        nodeToDel = nodeToDel.next

        #    nodeToDel=Node(nodeToDel.next.data,nodeToDel.next)

    if nodeToDel.next is not None:
        nodeToDel = Node(nodeToDel.next.data, nodeToDel.next.next)
    else:
        nodeToDel = None

    curNode.next = nodeToDel

    return head


# newHead = Delete2(node0, 6)
#
# newHead.printmetoend()
# newHead = Delete2(newHead, 0)

def ReversePrint(head):
    lst=list()
    if head is None:
        return
    else:
        while head is not None:
            lst.append(head.data)
            head=head.next
        aa = (print(x) for x in lst[::-1])

        for i in aa:
            i


ReversePrint(node0)



