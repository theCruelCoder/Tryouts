import pysnooper, datetime, math


# @pysnooper.snoop()
def prime_v1():
    starting_time = datetime.datetime.now()
    count = 1
    x = 2
    #print(x, count)
    for x in range(3, 100000, 2):  # 排除所有偶数
        if x % 6 != 1 and x % 6 != 5:  # 质数6的性质
            continue
        for i in range(3, int(x**0.5) + 1, 2):
            if x % i == 0:
                break
        else:
            #print(x)
            count += 1
    delta = (datetime.datetime.now() - starting_time).total_seconds()
    print("Need: {} seconds.".format(delta))
    print(count)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# prime number v2


# @pysnooper.snoop()
def prime_v2():
    starting_time = datetime.datetime.now()
    n = 100000
    lst = [2]
    #print(2)
    for i in range(3, n, 2):
        for j in range(3, int(i**0.5) + 1, 2):
            if i % j == 0:
                break
        else:
            #print(i)
            lst.append(i)
    delta = (datetime.datetime.now() - starting_time).total_seconds()
    print("Need: {} seconds.".format(delta))
    print(len(lst))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# prime number v3


# @pysnooper.snoop()
def prime_v3():
    starting_time = datetime.datetime.now()
    n = 100000
    primenumber = []
    for x in range(2, n):
        for i in primenumber:
            if x % i == 0:
                break
        else:
            #print(x)
            primenumber.append(x)
    delta = (datetime.datetime.now() - starting_time).total_seconds()
    print("Need: {} seconds.".format(delta))
    print(len(primenumber))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# prime number v4
# @pysnooper.snoop()
def prime_v4():
    starting_time = datetime.datetime.now()
    x = 5
    step = 2
    count = 2
    #print(2, 3, sep='\n')
    while x < 100000:
        for i in range(3, int(x**0.5) + 1, 2):
            if not x % i:
                break
        else:
            #print(x)
            count += 1
        x += step
        step = 4 if step == 2 else 2
    delta = (datetime.datetime.now() - starting_time).total_seconds()
    print("Need: {} seconds.".format(delta))
    print(count)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# prime number v5
def prime_v5():
    starting_time = datetime.datetime.now()
    primenumber = []
    flag = False
    for x in range(2, 100000):
        for i in primenumber:
            if x % i == 0:
                flag = True
                break
            if i >= math.ceil(math.sqrt(x)):
                flag = False
                break
        if not flag:
            #print(x)
            primenumber.append(x)
    delta = (datetime.datetime.now() - starting_time).total_seconds()
    print("Need: {} seconds.".format(delta))
    print(len(primenumber))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# prime number v6
def prime_v6():
    starting_time = datetime.datetime.now()
    count = 1
    primenumber = []
    flag = False
    for x in range(3, 100000, 2):
        up = math.ceil(math.sqrt(x))
        for i in primenumber:
            if x % i == 0:
                flag = True
                break
            if i >= up:
                flag = False
                break
        if not flag:
            #print(x)
            primenumber.append(x)
            count += 1
    delta = (datetime.datetime.now() - starting_time).total_seconds()
    print("Need: {} seconds.".format(delta))
    print(count)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

prime_v1()
prime_v2()
prime_v3()
prime_v4()
prime_v5()
prime_v6()
