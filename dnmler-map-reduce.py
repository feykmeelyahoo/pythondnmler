from functools import reduce

a = list(map(lambda x: x * 5, [1, 45, 24, 17, 99, 111]))

print(a)

aa = set(filter(lambda x: x < 55, [1, 45, 24, 17, 99, 111, 24, 17, 99, 111]))

print("aa = ", aa)


def square(x):
    return (x ** 2)


def cube(x):
    return (x ** 3)


funcs = [square, cube]
for r in range(5):
    value = map(lambda x: x(r), funcs)
    print(list(value))

print(list(map(pow, [2, 3, 4], [2, 5, 3])))

# m = [1,2,3]
# n = [1,4,9]
# new_tuple = tuple(map(None, m, n)) # Python3de olmuyo callabale degil
#
# print("new_tuple", new_tuple)

a = [12, 32, 3, 55, 71, 9]
b = [12, 32, 55, 6, 71, 8]
print([x for x in a if x in b])
print([x for x in a if x not in b])

print("myreduce")


def myreduce(fnc, seq):
    tally = seq[0]
    for next in seq[1:]:
        tally = fnc(tally, next)
    return tally


print(myreduce((lambda x, y: x * y), [1, 2, 3, 4]))

L = ['Testing ', 'shows ', 'the ', 'presence', ', ', 'not ', 'the ', 'absence ', 'of ', 'bugs']

print(reduce((lambda x, y: x + y), L))


mysum = lambda x, y: x + y

print(reduce(mysum, [1, 2, 3, 4, 5]))


dizi = list(map(int, "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20".split())) # Bu daha ideal sanırım multi processor
dizi2 = list(int(x) for x in "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20".split())

print(dizi[::2])
print(dizi2[::2])
