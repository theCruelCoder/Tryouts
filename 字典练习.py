#  Copyright (c) 2019. YH Software Inc. Corp.

# Author: Jiaheng Gary Li
# @Time : 5/7/2019 11:48 AM
# Project: 
# Name: 字典练习
# Description:

from collections import OrderedDict
import random

def q1():
    """
    用户输入一个数字
    打印每一位数字及其重复的次数
    :return:
    """
    d = {}
    i = input("Input a number:")
    for c in i:
        if c not in d:
            d[c] = 0
        d[c] += 1
    print(d)

#q1()

def q2():
    """
    数字重复统计
    随机产生100个整数
    数字范围[-1000,1000]
    升序输出所有不同的数字及其重复的次数
    :return:
    """
    lst = []
    d = OrderedDict()
    for i in range(100):
        lst.append(random.randint(-1000,1000))
    lst.sort()
    for num in lst:
        if num not in d:
            d[num] = 0
        d[num] += 1
    print(d)

q2()

def q3():
    """
    字符串重复统计
    字符表'abcdefghijklmnopqrstuvwxyz'
    随机挑选2个字母组成字符串，共挑选100个
    :return:
    """
    lst_alphabet = []
    lst_random = []
    alphabet = 'abcdefghijklmnopqrsuvwxyz'
    d = OrderedDict()
    for c in alphabet:
        lst_alphabet.append(c)
    for i in range(100):
        char1 = random.choice(lst_alphabet)
        char2 = random.choice(lst_alphabet)
        char = char1+char2
        lst_random.append(char)
    lst_random.sort(reverse=True)
    for key in lst_random:
        if key not in d:
            d[key] = 0
        d[key] += 1
    print(d)

def q3_teacher():
    alphabet = 'abcdefghijklmnopqrsuvwxyz'
    words = []

    for _ in range(100):
        words.append(''.join(random.choice(alphabet) for _ in range(2)))

    d = {}

    for x in words:
        d[x] = d.get(x,0) + 1
    print(d)

    d1 = sorted(d.items(), reverse=True)
    print(d1)

q3()
q3_teacher()