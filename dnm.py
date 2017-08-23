import operator
from functools import reduce
import sys

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]

    tempDict = {}
    finalDict = {}
    finalSet = set()
    max = None

    for a0 in range(m):
        a, b, k = input().strip().split(' ')
        a, b, k = [int(a), int(b), int(k)]
        # print(a, b, k)

        finalSet.update([a, b])
        if tempDict.get(a, b) != None:
            tempDict[(a, b)] = k
        else:
            tempDict[(a, b)] += k

    # print(tempDict.keys())
    # print(tempDict.values())
    # print(sorted(finalSet))
    sortedSet = sorted(finalSet)
    setLength = len(sortedSet)
    dKeys = tempDict.keys()
    # dKeys = list(tempDict.keys())
    # print(type(dKeys))
    # lengthKeys = len(dKeys)
    # print("dKeys", dKeys)
    # print("dKeys[0]", dKeys[0])

    for i in range(setLength - 1):
        for dKey in dKeys:
            if sortedSet[i] <= dKey[0] and sortedSet[i + 1] > dKey[0]:
                try:
                    finalDict[sortedSet[i], sortedSet[i + 1]] += tempDict[dKey]
                except(KeyError):
                    finalDict[sortedSet[i], sortedSet[i + 1]] = tempDict[dKey]

            elif sortedSet[i] >= dKey[0] and sortedSet[i] <= dKey[1]:
                try:
                    finalDict[sortedSet[i], sortedSet[i + 1]] += tempDict[dKey]
                except(KeyError):
                    finalDict[sortedSet[i], sortedSet[i + 1]] = tempDict[dKey]

    mx = None
    # mx =reduce(max, finalDict.values())
    # print(type((finalDict.values())))
    # print(list(finalDict.values()))
    # print(max(list(finalDict.values())))
    # mx = max(list(finalDict.values()))
    for i in finalDict.keys():
        if mx != None:
            if mx < finalDict[i]:
                mx = finalDict[i]
        else:
            mx = finalDict[i]

    print(mx)
    # dKeys = tempDict.keys()
    # dKeysLen=len(dKeys)
    # for i in dKeysLen-1:
    #     for st in sortedSet:
    #         if dKeys[i][0] >= st:

    # keys = list(tempDict.keys())
    # print(keys)
    # length = len(keys)
    # if length > 0:
    #     for i in range(length):
    #         if a == keys[i][0]:
    #             if b == keys[i][1]:
    #                 tempDict[a, b] += k;
    #             elif b < keys[i][1]:
    #                 temp = tempDict[keys[i][1]]
    #                 del tempDict[keys[i]]
    #                 tempDict[a, b] = temp + k
    #                 tempDict[b, keys[1]] = k
    #             elif b > keys[i][1]:
    #                 temp = tempDict[keys[i][1]]
    #                 tempDict[a, keys[i][1]] = temp + k
    #                 tempDict[keys[i][1], b] = k
    #         elif a < keys[i][0]:
    #
    #
    # else:
    #     tempDict[a, b] = k
