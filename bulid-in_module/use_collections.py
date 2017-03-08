#!/user/bin/python
#coding=utf-8
from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import Counter
# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，
# 并可以用属性而不是索引来引用tuple的某个元素。

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print('x=', p.x)
print('y=', p.y)
print(type(p))
print(isinstance(p, Point))
print(isinstance(p, tuple))

Circle = namedtuple('Circle', ['x', 'y', 'r'])
c = Circle(0, 0, 3)
print('****************************')

#deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
q = deque(['a', 'b', 'c'])
q.append('x')
print(q)
q.appendleft('y')
print(q)
q.pop()
print(q)
print('****************************')

#使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])
print('****************************')

#如果要保持dict中Key的顺序，可以用OrderedDict,OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)

od1 = OrderedDict()
od1['z'] = 1
od1['x'] = 2
od1['y'] = 3
print(od1)
print('****************************')
#Counter是一个简单的计数器，例如，统计字符出现的个数
c = Counter('programming')
# for ch in 'programming':
#     c[ch] = c[ch] + 1
print(c)