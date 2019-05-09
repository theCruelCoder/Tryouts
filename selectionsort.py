#  Copyright (c) 2019. YH Software Inc. Corp.

# Author: Jiaheng Gary Li
# @Time : 5/6/2019 2:54 PM
# Project: 
# Name: selection sort
# Description:

# 简单选择排序 simple selection sort
# 属于选择排序
#   两两比较大小，找出极值（极大值或极小值）被放置在固定的位置，这恶鬼固定的位置一般指的是某一段
#   结果分为升序和降序排列
# 降序
#   n个数从左至右，索引从0开始到n-1，两两依次比较，记录大值索引，此轮所有数比较完毕，将大数和索引0数交换，如果大数就是索引0，不交换。
#   第二轮，从1开始比较，找到最大值，将它和索引1位置交换，如果它就在索引1位置则不交换。依此类推，每次左边都会固定下一个大数。
# 升序
#   和降序相反

def simple_selection_sort():
    lst = [1, 9, 8, 7, 6, 5, 4, 3, 2]
    length = len(lst)
    for i in range(length):
        x = lst[i]
        maxindex = i
        for j in range(i + 1, length):
            if lst[j] > lst[maxindex]:
                maxindex = j
        if i != maxindex:
            lst[i], lst[maxindex] = lst[maxindex], lst[i]
    print(lst)


# 优化实现
# 二元选择排序 binary selection sort
# 同时固定左边最大值和右边最小值
# 优点：减少迭代次数

# 1、length // 2 整除，通过几次运算就可以发现规律
# 2、由于使用了负索引，所以条件中要增加
#   i == length + minindex

def binary_selection_sort():
    lst = [1, 1, 1, 1, 1, 3]
    count_swap = 0
    count_iter = 0
    length = len(lst)

    for i in range(length // 2):
        maxindex = i
        minindex = -i - 1
        minorigin = minindex
        # print(i)
        for j in range(i + 1, length - i):
            count_iter += 1
            # print(j)
            if lst[maxindex] < lst[j]:
                maxindex = j
            if lst[minindex] > lst[-j - 1]:
                minindex = -j - 1
        if lst[maxindex] == lst[minindex]:
            break
        if i != maxindex:
            lst[i], lst[maxindex] = lst[maxindex], lst[i]
            if i == minindex or i == length + minindex:
                minindex = maxindex
                count_swap += 1
        if minorigin != minindex:
            lst[minorigin], lst[minindex] = lst[minindex], lst[minorigin]
            count_swap += 1

    print(lst)
    print(count_iter)
    print(count_swap)

    # 简单选择排序总结
    #   简单选择排序需要数据一轮轮比较，并在每一轮中发现极值
    #   没有办法知道当前论是否已经达到排序要求，但是可以知道极值是否在目标索引位置上
    #   遍历次数n*(n-1)/2
    #   时间复杂度O(n^2)
    #   减少了交换次数，提高了效率，性能略好于冒泡法


# 改进实现
# 如果一轮比较后，极大值、极小值的值相等，说明比较的序列元素全部相等

binary_selection_sort()
