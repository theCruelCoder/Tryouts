#  Copyright (c) 2019. YH Software Inc. Corp.

# Author: Jiaheng Gary Li
# @Time : 5/9/2019 9:04 AM
# Project: 
# Name: 集合解析式
# Description:

# 集合解析式
#   语法
#       {返回值 for 元素 in 可迭代对象 if 条件}
#       列表解析式的中括号换成大括号{}就行了
#       立即返回一个集合

#   用法
a = {(x, x + 1) for x in range(10)}
#b = {[x] for x in range(10)} # unhashable
print(a) #, b)