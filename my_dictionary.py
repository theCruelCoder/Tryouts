#  Copyright (c) 2019. YH Software Inc. Corp.

# Author: Jiaheng Gary Li
# @Time : 5/7/2019 10:18 AM
# Project: 
# Name: my_dictionary
# Description: Dictionary

# 字典dict
# key-value键值对的数据的集合
# 可变的、无序的、key不重复

# 字典dict 初始化

d = {}
d = dict(a=1, b=2)
print(d)

# dict(**kwargs) 使用可迭代对象和name=value对构造字典，不过可迭代对象的元素必须是一个二元结构
d = dict(([1, 'a'], [2, 'b']))
print(d)

# dict(mapping, **kwarg) 使用一个字典构建另一个字典
d = {'a': 10, 'b': 20, 'c': None, 'd': [1, 2, 3]}

# 类方法dict.fromkeys(iterable,value)
d = dict.fromkeys(range(5))
print(d)
d = dict.fromkeys(range(5), 0)
print(d)

# 字典元素的访问
# d[key]
#   返回key对应的值value
#   key不存在抛出KeyError异常
# get(key[,default])
#   返回key对应的值value
#   key不存在返回缺省值，如果没有设置缺省值就返回None
# setdefault(key[, default])
#   返回key对应的值value
#   key不存在，添加kv对，value为default，并返回default，如果default没有设置，缺省为None

# 字典增加和修改
# d[key] = value
#   将key对应的值修改为value
#   key不存在添加新的kv对
# update([other]) -> None
#   使用另一个字典的kv对更新本字典
#   key不存在，就添加
#   key存在，覆盖已经存在的key对应的值
#   就地修改
d.update(red=1)
print(d)
d.update((('red', 2),))
print(d)
d.update({'red': 3})
print(d)

# 字典删除
# pop(key[, default])
#   key存在，移除它，并返回它的value
#   key不存在，返回给定的default
#   default未设置，key不存在则抛出KeyError异常

# popitem()
#   移除并返回一个任意的键值对
#   字典为empty，抛出KeyError异常

# clear()
#   清空字典

# 字典删除
# del语句
a = True
b = [6]
c = [1, 3, 5]
d = {
    'a': 1,
    'b': b,
    'c': c,
}
# del a
# del d['c']
# print(c)
# del b[0]
# c = b
# del c
# del b
# b = d['b']
# print(b)

# del d['c']看着像删除了一个对象，本质上减少了一个对象的引用，del实际上删除的是名称，而不是对象

# 字典遍历
#   for ... in dict
#       遍历key
for k in d:
    print(k)
for k in d.keys():
    print(k)

#   遍历value
for val in d.values():
    print(val)

for key in d.keys():
    print(d[key])

for key, value in d.items():
    print(key, value)

for _, value in d.items():
    print(value)

# 字典遍历
# 总结
#   Python3中，keys,values,items方法返回一个类似一个生成器的可迭代对象，不会把函数的返回结果复制到内存中
#   dictionary view对象
#   字典的entry的动态的视图，字典变化，视图将反映出这些变化

#   Python2中，上面的方法会返回一个新的列表，占据新的内存空间。
#   所以Python2建议使用iterkeys,itervalues,iteritems版本，返回一个迭代器，而不是一个copy

# 字典的移除
# for k in d:
#    print(k)
#    d.pop(k)
# 错误 用迭代器的时候不可以pop
# 非要用for循环
a = True
b = [6]
c = [1, 3, 5]
d = {
    'a': 1,
    'b': b,
    'c': c,
    'd': 'str1'
}
lst = []
for k in d:
    if isinstance(d[k], str):
        lst.append(k)
for k in lst:
    d.pop(k)  # ok

"""
for k in d:
    d['a100'] = 100

"""

# 遍历时候字典size不能改变


# 字典的key
# key的要求和set的元素要求一致
#   set的元素可以就是看做key,set可以看作dict的简化版
#   hashable可哈希才可以作为key,可以使用hash()测试
d = {1: 0, 2.0: 3, 'abc': None, ('hello', 'world', 'python'): 'string', b'abc': '135'}
print(d)

import random
from collections import defaultdict

d = {}
d = defaultdict(list)
for c in 'abcde':
    for i in range(random.randint(1, 5)):
        d[c].append(i)
print(d)

# defaultdict
# collections.defaultdict([default_factory[,...]])
# 第一个参数是default_factory,缺省是None,它提供一个初始化函数。当key不存在的时候，会调用这个工厂函数来生成key对应的value

from collections import OrderedDict
od = OrderedDict(a=1,b=2,c=3,d=4)
od[100] = 100
print(od)

# OrderedDict
# 有序字典可以记录元素插入顺序，打印的时候也是按照这个顺序输出打印
# 3.6版本的Python的字典就是记录key的插入顺序

# 应用场景：
#   假如使用字典记录了N个产品，这些产品使用ID由小到大加入到字典中
#   除了使用字典检索的遍历，有时候需要取出ID，但是希望是按照输入的顺序，因为输入顺序是有序的
#   否则还需要重新把遍历到的值排序
