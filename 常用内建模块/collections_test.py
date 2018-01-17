from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)

print(p.x, p.y)

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')

print(q)

from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1']) # key1存在
print(dd['key2']) # key2不存在，返回默认值

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)

c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)