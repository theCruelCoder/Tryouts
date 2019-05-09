#  Copyright (c) 2019. YH Software Inc. Corp.

# Author: Jiaheng Gary Li
# @Time : 5/8/2019 9:51 AM
# Project: 
# Name: 列表解析练习
# Description:

import random
import string


def q1():
    """
    返回1-10平方的列表
    :return:
    """
    a = [(i + 1) ** 2 for i in range(10)]
    print(a)


# q1()

def q2():
    """
    有一个列表lst = [1,4,9,16,2,5,10,15], 生成一个新列表，要求新列表元素是lst相邻2项的和
    :return:
    """
    lst = [1, 4, 9, 16, 2, 5, 10, 15]
    newlist = [lst[i] + lst[i + 1] for i in range(len(lst) - 1)]
    print(newlist)


# q2()

def q3():
    """
    打印九九乘法表
    :return:
    """
    a = ["{}*{}={}".format(i, j, i * j) for i in range(1, 10) for j in range(i, 10)]
    print(a)


# q3()

def q3_teacher():
    """
    打印九九乘法表
    :return:
    """
    a = [["{}*{}={}".format(i, j, i * j) for j in range(i, 10)] for i in range(1, 10)]
    [print(i) for i in a]


def q3_best():
    print("".join(
        ["{}*{}={:<3}{}".format(i, j, i * j, "" if j != 9 else "\n") for i in range(1, 10) for j in range(i, 10)]))


q3_best()


def q4():
    """
    生成ID
    "0001.abadicddws"是ID格式，要求ID格式是以点好分割，左边是4位从一开始的证书，右边是10位随机额小写英文字母。请以此生成前100个ID的列表
    :return:
    """
    # [(".".join(["{}".format(str(num+1).zfill(4)), "".join(c for c in random.sample(lst,10))])) for num in range(100) ]
    a = ['{:>04}.{}'.format(i + 1, ''.join(random.choice(string.ascii_lowercase) for _ in range(10))) for i in
         range(100)]
    print(a)


q4()
