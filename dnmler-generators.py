# def gen123():
#     yield 1
#     yield 2
#     yield 3
#
# g=gen123()
#
# print(next(g))
# print(next(g))
# print(next(g))
#
# for i in gen123():
#     print("Ikinci donum - ", i)

# def gen246():
#     print("About to yield 2")
#     yield 2
#     print("About to yield 4")
#     yield 4
#     print("About to yield 6")
#     yield 6
#     print("About return!!!")
#
# gg=gen246()
# print(next(gg))
# print(next(gg))
# print(next(gg))
# print(next(gg))

def take(count, iterable):
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def run_take():
    items = items = [2, 4, 6, 8, 10]
    for item in take(3, items):
        print(item)

# if __name__=='__main__':
#     run_take()

# run_take()
# print("")

def distinct(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)

def run_distinct():
    items = [5, 7, 7, 6, 5, 5]
    for item in distinct(items):
        print(item)

# run_distinct()

def run_pipeline():
    items = [3, 6, 6, 2, 2, 1]

    for item in take(4, distinct(items)):
        print(item)

run_pipeline()
