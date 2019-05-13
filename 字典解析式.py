#  Copyright (c) 2019. YH Software Inc. Corp.

# Author: Jiaheng Gary Li
# @Time : 5/13/2019 7:45 AM
# Project: 
# Name: 字典解析式
# Description:

# 字典解析式
# 语法
# {返回值 for 元素 in 可迭代对象 if 条件}
# 列表解析式的中括号换成大括号{}就行了
# 使用key:value形式
# 立即返回一个字典

# 用法

a = {x:(x,x+1) for x in range(10)}
a = {x:[x,x+1] for x in range(10)}
a = {(x,):[x,x+1] for x in range(10)}
#a = {[x]:[x,x+1] for x in range(10)}
a = {chr(0x41+x):x**2 for x in range(10)}
a = {str(x):y for x in range(3) for y in range(4)} # 输出多少元素？ 3
print(a)

# 总结

# python2 引入列表解析式
# python2.4 引入生成器表达式
# python3 引入集合解析式，并迁移到了2.7

# 一般来说，应该多应用解析式，简短、高效
# 如果一个解析式非常复杂，难以读懂，要考虑拆解成for循环
# 生成器和迭代器是不同的对象，但都是可迭代对象