#  Copyright (c) 2019. YH Software Inc. Corp.

# Author: Jiaheng Gary Li
# @Time : 5/13/2019 8:02 AM
# Project: 
# Name: 内建函数
# Description:

# 标识 id
# 返回对象的唯一标识，CPython返回内存地址

# 哈希 hash
# 返回一个对象的哈希值

# 类型 type
# 返回对象的类型

# 类型转换
#   float() int() bin() hex() oct() bool() list() tuple() dict() set() complex() bytes() bytearray()

# 输入 input([prompt])
#   接收用户输入，返回一个字符串

# 打印 print(*objects, sep='', end='\n', file=sys.stdout, flush=False)
#   打印输入，默认使用空格分隔、换行结尾，输出到控制台

# 对象长度 len(s)
#   返回一个集合类型的元素个数

# isinstance(obj, class_or_tuple)
#   判断对象obj是否属于某种类型或者元组中列出的某个类型
#   isinstance(True,int)

# issubclass(cls, class_or_tuple)
#   判断类型cls是否是某种类型的子类或元组中列出的某个类型的子类
#   issubclass(bool,int)

# 绝对值 abs(x) x为数值
# 最大值 max() 最小值 min()
#   返回可迭代对象中的最大或最小值
#   返回多个参数中最大或最小值

# round(x) 四舍六入五取偶，round(-0.5) # 0

# pow(x,y)等价于x**y
# range(stop) 从0开始到stop-1的可迭代对象；range(start, stop[, step])从start开始到stop-1结束步长为step的可迭代对象

# divmod(x,y) 等价于 tuple(x//y, x%y)

# sum(iterable[, start]) 对可迭代对象的所有数据元素求和
#   sum(range(1,100,2))

# chr(i) 给一个一定范围的整数返回对应的字符
#   chr(97) chr(20013)

# ord(c) 返回字符对应的整数
#   ord('a') ord('中')

# str()、repr()、ascii() 后面说
