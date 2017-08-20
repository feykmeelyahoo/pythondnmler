list = [1, 33 ,2, 44, 4, 2, 0, 11]
cplist1= list
cplist2= list[:]
cplist2[1]="Serkan"
print(cplist1 is list)
print(cplist2 is list)

print(list, cplist1, cplist2)

print(list[::1])
print(list[::2])
print(list[::3])
print(list[::-1])
print(list[::-2])
print(list[::-3])

dnm = ["    10  1 1 23 44        ".split()]
print(dnm)