# 字符串
# 一个个字符组成的有序的序列，是字符的集合
# 使用单引号、双引号、三引号引住的字符序列
# 字符串是不可变对象
# Python3起，字符串就是Unicode类型 UTF-8

# 字符串元素访问——下标

# 字符串支持使用索引访问
sql = "select * from user where name = 'tom'"
sql[4]
# sql[4] = "c" 不允许
# for i in sql: print i
print("-".join(sql))
print(sql)

# "string".join(iterable) -> str
# 将可迭代对象连接起来，使用String作为分隔符
# 可迭代对象本身元素都是字符串
# 返回一个新字符串

lst = [1, 2, 3, 4, 5]
print("~~~".join(map(str, lst)))
print(list(map(str, lst)))
print(lst)
lst = ['1', ['a', 'b'], '3']
print(" ".join(map(str, lst)))

# 字符串+连接
# + -> str
# 将2个字符串连接在一起
# 返回一个新字符串

# 字符串分割
# 分割字符串的方法
# split系
# 将字符串按照分隔符分割成若干字符串，并返回列表
# partition系
# 将字符串按照分隔符分割成2段，返回这2段的分隔符的元组

print("a\r\nb\tc d".split(None))
print("a\r\nb\tc d".split())
print("a\r\nb\tc d".split(sep=None))
print("a     b        c".split(' '))
print(','.join('abc').split(','))

# 字符串分割**
# split(sep=None, maxsplit=-1) -> list of strings
# 从左至右
# sep 指定分割字符串，缺省的情况下空白字符串作为分隔符
# maxsplit 指定分割的次数，-1表示遍历整个字符串

s1 = "I'm \ta super student."
print(s1.split())
print(s1.split('s'))
print(s1.split('super'))
print(s1.split('super '))
print(s1.split(' '))
#print(s1.split('', maxsplit=2)) # ValueError: empty separator
print(s1.split('\t', maxsplit=2))

# rsplit(sep=None, maxsplit=-1) -> list of strings
# 从右向左
# 其他同split

# splitlines([keepends]) -> list of stirngs
# 按照行来切分字符串
# keepends 指的是是否保留行分隔符
# 行分隔符包括\n、\r\n、\r等

# partition(sep)
# rpartition(sep)
print("a,b,c,d".partition(","))

# 字符串大小写
# upper()
# lower()
# 大小写，做判断的时候用
# swapcase()
# 交互大小写

# title() -> str
# 标题的每个单词都大写

# capitalize() -> str
# 首个单词大写

# center(width[, fillchar]) -> str
# width 打印宽度
# fillchar 填充的字符

# zfill(width) -> str
# width 打印宽度，居右，左边用0填充

# ljust(width[, fillchar]) -> str 左对齐
# rjust(width[, fillchar]) -> str 右对齐
# 中文用的少，了解一下

# 字符串修改*
# replace(old, new[, count]) -> str
# 字符串中找到匹配替换为新子串，返回新字符串
# count表示替换几次，不指定就是全部替换
print('www.magedu.com'.replace('w', 'p'))
print('www.magedu.com'.replace('w', 'p', 2))
print('www.magedu.com'.replace('w', 'p', 3))
print('www.magedu.com'.replace('ww', 'p', 2))
print('www.magedu.com'.replace('www', 'python', 2))

# strip([chars]) -> str
# 从字符串两端去除指定的字符集chars中的所有字符
# 如果chars没有指定，去除两端空白字符

# lstrip([chars]) -> str
# rstrip([chars]) -> str

# find(sub[, start[, end]]) -> int
# rfind(sub[, start[, end]]) -> int


