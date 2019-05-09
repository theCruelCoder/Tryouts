#  Copyright (c) 2019. YH Software Inc. Corp.

# Author: Jiaheng Gary Li
# @Time : 5/8/2019 8:55 AM
# Project: 
# Name: 解析式、生成器
# Description:

# 列表解析 List Comprehension

import datetime

# 语法
#   [返回值 for 元素 in 可迭代对象 if 条件]
#   使用中括号[]，内部是for循环，if条件语句可选
#   返回一个新的列表

#   列表解析是是一种语法糖
#       编译器会优化，不会因为简写而影响效率，反而因优化提高了效率
#       减少程序员工作量，减少出错
#       简化了代码，但可读性增强


# 举例
# 生成一个列表，元素0~9，对每个元素自增1后返回一个新的列表

nums = []
for i in range(10):
    nums.append((i + 1) ** 2)
print(nums)

a = [(i + 1) ** 2 for i in range(10)]
print(a)

b = [i for i in range(10)]
print(b)
nums = [_ for _ in sorted(range(10), reverse=True)]
print(nums)

# 举例
# 获取10以内的偶数，比较执行效率

now = datetime.datetime.now()
even = []
for x in range(100000):
    if x % 2 == 0:
        even.append(x)
delta = (datetime.datetime.now() - now).total_seconds()
print("Need: {}".format(delta))

now = datetime.datetime.now()
even = [x for x in range(100000) if x % 2 == 0]
delta = (datetime.datetime.now() - now).total_seconds()
print("Need: {}".format(delta))

# 思考
#   有这样的赋值语句newlist = [print(i) for i in range(10)], 请问newlist的元素打印出来是什么？
newlist = [print(i) for i in range(10)]
print(newlist)

# 获取20以内的偶数，如果数是3的倍数也打印[i for i in range(20) if i%2==0 elif i%3==0] 行吗？
lst = [i for i in range(20) if i % 2 == 0 or i % 3 == 0]
print(lst)

# 列表解析进阶
# [expr for item in iterable if cond1 if cond2]
# 等价于
# ret = []
# for item in iterable:
#   if cond1:
#       if cond2:
#           ret.append(expr)

# [expr for i in iterable for j in iterable2]
# 等价于
# ret = []
# for i in iterable1:
#   for j in iterable2:
#       ret.append(expr)

# 举例

print([(x, y) for x in 'abcde' for y in range(3)])
print([[x, y] for x in 'abcde' for y in range(3)])
print([{x: y} for x in 'abcde' for y in range(3)])

# 请问下面3种输出各是什么？为什么
a = [(i, j) for i in range(7) if i > 4 for j in range(20, 25) if j > 23]
print(a)
a = [(i, j) for i in range(7) for j in range(20, 25) if i > 4 if j > 23]
print(a)
a = [(i, j) for i in range(7) for j in range(20, 25) if i > 4 and j > 23]
print(a)

