#!/bin/python3

import sys

arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)


def findHourglass(arr2d):
    print(arr2d)
    rowL = len(arr2d)
    columnL = len(arr2d[0])

    retArr = []

    for i in range(rowL):
        for j in range(columnL):
            if i == 1:
                retArr.append(arr2d[1][1])
                break
            retArr.append(arr2d[i][j])

    print(retArr)
    print(sum(retArr))
    return sum(retArr)


rowL = len(arr)
columnL = len(arr[0])
max = None;
gonderArr = []
for i in range(rowL - 2):
    for k in range(columnL - 2):
        gonderArr = arr[i:i + 3]
        for j in range(3):
            gonderArr[j] = (gonderArr[j])[k:k + 3]
        newVal = findHourglass(gonderArr)
        if max == None or max < newVal:
            max = newVal

print(max)
