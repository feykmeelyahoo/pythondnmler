class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def printmetoend(self):
        print(self.data)
        if self.next is not None:
            self.next.printmetoend()


node6 = Node(6)
node5 = Node(5, node6)
node4 = Node(4, node5)
node3 = Node(3, node4)
node2 = Node(2, node3)
node1 = Node(1, node2)
node0 = Node(0, node1)

def Reverse(head):
    prev, curr = None, head
    while curr:
        prev, curr.next, curr = curr, prev, curr.next
    return prev

def Reverse2(head):
    lst = list()

    if head is None:
        return print()
    else:
        while head is not None:
            lst.append(head)
            head = head.next

    length = len(lst)

    if length is 1:
        return head

    node0 = None
    newHead = 0

    for i in range(length - 1):
        if i == 0:
            newHead = Node(lst[-i - 2].data)
            node0 = Node(lst[-i - 1].data, newHead)

        else:
            nextNode = Node(lst[-i - 2].data)
            newHead.next = nextNode
            newHead = newHead.next

    return node0


newHead = Reverse(node0)
newHead.printmetoend()
