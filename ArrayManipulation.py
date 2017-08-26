import operator
from functools import reduce
import sys

# if __name__ == "__main__":
#     n, m = input().strip().split(' ')
#     n, m = [int(n), int(m)]
#
#     finalDict = {}
#     finalSet = set()
#     max = None
#
#     for a0 in range(m):
#         a, b, k = input().strip().split(' ')
#         a, b, k = [int(a), int(b), int(k)]
#         # print(a, b, k)
#
#         list = sorted(finalSet)
#         length= len(list)
#         for i in range(length-1):
#             if a < list[i] :
#                 finalSet.update(a)
#                 finalDict[a]=k
#                 if b< list[i]:
#                     finalSet.update(b)
#                     finalDict[a] = k
#
#         if a in finalSet:
#             finalDict[a]+=k
#
#         #
#         # finalSet.update([a, b])
#         # if finalDict.get(a) == None:
#         #     finalDict[a] = k
#         # else:
#         #     finalDict[a] += k
#
#
# print(finalSet)
# print(finalDict.items())

from itertools import accumulate

n, m = map(int, input().split(' '))
# dx = [0] * (n + 1)  # allow run past end
dx = [1111] * 10**9  # allow run past end

for _ in range(m):
    a, b, c = map(int, input().split(' '))
    dx[a - 1] += c
    dx[b] -= c

print(max(accumulate(dx)))


def InsertNth(head, data, position):

    if head is None: # position must be 0
        return Node(data, None)

    if position == 0:
        return Node(data, head)

    prevNode = head
    for _ in range(position-1):
        prevNode = prevNode.next
    prevNode.next = Node(data, prevNode.next)
    return head