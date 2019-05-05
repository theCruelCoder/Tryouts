from collections import namedtuple

# 元组 tuple

# 一个有序的元素组成的集合
# 使用小括号()表示
# 元组是不可变对象

# 元组的定义和初始化
t = tuple()
t = tuple(range(5))
print(t)
print(id(t))
print(t[1])

for x in t:
    print(x)

t1 = (1)
print(type(t1))
t1 = (1, )
print(type(t1))
t1 = ((1, ), ) * 5
print(t1)
t1 = ((1, 2, 3), ) * 5
print(t1)
# 以下能不能改
t1 = ([1, 2, 3], ) * 5
t1[0][0] = 100
# t1[0] = [10, 2, 3] 不能改，tuple内存地址不允许修改

# 元组查询，类似列表查询
# index(value, [start, [stop]])
# count(value)
# Time complexity: O(n)
# len(tuple)
# Time complexity: O(1)

# 命名元组 namedtuple

Point = namedtuple('P', ['x', 'y'])
print(Point)
p1 = Point(1, 2)
print(p1)
print(p1.x, p1.y)
print(p1[0], p1[1])

Student = namedtuple('stu', 'name age')
print(Student)

s1 = Student('tom', 20)
s2 = Student('jerry', 18)
print(s1)
print(s2)
print(s1.name)
print(s1.age)

# 定义
# tuple() -> empty tuple
# tuple(iterable) -> tuple initialized from iterable's items

t = tuple() # 工厂方法
t = ()
t = tuple(range(1,7,2)) # iterable
t = (2,4,6,3,4,2)
t = (1,) # 一个元素元组的定义，注意有个逗号
t = (1,) * 5
print(t)
t = (1,2,3) * 6
print(t)

# 元组元素的访问
# 支持索引（下标）
# 正索引：从左至右，从0开始，为列表中每个元素编号
# 负索引：从右至左，从-1开始
# 正负索引不可以超界，否则引发异常IndexError
# 元组通过索引访问
# tuple[index], index就是索引, 使用中括号访问

t[1]
t[-2]
