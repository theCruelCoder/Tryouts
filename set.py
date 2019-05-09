# 集 set

import random

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

# set和线性结构
# 线性结构的查询时间复杂度是O(n),即随着数据规模的增大而增加耗时
# set、dict等结构，内部使用hash值作为key,时间复杂度可以做到O(1),查询时间和数据规模无关

# 可hash
# 数值型int float complex
# 布尔型 True Flase
# 字符串 string, bytes
# tuple
# None
# 以上都是不可变类型，称为可哈希类型，hashable

# 集合
# 基本概念
# 全集
# 所有元素的集合。例如实数集，所有实数组成的集合就是全集
# 子集 subset 和 超集 superset
# 一个集合A所有元素都在另一个集合B内，A是B的子集，B是A的超集

"""
    并集：
    union(*others)
    返回和多个集合合并后的新集
    | 运算符重载 = union
    
    update(*others)
    和多个集合合并，就地修改
    |= 等同于 update
"""

"""
    交集
    集合A和B，由所有属于A且属于B的元素组成的集合
    intersection(*others)
    返回和多个集合的交集
    & = intersection
    
    intersection_update(*others)
    获取和多个集合的交集，并就地修改
    &= 等同于intersection_update
"""

"""
    差集
    集合A和B，由所有属于A且不属于B的元素组成的集合
    
    difference(*others)
    - = difference
    
    difference_update(*others)
    -= 等同于difference_update
"""

"""
    对称差集
    集合A和B，由所有不属于A和B的交集元素组成的集合
    symmetric_difference(other)
    ^ = symmetric_difference
    
    symmetric_difference(other)
    ^= 等同 
"""

# issubset(other), <=
# set1 < set2

# issuperset(other), >=
# set1 > set2

# isdisjoint(other) 没有交集，返回True

def q1():
    """
    你的好友A、B、C，他的好友C、B、D，求共同好友
    :return: None
    """
    mine = {'A', 'B', 'C'}
    his = {'C', 'B', 'D'}
    mutual_friend = mine.intersection(his)
    print(mutual_friend)

def q2():
    """
    微信群提醒
    XXX与群里其他人都不是微信朋友关系
    :return:
    """
    my_friend = {'A', 'B', 'C', 'D'}
    group_member = {'E', 'F', 'G', 'H', 'D'}
    if my_friend.isdisjoint(group_member):
        print("Warning: Stranger!")
    else:
        print("Welcome my friend.")

def q3():
    """
    权限判断
    有一个API，要求权限同时具备A,B,C才能访问，用户权限是B,C,D，判断用户是否能够访问该API
    有一个API，要求权限具备A、B、C任意一项就可以访问，用户权限是B,C,D，判断用户是否能够访问该API
    一个总任务列表，存储所有任务。一个完成的任务列表。找出未完成的任务。
    :return:
    """
    auth = {'A', 'B', 'C'}
    user = {'C', 'B', 'D'}
    if auth.issubset(user):
        print("API1 Connected.")
    else:
        print("API1 Rejected.")
    if not auth.isdisjoint(user):
        print("API2 Connected.")
    else:
        print("API2 Rejected.")
    task_list = [
        "t1",
        "t2",
        "t3",
        "t4",
        "t5"
    ]
    task_complete = [
        't1',
        't2',
    ]
    task_incomplete = set(task_list) - set(task_complete)
    print(task_incomplete)

def q4():
    """
    随机产生2组各10个数字的列表，
    每个数字取值范围[10,20]
    统计20个数字中，一共有多少个不同的数字
    2组中，不重复的数字有几个？分别是什么？
    2组中，重复的数字有几个？分别是什么？
    :return:
    """
    lst1 = []
    lst2 = []
    for i in range(10):
        lst1.append(random.randint(10,20))
        lst2.append(random.randint(10,20))
    set1 = set(lst1)
    set2 = set(lst2)
    print(lst1, lst2)
    print(set1, set2)
    distinct_number = len(set1 | set2)
    print(distinct_number)
    non_dupl_member = set1 ^ set2
    non_dupl_count = len(non_dupl_member)
    print(non_dupl_count, non_dupl_member)
    dupl_member = set1 & set2
    dupl_count = len(dupl_member)
    print(dupl_count, dupl_member)



q1()
q2()
q3()
q4()