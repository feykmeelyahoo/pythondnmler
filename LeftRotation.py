#!/bin/python3

import sys


def leftRotation(a, d):
    length = len(a)
    firstArr = a[d:length]
    secondArr= a[:d]
    return firstArr + secondArr



if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    a = list(map(int, input().strip().split(' ')))
    result = leftRotation(a, d)
    print(" ".join(map(str, result)))
