import datetime

# my version
def my_yhtriangle():
    start_time = datetime.datetime.now()
    lst = [[1], [1, 1]]
    n = 1000
    for i in range(2, n):
        tmp_lst = [1]
        for j in range(1, len(lst[i-1])):
            tmp_lst.append(lst[i-1][j - 1] + lst[i-1][j])
        else:
            tmp_lst.append(1)
        lst.append(tmp_lst)
    #for i in lst:
    #    tmp_str = ""
    #    for j in i:
    #        tmp_str = tmp_str + " " + str(j)
    #    print(tmp_str)
    delta = (datetime.datetime.now() - start_time).total_seconds()
    print("Need: {} seconds.".format(delta))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# class v1
def yhtriangle_v1():
    start_time = datetime.datetime.now()
    triangle = [[1], [1, 1]]
    n = 1000

    for i in range(2, n):
        newline = [1] # 新行及第一个元素
        pre = triangle[i-1]
        for j in range(i-1):
            val = pre[j] + pre[j+1]
            newline.append(val)
        newline.append(1) # 尾巴
        triangle.append(newline)

    #print(triangle)
    delta = (datetime.datetime.now() - start_time).total_seconds()
    print("Need: {} seconds.".format(delta))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


my_yhtriangle()
yhtriangle_v1()

