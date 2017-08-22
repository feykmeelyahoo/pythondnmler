from urllib.request import urlopen

# with urlopen('https://raw.githubusercontent.com/feykmeelyahoo/pythondnmler/master/2DArray-DS-2.py') as story:
#     story_words = []
#     for line in story:
#         # line_words = line.decode('utf8').split()
#         line_words = line.split()
#         for word in line_words:
#             story_words.append(word)
#
# print(story_words)

a = dict(a=3, b=5)
a2 = {'aa': 3, 'bb': 5}
a3 = {1: 3, 'bb': 5}
print(type(a))
print(a)

a.update(a=33, b=55, c=77)
a2.update(aa=333, bb=555, cc=777)
print('a = ', a)
print('a2 = ', a2)
print('a3 = ', a3)

cc = dict([(1, 2), (3, 4)])

print('cc = ', cc)
del cc[3]
print('cc = ', cc)
