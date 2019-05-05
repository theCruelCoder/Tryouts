# 转换int后，判断大小排序。使用分支结构完成
def sort1_v1():
    first = int(input("First Number:"))
    second = int(input("Second Number:"))
    third = int(input("Third Number:"))

    if first >= second:
        if first >= third:
            if second >= third:
                print(third, second, first)
            else:
                print(second, third, first)
        else:
            print(second, first, third)
    else:
        if second >= third:
            if first >= third:
                print(third, first, second)
            else:
                print(first, third, second)
        else:
            print(first, second, third)

# Example No.1:
def sort1_v2():
    nums = []
    for i in range(3):
        nums.append(int(input('{}:'.format(i))))
    if nums[0] > nums[1]:
        if nums[0] > nums[2]:
            i3 = nums[0]
            if nums[1] > nums[2]:
                i2 = nums[1]
                i1 = nums[2]
            else:
                i2 = nums[2]
                i1 = nums[1]
        else:
            i2 = nums[0]
            i3 = nums[2]
            i1 = nums[1]
    else:
        if nums[0] > nums[2]:
            i3 = nums[1]
            i2 = nums[0]
            i1 = nums[2]
        else:
            if nums[1] < nums[2]:
                i1 = nums[0]
                i2 = nums[1]
                i3 = nums[2]
            else:
                i1 = nums[0]
                i2 = nums[2]
                i3 = nums[1]
    print(i1, i2, i3)

# Example 1 using index

def sort1_v3():
    nums = []
    out = None
    for i in range(3):
        nums.append(int(input('{}:'.format(i))))

    if nums[0] > nums[1]:
        if nums[0] > nums[2]:
            if nums[1] > nums[2]:
                out = [2,1,0]
            else:
                out = [1,2,0]
        else:
            out = [1,0,2]
    else:
        if nums[0] > nums[2]:
            out = [2,0,1]
        else:
            if nums[1] < nums[2]:
                out = [0,1,2]
            else:
                out = [0,2,1]
    out.reverse()
    for i in out:
        print(nums[i], end=', ')

# max min实现
def sort2_v1():
    nums = []
    out = None
    for i in range(3):
        nums.append(int(input('{}:'.format(i))))
    while True:
        cur = min(nums)
        print(cur)
        nums.remove(cur)
        if len(nums) == 1:
            print(nums[0])
            break

# list sort方法
def sort3_v1():
    nums = []
    out = None
    for i in range(3):
        nums.append(int(input('{}:'.format(i))))

    nums.sort()
    print(nums)
