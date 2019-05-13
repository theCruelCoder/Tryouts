#  Copyright (c) 2019. YH Software Inc. Corp.

# Author: Jiaheng Gary Li
# @Time : 5/9/2019 7:58 AM
# Project: 
# Name: 生成器练习
# Description:

# 习题
it = (print("{}".format(i+1)) for i in range(2))
first = next(it)
second = next(it)
print(type(first))
#val = first + second
#print(val)
#next(it)
# val的值是什么？ Error: NoneType + NoneType
# val = first+second语句之后能否再次next(it)？ 不可以 StopIteration

# 习题2
it = (x for x in range(10) if x % 2)
first = next(it)
second = next(it)
val = first + second # 4
print(val)
print(next(it))  # 5

# 和列表解析式的对比
#   计算方式
#       生成器表达式延迟计算，列表解析式立即计算
#   内存占用
#       单从返回值本身来说，生成器表达式生内存，列表解析式返回新的列表
#       生成器没有数据，内存占用极少，但是使用的时候，虽然一个个返回数据，但是合起来占用的内存也差不多
#       列表解析式构造新的列表需要占用内存
#   计算速度
#       单看计算时间看，生成器表达式耗时非常短，列表解析式耗时长
#       但是生成器本身并没有返回任何值，只返回了一个生成器对象
#       列表解析式构造并返回了一个新的列表

