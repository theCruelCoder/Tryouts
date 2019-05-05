# 列表查询

# list.index(value,[start,[stop]])
# 通过value,从指定区间检查索引号
# 返回索引号
lst = [0, 1, 1, 1, 0]
print(lst.index(1, -5, -1))

# list.count(value)
# 返回列表中匹配value的次数
print(lst.count(1))

# 时间复杂度
# index和count的复杂度都是O(n)
# 随着列表数据规模的增大，而效率下降

# 如何返回列表元素个数？如何遍历？如何设计高效？
print(len(lst))

# 列表修改
# 索引访问修改
# list[index] = value
lst[0] = 100
print(lst)

# 列表增加、插入元素
# append(object) -> None
# 列表尾部追加元素，返回None
# 返回None意味没有新的列表产生，就地修改
# 时间复杂度是O(1)

# insert(index, object) -> None
# 在指定的索引index处插入元素object
# 返回None就意味着没有新的列表产生，就地修改
# 时间复杂度是O(n)
# 索引能超上下界吗？超越上界，尾部追加。超越下界，尾部追加。

# extend(iterable) -> None
# 将可迭代对象的元素追加进来，返回None
# 就地修改

# + -> list (new)
# 连接操作，将两个列表连接起来
# 产生新的列表，原列表不变
# 本质上调用的是_add_()方法

# * -> list
# 重复操作，将本列表元素重复n次，返回新的列表

# 列表*重复的坑
x = [[1, 2, 3]] * 3
print(x)
x[0][1] = 20
print(x)

y = [1] * 5
y[0] = 6
y[1] = 7
print(y)

# 列表删除元素
# remove(value) -> None
# 从左至右查找第一个匹配value的值，移除该元素，返回None
# 就地修改
# 效率O(n)

# pop([index]) -> item
# 不指定索引index,就从列表尾部弹出一个元素
# 指定索引index,就从索引处弹出一个元素，索引超界抛出IndexError错误
# 效率？指定索引的时间复杂度为O(n)，不指定索引O(1)。

# clear() -> None
# 清楚列表所有元素，剩下一个空列表

# 列表其他操作
# reverse() -> None
# 将列表元素反转，返回None
# 就地修改

# sort(key=None, reverse=False) -> None
# 对列表元素进行排序，就地修改，默认升序
# reverse为True,反转，降序
# key一个函数，指定key如何排序
# lst.sort(key=functionname)

# in
# [3,4] in [1,2,[3,4]]
# for x in [1,2,3,4]

# 列表复制
# copy() -> list
# shadow copy 返回一个新的列表
# 影子拷贝，浅拷贝，遇到引用类型只拷贝引用地址

# 深拷贝
from copy import deepcopy
lst5 = deepcopy(lst)
