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
#
