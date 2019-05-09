#  Copyright (c) 2019. YH Software Inc. Corp.

# Author: Jiaheng Gary Li
# @Time : 5/8/2019 10:40 AM
# Project: 
# Name: 生成器.py
# Description:

# 生成器表达式Generator expression
# 语法
#   (返回值 for 元素 in 可迭代对象 if 条件)
#   列表解析式的中括号换成小括号就行了
#   返回一个生成器
# 和列表解析式的区别
#   生成器表达式是按需计算（或称惰性求值、延迟计算），需要的时候才计算值
#   列表解析是是立即返回值
# 生成器
#   可迭代对象
#   迭代器

# 判断是否是迭代器
# next()

# 举例
g = ("{:04}".format(i) for i in range(1,11))
next(g)
for x in g:
    print(x)
print("~~~~~~~~~~~~~~~~~~~~~")
for x in g:
    print(x)

# 总结
#   延迟计算
#   返回迭代器，可以迭代
#   从前到后走完一遍后，不能回头

# 对比列表
g = ["{:04}".format(i) for i in range(1,11)]
for x in g:
    print(x)
print("~~~~~~~~~~~~~~~~~~~~~")
for x in g:
    print(x)

# 总结
#   立即计算
#   返回的不是迭代器，返回可迭代对象列表
#   从前到后走完一遍后，可以重新回头迭代
