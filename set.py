# 集 set

# 约定
# set 翻译为集合
# collection 翻译为集合类型，是一个大概年
# set 可变的、无序的、不重复的元素的集合

s = set()
print(type(s))

s = set(range(10))
print(s)

s = {} # 字典
print(type(s))

# set定义 初始化

s1 = set()
s2 = set(range(5))
s3 = set(list(range(10)))
s4 = {} # WRONG DICT
s5 = {9, 10, 11} # set
s6 = {(1,2), 3, 'a'}
# s7 = {[1], (1,), 1}
# s8 = {(1,2), [3,4], 'a'} # Error: unhashable type 'list'

# set 的元素
# set的元素要求必须可以hash
# 目前学过的不可hash的类型有list、set
# 元素不可以索引
# set可以迭代

# set增加
# add(element)
# 增加一个元素到set中
# 如果元素存在，什么都不做
# update(*others)
# 合并其他元素到set集合中来
# 参数others必须是可迭代对象
# 就地修改

# set删除
# remove(element)
# 从set中移除一个元素
# 元素不存在，抛出KeyError异常。

# discard(element)
# 从set中移除一个元素
# 元素不存在，什么都不做

# pop() -> item
# 移除并返回任意元素
# 空集返回KeyError异常

# clear()
# 移除所有元素

# set 修改、查询
# 修改
# 要么删除，要么加入新的元素，没有修改
# 查询
# 非线性结构，无法索引
# 遍历
# 可以迭代所有元素
# 成员运算符
# in 和 not in 判断元素是否在set中
# 效率呢？O(1) 不会因为规模增加降低速度，hash算出内存地址（key）

