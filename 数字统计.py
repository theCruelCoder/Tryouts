#  Copyright (c) 2019. YH Software Inc. Corp.import randomdef q():    """    随机产生10个数字    要求：    每个数字取值范围[1,20]    统计重复的数字有几个？分别是什么？    统计不重复的数字有几个？分别是什么？    :return:    """    lst = []    not_dupl = []    dupl = []    for i in range(10):        lst.append(random.randint(1, 20))    set1 = set(lst)    print(lst)    for i in set1:        occ1 = lst.count(i)        if occ1 == 1:            not_dupl.append(i)        else:            dupl.append(i)    print(not_dupl)    print(dupl)q()def better_version():    lst = []    dupl_lst = []    uniq_list = []    for i in range(10):        t = random.randint(1, 20)        if t in lst and t not in dupl_lst:            dupl_lst.append(t)        lst.append(t)    for j in lst:        if j not in dupl_lst:            uniq_list.append(j)    print(lst)    print(dupl_lst)    print(uniq_list)better_version()def teacher_version():    nums = []    for _ in range(10):        nums.append(random.randrange(21))    print('Origin numbers = {}'.format(nums))    print()    length = len(nums)    samenums = []    diffnums = []    states = [0] * length    for i in range(length):        flag = False        if states[i] == 1:            continue        for j in range(i + 1, length):            if states[j] == 1:                continue            if nums[i] == nums[j]:                flag = True                states[j] = 1        if flag:            samenums.append(nums[i])            states[i] = 1        else:            diffnums.append(nums[i])    print(nums)    print(states)    print(samenums)    print(diffnums)teacher_version()