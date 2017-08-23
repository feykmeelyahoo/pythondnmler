#!/bin/python3

# sample Input
# 5 3
# 1 2 100
# 2 5 100
# 3 4 100
import operator
from functools import reduce
import sys

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]


    def ret0(x):
        return 0


    finalDict = {}
    max = None

    for a0 in range(m):
        a, b, k = input().strip().split(' ')
        a, b, k = [int(a), int(b), int(k)]
        # print(a,b,k)

        # print(list(operator.add(k, x) for x in finalList[a - 1:b]))
        # finalList[a - 1:b] = list(operator.add(k, x) for x in finalList[a - 1:b])

        for x in range(a - 1, b):
            if finalDict.get(x) != None:
                finalDict[x] += k
            else:
                finalDict[x] = k

            if max == None or max < finalDict[x] :
                max = finalDict[x]

                # ((finalDict[x] + k) if finalDict[x] not None else k)

                # print(max(finalDict))

                # print(finalDict)

    # redVal = reduce(lambda x, y: x if x > y else y, finalDict.values())
    # print(redVal)
    print(max)
    # max("finalDict", finalDict)
