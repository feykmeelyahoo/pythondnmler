# Start Challenge 1
# def end_other(a, b):
#     a=a.lower()
#     b=b.lower()
#     print("a = {}, b = {}".format(a, b))
#     print(b, len(b))
#     print(a, len(a))
#
#     print("a'nın b kadar sonu=",a[(len(b)):])
#     print("b'nın a kadar sonu=",b[-(len(a)):])
#
#     return a[(len(b)):]==b or b[-(len(a)):]==a
#
# ch = "Serkan"
# print("ch[:-1] = {}".format(ch[:-1]))
# print("ch[-1:] = {}".format(ch[-1:]))
#
# print('ch.endswith("kan") =', ch.endswith("kan"))
#
# print(end_other("Serkan", "kan"))
# print(end_other("rkan", "Serkan"))

# End Challenge 1

# Start Challenge 2
import operator
from functools import reduce


def doublemystring(mystring):
    print(reduce(operator.add, list(map(lambda x: x + x, list(mystring)))))


def doublemystring2(mystring):
    retStr = ''
    for i in mystring:
        retStr += 2 * i

    return print(retStr)


doublemystring("Serkan!")
doublemystring2("Serkan!")
# End Challenge 2
