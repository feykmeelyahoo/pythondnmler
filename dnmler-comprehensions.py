def func():
    a = (x for x in range(11))
    aa = tuple(x ** 3 for x in range(11))
    print(a)
    print("")
    print(aa)
    print("")
    return sum(a)


# print(func())

def func2(list):
    print(list)
    print(sum(list))


func2([x for x in range(11)])
print("")
func2(tuple(x for x in range(11)))

mylambda1 = lambda x: x ** 3
print("")

print(mylambda1(3))

mylambda2 = lambda: list(30 * x for x in range(1, 11))
print("")
print(mylambda2())

mylambda3 = lambda y: list(3 * x for x in range(1, y))
print("")
print(mylambda3(5))
