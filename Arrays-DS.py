import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

retStr=""
for i in arr[::-1] :
    retStr+=str(i) + " "

print(retStr)
