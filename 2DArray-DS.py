#!/bin/python3

import sys
import numpy

arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)

def findHourglass(arr2d):
    rowL = len(arr2d)
    columnL = len(arr2d[0])

    retArr=[]

    for i in range(rowL):
        for j in range (columnL):
            if i==1:
                retArr.append(arr2d[1][1])
                break
            retArr.append(arr2d[i][j])

    return sum(retArr)

nArr= numpy.array(arr)
rowL = len(nArr)
columnL = len(nArr[0])
max=None;
for i in range(rowL-2):
    for j in range(columnL-2):
        newVal=findHourglass(nArr[i:i + 3, j:j + 3])
        if max == None or max < newVal:
            max = newVal



print(max)
