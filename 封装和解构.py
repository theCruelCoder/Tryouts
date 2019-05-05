# 封装和结构

a = 4
b = 5
temp = a
a = b
b = temp
# 等价于
a, b = b, a
# 上句中，等号右边使用了封装，而左边就使用了解构

# 解构
# 把线性结构的元素解开，并顺序的赋给其他变量
# 左边接纳的变量数要和右边解开的元素个数一直
lst = [3,5]
first, second = lst
print(first, second)

# 非线性也可以解构
a,b = {
    'a':10,
    'b':20
}
print(a,b)

a, *b = {10, 20, 30}
print(a, b)

# python3的解构
# 使用 *变量名 接受，但不能单独使用
# 被 *变量名 收集后组成一个列表

lst = list(range(1,101,2))
head, *mid, tail = lst
print(head)
print(mid)
print(tail)
# *lst2 = lst
*body, tail = lst
head, *tail = lst
# head, *m1, *m2, tail= lst
head, *mid, tail = 'abcdefghijklmn'
print(mid)
print(type(mid))

# 丢弃变量
# 这是一个惯例， 是一个不成文的约定，不是标准
# 如果不关心一个变量，就可以定义该变量的名字为——
# _是一个合法的标识符，也可以作为一个有效的变量使用，但是定义成下划线就是希望不要被使用，除非你明确的知道这个数据需要使用

lst = [9,8,7,20]
first, *second = lst
head, *_, tail = lst
print(head)
print(tail)
print(_)

# lst = list(range(10)) # 这样一个列表，取出第二个、第四个、倒数第二个
lst = list(range(10))
_, second, _, fourth, *_, second_last, _ = lst
print(second, fourth, second_last)

lst = [1,(2,3,4),5]
_, (*_, tail), *_ = lst
print(tail)

mypath = 'JAVA_HOME=/usr/bin'
env_name, _, env_path = mypath.partition("=")
print(mypath.partition("="))
print(env_name, env_path)
